#!/usr/bin/env python3
""" Session Auth Module """
from api.v1.auth.auth import Auth
from api.v1.views.users import User
from api.v1.auth.auth import session_cookie
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