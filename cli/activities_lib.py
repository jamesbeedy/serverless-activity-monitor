#!/usr/bin/env python3
# Copyright (c) 2017 James Beedy <jamesbeedy@gmail.com>

import json
import urllib3
from urllib.parse import urlencode

from serverless_activity_monitor.cli.config import LAMBDA_URL_PREFIX


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


def activity_type_get(activity_type):
    ctxt = {'headers': {'Content-Type': 'application/json'},
            'method': 'GET',
            'url': url(activity_type)}

    http = urllib3.PoolManager()
    r = http.request(**ctxt)
    r_dict = json.loads(json.dumps(json.loads(r.data.decode())))
    if not r_dict['statusCode'] == 200:
        return None
    else:
        return [item['S'] for item in json.loads(r_dict['body'])['activities']]


def activity_type_create(activity_type):
    create_args = {'activity_type': activity_type}
    encoded_data = json.dumps(create_args).encode('utf-8')

    ctxt = {'body': encoded_data,
            'headers': {'Content-Type': 'application/json'},
            'method': 'POST',
            'url': url()}

    http = urllib3.PoolManager()
    r = http.request(**ctxt)
    if not r.status == 201:
        return None
    else:
        return "success"


def activity_type_list():
    ctxt = {'method': 'GET',
            'url': url()}

    http = urllib3.PoolManager()
    r = http.request(**ctxt)
    return [item['activity_type'] for item in
            json.loads(r.data.decode())['items']]


def activity_type_update(activity_type, data):
    update_args = {'activities': data,
                   'checked': True}
    encoded_data = json.dumps(update_args).encode('utf-8')

    ctxt = {'body': encoded_data,
            'headers': {'Content-Type': 'application/json'},
            'method': 'PUT',
            'url': url(activity_type)}

    http = urllib3.PoolManager()
    r = http.request(**ctxt)
    if json.loads(json.dumps(json.loads(r.data.decode())))['statusCode'] == 200:
        return "success"
    else:
        return "fail"



def activity_type_delete(activity_type):
    ctxt = {'headers': {'Content-Type': 'application/json'},
            'method': 'DELETE',
            'url': url(activity_type)}

    http = urllib3.PoolManager()
    r = http.request(**ctxt)
    if json.loads(r.data.decode())['statusCode'] == 204:
        return "success"
    else:
        return "fail"


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
