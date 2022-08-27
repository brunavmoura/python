# Script Python para Deletar Objetos no Google Cloud Storage

O Script é executado em threads para multiprocessamento, sendo bastante rápido para a exclusão de milhares de objetos.


## Instalar o gsutil

Para instalar o gsutil veja a [documentação](https://cloud.google.com/storage/docs/gsutil_install#linux).

Depois autorize o Cloud SDK através dos comandos abaixo:


```
gcloud auth login
gcloud config set project YOUR-PROJECT-ID
gcloud auth application-default login
gcloud auth list
```


## Instalar a lib do Google Cloud Storage

```
pip install google-cloud-storage
```


## Configurar a Service Account no GCP

A Service Account precisa de permissões de Storage Admin, Storage Object Admin ou roles apropriadas para a execução do seu script.


## Executar o Script Python

Antes da execução do script, insira o Nome do seu Bucket GCS na linha 3 em "nomedobucket" e os Diretórios que deseja deletar na linha 4 em "diretóriodoseubucket/", quantos diretórios forem necessários.

Para execução do script é necessário ter o Python 3 instalado.

```
python3 python_storage_delete_objects.py
```


## Executar o Script via Gsutil

Caso não precise excluir diversos diretórios simultaneamente, pode-se utilizar o gsutil.

```
gsutil -m rm -r gs://nomedoseubucket
```
A opção -m habilita o multiprocessamento do gsutil.


## Referências

- [Google Cloud - Excluir Buckets](https://cloud.google.com/storage/docs/deleting-buckets?hl=pt_br#storage-delete-bucket-python)
- [Google Cloud - Excluir um Objeto](https://cloud.google.com/storage/docs/deleting-objects?hl=pt_br#prereq-cli)
- [How to use gsutil and Python to deal with files in Google Cloud Storage](https://lynn-kwong.medium.com/how-to-use-gsutil-and-python-to-deal-with-files-in-google-cloud-storage-fc4f430b3b28)
- [Cloud Storage with Gsutils & Python Client Library](https://medium.com/google-cloud/using-google-cloud-storage-5b9d3f570945)
- [Blobs Objects](https://googleapis.dev/python/storage/latest/blobs.html)
- [Google APIs Python Storage](https://github.com/googleapis/python-storage/blob/HEAD/samples/snippets/storage_delete_bucket.py)
- [Google APIs Python Storage - Issue #36 - Parellelism](https://github.com/googleapis/python-storage/issues/36)
- [StackOverFlow - Delete Files from Google Cloud Storage](https://stackoverflow.com/questions/10555080/delete-files-from-google-cloud-storage)
- [Como usar o ThreadPoolExecutor em Python 3](https://www.digitalocean.com/community/tutorials/how-to-use-threadpoolexecutor-in-python-3-pt)
- [Google Cloud Storage - Blob Delete](https://cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob#google_cloud_storage_blob_Blob_delete)
- [Google Cloud Commands - Remove objects](https://cloud.google.com/storage/docs/gsutil/commands/rm)

# teste github bruna