const processStdoutWrite = process.stdout.write.bind(process.stdout);
const processStderrWrite = process.stderr.write.bind(process.stderr);

var toString = {}.toString;

/**
 * @param {*} value
 * @return {boolean}
 */
function isString(value) {
  return typeof value === 'string' || toString.call(value) === '[object String]';
}

/**
 * @param {Array.<string>} list
 * @param {number} fromInclusive
 * @param {number} toExclusive
 * @param {string} delimiterChar one character string
 * @returns {string}
 */
function joinList(list, fromInclusive, toExclusive, delimiterChar) {
  if (list.length === 0) {
    return '';
  }
  if (delimiterChar.length !== 1) {
    throw Error('Delimiter is expected to be a character, but "' + delimiterChar + '" received');
  }
  var addDelimiter = false
    , escapeChar = '\\'
    , escapeCharCode = escapeChar.charCodeAt(0)
    , delimiterCharCode = delimiterChar.charCodeAt(0)
    , result = ''
    , item
    , itemLength
    , ch
    , chCode;
  for (var itemId = fromInclusive; itemId < toExclusive; itemId++) {
    if (addDelimiter) {
      result += delimiterChar;
    }
    addDelimiter = true;
    item = list[itemId];
    itemLength = item.length;
    for (var i = 0; i < itemLength; i++) {
      ch = item.charAt(i);
      chCode = item.charCodeAt(i);
      if (chCode === delimiterCharCode || chCode === escapeCharCode) {
        result += escapeChar;
      }
      result += ch;
    }
  }
  return result;
}

/**
 * @param {String} message
 */
function warn(message) {
  const str = 'WARN - IDE integration: ' + message + '\n';
  try {
    processStderrWrite(str);
  }
  catch (ex) {
    try {
      processStdoutWrite(str);
    }
    catch (ex) {
      // do nothing
    }
  }
}

/**
 * @template T
 * @param {T} fn
 * @return T
 */
function safeFn(fn) {
  return function () {
    try {
      return fn.apply(this, arguments);
    } catch (ex) {
      warn(ex.message + '\n' + ex.stack);
    }
  };
}

/**
 * @tempate T
 * @param {T} fn
 * @return T
 */
function safeAsyncGeneratorFn(fn) {
  return async function* () {
    try {
      const asyncGenerator = fn.apply(this, arguments);
      for await (const result of asyncGenerator) {
        yield result;
      }
    } catch (e) {
      warn(e.message + '\n' + e.stack);
    }
  };
}

const LOCATION_DELIMITER_CHAR = '.';

/**
 * @param {TestSuiteNode} parentNode
 * @param {string} nodeName
 * @param {TestSuiteNode} testFileNode
 * @param {string} [testFilePath]
 * @static
 */
function getTestLocationPath(parentNode, nodeName, testFileNode, testFilePath) {
  const names = [nodeName];
  let currentParentNode = parentNode;
  while (currentParentNode !== testFileNode) {
    names.push(currentParentNode.name);
    currentParentNode = currentParentNode.parent;
  }
  names.push(testFilePath || '');
  names.reverse();
  return joinList(names, 0, names.length, LOCATION_DELIMITER_CHAR);
}

exports.isString = isString;
exports.safeFn = safeFn;
exports.safeAsyncGeneratorFn = safeAsyncGeneratorFn;
exports.warn = warn;
exports.getTestLocationPath = getTestLocationPath;
