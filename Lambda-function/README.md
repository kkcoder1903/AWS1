# AWS Lambda Function for Launching EC2 Instance and Creating Auto Scaling Group

This AWS Lambda function is designed to automate the process of launching an EC2 instance and creating an Auto Scaling group using the Boto3 library for Python. This README provides an overview of the function and instructions for its usage.

## Prerequisites

Before using this AWS Lambda function, ensure the following prerequisites are met:

- **AWS Account**: You should have an AWS account with the necessary permissions to create EC2 instances and Auto Scaling groups.

- **AWS Lambda**: Set up an AWS Lambda function with the appropriate IAM permissions to create EC2 instances and configure Auto Scaling groups.

- **Boto3 Library**: The Lambda function uses the Boto3 library to interact with AWS services. Ensure that the library is included in your Lambda deployment package.

## Configuration

The Lambda function can be configured using environment variables or by directly modifying the script. The following parameters should be customized:

- **ImageId**: Set the desired Amazon Machine Image (AMI) ID to use for the EC2 instance.

- **InstanceType**: Define the EC2 instance type (e.g., 't2.micro').

- **AutoScalingGroupName**: Specify the name for the Auto Scaling group.

- **LaunchConfigurationName**: Provide a name for the launch configuration.

- **MinSize and MaxSize**: Set the minimum and maximum sizes for the Auto Scaling group.

## Function Execution

When the Lambda function is triggered, it performs the following actions:

1. It uses the Boto3 library to create an EC2 instance with the specified configuration.

2. The function retrieves the instance ID of the created EC2 instance.

3. It creates an Auto Scaling group with the provided name and launch configuration.

4. The function attaches the newly created EC2 instance to the Auto Scaling group.

## Deployment

Deploy the Lambda function in your AWS environment. You can set up triggers (e.g., API Gateway, CloudWatch Events) to invoke the Lambda function.

## Monitoring and Error Handling

Implement proper monitoring, logging, and error handling in your Lambda function to capture any issues that may occur during the EC2 instance creation and Auto Scaling group configuration.

## Security and IAM Permissions

Ensure that the Lambda function's execution role has the necessary IAM permissions to create EC2 instances, launch configurations, and Auto Scaling groups.

## Testing

Test the Lambda function thoroughly to verify that it correctly launches EC2 instances and configures Auto Scaling groups based on your provided parameters.

