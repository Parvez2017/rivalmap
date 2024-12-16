from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter

from . import OPENAI_API_KEY

llm = ChatOpenAI(temperature=0, model_name="gpt-4o", 
                 api_key=OPENAI_API_KEY)

def make_chunks(content):
    text_splitter = RecursiveCharacterTextSplitter(
        # Set a really small chunk size, just to show.
        chunk_size=1000,
        chunk_overlap=40,
        length_function=len,
        is_separator_regex=False,
    )
    chunks = text_splitter.create_documents(content)
    return chunks

def summarize(content):
    map_prompt = ChatPromptTemplate.from_messages(
        [("system", """Write a short and concise insight from the following text, focusing on the key findings in bullet points.:\\n\\n{context}""")]
    )
    map_chain = map_prompt | llm | StrOutputParser()
    chunks = [content[i:i + 8000] for i in range(0, len(content), 8000)]
    summary = map_chain.invoke({"context": chunks})
    return summary