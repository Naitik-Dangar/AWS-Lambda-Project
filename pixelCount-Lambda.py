import json
import urllib.parse
import boto3
import cv2

sns_client = boto3.client('sns')
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # TODO implement
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(record['s3']['object']['key'])
        
    local_path = "/tmp/" + str(key)

    # Download file from S3
    s3.download_file(bucket, key, local_path)


    img = cv2.imread(local_path)
    if img is None:
        result_data = "Error: invalid file" + str(key)
    else: 
        height, width = img.shape[:2]
        pixel_cnt = height * width
        result_data = "Image: " + str(key) + "\nTotal_Pixels: " + str(pixel_cnt)

    response = sns_client.publish(
        TopicArn='arn:aws:sns:Example',
        Subject='Lambda Result Notification',
        Message=result_data
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!'),
        'key': key,
        'result': result_data,
        'local_path': local_path
    }
