import random
from os import path as op

__all__ = ['Texter']


class Texter(object):
    def __init__(self,fp:str):
        assert op.exists(fp),f"[ERROR] File {fp} not found!"
        fpt = open(fp)
        self.lines = fpt.readlines()
        self.count = len(self.lines)

    def sample(self, k:int = 10) -> list:
        """
        Random sample lines
        """
        if k > self.count:
            return self.lines
        else:
            return random.sample(self.lines,k)

    def first(self):
        """
        Get first line
        """
        if self.count > 0:
            return self.lines[0]
        else:
            return None

    def head(self, k:int=10) -> list:
        if self.count > k:
            return self.lines[:k]
        else:
            return self.lines

    def tail(self, k:int=10):
        if self.count > k:
            return self.lines[-k:]
        else:
            return self.lines

