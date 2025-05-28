#!/usr/bin/env python3
""" Session Auth Module """
from api.v1.auth.auth import Auth
from api.v1.views.users import User
import uuid


class SessionAuth(Auth):
    """ SessionAuth Class """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Create Session Function """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        session = str(uuid.uuid4())
        self.user_id_by_session_id[session] = user_id

        return session

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ User Id For Session ID Function """
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        value = self.user_id_by_session_id.get(session_id)

        return value

    def destroy_session(self, request=None):
        """ Destroy Session Function """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        
        if session_cookie is None:
            return False
        user_id = self.user_id_for_session_id(session_id)
        
        del user_id_by_session_id(session_cookie)
        return True

    def current_user(self, request=None) -> User:
        """
        Current User Function

        Methods:
        Check is request is None
        Get cookie_value, and ensure it is not None
        Get user_id, and ensure it is not None
        Get the user instance

        Returns:
        The User ID based on the cookie
        """
        if request is None:
            return None
        cookie_value = self.session_cookie(request)
        if cookie_value is None:
            return None
        user_id = self.user_id_for_session_id(cookie_value)
        if user_id is None:
            return None

        return User.get(user_id)
