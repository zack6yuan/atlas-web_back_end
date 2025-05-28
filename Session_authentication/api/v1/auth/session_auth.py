#!/usr/bin/env python3
""" Session Auth Module """
from api.v1.auth.auth import Auth
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