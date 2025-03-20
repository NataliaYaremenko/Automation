const Tree = require('../base-test-reporter/intellij-tree.js');
const utils = require('../base-test-reporter/intellij-util');
const tree = new Tree(null, getStdoutWrite());
const vitestIntellijUtil = require('./vitest-intellij-util');
const path = require('path');

function getStdoutWrite() {
  return process.stdout.write.bind(process.stdout);
}

/** @type {boolean} */
let beforeTestingStart = true;

/** @type {Object<string, TestSuiteNode>} */
let filePathToFileNodeMap = {};

/** @type {Object<string, Stat>} */
let collectedFilePathToTestStatMap = {};

/** @type {Object<string, TestNode>} */
let testIdToTestNodeMap = {};

class Stat {
  collectedTestCount = 0;
  finishedTestCount = 0;
}

tree.startNotify();

function IntellijReporter() {
}

function startTestingIfNeeded() {
  if (beforeTestingStart) {
    tree.testingStarted();
    beforeTestingStart = false;
    filePathToFileNodeMap = {};
    collectedFilePathToTestStatMap = {};
    testIdToTestNodeMap = {};
  }
}

function finishTesting() {
  if (beforeTestingStart) {
    utils.warn('Cannot finish not started testing');
    return;
  }
  tree.testingFinished();
  beforeTestingStart = true;
}

IntellijReporter.prototype.onInit = utils.safeFn((vitestCtx) => {
  if (process.env['_JETBRAINS_VITEST_RUN_WITH_COVERAGE']) {
    vitestIntellijUtil.configureCoverage(vitestCtx.config, tree);
  }
});

// Not working in vitest
// IntellijReporter.prototype.onPathsCollected = utils.safeFn((paths) => {
// });

/**
 * @param {String} filePath
 * @returns {Stat}
 */
function getOrCreateStat(filePath) {
  let stat = collectedFilePathToTestStatMap[filePath];
  if (stat == null) {
    stat = new Stat();
    collectedFilePathToTestStatMap[filePath] = stat;
  }
  return stat;
}

IntellijReporter.prototype.onCollected = utils.safeFn((files) => {
  startTestingIfNeeded();
  buildTreeAndProcessTests(files, (testTask, testNode, filePath) => {
    getOrCreateStat(filePath).collectedTestCount++;
  });
});

function buildTreeAndProcessTests(files, callback) {
  for (const file of files) {
    const filePath = file.filepath;
    const fileNode = getOrCreateFileNode(filePath, file.projectName);
    for (const task of file.tasks) {
      traverseSuitesAndProcessTests(task, [], (ancestorSuiteNames, testTask) => {
        if (testTask.mode === 'skip' && vitestIntellijUtil.isSuitesOrTestsScope()) {
          return; // ignore other tests when running a single suite/test
        }
        let currentParentNode = fileNode;
        for (const suiteName of ancestorSuiteNames) {
          let childSuiteNode = currentParentNode.findChildNodeByName(suiteName);
          if (!vitestIntellijUtil.isSuiteNode(childSuiteNode)) {
            const suiteLocationPath = utils.getTestLocationPath(currentParentNode, suiteName, fileNode, filePath);
            childSuiteNode = currentParentNode.addTestSuiteChild(suiteName, 'suite', suiteLocationPath);
            childSuiteNode.start();
          }
          currentParentNode = childSuiteNode;
        }
        const testNode = getOrCreateTestNode(currentParentNode, testTask, fileNode, filePath)
        callback(testTask, testNode, filePath);
      })
    }
  }
}

function getOrCreateTestNode(currentParentNode, testTask, fileNode, filePath) {
  let testNode = testIdToTestNodeMap[testTask.id];
  if (testNode == null) {
    const testLocationPath = utils.getTestLocationPath(currentParentNode, testTask.name, fileNode, filePath)
    testNode = currentParentNode.addTestChild(testTask.name, 'test', testLocationPath)
    testIdToTestNodeMap[testTask.id] = testNode;
    testNode.start()
  }
  return testNode
}

