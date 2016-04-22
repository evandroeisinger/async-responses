# -*- coding: utf-8 -*-

from tornado.testing import AsyncTestCase
from tornado.testing import gen_test


class TestAsyncResponses(AsyncTestCase):

    @gen_test
    def test_http_fetch_mock(self):
        pass
