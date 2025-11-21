import os 
from groq import Groq 
import chromadb

def search_vector(user_input): 

    client = chromadb.PersistentClient("emergency_vector_data")

    collection = client.get_collection(name="emergency_ai")

    results = collection.query(
        query_texts=[user_input],
        n_results=1
    )

    # check if the distance is less than 0.5 then return the document
    if results['distances'][0][0] > 0.5: 
        return results['documents'][0]
    
    return None 

def call_llm_groq(user_input, context):

    client = Groq(
        api_key=os.environ.get('GROQ_API_KEY'),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"you're an helpful ai receptionist,if the context is None, answer by saying 'i am not able you answer your query' , answer user_question based only on context, avoid adding anything by your self.USER_QUESTION: {user_input},CONTEXT: {context}"
        }], 
        model="llama3-8b-8192",
    )

    response = chat_completion.choices[0].message.content
    return response 

def classify_emergency(user_input):

    client = Groq(
        api_key=os.environ.get('GROQ_API_KEY')
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"check if the given text is relevant to medical condition or not TEXT: {user_input}, Answer strictly in one word either 'yes' or 'no' "
        }], 
        model="llama3-8b-8192",
    )

    response = chat_completion.choices[0].message.content

    return response 