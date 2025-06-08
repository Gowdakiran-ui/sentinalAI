import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEmbeddings
from chat_openrouter import ChatOpenRouter
from analysis.packet_parser import parse_pcap

def load_knowledge_base():
    kb_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "docs", "knowledge_base.md"))
    documents = TextLoader(kb_path).load()
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.from_documents(documents, embeddings).as_retriever()

def classify_packets(packet_df):
    retriever = load_knowledge_base()
    llm = ChatOpenRouter(
    model="deepseek-coder:meta-llama/Meta-Llama-3-8B-Instruct",
    temperature=0,
    openai_api_key=""
)

    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return [(row.to_dict(), qa_chain.run(f"Analyze network packet:\n{row}")) for _, row in packet_df.iterrows()]

if __name__ == "__main__":
    df = parse_pcap(os.path.join(os.path.dirname(__file__), "packets.pcap"))
    for pkt, res in classify_packets(df):
        print(f"{pkt['summary']} ➜ {res}")
