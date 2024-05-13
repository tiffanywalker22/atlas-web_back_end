#!/usr/bin/env python3
"""class is the template for all authentication system you will implement"""
from typing import List, Type, TypeVar
from flask import request

User = TypeVar('User')


class Auth:
    """a class to manage the API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method to check if authentication is required """
        return False

    def authorization_header(self, request=None) -> str:
        """ Method to get the authorization header """
        return None

    def current_user(self, request=None) -> User:
        """ Method to get the current user """
        return None
