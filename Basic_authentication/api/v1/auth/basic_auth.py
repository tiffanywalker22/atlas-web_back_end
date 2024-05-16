#!/usr/bin/env python3
"""basic auth class"""
from api.v1.auth.auth import Auth
import base64
from typing import Tuple, Optional, TypeVar
from models.user import User

User = TypeVar('User')


class BasicAuth(Auth):
    """class for basic auth"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extracts the base64 part of the authorization header for a basic auth
        """
        if authorization_header is None:
            return None
        elif not isinstance(authorization_header, str):
            return None
        elif not authorization_header.startswith("Basic "):
            return None
        return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Decodes the base64 part of the auth header
        """
        if base64_authorization_header is None:
            return None
        elif not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> Tuple[str, str]:
        """
        Extracts the user email and password from the Base64 decoded value
        """
        if decoded_base64_authorization_header is None:
            return None, None
        elif not isinstance(decoded_base64_authorization_header, str):
            return None, None
        elif ':' not in decoded_base64_authorization_header:
            return None, None

        user_email, user_password = (
            decoded_base64_authorization_header.split(':', 1)
        )
        return user_email, user_password

    def user_object_from_credentials(
                self, user_email: str, user_pwd: str) -> TypeVar('User'):
            """
            Returns the user instance based on email and password
            """
            if user_email is None or type(user_email) is not str:
                return None
            if user_pwd is None or type(user_pwd) is not str:
                return None
            try:
                user_list = User.search({'email': user_email})
            except Exception:
                return None
            for user in user_list:
                if user.is_valid_password(user_pwd):
                    return user
            return None


    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the User instance for a request using basic auth
        """
        if request is None:
            return None

        auth_header = request.headers.get('Authorization')
        base64_header = self.extract_base64_authorization_header(auth_header)
        decoded_header = self.decode_base64_authorization_header(base64_header)
        user_email, user_pwd = self.extract_user_credentials(decoded_header)
        return self.user_object_from_credentials(user_email, user_pwd)
