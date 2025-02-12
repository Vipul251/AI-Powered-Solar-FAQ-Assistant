# langchain_faiss.py
import faiss
import pickle
import numpy as np
from langchain.vectorstores import faiss
from sentence_transformers import SentenceTransformer  # Import SentenceTransformer
import faiss
from faq_data import faq_data
# Load FAISS index and vector data from 'knowledge_base' folder
faiss_index = faiss.read_index("knowledge_base/faq_index.faiss")
print("[DEBUG] FAISS index loaded successfully.")

with open("knowledge_base/faq_vectors.pkl", 'rb') as f:
    faq_embeddings = pickle.load(f)
# Initialize the model for embedding user queries
model = SentenceTransformer('all-MiniLM-L6-v2')  # Use the SentenceTransformer to generate embeddings
# Define a function to retrieve answers from the FAQ based on user query
def get_answer_from_faq(query, top_k=3):
    query_embedding = model.encode([query])  # Get the embedding of the user query
    distances, indices = faiss_index.search(np.array(query_embedding).astype('float32'), top_k)
    
    answers = []
    for i in range(top_k):
        question = faq_data[indices[0][i]][0]  # Retrieve question based on index
        answer = faq_data[indices[0][i]][1]    # Retrieve answer based on index
        answers.append(f"**Q: {question}**\nA: {answer}")
    
    return "\n\n".join(answers)