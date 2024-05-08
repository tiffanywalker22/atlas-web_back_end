#!/usr/bin/env python3
"""Write a function called filter_datum that
returns the log message obfuscated"""
import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """
    Formatter class for redacting sensitive information in log messages

    Attributes:
    REDACTION (str): The redacted string to replace sensitive information
    FORMAT (str): The log message format including placeholders
    for logging attributes
    SEPARATOR (str): The separator character used to separate
    fields in log messages

    Args:
    fields (List[str]): A list of strings representing fields
    with sensitive information

    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the RedactingFormatter

        Args:
        fields (List[str]): A list of strings representing fields
        with sensitive information

        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        def filter_datum(
                        fields: List[str],
                        redaction: str,
                        message: str,
                        separator: str
                        ) -> str:
            """
            Obfuscates specified fields in a log message

            Arguments:
            fields (List[str]): A list of strings representing
            all fields to obfuscate
            redaction (str): A string representing by what the field
            will be obfuscated
            message (str): A string representing the log line
            separator (str): A string representing by which character is
            separating all fields in the log line (message)

            Returns:
            str: The obfuscated log message
            """
            for field in fields:
                message = re.sub(f"(?<={field}=).*?(?={separator})",
                                 redaction, message)
            return message

        record.msg = filter_datum(self.fields, self.REDACTION, record.msg,
                                  self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
