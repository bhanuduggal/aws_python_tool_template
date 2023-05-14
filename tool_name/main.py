from env_loader import load_env_variables

def lambda_handler(event, context):
    parameters = load_env_variables()
    REGION = parameters['REGION']
    print(REGION)


if __name__=="__main__":
    lambda_handler(None, None)