#!/usr/bin/env python3
# Copyright (c) 2017 James Beedy <jamesbeedy@gmail.com>

import mock
import tempfile
import unittest
from pathlib import Path


from charmhelpers.core import unitdata


class TestActivitiesEndpoint(unittest.TestCase):
    def setUp(self):
        tests_dir = Path(__file__).parent

        tf = tempfile.NamedTemporaryFile(delete=False)
        tf.close()
        self.test_db = Path(tf.name)
        unitdata._KV = self.kv = unitdata.Storage(str(self.test_db))

        self.possible_responses = {
            'create': [
                {
                    'test1':''
                },
                {
                    'test2':''
                },
            ],
            'get': [
                {
                    'test1':''
                },
                {
                    'test2':''
                },
            ],
            'list': [
                {
                    'test1':''
                },
                {
                    'test2':''
                },
            ],
            'update': [
                {
                    'test1':''
                },
                {
                    'test2':''
                },
            ],
            'delete': [
                {
                    'test1':''
                },
                {
                    'test2':''
                },
            ],
        }

        def _request_method_response(request_method):
            return self.possible_responses[request_method]


    def tearDown(self):
        """Defines tearDown procedure
        """

    def test_method_create(self):
        """This function defines the tests for the 'create' request method
        """
        assert False
  

    def test_method_get(self):
        """This function defines the tests for the 'get' request method
        """
        assert False

    def test_method_list(self):
        """This function defines the tests for the list request method
        """
        # Define assert statements here
        # self.assertIsNone()
        # assert not ....
        # assert ... 
        assert False

    def test_method_update(self):
        """This function defines the tests for the update request method
        """
        # Define assert statements here
        # self.assertIsNone()
        # assert not ....
        # assert ... 
        assert False

    def test_method_delete(self):
        """This function defines the tests for the delete request method
        """
        # Define assert statements here
        # self.assertIsNone(None)
        # assert not ....
        # assert ... 
        assert False
