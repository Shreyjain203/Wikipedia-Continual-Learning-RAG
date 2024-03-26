from langchain import PromptTemplate

def get_prompt_template():
    SYSTEM_PROMPT = """
                    Use the following pieces of context to answer the question 
                    at the end. Each retrieved context will have a symptom that 
                    best describes the issue that user is facing with his device. 
                    The context will also have the solution. Return only this 
                    solution broken down into nicely formatted steps. If you don't
                    know the answer, just print "I don't know", don't try to 
                    make up an answer.
                    """
    input_prompt = """{context}

    Question: {question}
    """
    template = f"""
            {SYSTEM_PROMPT}
            
            {input_prompt} 
            """.strip()

    return PromptTemplate(
        template=template,
        input_variables=["context", "question"]
        )