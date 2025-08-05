import streamlit as st
from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

st.set_page_config(page_title="Q&A with Transformers")
st.title("🤖 Question Answering Web App")
st.markdown("Ask questions based on the context you provide.")

context = st.text_area("📜 Enter the context passage:")
question = st.text_input("❓ Enter your question:")

if st.button("Get Answer"):
    if context and question:
        with st.spinner("Thinking..."):
            result = qa_pipeline(question=question, context=context)
            st.success(f"**Answer:** {result['answer']}")
    else:
        st.warning("Please provide both context and question.")
