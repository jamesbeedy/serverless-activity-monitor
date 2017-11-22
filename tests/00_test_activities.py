#!/usr/bin/env python3
import json

from nose.tools import (
    assert_list_equal
)

from random import SystemRandom, randint

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
    new_activity_type = 'activity-type-{}'.format(generate_random_string())

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
    new_activity_type = 'activity-type-{}'.format(generate_random_string())

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
    assert_list_equal(sorted(activity_type_list()),
                      sorted(init_existing_activity_types))


def test_update_activity_type_pass():
    """This test is intended to test that updating the activities
    for an activity_type succeeds.
    """
    # Generate a new activity_type that *should* not be in the database
    new_activity_type = 'activity-type-{}'.format(generate_random_string())

    # Check/ensure that new_activity_type doesn't already exist
    init_existing_activity_types = activity_type_list()
    if new_activity_type in init_existing_activity_types:
        return False

    # Create the new activity_type
    create_new_activity_resp = activity_type_create(new_activity_type)

    # Verify the new activity_type exists
    if not new_activity_type in activity_type_list():
        return False

    # Verify the new activity_type has no activities associated initially
    # as it shouldn't contain any activities immediately following initialization
    if not len(activity_type_get(new_activity_type)) == 0:
        return False

    new_activities = ['activity-{}'.format(generate_random_string()),
                      'activity-{}'.format(generate_random_string())]
    update_activity_type_resp = \
        activity_type_update(new_activity_type, new_activities)

    assert_list_equal(sorted(new_activities),
                      sorted(activity_type_get(new_activity_type)))


def test_list_activity_type_pass():
    """Test that listing activity_types returns the expected
    activity_types
    """
    # Generate a new activity_type that *should* not be in the database
    new_activity_type = 'activity-type-{}'.format(generate_random_string())

    # Check/ensure that new_activity_type doesn't already exist
    init_existing_activity_types = activity_type_list()
    if new_activity_type in init_existing_activity_types:
        return False

    # Create the new activity_type
    create_new_activity_resp = activity_type_create(new_activity_type)

    # Assert the new activity_type exists in the list, and that it is
    # equal to the initial activity_type_list + new_activity_type
    assert_list_equal(sorted(init_existing_activity_types + [new_activity_type]),
                      sorted(activity_type_list()))


def test_get_activities_for_activity_type_pass():
    """Test that getting the activities for a singleton activity_type
    returns the expected result
    """
    # Generate a new activity_type that *should* not be in the database
    new_activity_type = 'activity-type-{}'.format(generate_random_string())

    # Check/ensure that new_activity_type doesn't already exist
    init_existing_activity_types = activity_type_list()
    if new_activity_type in init_existing_activity_types:
        return False

    # Create the new activity_type
    create_new_activity_resp = activity_type_create(new_activity_type)

    # Assert that no activities exist for the new activity_type
    assert_list_equal([], activity_type_get(new_activity_type))
