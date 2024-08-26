import logging
from logging.handlers import RotatingFileHandler


def get_logger(name):
    """Gets a logger based on the passed name

    Parameters
    ----------
    name: str
        Name of the logger. It would be a good practice to pass the consumer module name via __name__
    """

    # Create a custom logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Set the default logging level

    # Create handlers
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Store logs in a max 20kB size file
    file_handler = RotatingFileHandler("app.log", maxBytes=20000, backupCount=3)
    file_handler.setLevel(logging.WARNING)

    # Create formatters and add it to handlers
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
