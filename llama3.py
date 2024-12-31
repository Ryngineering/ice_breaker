from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from third_party_apis.linkedIn_profile import scrape_linkedIn_profile
import os

if __name__ == "__main__":
    load_dotenv()
    # create a prompt template
    summary_template = """
        given the linkedin information {information} about a person i want you to create:
            1. A Short Summary 
            2. two interesting facts about them
    """
    prompt = PromptTemplate.from_template(summary_template)
    llm = ChatOllama(model="llama3")  
    # create a chain . Use StrOutputParser to get the output as a string . If not used , the output will be in the format of content = <value?
    chain = prompt | llm | StrOutputParser();
    gist_endpoint = 'https://gist.githubusercontent.com/Ryngineering/f66d38df4bf875075fab1b0538159334/raw/50cdc1c9666a3f96d172fec061a5a314d9f5283a/linkedIn_profile.json'
    linkedin_data = scrape_linkedIn_profile(gist_endpoint)
    # invoke the chain
    
    print(chain.invoke({"information": linkedin_data}))
