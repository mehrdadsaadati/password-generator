import secrets
from password_generator.logger import get_logger

logger = get_logger(__name__)

_lower_case_letters = "abcdefghijklmnopqrstuvwxyz"
_upper_case_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
_numbers = "0123456789"
_symbols = "`~!@#$%^&*()_+-=[]{}:;'\",./<>?"
_lower_case_hex_digits = "0123456789abcdef"
_upper_case_hex_digits = "0123456789ABCDEF"


class PasswordParamsError(Exception):
    """Exception for invalid password generate requests"""

    pass


def generate(
    len: int, format: str = "Aa0@", exclude: str = None, custom: str = None
) -> str:
    """Generates a secure random password.

    `len` is required and must be greater than 0.
    If 'h' or 'H' is used in the `format` and `exclude`, the result is a hex string.
    If `custom` is defined, the `format` and `exclude` will be ignored.

    Args:
        len (int): Length of the password
        format (str, optional): Format of the password. Can contain 'a' for lower case letters, 'A' for upper case letters, '0' for numbers, '@' for symbols, 'h' for small case hex number and 'H' for upper case hex numbers. Defaults to "Aa0@".
        exclude (str, optional): List of characters to exclude from generated password. Defaults to None.
        custom (str, optional): List of custom characters to generate password from. Using this parameter will ignore the `format`. Defaults to None.

    Returns:
        str: A secure random password

    Raises:
        PasswordParamsError: If format is empty or invalid
    """

    logger.debug(
        f"Password generator parameters: {len=}, {format=}, {exclude=}, {custom=}"
    )

    # check len
    if len <= 0:
        raise PasswordParamsError(f"Password len is less than 1: {len=}.")

    # generate password based on custom list of characters (ignore the format)
    if custom:
        logger.info("Generating custom password")
        return __secure_random_pick(len, custom)

    # if custom is not used, then format is required
    if not format:
        raise PasswordParamsError(f"Password format must be a str: {format}.")

    # generate hex number sequence (ignore the format)
    if "h" in format:
        logger.info("Generating lower case hex password")
        return __secure_random_pick(len, _lower_case_hex_digits)
    if "H" in format:
        logger.info("Generating upper case hex password")
        return __secure_random_pick(len, _upper_case_hex_digits)

    # generate password based on the format
    chars = []
    if "A" in format:
        chars.extend(_upper_case_letters)
    if "a" in format:
        chars.extend(_lower_case_letters)
    if "0" in format:
        chars.extend(_numbers)
    if "@" in format:
        chars.extend(_symbols)

    if not chars:
        raise PasswordParamsError(
            f"Password format is not valid: {format=}. Must contain at least 'a', 'A', '0' or '@'"
        )

    # remove characters based on exclude list
    if exclude:
        for e in exclude:
            chars.remove(e)

    if not chars:
        raise PasswordParamsError(
            f"Exclude removed all possible characters to generate password: {format=}, {exclude=}."
        )

    logger.info(f"Generating formatted password: {format=}, {exclude=}")
    return __secure_random_pick(len, chars)


def __secure_random_pick(len: int, chars: str) -> str:
    """Secure randomly picks characters from a string in specified length

    Args:
        len (int): Len of the selection
        chars (str): List of the chars to pick from

    Returns:
        str: Secure randomly picked list
    """

    return "".join(secrets.choice(chars) for i in range(len))
