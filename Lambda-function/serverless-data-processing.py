#On aws management console go to Lambda service and create a function 
#select an author from scratch
#Name function as Serverless-Data_processing
#Select Runtime as Python 3.7
#Under execution role select Create a new role with basic Lambda permissions
#Click Create Function
#Under Function code we can see the default code in lambda_function.py file

import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }




# Click on configure test event and configure the event
#Click on test and further you can check log in cloud watch
#Go back to Lambda function and under function overview click on trigger and select s3 bucket
#Create Serverless-Data-Processing Bucket and select as well
#Click on add 
#Go to S3 bucket that we created and upload an excel file
#Check monitoring log under cloud watch
#Create a glue job under lambda function called data processing
#go to lamda function and edit code

import json
import boto3


def lambda_handler(event, context):
    # TODO implement
    client=boto3.client('glue')
    client.start_job_run (
        JobName='dataprocessing',
        Arguments ={})
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

Test and deploy 
