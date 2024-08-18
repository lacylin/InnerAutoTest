# -*- coding: utf-8 -*-
"""
 单例模式的元类 metaclass
"""


class BaseSingleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)

        return cls._instance[cls]
