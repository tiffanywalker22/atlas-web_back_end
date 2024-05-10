#!/usr/bin/env python3
"""Implement a hash_password function that expects one string
argument name password and returns a salted, hashed password,
which is a byte string./main.py"""
import bcrypt


def hash_password(password):
    """Generate a salt and hash the password using bcrypt"""

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
