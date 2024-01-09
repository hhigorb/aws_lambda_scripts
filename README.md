# AWS Lambda Functions 

Welcome to the AWS Lambda Functions project! This guide will help you set up and deploy your application effortlessly using Chalice. Before we dive in, make sure you have your AWS CLI configured with the following steps:

1. Open your terminal and run the command aws configure.
2. Enter your Access Key, Secret Key, and preferred Region when prompted.
3. Run the command `export AWS_PROFILE="your-aws-profile"`

## Setting Up a Virtual Environment

It's best practice to use a virtual environment to manage your project dependencies. Choose one of the following methods:

####  Using Virtualenvwrapper

1. Run the command to locate your Python3 installation: which python3
2. Create a virtualenv named 'aws_lambda': mkvirtualenv aws_lambda --python=/usr/bin/python3
3. Activate the virtualenv: source /Users/higor.silva/.virtualenvs/aws_lambda/bin/activate (Adjust the path according to your setup)

#### Using Built-in venv

1. Create a virtual environment named 'aws_lambda': python3 -m venv aws_lambda
2. Activate the virtualenv: source aws_lambda/bin/activate

Remember to install your project dependencies using:

pip install -r requirements.txt

## Setting up a new chalice project 

To create a new chalice project, just run the following command:

`chalice new-project`

## Testing your Application with local Docker

To test your Application locally with Docker, follow these steps:

1. Build the Dockerfile image.
2. Run the generate_aws_credencials.sh file.
3. Run the test_event_lambda_local.sh file, using the parameters according to your lambda function.

Inside the files you can find some explanations of how to complete your tests.

## Testing your Application with Chalice

To test your Application using Chalice, make sure you have pytest installed on your virtualenv. 

Just run `pytest path_to_your_test_app.py`

The test_app.py is normally found in the tests folder.

## Deploying Your Application with ECR (Docker)

After testing your Application and making sure it's everything all right, just run the deploy_ecr.sh script and follow the instructions within the script itself.

## Deploying Your Application with Chalice

To deploy your application to AWS Lambda, follow these simple steps:

1. Run the command: chalice deploy

That's it! Your application is now deployed and ready to go.

