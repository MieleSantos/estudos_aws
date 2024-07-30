import json
from log import log


def lambda_handler(event, context):

    log(f"Log teste: {event}")
    return {"statusCode": 200, "body": event}
