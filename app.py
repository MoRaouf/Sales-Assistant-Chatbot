import chainlit as cl
from src.ChatChain import SalesChatChain

from dotenv import load_dotenv


#===================================================================================
#--------------------------------------- Keys --------------------------------------
#===================================================================================

# load necessary keys from `.env` file if you will NOT provide it through the app
from dotenv import load_dotenv
load_dotenv()  

#===================================================================================
#----------------------------------- Chainlit App ----------------------------------
#===================================================================================

model = "gpt-3.5-turbo"
temperature = 0

@cl.langchain_factory(use_async=False)
def factory():

    # user_env = cl.user_session.get("env")

    chain = SalesChatChain(model=model, temperature=temperature, use_chainlit=False, create_new_db=False)

    return chain.query()
