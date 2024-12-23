from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()
    # create a prompt template
    prompt = PromptTemplate.from_template("Describe {country} in less than 100 words")
    # create a chat openai model
    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")
    # create a chain
    chain = prompt | llm
    # invoke the chain
    print(chain.invoke({"country": "France"}))
