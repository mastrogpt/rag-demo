#--web true
import json

def main(_):
    data = {
        "services": [
            {
                "name": "Ambra",
                "url": "openai/ambra"
            },
            {
                "name": "OpenAI",
                "url": "openai/chat"
            },
            {
                "name": "Wordpress",
                "url": "openai/wordpress"
            },
            { 
                "name": "Demo", 
                "url": "mastrogpt/demo",
            },
            { 
                "name": "Calendar", 
                "url": "openai/chat",
            },
            { 
                "name": "Rag", 
                "url": "mastrogpt/rag",
            }  
        ]
    }
    return {"body": data}