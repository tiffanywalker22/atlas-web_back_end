#!/usr/bin/env python3
""" user auth """

import bcrypt


def _hash_password(password: str) -> bytes:
    """Hash a password string using bcrypt and return the hashed bytes"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
