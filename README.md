# EC2 Stop Lambda Function

This project contains a Lambda function that stops all running EC2 instances in a specified AWS region daily at 7 PM UTC. I chose my local time which was around 4:31pm. The function is triggered automatically using Amazon EventBridge (formerly CloudWatch Events).

## Features
- Stops all running EC2 instances dynamically.
- Scheduled execution using Amazon EventBridge.
- Logs detailed activity to AWS CloudWatch for monitoring.

## Prerequisites
Before deploying this Lambda function, ensure you have the following:
- An AWS account with permissions to manage EC2 instances and create Lambda functions.
- AWS CLI installed and configured on your machine.
- Python 3.x installed locally.

## Project Structure
The project consists of the following files:
- `lambda_function.py`: The main Lambda function script that stops EC2 instances.
- `README.md`: This file, providing an overview of the project.

## How It Works
1. **Lambda Function**:
   - The `lambda_function.py` script uses the `boto3` library to interact with AWS services.
   - It queries all running EC2 instances in the specified region and stops them.

2. **EventBridge Trigger**:
   - An EventBridge rule is set up to trigger the Lambda function daily at 7 PM UTC.
   - I chose my local time which was 4:31pm

## Deployment Instructions
1. **Set Up AWS CLI**:
   - Install and configure the AWS CLI:
     ```bash
     aws configure
     ```
   - Ensure your credentials have the necessary permissions (`AmazonEC2FullAccess` and `AWSLambdaBasicExecutionRole`).

2. **Deploy the Lambda Function**:
   - Zip the `lambda_function.py` file:
     ```bash
     zip lambda_code.zip lambda_function.py
     ```
   - Create a new Lambda function in the AWS Console:
     - Runtime: Python 3.x.
     - Upload the `lambda_code.zip` file.
     - Set the handler to `lambda_function.lambda_handler`.

3. **Set Up EventBridge Rule**:
   - Go to the EventBridge Dashboard.
   - Create a new rule with the following cron expression:
     ```
     31 16 * * ? *
     ```
   - Set the target to your Lambda function.

4. **Test the Setup**:
   - Manually trigger the Lambda function or wait for the scheduled time.
   - Check the CloudWatch logs to verify the function executed successfully.

