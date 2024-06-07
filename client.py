from minio import Minio

class MinIOClient:
    """
    Class to represent a MinIO client.

    Attributes:
    client: Instance of the MinIO client.
    """
    def __init__(self, endpoint, access_key, secret_key):
        self.client = Minio(endpoint, access_key=access_key, secret_key=secret_key, secure=False)

    def bucket_exists(self, bucket_name):
        """
        Check if a bucket exists.

        Parameters:
        bucket_name (str): Name of the bucket.

        Returns:
        bool: True if the bucket exists, False otherwise.
        """
        return self.client.bucket_exists(bucket_name)

    def make_bucket(self, bucket_name):
        """
        Create a bucket if it does not exist.

        Parameters:
        bucket_name (str): Name of the bucket.
        """
        if not self.bucket_exists(bucket_name):
            self.client.make_bucket(bucket_name)

    def list_buckets(self):
        """
        List all buckets.

        Returns:
        list: List of buckets.
        """
        return self.client.list_buckets()

    def fput_object(self, bucket_name, object_name, file_path):
        """
        Upload a file to a bucket.

        Parameters:
        bucket_name (str): Name of the bucket.
        object_name (str): Name of the object.
        file_path (str): Path to the file.
        """
        self.client.fput_object(bucket_name, object_name, file_path)

    def get_object(self, bucket_name, object_name):
        """
        Get an object from a bucket.

        Parameters:
        bucket_name (str): Name of the bucket.
        object_name (str): Name of the object.

        Returns:
        Object: Object from the bucket.
        """
        return self.client.get_object(bucket_name, object_name)