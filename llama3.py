from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()
    # create a prompt template
    prompt = PromptTemplate.from_template("Describe {country} in less than 100 words")
    llm = ChatOllama(model="llama3")  
    # create a chain . Use StrOutputParser to get the output as a string . If not used , the output will be in the format of content = <value?
    chain = prompt | llm | StrOutputParser();
    # invoke the chain
    print(chain.invoke({"country": "France"}))
