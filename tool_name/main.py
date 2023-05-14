import os
from env_loader import load_env_variables

def lambda_handler(event, context):
    parameters = load_env_variables()
    REGION = parameters['REGION']
    environment = 'Local' if os.getenv('ENVIRONMENT') == None else os.getenv('ENVIRONMENT')
    print(f'{environment} - Lambda is working successfully in {REGION}.')


if __name__=="__main__":
    lambda_handler(None, None)