#!/usr/bin/env python3
"""Write a function called filter_datum that
returns the log message obfuscated"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates specified fields in a log message

    Arguments:
    fields (list): A list of strings representing all fields to obfuscate
    redaction (str): A string representing by what the field
    will be obfuscated
    message (str): A string representing the log line
    separator (str): A string representing by which character is
    separating all fields in the log line (message)

    Returns:
    str: The obfuscated log message
    """
    return re.sub(fr'(?<={separator})({"|".join(fields)})(?={separator})', redaction, message)
