import json
import logging
import uuid

from activities.activity_model import ActivityTypeModel


def create(event, context):

    data = json.loads(event['body'])

    if 'activity_type' not in data:
        logging.error('Validation Failed')
        return {'statusCode': 422,
                'body': json.dumps(
                    {'error_message': "Couldn't create the activity item."})}

    if not data['activity_type']:
        logging.error('Validation Failed - activity_type empty. %s', data)
        return {'statusCode': 422,
                'body': json.dumps(
                    {'error_message':
                     "Couldn't create the activity_type item. "
                     "activity_type was empty."})}

    a_activity_type = ActivityTypeModel(activity_type_id=str(uuid.uuid1()),
                                        activity_type=data['activity_type'],
                                        checked=False)

    a_activity_type.save()

    return {'statusCode': 201,
            'body': json.dumps(dict(a_activity_type))}
