import json
from nose.tools import assert_is_none, assert_equal, assert_true
from unittest.mock import Mock, patch

from cli.activities_lib import (
    url,
    activity_type_get,
    activity_type_list,
    activity_type_update,
    activity_type_delete,
    activity_type_create,
)


class TestActivities(object):
    @classmethod
    def setup_class(cls):
        cls.mock_get_patcher = \
            patch('serverless-activity-monitor.cli.activities_lib.activity_type_get')
        cls.mock_get = cls.mock_get_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_get_patcher.stop()

    def test_activity_type_get(self):
        """This test is intended to test the activity_type_get functionality
        More to come ....
        """
        self.mock_get.return_value.ok = True
        activity_crud_get_resp = activity_type_get('academia')

        self.mock_get.return_value = Mock()
        self.mock_get.return_value.json.return_value = activity_crud_get_resp

        assert_equal(activity_crud_get_response,  )

    def test_getting_todos_when_response_is_not_ok(self):
        self.mock_get.return_value.ok = False
        response = get_todos()

        # If the response contains an error, I should get no todos.
        assert_is_none(response)


