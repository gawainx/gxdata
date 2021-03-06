import json
import os
import random
from typing import Union

__all__ = ['Jsoner']


class Jsoner:
    def __init__(self, fn: str):
        assert os.path.exists(fn), f"{fn} not exist"
        self._obj = json.load(open(fn))
        self.length = len(self._obj)

    def raw(self):
        return self._obj

    def Type(self, display: bool = True):
        if display:
            print(f"Type of json object is {type(self._obj)}")
        return type(self._obj)

    def first(self, display: bool = True):
        assert isinstance(self._obj, list), f"first method must be used for list, but got {type(self._obj)}"
        res = self._obj[0]
        if display:
            print(f"first item is {res}")
        return res

    def keys(self) -> list:
        assert isinstance(self._obj, dict), f"keys method must be used for dict, but got {type(self._obj)}"
        return list(self._obj.keys())

    def sample(self, k=10) -> Union[list,dict]:
        """
        k is length of sampler
        """
        if self.length < k:
            return self._obj
        if isinstance(self._obj, list):
            return random.sample(self._obj, k)
        elif isinstance(self._obj, dict):
            sampler_keys = random.sample(list(self._obj.keys()), k)
            sampler_vals = [self._obj[k] for k in sampler_keys]
            sampler = dict(zip(sampler_keys, sampler_vals))
            return sampler


def analyzer(file: str, prefix="ana"):
    """Analyze json key and value
    :param file: json file
    """
    data = json.load(open(file))
    target = open(f"{file.split('.')[0]}-{prefix}.txt", 'w')
    if isinstance(data, list):
        line = f"------file type\tlist------"
        item = data[0]
        print(line, file=target)
        line = f"------One item type\t{item.__class__}------"
        print(line, file=target)
        if isinstance(item, dict):
            line = "key_type\tkey\tvalue_type\tvalue"
            print(line, file=target)
            for k in item.keys():
                line = f"{k.__class__}\t{k}\t{item[k].__class__}\t{item[k]}"
                print(line, file=target)
    target.close()
