from password_generator import generate, PasswordParamsError
import pytest
import re


def test_generate_length():
    """Test password generation length"""

    assert len(generate(16)) == 16
    assert len(generate(64)) == 64
    assert len(generate(1)) == 1
    with pytest.raises(PasswordParamsError):
        generate(0)
    with pytest.raises(PasswordParamsError):
        generate(-1)


def test_generate_format():
    """Test password generation format"""

    # check for uppercase letters only
    assert re.fullmatch(r"^[A-Z]+$", generate(16, "A")) is not None
    assert re.fullmatch(r"^[A-Z]+$", generate(32, "A")) is not None
    assert re.fullmatch(r"^[A-Z]+$", generate(64, "A")) is not None
    # check for lowercase letters only
    assert re.fullmatch(r"^[a-z]+$", generate(16, "a")) is not None
    assert re.fullmatch(r"^[a-z]+$", generate(32, "a")) is not None
    assert re.fullmatch(r"^[a-z]+$", generate(64, "a")) is not None
    # check for letters only
    assert re.fullmatch(r"^[a-zA-Z]+$", generate(16, "Aa")) is not None
    assert re.fullmatch(r"^[a-zA-Z]+$", generate(32, "Aa")) is not None
    assert re.fullmatch(r"^[a-zA-Z]+$", generate(64, "Aa")) is not None
    # check for numbers only
    assert re.fullmatch(r"^[0-9]+$", generate(16, "0")) is not None
    assert re.fullmatch(r"^[0-9]+$", generate(32, "0")) is not None
    assert re.fullmatch(r"^[0-9]+$", generate(64, "0")) is not None
    # check for symbols only
    assert re.fullmatch(r"^[^a-zA-Z0-9]+$", generate(16, "@")) is not None
    assert re.fullmatch(r"^[^a-zA-Z0-9]+$", generate(32, "@")) is not None
    assert re.fullmatch(r"^[^a-zA-Z0-9]+$", generate(64, "@")) is not None
    # check for numbers and symbols only
    assert re.fullmatch(r"^[^a-zA-Z]+$", generate(16, "0@")) is not None
    assert re.fullmatch(r"^[^a-zA-Z]+$", generate(32, "0@")) is not None
    assert re.fullmatch(r"^[^a-zA-Z]+$", generate(64, "0@")) is not None
    # check for alphanumerics
    assert re.fullmatch(r"^[a-zA-Z0-9]+$", generate(16, "Aa0")) is not None
    assert re.fullmatch(r"^[a-zA-Z0-9]+$", generate(32, "Aa0")) is not None
    assert re.fullmatch(r"^[a-zA-Z0-9]+$", generate(64, "Aa0")) is not None


def test_hex_numbers():
    """Test hex numbers"""

    # check for hex numbers (lowercase)
    assert re.fullmatch(r"^[0-9a-f]+$", generate(16, "h")) is not None
    assert re.fullmatch(r"^[0-9a-f]+$", generate(32, "h")) is not None
    assert re.fullmatch(r"^[0-9a-f]+$", generate(64, "h")) is not None
    # check for hex numbers (uppercase)
    assert re.fullmatch(r"^[0-9A-F]+$", generate(16, "H")) is not None
    assert re.fullmatch(r"^[0-9A-F]+$", generate(32, "H")) is not None
    assert re.fullmatch(r"^[0-9A-F]+$", generate(64, "H")) is not None


def test_custom_format():
    """Test custom formats"""

    # check for custom format
    assert re.fullmatch(r"^[abcd1234#]+$", generate(16, custom="abcd1234#")) is not None
    assert re.fullmatch(r"^[abcd1234#]+$", generate(32, custom="abcd1234#")) is not None
    assert re.fullmatch(r"^[abcd1234#]+$", generate(64, custom="abcd1234#")) is not None


def test_exclusion():
    """Test character exclusion from the password"""

    # check for exclusion
    assert (
        re.fullmatch(r"^[^08liLIoO]+$", generate(16, format="Aa0@", exclude="08liLIoO"))
        is not None
    )
    assert (
        re.fullmatch(r"^[^08liLIoO]+$", generate(32, format="Aa0@", exclude="08liLIoO"))
        is not None
    )
    assert (
        re.fullmatch(r"^[^08liLIoO]+$", generate(64, format="Aa0@", exclude="08liLIoO"))
        is not None
    )
    assert (
        re.fullmatch(
            r"^[^08liLIoO]+$", generate(128, format="Aa0@", exclude="08liLIoO")
        )
        is not None
    )
    assert (
        re.fullmatch(
            r"^[^08liLIoO]+$", generate(256, format="Aa0@", exclude="08liLIoO")
        )
        is not None
    )


def test_invalid_exclude():
    with pytest.raises(PasswordParamsError):
        generate(32, format="0", exclude="0123456789")
    with pytest.raises(PasswordParamsError):
        generate(32, format="a", exclude="abcdefghijklmnopqrstuvwxyz")
    with pytest.raises(PasswordParamsError):
        generate(32, format="a0", exclude="abcdefghijklmnopqrstuvwxyz0123456789")


def test_invalid_format():
    """Test invalid format exceptions"""
    with pytest.raises(PasswordParamsError):
        generate(32, format="jkv9x")
    with pytest.raises(PasswordParamsError):
        generate(32, format=None)
    with pytest.raises(PasswordParamsError):
        generate(32, format="")
