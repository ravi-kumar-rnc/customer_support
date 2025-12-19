from langchain_astradb import AstraDBVectorStore
from dotenv import load_dotenv
import os
import pandas as pd
from data_ingestion.data_transform import data_converter
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE = os.getenv("ASTRA_DB_KEYSPACE")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

os.environ["GOOGLE_API_KEY"]=GOOGLE_API_KEY
os.environ["ASTRA_DB_API_ENDPOINT"]=ASTRA_DB_API_ENDPOINT
os.environ["ASTRA_DB_APPLICATION_TOKEN"]=ASTRA_DB_APPLICATION_TOKEN
os.environ["ASTRA_DB_KEYSPACE"]=ASTRA_DB_KEYSPACE

class ingest_data:
    def __init__(self):
        print("Data Ingestion class initialized")
        self.embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-005")
        self.data_conv = data_converter()

    def data_ingestion(self, status):
        data_conv = data_converter()
        docs = data_conv.data_transformation()
        vectorstore = AstraDBVectorStore(
            embedding=self.embeddings,
            collection_name="flipkart-chatbot-db",
            astra_db_api_endpoint=ASTRA_DB_API_ENDPOINT,
            astra_db_application_token=ASTRA_DB_APPLICATION_TOKEN,
            namespace=ASTRA_DB_KEYSPACE
        )

        storage = status
        if storage == None:
            doc = self.data_conv.data_transformation()
            inserted_ids=vectorstore.add_documents(docs)
            print(f"Data Ingestion completed. Inserted IDs: {inserted_ids}")

if __name__ == "__main__":
    data_ingestion = ingest_data()