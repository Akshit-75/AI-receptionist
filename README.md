# AI_receptionist
AI receptionist - works as a human receptionist in healthcare.

[![AI Healthcare Receptionist](https://img.youtube.com/vi/EfwcaErl3g4/maxresdefault.jpg)](https://www.youtube.com/watch?v=EfwcaErl3g4)


This project is an AI-driven healthcare receptionist system built using asyncio and Flask API. It is designed to handle both emergency situations and user messages. The system uses asynchronous programming to manage tasks efficiently and interact with external APIs to provide responses based on context.


## Features

- **Emergency and Message Handling**: The system differentiates between emergencies and messages, providing appropriate responses based on the user's input.
- **Contextual Responses**: The AI receptionist uses a combination of vector searches (via ChromaDB) and a language model (via Groq API) to provide context-aware responses.
- **Artificial Delays**: The system simulates a 10-second delay when querying the database, ensuring that asynchronous tasks are handled efficiently without blocking the user interaction.
- **Task Coordination**: Conversations with the user continue while the system performs background tasks. If the background task (LLM call) is still running after the conversation ends, the system prints a "Please hold for a second..." message before displaying the response.
- **Error Handling**: Basic error handling is implemented for unrecognized user input and missing responses, ensuring that the system handles unexpected scenarios gracefully.

## Technologies Used

- **Python**: The core language for the system.
- **Asyncio**: For managing asynchronous tasks and handling multiple operations concurrently.
- **Groq API**: A language model API used to generate responses based on context.
- **ChromaDB**: A vector database for storing and querying embeddings related to emergency scenarios.
- **Flask**: The framework for building the API.
  
## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/ai-healthcare-receptionist.git
   cd ai-healthcare-receptionist 
   ```

2. **Install Dependencies**: Create a virtual environment and install the required packages:
    ```bash 
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Set Environment Variables**: need to set your GROQ_API_KEY as an environment variable to authenticate with the Groq API, Groq API is free for consumers.
    ```bash 
    set GROQ_API_KEY="groq_api_key"
    ```

4. **Run the Program**: Start the program using Python 
    ```bash
    mkdir emergency_vector_data
    python vector_collection.py
    python app.py 
    ```

## Example Workflow

1. The user inputs "emergency".
2. They describe the emergency situation.
3. The system continues the conversation by asking for the user's location.
4. While the conversation is happening, the system performs a 10-second database call simulation.
5. If the conversation ends before the 10 seconds are up, the system prints a hold message before showing the AI-generated response.
6. If the AI-generated response is ready before the conversation ends, the response is displayed immediately.

## Potential Corner Cases

- **Unrecognized User Input**: The system handles invalid user inputs by prompting for a valid response.
- **Empty Vector Search Results**: If no matching context is found for the emergency, the user is informed that the request cannot be processed.
- **API Errors**: Basic error handling for missing API keys or failed API calls ensures the system doesn’t crash unexpectedly.

## Future Enhancements

- **Improve RAG workflow**: make RAG and vector search pipeline more robust as new data added.

## References: 
- Umar Jamil: RAG https://youtu.be/rhZgXNdhWDY?si=1PCSQdHSaitmwaUy
- ChromaDB Documentation: https://docs.trychroma.com/getting-started
- Asychronous Programming: https://youtube.com/playlist?list=PLhTjy8cBISEpfMihZ8E5yynf5sqPCcBXD&si=s6aEu6OAlkyZjOPr  --> buildwithpython playlist youtube series
- ChromaDB: https://realpython.com/chromadb-vector-database/#get-started-with-chromadb-an-open-source-vector-database
- Daniel Bourke RAG: 
