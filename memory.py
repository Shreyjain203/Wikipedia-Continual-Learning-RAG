from langchain.memory import ConversationBufferMemory
def memory():
    return ConversationBufferMemory(
        memory_key="chat_history",
        output_key='answer',
        return_messages=False
        )