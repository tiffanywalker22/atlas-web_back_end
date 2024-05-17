#!/usr/bin/env python3
"""class is the template for all authentication system you will implement"""
from flask import request
from typing import List, Type, TypeVar
import os


class Auth:
    """a class to manage the API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method to check if authentication is required """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
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

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method to get the current user """
        return None

    def session_cookie(self, request=None):
        """ Method to get the session cookie value from the request """
        if request is None:
            return None

        session_name = os.getenv('SESSION_NAME')
        if session_name is None:
            return None

        return request.cookies.get(session_name)
