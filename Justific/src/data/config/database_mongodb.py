import os
from dotenv import load_dotenv

load_dotenv()

database_infos = {
    'url_connection': os.getenv('JUSTIFIC_DB_MONGO_URL_CONNECTION'),
    'database_name': 'justific_db'
}
