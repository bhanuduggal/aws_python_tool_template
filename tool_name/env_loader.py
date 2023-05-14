import os
import boto3


def load_env_variables():
    # Load environment variables]
    if 'LAMBDA_TASK_ROOT' in os.environ:
        environment = os.getenv('ENVIRONMENT')
        ssm = boto3.client('ssm', region_name='eu-west-1')
        parameters = {
            'REGION': ssm.get_parameter(Name=f'/{environment}/REGION', WithDecryption=False)['Parameter']['Value'],
    }
    else:
        parameters = {
            'REGION': os.getenv('REGION'),
        }

    return parameters