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
                Format of the password
            exclude: str
                List of characters to exclude from the generated password
            custom: str
                Custom list of characters to generate password from
        """

        self.length = length
        self.format = format
        self.exclude = exclude
        self.custom = custom
