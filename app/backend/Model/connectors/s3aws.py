import boto3

class S3AwsConnector:
    def __init__(self, connector_name, properties):
        self.connector_name = connector_name

        self.ACCESS_KEY = properties["access_key"]
        self.SECRET_ACCESS_KEY = properties["secret_access_key"]
        self.REGION = properties["region"]

        self.CONN = boto3.resource(
                service_name='s3',
                region_name=self.REGION,
                aws_access_key_id=self.ACCESS_KEY,
                aws_secret_access_key=self.SECRET_ACCESS_KEY
        )

    def connection_test(self):
        for bucket in self.CONN.buckets.all():
            print(bucket.name)
        return str("DONE")

    def get_schema(self, data):
        for bucket in self.CONN.buckets.all():
            print(bucket.name)
        return str("DONE")

    def execute(self, request):
        bucket_name = request["bucket_name"]
        file_name = request["file_name"]
        
        my_bucket = self.CONN.Bucket(bucket_name)

        for my_bucket_object in my_bucket.objects.all():
            print(my_bucket_object.key)

        obj = self.CONN.Object(bucket_name, file_name)
        obj.get()['Body'].read().decode('utf-8') 
        body = obj.get()['Body'].read()
        return body