import os
import logging

import boto3

logging.getLogger('boto3').setLevel(logging.CRITICAL)
logging.getLogger('botocore').setLevel(logging.CRITICAL)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def handler(event, context):
    logger.debug(event)
    client = boto3.client('ecs')

    response = client.run_task(
        cluster=os.environ['ECSCluster'],
        taskDefinition=os.environ['ECSTaskArn'],
        count=1,
        launchType='FARGATE',
        networkConfiguration={
            'awsvpcConfiguration': {
                'subnets': [
                    os.environ['ECSSubnet'],
                ],
                'securityGroups': [
                    os.environ['ECSSecGroup'],
                ],
                'assignPublicIp': 'ENABLED'
            }
        },
        overrides={
            'containerOverrides': [
                {
                    'name': 'data_from_lambda_to_fargate',
                    'environment': [
                        {
                            'name': "LAMBDA_NAME",
                            'value': context.function_name
                        },
                        {
                            'name': "REQUEST_ID",
                            'value': context.aws_request_id
                        }
                    ]
                }
            ]
        }
    )

    logger.debug(response)
