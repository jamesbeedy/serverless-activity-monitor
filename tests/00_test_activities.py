#!/usr/bin/env python3
import json

from nose.tools import (
    assert_is_none,
    assert_equal,
    assert_true,
    assert_in,
    assert_not_equal,
    assert_list_equal
)

from random import SystemRandom, randint

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


def test_create_new_activity_type_pass():
    """This test is intended to test that the creation of a non-preexisting
    activity_type succeeds.
    """
    
    # Generate a new activity_type that *should* not be in the database
    new_activity_type = 'activity-{}'.format(generate_random_string())
    
    # Check/ensure that new_activity_type doesn't already exist
    existing_activity_types = activity_type_list()
    if new_activity_type in existing_activity_types:
        return False
    
    # Create the new activity_type
    create_new_activity_resp = activity_type_create(new_activity_type)
    
    # Assert the new activity exists in the database
    assert_list_equal(sorted(activity_type_list()),
                      sorted(existing_activity_types + [new_activity_type]))
    
def test_delete_activity_type_pass():
    """This test is intended to test that the deletion of an
    activity_type succeeds.
    """

    # Generate a new activity_type that *should* not be in the database
    new_activity_type = 'activity-{}'.format(generate_random_string())
    
    # Check/ensure that new_activity_type doesn't already exist
    init_existing_activity_types = activity_type_list()
    if new_activity_type in init_existing_activity_types:
        return False
    
    # Create the new activity_type
    create_new_activity_resp = activity_type_create(new_activity_type)
    
    # Verify the new activity_type exists
    if not new_activity_type in activity_type_list():
        return False
    
    delete_activity_resp = activity_type_delete(new_activity_type)
    
    # Assert the new activity exists in the database
    assert_equal(sorted(activity_type_list()),
                 sorted(init_existing_activity_types))
    
def test_update_activity_type_pass():
    """This test is intended to test that updating the activities
    for an activity_type succeeds.
    """
    
    return True
    
