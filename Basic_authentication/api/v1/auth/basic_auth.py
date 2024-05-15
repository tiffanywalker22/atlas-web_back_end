#!/usr/bin/env python3
"""basic auth class"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """class for basic auth"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extracts the base64 part of the authorization header for a basic auth
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[len("Basic "):]
