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


class TestActivitiesEndpoint(object):
    @classmethod
    def setup_class(cls):
        cls.mock_get_patcher = \
            patch('serverless-activity-monitor.cli.activities_lib.activity_type_get')
        cls.mock_get = cls.mock_get_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_get_patcher.stop()

    def test_create_new_activity_type(self):
        """This test is intended to test the creation of a new,
        non-preexisting  activity_type
        """
        # Create a new activity that will not be in the database
        new_activity = \
            'activity-{}'.format(
                ''.join(random.choice(string.lowercase) for x in range(X)))

        # Ensure activity_doesn't exist
      
        self.mock_get.return_value.ok = True
        #activity_crud_get_resp = 

        #self.mock_get.return_value = Mock()
        #self.mock_get.return_value.json.return_value = activity_crud_get_resp

        #assert_equal(activity_crud_get_response,  )


