from src.DeepLake import DeepLakeLoader

from dotenv import load_dotenv



#===================================================================================
#------------------------------ Create New DB instance -----------------------------
#===================================================================================

org_id = "moraouf"
dataset_name = "sales_assistant"
source_data_path = 'data/sales_data.txt'

db_loader = DeepLakeLoader(org_id, dataset_name, source_data_path)
new_db = db_loader.create_db()