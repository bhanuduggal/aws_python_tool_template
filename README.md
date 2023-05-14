# 🚀 Setup AWS Account

Create an AWS account if you haven't already done so. Go to [https://aws.amazon.com/lambda/](https://aws.amazon.com/lambda/) and click on the "Create a Free Account" button.

# 📥 Clone Repository

- Open this repository: [https://github.com/bhanuduggal/aws_python_tool_template](https://github.com/bhanuduggal/aws_python_tool_template)
- Click on the green button that says 'Use as template'. Using this create your own repository.
- Makes sure you include the branches that come with this repository. The deployment workflows depend on these branches - {dev, main and prod}
- Now clone your newly created repository to your machine.

# 🔄 Change Workflow

1. New Feature or Fix: When a new feature needs to be added or a bug needs to be fixed, the developer creates a new branch from the main branch.
2. Development: The developer works on their changes in this new branch.
3. Merge into Dev: Once the changes are complete and have been tested locally, the developer merges their branch into the dev branch.
4. Testing in Dev: The merged changes are tested in the dev environment. If any issues are found, they are fixed in the dev branch.
5. Merge into Main: After successful testing in the dev environment, the dev branch is merged into the main branch. At this point, the main branch is the most up-to-date branch.
6. Release: When a release is ready, the main branch is merged into the prod branch, and the changes are deployed to the prod environment.
7. Emergency Fix: If the main branch goes awry, the prod branch is merged back into the main branch to bring it back to the last known stable state.
```
       +---+   New Branch    +-----+  Merge  +-----+  Merge  +-----+
       |Main| <------------- |Work  | ------->| Dev | ------->| Main|
       +-+-+                 +--+--+          +--+--+         +--+--+
         |                      |               |              |
         |                      |               |              |
         | Merge (Emergency)    |               |              |
         V                      |               |              |
       +---+                    |               |              |
       |Prod|                   |               |              |
       +---+                    |               |              |
                                |               |              |
                                |               |              |
                                +---------------+              |
                                | Merge after Testing         |
                                |                             |
                                |                             |
                                |                             |
                                |                             |
                                | Merge for Release          |
                                +----------------------------->
```

# 🔑 IAM User Setup and Access Key

1. **Create an IAM user in the AWS Management Console.** To access AWS resources from GitHub Actions, you'll need to create an IAM user with the necessary permissions. You can create a two users with the "Programmatic access" option selected.
   - Name them dev_github and prod_github
2. **Attach the necessary IAM policies to your user.** Depending on the AWS resources you want to access, you'll need to attach the appropriate IAM policies to your user. For example, if you're deploying code to AWS Lambda, you'll need to attach the AWSLambdaFullAccess policy. Other policies I added:
   - AWSCloudFormationFullAccess
   - AmazonS3FullAccess
   - CloudWatchLogsFullAccess
   - IAMFullAccess
   - CloudWatchEventsFullAccess
   - AmazonS3FullAccess
   - AmazonSSMReadOnlyAccess
3. **Store your AWS access key and secret access key as secrets in your GitHub repository.** To ensure the security of your AWS credentials, you should store them as secrets in your GitHub repository. You can create secrets by going to your repository's Settings > Secrets, and then clicking "New repository secret".

# 💻 Write your code for Lambda

- Rename the directory `tool_name` to your desired name. Also, rename the file `main.py` (found within `tool_name` folder) to a desired name.
- Modify the `lambda_handler` method within `tool_name.py`.
- To install new packages for your work, use `pipenv`. The new packages will get added to `Pipfile` and will get used during deployment.
  - For example, `python -m pipenv install pandas`.

**Parameters and Secrets** For best practice, store the parameters in a .env locally and use an AWS service. I have added an example to use AWS Parameter Store in 'main.py' but there could be other services.

**Attach the necessary IAM policies to your lambda role.** As you will build any lambda's and store any variables in parameter store, you will need the a policy along the following lines. This will need adding to the lambda role that will be created when the code is deployed. **The lambda will not work if the policy is not attached.**
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "ssm:GetParameter",
            "Resource": "arn:aws:ssm:eu-west-1:{aws_account}:parameter/*"
        }
    ]
}
```


# 📝 Setup Serverless.yaml

- Now in `Serverless.yml`, update the following:
  - `service`: call it as desired.
  - `theLambda`: this is a lambda function identifier. Rename this to what the lambda does.
  - `name`: could be the same as above separated with hyphens.
  - `description`: give a description to your lambda function.
  - `handler`: path to your lambda handler method. If you keep the same structure, then just replace `tool_name` with the name of your own tool name.

# 🚀 Deployment Progress

With the above steps, you should be good to go. On Github, go to the Actions tab to view the deployment progress. 🎉