function getOrCreateFileNode(filePath, projectName) {
  const isWorkspace = projectName != null;
  const fileNodeKey = isWorkspace ? projectName + '|' + filePath : filePath;
  let fileNode = filePathToFileNodeMap[fileNodeKey];
  if (fileNode == null) {
    if (vitestIntellijUtil.isSingleTestFileScope()
      // Don't update the root node for workspaces, because they can rerun file more than once
      && !isWorkspace
    ) {
      tree.updateRootNode(
        vitestIntellijUtil.createFileNodeName(filePath, projectName),
        path.relative('', path.dirname(filePath)),
        'file://' + filePath
      );
      fileNode = tree.root;
    }
    else {
      fileNode = vitestIntellijUtil.addTestFileNode(tree, filePath, projectName);
      fileNode.start();
    }
    filePathToFileNodeMap[fileNodeKey] = fileNode;
  }
  return fileNode;
}

function traverseSuitesAndProcessTests(task, suiteNames, callback) {
  if (task.type === 'test') {
    callback(suiteNames, task);
  }
  else if (task.type === 'suite') {
    suiteNames.push(task.name);
    for (const childTask of task.tasks) {
      traverseSuitesAndProcessTests(childTask, suiteNames, callback);
    }
    suiteNames.pop();
  }
}

IntellijReporter.prototype.onUserConsoleLog = utils.safeFn((log) => {
  const testNode = testIdToTestNodeMap[log.taskId];
  if (testNode) {
    vitestIntellijUtil.sendConsoleLog(testNode, log);
  }
});

IntellijReporter.prototype.onFinished = utils.safeFn((files, errors) => {
  if (beforeTestingStart) {
    utils.warn("Got finished tests before collecting them");
  }
  buildTreeAndProcessTests(files, (testTask, testNode, filePath) => {
    vitestIntellijUtil.finishTestNode(testTask, testNode);
    const stat = collectedFilePathToTestStatMap[filePath];
    if (stat != null) {
      stat.finishedTestCount++;
    }
  });
  if (Array.isArray(errors)) {
    for (const error of errors) {
      const normalizedError = vitestIntellijUtil.normalizeError(error);
      vitestIntellijUtil.addErrorTestChild(tree.root, normalizedError.name, normalizedError.message, normalizedError.stack);
    }
  }

  for (const file of files) {
    const filePath = file.filepath;
    const fileNode = getOrCreateFileNode(filePath, file.projectName);
    const fileError = vitestIntellijUtil.getNormalizedErrorByTask(file);
    if (fileError != null) {
      vitestIntellijUtil.addErrorTestChild(fileNode, fileError.name, fileError.message, fileError.stack);
    }
    const stat = getOrCreateStat(filePath);
    if (stat.collectedTestCount === stat.finishedTestCount) {
      fileNode.children.forEach(function (childNode) {
        childNode.finishIfStarted();
      });
      fileNode.finish(false);
    }
  }
  if (Object.values(collectedFilePathToTestStatMap).every((stat) => stat.collectedTestCount <= stat.finishedTestCount)) {
    finishTesting();
  }
});

module.exports = IntellijReporter;

/*
function traceCalls(functionName, fn) {
  const old = IntellijReporter.prototype[functionName];
  IntellijReporter.prototype[functionName] = function () {
    process.stdout.write('trace: ' + functionName + '\n');
    if (typeof fn === 'function') {
      fn.apply(this, arguments);
    }
    if (typeof old === 'function') {
      old.apply(this, arguments);
    }
  }
}

traceCalls('onInit');
traceCalls('onPathsCollected');
traceCalls('onCollected', (files) => {
  logFiles('onCollected', files);
});
traceCalls('onFinished', (files) => {
  logFiles('onFinished', files);
});
traceCalls('onTaskUpdate');
traceCalls('onTestRemoved');
traceCalls('onWatcherStart');
traceCalls('onWatcherRerun');
traceCalls('onServerRestart');
traceCalls('onUserConsoleLog');

function logFiles(message, files) {
  process.stdout.write(message + ' ' + files.length + '\n' + files.map(file => '  ' + file.filepath).join('\n') + '\n');
}

*/
