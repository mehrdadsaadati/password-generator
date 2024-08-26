import argparse
from password_generator import generate
from password_generator.logger import get_logger

logger = get_logger("cli")


def main():
    """Main entry point of the app"""

    # parse user input arguments
    parser = argparse.ArgumentParser(
        prog="password_generator",
        description="Generates secure random passwords based on user inputs",
    )
    # add positional argument len
    parser.add_argument("len", type=int)
    # add option format (we use 'Aa0@' as default to avoid passing None to generate function)
    parser.add_argument(
        "-f",
        "--format",
        default="Aa0@",
        type=str,
        help="""Format of the password (String, default 'Aa0@'). Can be one of these options or a mix of them:
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
    # generate password based on user input
    try:
        logger.debug(
            f"Parsed input arguments: {args.len=}, {args.format=}, {args.exclude=}, {args.custom=}"
        )
        password = generate(args.len, args.format, args.exclude, args.custom)

        logger.info(f"Password of length {args.len} generated successfully")
        print(f"Password: {password}")
    except Exception as ex:
        logger.error(f"{ex}")


if __name__ == "__main__":
    main()
