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


def get_db() -> mysql.connector.connection.MySQLConnection:
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


def main():
    """The function will obtain a database connection
    using get_db and retrieve all rows in the users
    table and display each row under a filtered format"""
    db = get_db()
    logger = get_logger()
    db_cursor = db.cursor()
    db_cursor.execute("SELECT * FROM users;")
    for row in db_cursor:
        new_row = logger._formatter.format(record=logging.LogRecord
                                           (name="user_data",
                                            level=logging.INFO, pathname="",
                                            lineno=0, msg=row, args=None,
                                            exc_info=None))
        logger.info(new_row)
    db_cursor.close()
    db.close()


if __name__ == "__main__":
    main()
