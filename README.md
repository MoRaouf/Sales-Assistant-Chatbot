# Sales-Assistant-Chatbot 💬

AI-powered sales assistant chatbot that helps sales representatives in answering customer objections. It's developed using [OpenAI](https://openai.com/)'s `gpt-3.5-turbo` model, [LangChain](https://github.com/hwchase17/langchain) & [Deep Lake](https://github.com/activeloopai/deeplake) as a Vector Store.


Dataset
---
The app uses [this](https://blog.hubspot.com/sales/handling-common-sales-objections) as a knowledge base, located in the data folder. To use your own knowledge base:

1. Put your knowledge base in the `data` folder in the form of a text file
2. Update the path in `source_data_path` variable in `src/ChatChain.py` to the path of your knowledge base
3. Adjust the `split_data` method in `DeepLake.py` to split your document effectively.


Setup
---
1. Clone this repository:
    ```
    git clone https://github.com/MoRaouf/Sales-Assistant-Chatbot.git
    ```
2. Set up the virtual environment and all required dependencies by:
  * Setting up a `python=3.8` virtual environment
  * run: `pip install -r requirements.txt`

3. Add your OpenAI API key & Activeloop Deep Lake key in .env` file

4. Create a new database instance & save your data in it 
    ```
    python src/NewDB.py
    ```

5. Change directory & run Chainlit app:
    ```
    cd Sales-Assistant-Chatbot
    chainlit run app.py
    ```
6. Open a web browser and go to http://localhost:8000 to access the application.



License
---
[MIT License](https://github.com/e-johnstonn/SalesCopilot/blob/master/LICENSE)
