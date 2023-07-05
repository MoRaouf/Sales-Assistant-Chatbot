from src.ChatChain import SalesChatChain

from dotenv import load_dotenv



#===================================================================================
#--------------------------------------- Keys --------------------------------------
#===================================================================================

# load necessary keys from `.env` file if you will NOT provide it through the app
from dotenv import load_dotenv
load_dotenv()  

#===================================================================================
#------------------------------ Create New DB instance -----------------------------
#===================================================================================

model = "gpt-3.5-turbo"
temperature = 0
first_time_chain = SalesChatChain(model=model, temperature=temperature, use_chainlit=False, create_new_db=True)