# -*- coding: utf-8 -*-


class async_responses:

    @classmethod
    def mock(cls, fixture_path):

        def decorator(f):

            def wrapper(*args, **kwargs):
                f(*args, **kwargs)

            return wrapper

        return decorator
