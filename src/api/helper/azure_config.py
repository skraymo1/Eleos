import os
from dotenv import load_dotenv 

class AzureConfig:
    def __init__(self):
        load_dotenv()
        self.azure_endpoint: str = os.getenv("AZURE_OPENAI_API_ENDPOINT")
        self.azure_openai_api_key: str = os.getenv("AZURE_OPENAI_API_KEY")
        self.azure_openai_api_version: str = os.getenv("AZURE_OPENAI_API_VERSION")
        self.azure_emdedding_deployment: str = os.getenv("AZURE_OPENAI_API_EMBEDDINGS_DEPLOYMENT_NAME")
        self.azure_deployment: str = os.getenv("AZURE_OPENAI_API_DEPLOYMENT_NAME")
        self.vector_store_address: str = os.getenv("AZURE_AISEARCH_ENDPOINT")
        self.vector_store_password: str = os.getenv("AZURE_AISEARCH_KEY")
        self.index_name: str = os.getenv("AZURE_ENV_NAME")
        self.blob_storage_url: str = os.getenv("AZURE_BLOB_STORAGE_URL")
        self.blob_container_name: str = os.getenv("AZURE_BLOB_STORAGE_CONTAINER")
        self.history_store_address: str =  os.getenv("AZURE_COSMOSDB_ENDPOINT")
        self.history_store_password: str =  os.getenv("AZURE_COSMOSDB_KEY")
        self.history_connection_string: str =  os.getenv("AZURE_COSMOSDB_CONNECTION_STRING")
        self.history_store_database: str =  os.getenv("AZURE_COSMOSDB_DATABASE_NAME")
        self.history_store_container: str =  os.getenv("AZURE_COSMOSDB_CONTAINER_NAME")