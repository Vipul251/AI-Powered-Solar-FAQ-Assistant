import streamlit as st
import faq_data
from langchain_faiss import get_answer_from_faq  # Import the function to retrieve FAQ answers

# Streamlit UI
def main():
    st.title("AI Powered Solar FAQ Assistant")

    # Initialize session state for chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Input field for user query
    user_input = st.text_input("Ask a question about Solar Energy:")

    # Create two buttons side by side
    col1, col2 = st.columns([1, 1])  # Creating two equal-width columns

    with col1:
        get_answer_btn = st.button("Get Answer")

    with col2:
        clear_chat_btn = st.button("Clear Conversation")

    # Fetch answer when "Get Answer" button is clicked
    if get_answer_btn:
        if user_input:
            answer = get_answer_from_faq(user_input)
            response_text = f"**Response**:\n\n{answer}"
            
            # Store conversation in session state
            st.session_state.messages.append({"question": user_input, "answer": response_text})

    # Display conversation history
    for msg in st.session_state.messages:
        st.markdown(f"**Q:** {msg['question']}")
        st.markdown(msg['answer'])
        st.markdown("---")

    # Clear conversation when "Clear Conversation" button is clicked
    if clear_chat_btn:
        st.session_state.messages = []  # Reset chat history
        st.rerun()  # Refresh app to clear output

if __name__ == "__main__":
    main()

# # app.py
# import streamlit as st
# import faq_data
# from langchain_faiss import get_answer_from_faq  # Import the function to retrieve FAQ answers
# import numpy as np
# from sklearn.metrics.pairwise import cosine_similarity
# # Streamlit UI
# def main():
#     st.title("AI Powered Solar FAQ Assistant")

#     # Input field for user query
#     user_input = st.text_input("Ask a question about Solar Energy:")
#     # When the user submits a question
#     if st.button("Get Answer"):
#         if user_input:
#             # Fetch the most relevant FAQ answers based on the query
#             answer = get_answer_from_faq(user_input)
#             st.markdown(f"**Response**:\n\n{answer}")
#         else:
#             st.warning("Please enter a question to get an answer.")
# if __name__ == "__main__":
#     main()
