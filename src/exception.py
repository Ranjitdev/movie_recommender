import sys
import os
from src.logger import logging


def get_error_message(message, details: sys):
    exc_type, exc_obj, exc_tb = details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "error occured script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(message)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error, error_details:sys):
        super().__init__(error)
        self.error_message = error
        self.error_detail = error_details
        self.message = get_error_message(self.error_message, self.error_detail)

    def __str__(self):
        logging.error(self.message)
        print(self.message)
        return self.message
