#!/usr/bin/env python3
import json

from nose.tools import (
    assert_is_none,
    assert_equal,
    assert_true,
    assert_in,
    assert_list_equal
)

from random import SystemRandom

from unittest.mock import Mock, patch
import sys

sys.path.append('..')


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
            patch('serverless_activity_monitor.cli.activities_lib.activity_type_get')
        cls.mock_get = cls.mock_get_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_get_patcher.stop()

    def test_create_new_activity_type_pass(self):
        """This test is intended to test the creation of a non-preexisting
        activity_type succeeds.
        """
        self.mock_get.return_value.ok = True

        # Generate a new activity_type that *should* not be in the database
        new_activity_type = 'activity-{}'.format(generate_random_string())

        # Check/ensure that new_activity_type doesn't already exist
        existing_activity_types = activity_type_list()
        if new_activity_type in existing_activity_types:
            return False

        self.mock_get.return_value = Mock()
        self.mock_get.return_value.json.return_value = existing_activity_types + [new_activity_type]

        # Create the new activity_type
        create_activity_resp = activity_type_create(new_activity_type)

        # Assert the new activity exists in the database
        assert_list_equal(sorted(activity_type_list()), sorted(existing_activity_types + [new_activity_type]))
