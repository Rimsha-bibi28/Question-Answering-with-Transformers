TASK 2 – Question Answering System using Transformers
Provided by: Elevvo Pathways

Objective:
Build a Question Answering (QA) system using Hugging Face Transformers and the SQuAD v1.1 dataset. This system takes a context passage and a question, then provides an accurate answer based on that passage.

Project Steps:
1. Load a pre-trained QA model from Hugging Face (DistilBERT-based).
2. Build a basic CLI using input() and print().
3. Build a Streamlit-based web app to:
   - Upload a passage
   - Type a question
   - Display the answer
4. Evaluate and compare multiple models using F1 and EM scores.
5. Plot performance metrics for model comparison.

Tools Used:
- Python
- PyTorch
- Hugging Face Transformers
- Streamlit
- Matplotlib

How to Run:

CLI Version:
$ Transformer.ipynb

Streamlit App:
$ streamlit run qa_app.py

Note:
Make sure all required libraries are installed:
$ pip install -r requirements.txt

Status:
✅ Completed
