import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    bucket_name = "deepika-day1-s3-demo"
    file_name = "hello.txt"

    response = s3.get_object(Bucket=bucket_name, Key=file_name)
    content = response['Body'].read().decode('utf-8')

    print("File content:", content)

    return {
        'statusCode': 200,
        'body': content
    }
