from password_generator.utils.arg_parser import parse_input_args
from password_generator.models.generate_request import GenerateRequest
from unittest.mock import patch
import sys


def test_parse():
    """Test input arguments parse"""

    # test with len (positional param)
    with patch.object(sys, "argv", ["password_generator", "16"]):
        assert parse_input_args() == GenerateRequest(16)
