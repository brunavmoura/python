from google.cloud import storage
import threading
bucket_name = "nomedobucket"
directory_names = ["diretóriodoseubucket/", "diretório2doseubucket/"]
client = storage.Client()
bucket = client.get_bucket(bucket_name)
storage_client = storage.Client()
def delete_s3_objects(blob):
    try:
        print(blob.name)
        return blob.delete()
    except Exception as e:
        raise e
def main():
    try:
        threads = []
        for directory_name in directory_names:
            blobs = storage_client.list_blobs(bucket_name, prefix=directory_name)
            for blob in blobs:
                process = threading.Thread(target=delete_s3_objects, args=(blob,))
                threads.append(process)
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
    except Exception as e:
        raise e
if __name__ == "__main__":
    main()
