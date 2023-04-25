# 🚀 Setup AWS Account

Create an AWS account if you haven't already done so. Go to [https://aws.amazon.com/lambda/](https://aws.amazon.com/lambda/) and click on the "Create a Free Account" button.

# 📥 Clone Repository

- Open this repository: [https://github.com/bhanuduggal/aws_python_tool_template](https://github.com/bhanuduggal/aws_python_tool_template)
- Click on the green button that says 'Use as template'. Using this create your own repository.
- Now clone your newly created repository to your machine.

# 🔑 IAM User Setup and Access Key

1. **Create an IAM user in the AWS Management Console.** To access AWS resources from GitHub Actions, you'll need to create an IAM user with the necessary permissions. You can create a new user with the "Programmatic access" option selected.
2. **Attach the necessary IAM policies to your user.** Depending on the AWS resources you want to access, you'll need to attach the appropriate IAM policies to your user. For example, if you're deploying code to AWS Lambda, you'll need to attach the AWSLambdaFullAccess policy. Other policies I added:
   - AWSCloudFormationFullAccess
   - AmazonS3FullAccess
   - CloudWatchLogsFullAccess
   - IAMFullAccess
3. **Store your AWS access key and secret access key as secrets in your GitHub repository.** To ensure the security of your AWS credentials, you should store them as secrets in your GitHub repository. You can create secrets by going to your repository's Settings > Secrets, and then clicking "New repository secret".

# 💻 Write your code for Lambda

- Rename the directory `tool_name` to your desired name. Also, rename the file `tool_name.py` (found within `tool_name` folder) to a desired name.
- Modify the `lambda_handler` method within `tool_name.py`.
- To install new packages for your work, use `pipenv`. The new packages will get added to `Pipfile` and will get used during deployment.
  - For example, `python -m pipenv install pandas`.

# 📝 Setup Serverless.yaml

- Now in `Serverless.yml`, update the following:
  - `service`: call it as desired.
  - `theLambda`: this is a lambda function identifier. Rename this to what the lambda does.
  - `name`: could be the same as above separated with hyphens.
  - `description`: give a description to your lambda function.
  - `handler`: path to your lambda handler method. If you keep the same structure, then just replace `tool_name` with the name of your own tool name.

# 🚀 Deployment Progress

With the above steps, you should be good to go. On Github, go to the Actions tab to view the deployment progress. 🎉
