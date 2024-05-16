#!/usr/bin/env python3
"""Implement the format method to filter values in incoming log
records using filter_datum. Values for fields in
fields should be filtered"""
import re
from typing import List
import logging
import csv
import os
import mysql.connector

PII_FIELDS = ('name', 'email', 'phone', 'password', 'ssn')


def get_db():
    """
    Connect to the MySQL database using environment variables for credentials
    Returns:
    mysql.connector.connection.MySQLConnection: The database connection object
    Raises:
    mysql.connector.Error: If there is an error connecting to the database
    """

    db_username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    db_password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    db_host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    try:
        connection = mysql.connector.connect(
            user=db_username,
            password=db_password,
            host=db_host,
            database=db_name
        )
        return connection
    except mysql.connector.Error as error:
        print(f"Error connecting to the database: {error}")
        raise


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
        """Customizes the format of log messages by
        obfuscating sensitive information  """
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


def get_logger() -> logging.Logger:
    """
    Get a configured logger object for logging user data.
    Returns:
        .Logger: The configured logger object.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger
