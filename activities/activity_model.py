import os
from datetime import datetime

from pynamodb.attributes import (
    # MapAttribute,
    ListAttribute,
    # NumberAttribute,
    UnicodeAttribute,
    BooleanAttribute,
    UTCDateTimeAttribute
)

from pynamodb.models import Model


# class ActivityMap(MapAttribute):
#    activity_id = NumberAttribute(null=True)
#    activity = UnicodeAttribute(null=True)


class ActivityTypeModel(Model):
    class Meta:
        table_name = os.environ['DYNAMODB_TABLE']
        region = 'us-west-2'
        host = 'https://dynamodb.us-west-2.amazonaws.com'

    activity_type = UnicodeAttribute(hash_key=True, null=False)
    activity_type_id = UnicodeAttribute(null=False)
    # activities = ListAttribute(of=ActivityMap, null=True)
    activities = ListAttribute(null=False, default=[])
    checked = BooleanAttribute(null=False)
    createdAt = UTCDateTimeAttribute(null=False, default=datetime.now())
    updatedAt = UTCDateTimeAttribute(null=False)

    def save(self, conditional_operator=None, **expected_values):
        self.updatedAt = datetime.now()
        super(ActivityTypeModel, self).save()

    def __iter__(self):
        for name, attr in self._get_attributes().items():
            yield name, attr.serialize(getattr(self, name))
