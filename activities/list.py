import json

from activities.activity_model import ActivityTypeModel


def list(event, context):

    # fetch all activities from the database
    results = ActivityTypeModel.scan()

    # create a response
    return {'statusCode': 200,
            'body': json.dumps(
                {'items': [dict(result) for result in results]})}
