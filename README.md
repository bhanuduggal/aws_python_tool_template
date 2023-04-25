# 🚀 Setup AWS Account

First things first! If you haven't already done so, create an AWS account to access all the amazing features of AWS Lambda. Just click on the "Create a Free Account" button on [this link](https://aws.amazon.com/).

# 📥 Clone Repository

Next, you need to clone this repository: `https://github.com/bhanuduggal/aws_python_tool_template`.

# 🔑 IAM User Setup and Access Key

1. Create an IAM user in the AWS Management Console with "Programmatic access" option selected.
2. Attach the necessary IAM policies to your user, such as AWSLambdaFullAccess, AWSCloudFormationFullAccess, AmazonS3FullAccess, CloudWatchLogsFullAccess, and IAMFullAccess.
3. Store your AWS access key and secret access key as secrets in your GitHub repository by going to your repository's Settings > Secrets, and then clicking "New repository secret". This ensures the security of your AWS credentials.

# 📝 Setup Serverless.yaml

Now, it's time to set up your `serverless.yaml` file.

1. First, rename the directory `tool_name` to your desired name. Also, rename the file `tool_name.py` (found within the `tool_name` folder) to your desired name.
2. Modify the `lambda_handler` method within `tool_name.py`.
3. Update the following in `serverless.yml`:
    - `service`: give it a name that you like.
    - `theLambda`: this is a lambda function identifier, rename it to describe what the lambda does.
    - `name`: could be the same as above separated with hyphens.
    - `description`: give a brief description to your lambda function.

# 👨‍💻 Deployment Progress

Voila! With the above steps, you are ready to go. You can now view the deployment progress by going to the Actions tab on GitHub. Happy coding! 🎉
