class GenerateRequest:
    """DTO class used to pass generate password request

    Attributes
    ----------
        length: int
            Length of the password
        format: str
            Format of the password
        exclude: str
            List of characters to exclude from the generated password
        custom: str
            Custom list of characters to generate password from
    """

    def __init__(
        self, length: int, format: str = None, exclude: str = None, custom: str = None
    ) -> None:
        """
        Parameters
        ----------
            length: int
                Length of the password
            format: str
                Format of the password. A string containing one of or mixture of these characters:
                    a: Lower case letters
                    A: Upper case letters
                    0: Numbers from 0 to 9
                    @: Symbols
                    h: Lower case hex number (other formats will be ignored)
                    H: Upper case hex number (other formats will be ignored)
            exclude: str
                List of characters to exclude from the generated password
            custom: str
                Custom list of characters to generate password from
        """

        self.length = length
        self.format = format
        self.exclude = exclude
        self.custom = custom

    def __eq__(self, value: object) -> bool:
        if isinstance(value, GenerateRequest):
            return (
                self.length == value.length
                and self.format == value.format
                and self.exclude == value.exclude
                and self.custom == value.custom
            )
        else:
            return False
