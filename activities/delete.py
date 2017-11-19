import json

from pynamodb.exceptions import DoesNotExist, DeleteError
from activities.activity_model import ActivityTypeModel


def delete(event, context):
    try:
        found_activity_type = \
            ActivityTypeModel.get(hash_key=event['path']['activity_type'])
    except DoesNotExist:
        return {'statusCode': 404,
                'body': json.dumps(
                    {'error_message': 'Activity_type was not found'})}
    try:
        found_activity_type.delete()
    except DeleteError:
        return {'statusCode': 400,
                'body': json.dumps(
                    {'error_message': 'Unable to delete the activity_type'})}

    # create a response
    return {'statusCode': 204}
