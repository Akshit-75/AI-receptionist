import chromadb 

# create new folder called emergency_vector_data
chroma_client = chromadb.PersistentClient("emergency_vector_data") 

collection = chroma_client.get_or_create_collection(name="emergency_ai") 

with open('data\emergency.txt') as f:
    emergency_care = [line.strip() for line in f if line.strip()]
    emergency = [line.split(":")[0] for line in emergency_care]

print(len(emergency_care)) 
print(emergency)

print("Starting add collection")

collection.upsert(
    documents = emergency_care, 
    metadatas = [{"emergency": emergency[i]} for i in range(len(emergency_care))], 
    ids = [f"id{i}" for i in range(1, len(emergency_care)+1)],
)

print("Done collection of data")

print(collection.get())


# results = collection.query(
#     query_texts=["I'm having a heart attack"],
#     n_results=1
# )


# print(results['distances'],results['documents'])