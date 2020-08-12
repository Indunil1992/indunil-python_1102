import boto3
s3 = boto3.client("s3")

def handler(event, context):
    try:
        data = s3.list_objects(
            Bucket="indu-s3-12",
            MaxKeys=10
        )
    except BaseException as e:
        print(e)
        raise(e)
    
    return {"message": "Successfully executed"}
