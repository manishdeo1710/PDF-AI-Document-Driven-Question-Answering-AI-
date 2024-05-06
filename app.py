from dotenv import load_dotenv
import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS 
from langchain.chains.question_answering import load_qa_chain
from langchain import HuggingFaceHub
import pickle


class PDF_AI:
    def __init__(self):
        load_dotenv()
        st.set_page_config(
            page_title="PDF_AI",
            page_icon="🤖",
            layout="wide",
            initial_sidebar_state="expanded",
            menu_items={
                'Get Help': 'https://www.extremelycoolapp.com/help',
                'Report a bug': "https://www.extremelycoolapp.com/bug",
                'About': "# This is a header. This is an *extremely* cool app!"
                }
            )
        st.markdown("<h1 style='text-align: center; color: gray;'><i>PDF_AI</i></h1>", unsafe_allow_html=True)

    def run(self):
        pdf = st.file_uploader("Upload your pdf",type="pdf")

        if pdf is not None:
            try:
                pdf_reader = PdfReader(pdf)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()
            except Exception as e:
                st.write(f"Error reading PDF: {e}")
                return

            # spilit ito chuncks
            text_splitter = CharacterTextSplitter(
                separator="\n",
                chunk_size=950,
                chunk_overlap=200,
                length_function=len
            )
            chunks = text_splitter.split_text(text)

            # create embedding
            store_name = pdf.name[:-4]
            st.write(f'{store_name}')
 
            if os.path.exists(f"Database\{store_name}.pkl"):
                with open(f"Database\{store_name}.pkl", "rb") as f:
                    VectorStore = pickle.load(f)
            else:
                embeddings = HuggingFaceEmbeddings()
                VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
                with open(f"Database\{store_name}.pkl", "wb") as f:
                    pickle.dump(VectorStore, f)


            user_question = st.text_input("What Are You Looking For In DOC? ")
            if user_question:
                docs = VectorStore.similarity_search(user_question,k=3)
                llm = HuggingFaceHub(repo_id="google/flan-t5-large", model_kwargs={"temperature":5,
                                                          "max_length":64})
                chain = load_qa_chain(llm,chain_type="stuff")
                response = chain.run(input_documents=docs,question=user_question,return_only_outputs=True)

                st.write(response)


if __name__ == '__main__':
    app = PDF_AI()
    app.run()
