#!/usr/bin/env python3
# Copyright (c) 2017 James Beedy <jamesbeedy@gmail.com>

import json
import urllib3
from urllib.parse import urlencode

from config import LAMBDA_URL_PREFIX


# Disable ssl warnings for dev
urllib3.disable_warnings()


def url(activity=None):
    """Assemble url
    """

    if not activity:
        BASE_URL = \
            ('https://{}.execute-api.us-west-2.amazonaws.com'
             '/dev/activities'.format(LAMBDA_URL_PREFIX))
    else:
        BASE_URL = \
            ('https://{}.execute-api.us-west-2.amazonaws.com'
             '/dev/activities/{}'.format(LAMBDA_URL_PREFIX, activity))
    return BASE_URL


def get_activity_crud(operation, activity_type=None, data=None, format=None):
    """Preform CRUD operation

    operation (string) (valid choices):
        'create', 'list', 'get', 'update', 'delete'

    returns: response as dict
    """

    ctxt = {}

    if operation == 'create':
        create_args = {'activity_type': activity_type}
        encoded_data = json.dumps(create_args).encode('utf-8')
        ctxt['body'] = encoded_data
        ctxt['headers'] = {'Content-Type': 'application/json'}
        ctxt['method'] = 'POST'
        ctxt['url'] = url()

    elif operation == 'list':
        ctxt['method'] = 'GET'
        ctxt['url'] = url()

    elif operation == 'get':
        ctxt['headers'] = {'Content-Type': 'application/json'}
        ctxt['method'] = 'GET'
        ctxt['url'] = url(activity_type)

    elif operation == 'update':
        update_args = {'activities': data,
                       'checked': True}
        encoded_data = json.dumps(update_args).encode('utf-8')
        ctxt['body'] = encoded_data
        ctxt['headers'] = {'Content-Type': 'application/json'}
        ctxt['method'] = 'PUT'
        ctxt['url'] = url(activity_type)

    elif operation == 'delete':
        ctxt['headers'] = {'Content-Type': 'application/json'}
        ctxt['method'] = 'DELETE'
        ctxt['url'] = url(activity_type)

    http = urllib3.PoolManager()
    r = http.request(**ctxt)
    return json.loads(json.dumps(json.loads(r.data.decode())))


def activity_response_output_parser(args, activity_crud):
    """Parse output to something that makes sense for humans
    """

    if args.operation == 'create':
        print("Created activity: {}\n".format(args.activity_type))
        return
    elif args.operation == 'list':
        print("Types of activities:\n")
        for act in activity_crud['items']:
            print(act['activity_type'])
        return
    elif args.operation == 'get':
        print("Activities associated with {}:\n".format(args.activity_type))
        for act in json.loads(activity_crud['body'])['activities']:
            print(act)
        return
    elif args.operation == 'update':
        print("Updated activity: {}\n".format(args.activity_type))
        return
    elif args.operation == 'delete':
        print("Deleted activity: {}\n".format(args.activity_type))
    return
