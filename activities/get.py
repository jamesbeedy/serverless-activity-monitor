import json

from pynamodb.exceptions import DoesNotExist
from activities.activity_model import ActivityTypeModel


def get(event, context):

    try:
        found_activity_type = \
            ActivityTypeModel.get(hash_key=event['path']['activity_type'])
    except DoesNotExist:

        return {'statusCode': 404,
                'body': json.dumps(
                     {'error_message': 'Activity_type was not found.'})}

    return {'statusCode': 200,
            'body': json.dumps(dict(found_activity_type))}
