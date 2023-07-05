from langchain.chat_models import ChatOpenAI

from langchain.chains import RetrievalQA
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from src.DeepLake import DeepLakeLoader
from src import prompts
import chainlit as cl


class SalesChatChain:
    """
    A class for interacting with an AI chat model and helping sales agent in answering customer objection queries.
    """

    def __init__(self, model, temperature, use_chainlit=True, open_api_key:str = None, create_new_db=False):
        """
        Initializes a SalesChatChain instance.

        """

        # OpenAI Chat model parameters  
        self.model_name=model
        self.temperature = temperature
        
        if use_chainlit:
            # OpenAI Chat model, getting user key for Chainlit
            self.llm_chat = ChatOpenAI(model=self.model_name, temperature=self.temperature, openai_api_key=open_api_key)
        else: 
            # OpenAI Chat model
            self.llm_chat = ChatOpenAI(model=self.model_name, temperature=self.temperature)

        if create_new_db:
            # New Deep Lake instance
            self.deeplake = DeepLakeLoader(org_id="moraouf", 
                                        dataset_name="sales_assistant", 
                                        source_data_path='data/sales_data.txt', 
                                        create_new_db = True)
        else:
            # New Deep Lake instance
            self.deeplake = DeepLakeLoader(org_id="moraouf", 
                                        dataset_name="sales_assistant", 
                                        source_data_path='data/sales_data.txt')


    def query(self, query:str = None):
        """
        Generates a response from customer objection query. Queries a Deep Lake DB for relevant guidelines.

        Parameters:
            query (str): The query to generate a response for.

        Returns:
            str: The response generated from chain
        """

        #Chat Prompt Tempalate
        system_message_prompt = SystemMessagePromptTemplate.from_template(prompts.OBJECTION_GUIDELINES_PROMPT)
        human_template="Customer objection: {question}"
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

        chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

        chain_type_kwargs = {"prompt": chat_prompt}  

        # create a retrieval chain
        qa = RetrievalQA.from_chain_type(
            llm=self.llm_chat, 
            chain_type="stuff", 
            retriever=self.deeplake.db.as_retriever(), 
            chain_type_kwargs=chain_type_kwargs
        )

        # return qa.run(query)
        return qa



       










