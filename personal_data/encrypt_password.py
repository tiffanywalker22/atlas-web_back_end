#!/usr/bin/env python3
"""Implement a hash_password function that expects one string
argument name password and returns a salted, hashed password,
which is a byte string./main.py"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Generate a salt and hash the password using bcrypt"""

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def is_valid(hashed_password, password):
    """Check if the provided password matches the hashed password"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
