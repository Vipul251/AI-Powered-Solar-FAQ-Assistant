# Solar FAQ Assistant

This is an AI-powered FAQ chatbot that helps users get answers related to solar energy. The chatbot uses **FAISS** for efficient search over a set of FAQ data.

---

## Solar Industry AI Assistant - Project Documentation

### Overview
This project is designed to create an AI-powered assistant specializing in solar industry consulting. It provides accurate and helpful information about solar energy to both technical and non-technical users. The assistant leverages Natural Language Processing (NLP) techniques and a custom FAQ dataset stored in a FAISS vector index, allowing it to retrieve relevant answers to user queries about solar panel technology, installation processes, maintenance, cost analysis, and more.

### Project Goal
The goal of this project is to create an intelligent assistant that:
- Responds to user queries about solar energy.
- Provides detailed, accurate, and contextually relevant answers from a predefined knowledge base.

---

## Technologies Used
- **Streamlit**: For building the web interface.
- **LangChain**: For managing the interaction with the knowledge base and handling responses.
- **FAISS**: For efficient similarity search over a large set of embeddings.
- **SentenceTransformer**: For converting text queries and documents into vector embeddings for similarity comparison.
- **Pickle**: For saving and loading the preprocessed data and FAISS index.
- **Custom Data**: The FAQ dataset is stored in FAISS for efficient retrieval.

---

## Components

### 1. Streamlit Frontend (`app.py`)
This component is responsible for creating the user interface. It allows users to input their queries about solar energy and get responses from the knowledge base. The chat history is maintained during the session.

#### Key Features:
- **Text Input**: Users can type in their queries about solar energy.
- **Response Display**: The assistant displays relevant answers.
- **Conversation History**: All interactions are logged and displayed during the session.
- **Clear Chat**: Users can clear the chat history at any time.

### 2. Backend (`langchain_faiss.py`)
This component handles the logic for querying the knowledge base. It uses FAISS to perform similarity search over the preprocessed FAQ data stored as embeddings. The SentenceTransformer model is used to embed user queries and compare them against stored embeddings.

#### Key Features:
- **FAISS Index**: The index stores vector representations of FAQs for efficient similarity search.
- **Custom Data Storage**: The FAQ data is stored in FAISS for fast and efficient retrieval.
- **Sentence Embedding**: The SentenceTransformer model converts user queries and stored FAQs into vector embeddings.
- **Query Handling**: The `get_answer_from_faq` function retrieves the most relevant FAQ answers based on the user's query.

---

## How It Works
1. **FAISS Indexing**: The FAQ data is preprocessed and converted into vector embeddings using the SentenceTransformer model. These embeddings are indexed using FAISS to allow efficient nearest-neighbor search.
2. **User Query Handling**: When a user submits a query, the query is embedded using the same model, and a similarity search is performed against the FAISS index.
3. **Answer Retrieval**: The top **k** most similar FAQs are retrieved, and their corresponding answers are displayed to the user.
4. **Streamlit UI**: The user interacts with the app through a clean interface, submitting queries and receiving responses in real-time.

---

## File Structure
```
/solar-faq-assistant
│
├── /knowledge_base
│   ├── faq_index.faiss              # FAISS index file for FAQ embeddings
│   ├── faq_vectors.pkl              # Preprocessed FAQ embeddings
│
├── app.py                           # Streamlit app for the user interface
├── langchain_faiss.py               # Backend logic for querying FAISS index
├── faq_data.py                      # Contains FAQ data (questions and answers)
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation (this file)
```

---

## Setup Instructions

### 1. Clone the Repository:
```bash
git clone https://github.com/your-repo/solar-faq-assistant.git
cd solar-faq-assistant
```

### 2. Create a Virtual Environment (Optional):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies:
```bash
pip install -r requirements.txt
```

### 4. Run the App:
```bash
streamlit run app.py
```

---

## Example Use Cases

**User:** "What is the lifespan of a solar panel?"

**Assistant:** "The typical lifespan of a solar panel is 25-30 years, depending on the quality of the panels and the environmental conditions."

**User:** "How much does it cost to install solar panels?"

**Assistant:** "The cost of installing solar panels varies depending on the location, the size of the installation, and the type of panels. On average, residential solar installations cost between $10,000 to $30,000."

---

## Future Improvements
- **Expansion of Knowledge Base**: Include more detailed topics such as solar energy incentives, international market trends, and advanced technical information.
- **Multi-Language Support**: Implement support for multiple languages to reach a wider audience.
- **Real-time Data Integration**: Integrate with APIs for real-time data on solar energy production, cost, and regulations.

---

## Code Quality
The code is organized into two main components: a frontend (Streamlit) and a backend (LangChain and FAISS). The code is modular, with functions for embedding queries, searching the knowledge base, and displaying results. Error handling is implemented to ensure that invalid queries or missing data do not break the application.

---

## Contact
For queries or contributions, feel free to reach out:
**Email:** stl.1547vipul@gmail.com

