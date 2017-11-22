#!/usr/bin/env python3
import requests

from unittest.mock import Mock, patch

from nose.tools import assert_is_not_none, assert_true

from cli.activities_lib import (
    url,
    get_activity_crud
)


# Base Case: Assert response is not none
def test_activities_get_not_none():
    # Make api request, get response
    response = requests.get(url())
    # Confirm that the request-response is ok
    assert_true(response.ok)



@patch('serverless-activity-monitor.cli.activities_lib.get_activity_crud')
def test_getting_todos(mock_get):
    # Configure the mock to return a response with an OK status code.
    mock_get.return_value.ok = True

    # Call the service, which will send a request to the server.
    response = get_activity_crud('list')


    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(response)



