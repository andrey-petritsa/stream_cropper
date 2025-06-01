import boto3

import utils


class S3Bucket:
    @classmethod
    def upload_file(cls, file_path_in, file_path_out):
        s3 = boto3.client('s3', endpoint_url='https://storage.yandexcloud.net', region_name='ru-central1')

        bucket_name = 'streamcropper'
        s3.upload_file(file_path_in, bucket_name, file_path_out)

        utils.logger.info(f'File {file_path_in} uploaded to bucket {bucket_name} to {file_path_out}')
