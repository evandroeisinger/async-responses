# -*- coding: utf-8 -*-

import yaml

from io import StringIO

from unittest.mock import patch

from tornadoalf.client import Client

from tornado.httpclient import HTTPRequest
from tornado.httpclient import HTTPResponse
from tornado.httpclient import AsyncHTTPClient
from tornado.testing import gen_test
from tornado.concurrent import Future
from tornado import gen


class async_responses:

    @property
    def _response(self):
        request = HTTPRequest("")
        status_code = self.fixture.get("code", 200)
        headers = self.fixture.get("headers", {})
        body = StringIO(self.fixture.get("body", ""))

        return HTTPResponse(request, status_code, headers, body)

    def __init__(self, fixture_path):
        self.fixture = yaml.load(open(fixture_path).read())

    def __call__(self, f):
        coroutine = gen.coroutine(f)

        @gen_test
        def wrapper(*args, **kargs):
            future = Future()
            future.set_result(self._response)

            with patch.object(AsyncHTTPClient, "fetch", return_value=future):
                with patch.object(Client, "fetch", return_value=future):
                    yield coroutine(*args, **kargs)

        return wrapper
