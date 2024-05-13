#!/usr/bin/env python3
"""class is the template for all authentication system you will implement"""
from typing import List, Type, TypeVar
from flask import request

User = TypeVar('User')


class Auth:
    """a class to manage the API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method to check if authentication is required """
        if not path or not excluded_paths:
            return True
        path = path.rstrip('/') + '/'
        excluded_paths = [p.rstrip('/') + '/' for p in excluded_paths]

        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """ Method to get the authorization header """
        if request is None or "Authorization" not in request.headers:
            return None
        return request.headers["Authorization"]

    def current_user(self, request=None) -> User:
        """ Method to get the current user """
        return None
