import os 
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

load_dotenv()

api = os.getenv("GROQ_API")

llm = ChatGroq(api_key=api,
               model="openai/gpt-oss-120b",
               model_kwargs={
                   "response_format":{
                       "type":"json_object"
                   }})

def extract_text(article_text):

    prompt = """
    From the below news article, extract revenue and eps in JSON format containing
    following keys: 'revenue_actual','revenue_expected', 'eps_actual', 'eps_expected'.

    Each value should have a unit such as million or billions.

    Only return the valid JSON.  No preamble.

    {format_instructions}

    Article
    ========
    {article}
    """

    global llm 
    
    parser = JsonOutputParser()
    pt = PromptTemplate.from_template(prompt,
                                      partial_variables={
                                          "format_instructions":parser.get_format_instructions()
                                      })
    chain = pt | llm | parser
    
    try:
        result = chain.invoke({"article":article_text})
        return result
    except OutputParserException as e:
        raise OutputParserException("Failed to parse model output as JSON. " \
        "Possibly malformed output or context is too large.") from e
    
