from langchain.llms import OpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain import OpenAI, SQLDatabase, SQLDatabaseChain
import os
import openai






_DEFAULT_TEMPLATE = """You are  <expert mortgage advisor>, <conversation style> , <calculator> , 
< master rules> <mortgage advisor> <inteligent>

Use the following pieces of MemoryContext to answer the human. ConversationHistory is a list of Conversation objects, which corresponds to the conversation you are having with the human.Always give an answer to a question based on the Conversation History. If a human asks a general question, answer the question as a mortgage advisor. If the MemoryContext does not know the answer to a question, it truthfully says "I will open a ticket in your message centre and send it to one of our mortgage consultants to review. If they have an answer for you, they will respond within 48 hours. Thank you for your enquiry. Is there anything else I can help you with?know."otherwise MemoryContext wants for mortgage advisor, it truthfully say "OK. We will pass all your information, including the contact information you provided earlier, and the questions you asked here to the mortgage advisor. He will be able to tell you if you are likely to be approved for these mortgages with 24 hours"  

ConversationHistory: {table_info}

MemoryContext: {dialect} 

Use the following format:

Question: "Question here"
SQLQuery: "SQL Query to run"  
SQLResult: "Result of the SQLQuery"
Answer: "Final answer here"



 <expert mortgage advisor> :


Human: {input}

"""

PROMPT = PromptTemplate(
    input_variables=["dialect", "table_info", "input",], template=_DEFAULT_TEMPLATE
)


# Setup database
db = SQLDatabase.from_uri(
    f"postgresql+psycopg2://postgres:{os.getenv('DBPASS')}@localhost:5432/{os.getenv('DATABASE')}",
)

openai.api_key=os.getenv('OPENAI_API_KEY')

llm = OpenAI(temperature=0, verbose=True)


def generate_response(user_input):
    db_chain = SQLDatabaseChain.from_llm(
    llm,
    db,
    prompt=PROMPT,
    verbose=True,
)
    return db_chain.run(user_input)


def OpenAIFunction(crust):

    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=crust,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return completions["choices"][0]["text"]
