import boto3

def lambda_handler(event, context):

    # Get the EC2 client
    ec2 = boto3.client('ec2')

    # Create an EC2 instance
    response = ec2.run_instances(
        ImageId='ami-01234567890abcdef0',
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1
    )

    # Get the instance ID
    instance_id = response['Instances'][0]['InstanceId']

    # Create an Auto Scaling group
    response = ec2.create_auto_scaling_group(
        AutoScalingGroupName='my-auto-scaling-group',
        LaunchConfigurationName='my-launch-configuration',
        MinSize=1,
        MaxSize=2
    )

    # Attach the instance to the Auto Scaling group
    response = ec2.attach_instances(
        AutoScalingGroupName='my-auto-scaling-group',
        InstanceIds=[instance_id]
    )

    return {
        'statusCode': 200,
        'body': json.dumps('EC2 instance launched and attached to Auto Scaling group.')
    }
