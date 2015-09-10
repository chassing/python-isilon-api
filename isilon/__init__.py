from .session import Session
from .namespace import Namespace
from .platform import Platform

from .exceptions import ObjectNotFound, APIError, ConnectionError, IsilonLibraryError

__all__ = [
    "ObjectNotFound", "APIError", "ConnectionError", "IsilonLibraryError", "API"
]


class API(object):

    '''Implements higher level functionality to interface with an Isilon cluster'''

    def __init__(self, *args, **kwargs):

        self.session = Session(*args, **kwargs)
        self.namespace = Namespace(self.session)
        self.platform = Platform(self.session)
