import json
import urllib.parse
import boto3

s3 = boto3.client('s3')

def validFile(fileObject):
    try:
        contentType = fileObject['ContentType']
        print('Content Type: ' + contentType)
        if not contentType.startswith('text/'):
            print('Content Type ' + contentType + ' not allowed, only text files')
            return False
        return True
    except Exception as e:
        print(e)
        raise e

def s3FileRead(fileObject):
    try:
        print('Start of file read')
        print(fileObject['Body'].read().decode('utf-8'))
        print('End of file read')
    except UnicodeDecodeError as une:
        print('File cannot be decoded as UTF-8')
    except Exception as e:
        print(e)
        raise e
        
def s3FileDelete(bucket, key):
    try:
        print('Deleting file...')
        s3.delete_object(Bucket=bucket, Key=key)
        print('File deleted!')
    except Exception as e:
        print(e)
        raise e

def s3FileUploadEvent(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    try:
        # Get the object from the event and show its content type
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
        print('File "' + key + '" received in S3 bucket "' + bucket + '"')        
        fileObject = s3.get_object(Bucket=bucket, Key=key)
        isValid = validFile(fileObject)
        if isValid:
            s3FileRead(fileObject)
        s3FileDelete(bucket, key)
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e