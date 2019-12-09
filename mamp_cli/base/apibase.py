"""
base class for api instances


"""
from abc import ABC, abstractmethod


class ApiBase(ABC):

    def __init__(self):
        super().__init__()

    @classmethod
    def build_new(cls, **kwargs):
        cls(**kwargs)
