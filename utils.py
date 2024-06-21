import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import OpenAI
from langchain.chains.llm import LLMChain
from langchain_core.prompts import ChatPromptTemplate

def load_environment_variables():
    """Load environment variables from the .env file."""
    _ = load_dotenv(find_dotenv())  # read local .env file

def initialize_openai_api():
    """Initialize the OpenAI API with the API key from the environment variables."""
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")
    return api_key

def create_prompt_template():
    """Create and return a LangChain prompt template."""
    return ChatPromptTemplate.from_template("""
        Identify the following items from the review text: 
        - Sentiment (Positive or Negative)
        - Is the reviewer expressing anger? (True or False)
        - Is the reviewer content? (True or False)
        - Item purchased by reviewer
        - Manufacturer of the item

        The review is delimited with triple backticks. \
        Format your response as a JSON object with \
        "Sentiment", "Anger", "Content", "Item" and "Brand" as the keys.
        If the information isn't present, use "Unknown" as the value. \
        Make the response as short as possible.\
        Format the Anger and Content values as boolean.

        Review text: '''{review}'''
    """)

def create_chain():
    """Create and return an LLMChain using LangChain."""
    llm = OpenAI(model="gpt-3.5-turbo", temperature=0)
    prompt_template = create_prompt_template()
    return LLMChain(llm=llm, prompt=prompt_template)


def process_review(chain, review):
    """Process a single review using the provided chain and return the response."""
    return chain.run({"review": review})

def process_reviews(chain, reviews):
    """Process a list of reviews and return the results."""
    results = []
    for review in reviews:
        response = process_review(chain, review)
        results.append(response)
    return results

