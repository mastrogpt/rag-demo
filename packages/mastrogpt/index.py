#--web true
import json

def main(_):
    data = {
        "services": [
            { 
                "name": "Rag", 
                "url": "mastrogpt/rag",
            }  
        ]
    }
    return {"body": data}