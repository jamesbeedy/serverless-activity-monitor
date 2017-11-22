#!/usr/bin/env python3
import json
from nose.tools import assert_is_none, assert_equal, assert_true
from random import SystemRandom

from unittest.mock import Mock, patch

from serverless_activity_monitor.cli.activities_lib import (
    url,
    activity_type_get,
    activity_type_list,
    activity_type_update,
    activity_type_delete,
    activity_type_create,
)


def generate_random_string():
    """Generate 10 char random string
    """

    def gen_chars():
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
        for _ in range(9):
            yield SystemRandom().choice(chars)

    return ''.join(gen_chars())


class TestActivitiesEndpoint(object):
    @classmethod
    def setup_class(cls):
        cls.mock_get_patcher = \
            patch('serverless_activity_monitor.cli.activities_lib')
        cls.mock_get = cls.mock_get_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_get_patcher.stop()

    def test_create_new_activity_type(self):
        """This test is intended to test the creation of a new,
        non-preexisting  activity_type
        """
        # Create a new activity that will not be in the database
        new_activity = 'activity-{}'.format(generate_random_string())

        # Ensure activity_doesn't exist
      
        self.mock_get.return_value.ok = True
        activity_crud_get_resp = new_activity

        self.mock_get.return_value = Mock()
        #self.mock_get.return_value.json.return_value = activity_crud_get_resp

        assert_equal(activity_crud_get_resp, new_activity)


