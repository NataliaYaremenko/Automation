import logging

def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s'
        )
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)






import pytest
from unittest.mock import patch


@patch('logging.getLogger')
def test_log_success(mock_get_logger):
    mock_logger = mock_get_logger.return_value

    log_event("test_user", "success")

    mock_logger.info.assert_called_once_with(
        "Login event - Username: test_user, Status: success"
    )

@patch('logging.getLogger')
def test_log_expired(mock_get_logger):
    mock_logger = mock_get_logger.return_value

    log_event("test_user", "expired")

    mock_logger.warning.assert_called_once_with(
        "Login event - Username: test_user, Status: expired"
    )

@patch('logging.getLogger')
def test_log_failed(mock_get_logger):
    mock_logger = mock_get_logger.return_value

    log_event("test_user", "failed")

    mock_logger.error.assert_called_once_with(
        "Login event - Username: test_user, Status: failed"
    )

@patch('logging.getLogger')
def test_log_unknown_status(mock_get_logger):
    mock_logger = mock_get_logger.return_value

    log_event("test_user", "unknown")

    mock_logger.error.assert_called_once_with(
        "Login event - Username: test_user, Status: unknown"
    )