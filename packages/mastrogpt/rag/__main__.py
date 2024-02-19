#--kind python:default
#--web true
#--param MINIO_ACCESS_KEY $MINIO_ACCESS_KEY
#--param MINIO_SECRET_KEY $MINIO_SECRET_KEY
#--param MINIO_DATA_BUCKET $MINIO_DATA_BUCKET
#--param MINIO_HOST $MINIO_HOST
#--param MINIO_PORT $MINIO_PORT

import json
from minio import Minio
from haystack.document_stores.in_memory import InMemoryDocumentStore
#from haystack.document_stores import InMemoryDocumentStore
import chevron



def question(args):
    try:
        minio_host = args['MINIO_HOST']
        minio_port = args['MINIO_PORT']
        minio_access_key = args['MINIO_ACCESS_KEY']
        minio_secret_key = args['MINIO_SECRET_KEY']
        minio_data_bucket = args['MINIO_DATA_BUCKET']

        minio_client = Minio(
            f"{minio_host}:{minio_port}",
            access_key=minio_access_key,
            secret_key=minio_secret_key,
            secure=False
        )

        objects = minio_client.list_objects(minio_data_bucket)
        
        documents = []

        for obj in objects:
            print("docuemento caricato")
            document = {
                "text": minio_client.get_object(minio_data_bucket, obj.object_name).data.decode('utf-8'),
                "meta": {"name": obj.object_name}
            }
            print(json.dumps(document))
            documents.append(document)

        document_store = InMemoryDocumentStore(use_bm25=True)

        # document_store = MinioDocumentStore(
        #      minio_bucket=minio_data_bucket,
        #      minio_client=minio_client,
        #      base_url=f"http://{minio_host}:{minio_port}/{minio_data_bucket}",
        #      embedding_field=None
        #  )
        print("document store try")
        document_store = InMemoryDocumentStore()
        print("-------")
        # document_store.write_documents(documents)

        query = args.get("input", "describe documents")

        # result = document_store.query(query)

        # print_answers(result, details="medium")
    except:
        print("Error")

def render(src, args):
    with open(src) as f:
        return chevron.render(f, args)
    
def main(args):
    if(args.get("input")):
        print("input is ", args.get("input"))
        question(args)

    out = render("upload.html", args)
    code = 200 if out != "" else 204
    
    return {
        "body": {
            "output":"Hi, here you can ask some questions about your input files",
            "html": out,
            "statusCode": code
        }
    }
