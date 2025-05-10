import boto3

# Replace with your EC2 region
REGION = 'us-east-1'

def lambda_handler(event=None, context=None):
    try:
        print("Starting the Lambda function...")  # Confirm the script starts

        # Initialize the EC2 client
        print("Initializing the EC2 client...")
        ec2 = boto3.client('ec2', region_name=REGION)
        print("EC2 client initialized successfully.")

        # Describe instances that are running
        print("Fetching all running EC2 instances...")
        response = ec2.describe_instances(
            Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
        )
        print(f"Describe Instances Response: {response}")  # Log the raw response for debugging

        # Extract instance IDs
        print("Extracting instance IDs from the response...")
        instance_ids = []
        for reservation in response.get('Reservations', []):
            for instance in reservation.get('Instances', []):
                instance_id = instance.get('InstanceId')
                if instance_id:
                    instance_ids.append(instance_id)

        # Log the instance IDs
        if instance_ids:
            print(f"Found running instances: {instance_ids}")
        else:
            print("No running instances found.")
            return {"statusCode": 200, "body": "No running instances to stop."}

        # Stop the instances
        print(f"Stopping instances: {instance_ids}")
        ec2.stop_instances(InstanceIds=instance_ids)
        print(f"Stopped instances: {instance_ids}")

        return {"statusCode": 200, "body": f"Stopped instances: {instance_ids}"}

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return {"statusCode": 500, "body": f"Error: {str(e)}"}

# Call the handler function directly for local testing
if __name__ == "__main__":
    lambda_handler()