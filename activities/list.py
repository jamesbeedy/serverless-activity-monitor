import json

from activities.activity_model import ActivityTypeModel


def list(event, context):
    """List activity_types
    """
    results = ActivityTypeModel.scan()
    return {'statusCode': 200,
            'body': json.dumps(
                {'items': [dict(result) for result in results]})}
