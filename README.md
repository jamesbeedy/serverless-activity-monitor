# Activity Monitor

Simple CRUD interface using [Serverless](https://serverless.com)

AND 

Python CLI.

AND

Python importable module


## Web API Usage Examples
The CRUD API is capible of preforming the following operations on an `activity_type`:

    - create
    - list
    - get
    - update
    - delete


### Create an `activity_type`
```bash
$ curl -X POST https://XXXXXXXXXX.execute-api.us-west-2.amazonaws.com/dev/activities \
    --data '{ "activity_type": "academia" }'
```
```json
{
  "activities": [],
  "activity_type": "academia",
  "activity_type_id": "9f364508-cd4e-11e7-8aac-7eba570dda78",
  "checked": false,
  "createdAt": "2017-11-19T17:24:40.986875+0000",
  "updatedAt": "2017-11-19T17:25:22.036794+0000"
}
```

### List all `activity_type`

```bash
$ curl https://XXXXXXXXXX.execute-api.us-west-2.amazonaws.com/dev/activities
```
```json
{
  "items": [
    {
      "activities": [],
      "activity_type": "academia",
      "activity_type_id": "f38c11b4-cd4e-11e7-8aac-7eba570dda78",
      "checked": false,
      "createdAt": "2017-11-19T17:24:40.986875+0000",
      "updatedAt": "2017-11-19T17:27:43.527703+0000"
    },
    {
      "activities": [],
      "activity_type": "personal",
      "activity_type_id": "fcb23340-cd4e-11e7-8aac-7eba570dda78",
      "checked": false,
      "createdAt": "2017-11-19T17:24:40.986875+0000",
      "updatedAt": "2017-11-19T17:27:58.877055+0000"
    },
    {
      "activities": [],
      "activity_type": "sports",
      "activity_type_id": "cb3c65e2-cd4e-11e7-8aac-7eba570dda78",
      "checked": false,
      "createdAt": "2017-11-19T17:24:40.986875+0000",
      "updatedAt": "2017-11-19T17:26:35.896703+0000"
    }
  ]
}
```

### Get a singleton `activity_type`

```bash
https://XXXXXXX.execute-api.us-west-2.amazonaws.com/dev/activities/<activity_type>
```
Where `<activity_type>` is an `activity_type` created in a previous step (must exist in the db).

```bash
$ curl https://XXXXXXX.execute-api.us-west-2.amazonaws.com/dev/activities/academia
```
```json
{
  "statusCode": 200,
  "body": "{\"activities\": [], \"activity_type\": \"academia\", \"activity_type_id\": \"f38c11b4-cd4e-11e7-8aac-7eba570dda78\", \"checked\": false, \"createdAt\": \"2017-11-19T17:24:40.986875+0000\", \"updatedAt\": \"2017-11-19T17:27:43.527703+0000\"}"
}
```

### Update the `activities` associated with an `activity_type`
```bash
$ curl -H 'Content-Type: application/json' -X PUT \
    --data '{ "activities":["baseball","football","baseketball"], "checked": true }' \
    https://99un5l50x1.execute-api.us-west-2.amazonaws.com/dev/activities/sports
```
```json
{
  "statusCode": 200,
  "body": "{\"activities\": [{\"S\": \"baseball\"}, {\"S\": \"football\"}, {\"S\": \"baseketball\"}], \"activity_type\": \"sports\", \"activity_type_id\": \"cb3c65e2-cd4e-11e7-8aac-7eba570dda78\", \"checked\": true, \"createdAt\": \"2017-11-19T17:24:40.986875+0000\", \"updatedAt\": \"2017-11-19T20:46:42.265935+0000\"}"
}
```

### Delete an `activity_type`

```bash
$ curl -X DELETE https://XXXXXXXXXX.execute-api.us-west-2.amazonaws.com/dev/activities/sports
```
```json
{"statusCode": 204}
```

## Activites CLI
The activities API is accompanied by a python CLI.
```bash
$ cli/activity-monitor --help
usage: activity-monitor [-h] [-a ACTIVITY_TYPE] [-d DATA [DATA ...]] [-v]
                        [-f FORMAT]
                        operation

activity-monitor

positional arguments:
  operation             Web request method to make

optional arguments:
  -h, --help            show this help message and exit
  -a ACTIVITY_TYPE, --activity-type ACTIVITY_TYPE
                        Data to add to request
  -d DATA [DATA ...], --data DATA [DATA ...]
                        Activity type to update - only used with "update"
                        operation
  -v, --version         show program's version number and exit
  -f FORMAT, --format FORMAT
                        format to json
```

### Example usage:

#### Create
```bash
$ cli/activity-monitor create --activity-type health
Created activity: health

```

#### List
```bash
$ cli/activity-monitor list
Types of activities:

academia
personal
```

#### Get
```bash
$ cli/activity-monitor get --activity-type personal
Activities associated with personal:


```

#### Update
```bash
$ cli/activity-monitor update --activity-type health --data diet exercise
Updated activity: health

```

#### Delete
```bash
$ cli/activity-monitor delete --activity-type health
Deleted activity: health

```

## Python Package
The python package lets you interact with the activities API from python.

Just import the `activities_lib` from the `cli` directory to use it inline.
```bash
$ python3 -i cli/activities_lib.py 
```
```python
from activities_lib import get_activity_crud

# Create

activities = get_activity_crud("create", "personal")
print(activities)
{'activity_type': 'personal', 'createdAt': '2017-11-19T21:22:57.750130+0000', 'checked': False, 'updatedAt': '2017-11-19T21:29:06.092158+0000', 'activities': [], 'activity_type_id': 'abd407b0-cd70-11e7-ae97-72c2f18af503'}

# List
activities = get_activity_crud("list")
print(activities)
{'items': [{'checked': False, 'createdAt': '2017-11-19T17:24:40.986875+0000', 'activities': [], 'activity_type_id': 'f38c11b4-cd4e-11e7-8aac-7eba570dda78', 'updatedAt': '2017-11-19T17:27:43.527703+0000', 'activity_type': 'academia'}, {'checked': False, 'createdAt': '2017-11-19T17:24:40.986875+0000', 'activities': [], 'activity_type_id': 'fcb23340-cd4e-11e7-8aac-7eba570dda78', 'updatedAt': '2017-11-19T17:27:58.877055+0000', 'activity_type': 'personal'}]}

# Get
activities = get_activity_crud("get", "academia")
print(activities)
{'statusCode': 200, 'body': '{"activities": [], "activity_type": "academia", "activity_type_id": "f38c11b4-cd4e-11e7-8aac-7eba570dda78", "checked": false, "createdAt": "2017-11-19T17:24:40.986875+0000", "updatedAt": "2017-11-19T17:27:43.527703+0000"}'}

# Update
activities = get_activity_crud("update", "personal", ["reading","sleeping"])
print(activities)
{'statusCode': 200, 'body': '{"activities": [{"S": "reading"}, {"S": "sleeping"}], "activity_type": "personal", "activity_type_id": "abd407b0-cd70-11e7-ae97-72c2f18af503", "checked": true, "createdAt": "2017-11-19T21:22:57.750130+0000", "updatedAt": "2017-11-19T21:30:53.996112+0000"}'}

# Delete
activities = get_activity_crud("delete", "personal")
activities
{'statusCode': 204}

```

## Testing
Two forms of tests are packaged with this application.

    - linting
    - functional

### Linting
The linting functionality has is built into the `Makefile`. To lint the code in this repository run:
```bash
make test
```

### Functional
Functional tests run as part of the labda service/framework.


#### Copyright
* AGPLv3 (see `copyright` file)

#### Authors
* James Beedy <jamesbeedy@gmail.com>

