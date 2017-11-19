import json
import logging

from pynamodb.exceptions import DoesNotExist
from activities.activity_model import ActivityTypeModel


def update(event, context):
    # TODO: Figure out why this is behaving differently to the other endpoints
    # data = json.loads(event['body'])
    data = event['body']

    if 'activity_type' not in data and 'checked' not in data:
        return {'statusCode': 422,
                'body': json.dumps({'error_message':
                                    'Trouble updating the activity_type,
                                    'please debug.'})}
    try:
        found_activity_type = \
            ActivityTypeModel.get(hash_key=event['path']['activity_type'])
    except DoesNotExist:
        return {'statusCode': 404,
                'body': json.dumps(
                    {'error_message': 'Activity_type not found'})}

    activity_type_changed = False

    if 'activities' in data and data['activities'] != \
       found_activity_type.activities:
        found_activity_type.activities = data['activities']
        activity_type_changed = True

    if 'checked' in data and data['checked'] != found_activity_type.checked:
        found_activity_type.checked = data['checked']
        activity_type_changed = True

    if activity_type_changed:
        found_activity_type.save()
    else:
        logging.info('Nothing changed did not update')

    return {'statusCode': 200,
            'body': json.dumps(dict(found_activity_type))}
