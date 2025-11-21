import asyncio 
from main import classify_emergency, search_vector, call_llm_groq

async def emergency_or_message():
    user_input = input("Are you in an emergency or would you like to leave a message? ").strip().lower()

    # loop until the user enters a valid input
    while user_input not in ["emergency", "message"]:
        user_input = input("Please select between 'emergency' or 'message': ").strip().lower()

    # if the user wants to leave a message, prompt the user to leave a message and conversation ends here.
    if user_input == "message":
        input("Please leave a message: ")
        print("Thank you for the message, we will forward it to Dr. Adrin.")
        return None
    else: # if the user is in an emergency, prompt the user to describe the emergency and proceed further
        return await emergency()

async def emergency():
    emergency_desc = input("We're here with you, please tell us about your emergency: ")
    
    # here we're using llm to judge if the given text is a medical emergency or not
    response = classify_emergency(emergency_desc)  # should be text-classification model to check if the given text is a medical emergency or not
    print(response)
    if response.strip().lower() == "yes":
        return emergency_desc
    else: # if the given text is not a medical emergency, prompt the user to leave a message or rerequest properly
        print("Sorry, your request can't be processed, as it doesn't seem to be an emergency. Please leave a message instead or Rerequest properly.")
        return await emergency_or_message()
    # return emergency_desc
    
# call llm to search over vector db and then generate a response
async def call_llm(emergency):
    print("Calling to Database")
    response = search_vector(emergency)
    # if the given emergency is found in the database, call llm to generate a response
    if response is not None:
        print("Calling to GROQ")
        await asyncio.sleep(10) # artificially slowed down the response by 15 seconds.
        response = call_llm_groq(emergency, response)
        print(response)
    else: 
        return None 

async def hold_for_second(): 
    await asyncio.sleep(0.1)
    print("Please hold for a second........")

async def making_conversation(): 
    user_area = input("I'm checking what you should do immediately, meanwhile can you tell me which area are you located right now?")
    print(f"Dr. Adrin will be coming {user_area} immediately, in 10 minutes")

async def main(): 
    # node 1: confirm if the user is in an emergency or would like to leave a message
    response = await emergency_or_message()
    
    # if there is the situation of emergenc
    if response is not None:
        # call llm to search over vector db and then generate a response
        llm_task = asyncio.create_task(call_llm(response)) 
        # while the llm_task is not done, make a conversation with the user
        conversation_task = asyncio.create_task(making_conversation())
        await conversation_task
        user_status = input("arrival be too late?")
        if user_status == "yes":
            if not llm_task.done(): 
                await hold_for_second()
                
        await llm_task
        # if llm_response: 
        # print(llm_response)
        # else: 
            # print("Sorry, we couldn't process your request.Please rerequest or contact emergency services directly.")


if __name__ == "__main__": 
    asyncio.run(main())