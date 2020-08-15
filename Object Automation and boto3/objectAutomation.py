## Code submitted by Haiying Man

#Code to try to get the names of the images automatically listed
#key = names of the images in the s3 bucket (ex: flood.png)
#object = the images itself

#import boto3
#custom_session = boto3.session.Session(profile_name="dev_root")
#s3_re = custom_session.resource(service_name="s3", region_name="us-east-1")

#for each_object_info in s3_re.objects.all():
#    print(each_object_info.name)

#import boto3
#s3_resource = boto3.client("s3")
#objects = s3_resource.list_objects(Bucket="pdfimagesbucket")#[Contents]
#if len(objects)>0:
#    print("objects exists")
#for object in objects:
#    print(object["Key"])


import boto3
s3 = boto3.client('s3')
s3.list_objects_v2(Bucket='pdfimagesbucket')

def get_s3_keys(bucket):
    """Get a list of keys in an S3 bucket."""
    keys = []
    resp = s3.list_objects_v2(Bucket=bucket)
    for obj in resp['Contents']:
        keys.append(obj['Key'])
    print(keys)
