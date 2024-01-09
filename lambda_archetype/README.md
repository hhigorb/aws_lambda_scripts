# lambda-archetype

Welcome to the AWS Lambda Functions project! This guide will help you set up and deploy your application effortlessly using Terraform. Before we dive in, make sure you have your AWS CLI configured with the following steps:

1. Open your terminal and run the command aws configure.
2. Enter your Access Key, Secret Key, and preferred Region when prompted.
3. Run the command `export AWS_PROFILE="your-aws-profile"`

## Setting Up a Virtual Environment

It's best practice to use a virtual environment to manage your project dependencies. Choose one of the following methods:

####  Using Virtualenvwrapper

1. Run the command to locate your Python3 installation: `which python3`
2. Create a virtualenv named 'aws_lambda': `mkvirtualenv aws_lambda --python=/usr/bin/python3`
3. Activate the virtualenv: `source /Users/higor.silva/.virtualenvs/aws_lambda/bin/activate` (Adjust the path according to your setup)

#### Using Built-in venv

1. Create a virtual environment named 'aws_lambda': `python3 -m venv aws_lambda`
2. Activate the virtualenv: `source aws_lambda/bin/activate`

Remember to install your project dependencies using:

```terminal
pip install -r requirements.txt
```

# Deploy the Project on AWS

1. Go to AWS ECR and create a private repository following the `company-de-project-name` pattern.

2. Navigate to the "application" folder and correctly fill in the "env.sh" file with names matching the ECR repository and the `AWS_ECR_ACCOUNT_ID` variable. Run the command `source env.sh`.

3. Open the Makefile and change the value of the `APP_NAME` variable to match the ECR repository name. Execute the command `make docker/push TAG=company-de-project-name`.

If you encounter the following error:

```terminal
ERROR: permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/_ping": dial unix /var/run/docker.sock: connect: permission denied
make: *** [Makefile:14: docker/build] Erro 1
```

Run the following command:

`sudo chmod 666 /var/run/docker.sock`

If you encounter the following error:

```terminal
ERROR: failed to solve: public.ecr.aws/lambda/python:3.9: pulling from host public.ecr.aws failed with status code [manifests 3.9]: 403 Forbidden
make: *** [Makefile:14: docker/build] Erro 1
```

Run the following command:

`aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws`

After that, the image will be published in the ECR.

1. Before running Terraform, correctly configure the `aws.tf` file with the AWS ECR correct data. After that, run the Terraform commands in the project's root.

```terminal
terraform init
terraform plan -var="env_name=lambda_function_name"
terraform apply -var="env_name=lambda_function_name"
```

**REMEMBER:** Always use the company-de-project-name pattern.

# Test the project locally

To execute and test the project locally, go to the `application` folder and run the commands:

```terminal
make docker/build 
make docker/run 
```

Afterwards, your application will be running. To send events to it, run this command in another terminal:


```terminal
make docker/test
```
