import argparse
from password_generator.models.generate_request import GenerateRequest


class ArgParseException(Exception):
    """Exception to indicate failure in parsing app arguments"""

    pass


def parse_input_args() -> GenerateRequest:
    """Parses the app input arguments and creates a GenerateRequest object based on user inputs
    Returns
    ------------
        GenerateRequest
            A GenerateRequest object if user input is valid
    Raises
    -----------
        ArgParseException
    """

    parser = argparse.ArgumentParser(
        prog="password_generator",
        description="Generates secure random passwords based on user inputs",
    )
    # add positional argument len
    parser.add_argument("len", type=int)
    # add option format
    parser.add_argument(
        "-f",
        "--format",
        default=None,
        type=str,
        help="""Format of the password (String). Format of the password. Can be one of these options or a mix of them:
    'a': lower case characters
    'A': lower case characters
    '0': numbers from 0 to 9
    '@': symbols
    'h': lower case hex number (other formats will be ignored)
    'H': upper case hex number (other formats will be ignored)
""",
    )
    # add option exclude
    parser.add_argument(
        "-e",
        "--exclude",
        default=None,
        type=str,
        help="A string of characters (letters, numbers and symbols) to exclude from the generated password",
    )
    # add option custom
    parser.add_argument(
        "-c",
        "--custom",
        default=None,
        type=str,
        help="A custom string of letters, numbers and symbols to pick characters from. If this parameter is passed, format is ignored",
    )

    args = parser.parse_args()

    return GenerateRequest(
        args.len, format=args.format, exclude=args.exclude, custom=args.custom
    )
