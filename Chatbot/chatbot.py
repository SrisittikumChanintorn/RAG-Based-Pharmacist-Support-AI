import os
import sys
import tkinter as tk
from tkinter import scrolledtext
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
from langchain.text_splitter import CharacterTextSplitter
from langchain_anthropic import ChatAnthropic
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

# Constants and Configuration
PDF_PATH = "ข้อมูลยา 50 ชนิด.pdf"
MODEL_NAME = "claude-3-5-sonnet-20240620"
MODEL_MAX_TOKENS = 1024
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 0



# Ensure API keys are set in environment before running
os.environ.setdefault(
    "ANTHROPIC_API_KEY",
    "YOUR_ANTHROPIC_API_KEY",
)
os.environ.setdefault(
    "OPENAI_API_KEY",
    "YOUR_OPENAI_API_KEY",
)

# Load and split PDF documents
def load_documents(pdf_path: str) -> list:
    """
    Load and split PDF file into document chunks.
    :param pdf_path: Path to the local PDF file.
    :return: List of document chunks.
    """
    if not os.path.isfile(pdf_path):
        sys.exit(f"Error: PDF file not found at '{pdf_path}'")
    loader = PyMuPDFLoader(file_path=pdf_path)
    raw_docs = loader.load_and_split()
    splitter = CharacterTextSplitter(
        separator="\n\n",
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )
    return splitter.split_documents(raw_docs)


# Create a conversational retrieval chain using the Anthropic Claude model
def build_retrieval_chain(docs: list) -> ConversationalRetrievalChain:
    """
    Create a conversational retrieval chain using Anthropic Claude model.
    :param docs: List of pre-split document chunks.
    :return: Configured retrieval chain.
    """
    embeddings = OpenAIEmbeddings()
    vector_store = Chroma.from_documents(documents=docs, embedding=embeddings)
    retriever = vector_store.as_retriever(search_kwargs={"k": 1 })
    prompt_template = PromptTemplate(
        input_variables=["context", "question"],
        template=(
            "You are an AI Thai language assistant and medicine expert.\n"
            "Answer based ONLY on the context below.\n"
            "{context}\n"
            "Question: {question}"
        ),
    )
    llm = ChatAnthropic(
        model=MODEL_NAME,
        max_tokens=MODEL_MAX_TOKENS,
    )
    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        combine_docs_chain_kwargs={"prompt": prompt_template},
    )

# Launch the GUI for user interaction
def launch_gui(chain: ConversationalRetrievalChain) -> None:
    """
    Initialize and run the Tkinter GUI for user interaction.
    Keeps consistent theme, aligns input and Ask button on the same row,
    preserves layout with optional Refresh button if needed.
    """
    chat_history: list = []

    def on_user_submit(event=None):
        """
        Handle user message submission and update chat log with assistant response.
        """
        user_input = entry.get().strip()
        if not user_input:
            return
        if user_input.lower() in ("q", "quit", "exit"):
            root.destroy()
            return

        chat_history.append(("User", user_input))
        response = chain.invoke({"question": user_input, "chat_history": chat_history})
        assistant_reply = response.get("answer", "")
        chat_history.append((user_input, assistant_reply))

        chat_log.config(state=tk.NORMAL)
        chat_log.insert(tk.END, f"\nUser: {user_input}\nAssistant: {assistant_reply}\n")
        chat_log.config(state=tk.DISABLED)
        chat_log.yview(tk.END)
        entry.delete(0, tk.END)




    def on_refresh():
        """
        Clear chat history and reset chat log.
        """
        chat_history.clear()
        chat_log.config(state=tk.NORMAL)
        chat_log.delete(1.0, tk.END)
        chat_log.config(state=tk.DISABLED)

    # Root window setup
    root = tk.Tk()
    root.title("Pharmacist Assistant AI")
    root.configure(bg="#212121")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Main container
    main_frame = tk.Frame(root, bg="#212121")
    main_frame.grid(sticky="nsew")
    main_frame.columnconfigure(0, weight=5)  # Wider input field
    main_frame.columnconfigure(1, weight=1)  # Narrower Ask button
    main_frame.columnconfigure(2, weight=0)  # Optional refresh button
    main_frame.rowconfigure(0, weight=1)

    # Chat log display (read-only)
    chat_log = scrolledtext.ScrolledText(
        main_frame,
        wrap=tk.WORD,
        state=tk.DISABLED,
        font=("Arial", 11),
        bg="#2E2E2E",
        fg="#FFFFFF",
    )
    chat_log.grid(
        row=0,
        column=0,
        columnspan=3,
        sticky="nsew",
        padx=10,
        pady=10,
    )

    # User input entry
    entry = tk.Entry(
        main_frame,
        font=("Arial", 11),
        bg="#1E1E1E",
        fg="#FFFFFF",
    )
    entry.grid(
        row=1,
        column=0,
        sticky="ew",
        padx=(10, 5),
        pady=(0, 10),
    )
    entry.bind("<Return>", on_user_submit)

    # Submit button (Ask)
    send_button = tk.Button(
        main_frame,
        text="Ask",
        command=on_user_submit,
        font=("Arial", 11),
        bg="#32CD32",
        fg="#000000",
    )
    send_button.grid(
        row=1,
        column=1,
        sticky="ew",
        padx=(0, 5),
        pady=(0, 10),
    )

    # Optional Refresh button
    refresh_button = tk.Button(
        main_frame,
        text="Refresh",
        command=on_refresh,
        font=("Arial", 11),
        bg="#FFD700",
        fg="#000000",
    )
    refresh_button.grid(
        row=1,
        column=2,
        sticky="ew",
        padx=(0, 10),
        pady=(0, 10),
    )

    root.mainloop()





# Main function to load documents, build retrieval chain, and launch GUI
def main() -> None:
    """
    Main entry point for the application.
    """
    documents = load_documents(PDF_PATH)
    retrieval_chain = build_retrieval_chain(documents)
    launch_gui(retrieval_chain)
if __name__ == "__main__":  # Run application
    main()
