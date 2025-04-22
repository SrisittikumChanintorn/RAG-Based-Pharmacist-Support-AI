# Pharmacist Assistant AI (Thai Language)

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python Version](https://img.shields.io/badge/Python-3.11.6-blue.svg)
![Langchain Version](https://img.shields.io/badge/Langchain-0.3.x-brightgreen.svg)
![Anthropic Claude Version](https://img.shields.io/badge/Anthropic%20Claude-3.5%20Sonnet-orange.svg)
![OpenAI Embeddings](https://img.shields.io/badge/OpenAI%20Embeddings-text--embedding--ada--002-lightgrey.svg)

**Pharmacist Assistant AI** is a Python-based application designed to assist pharmacists in providing drug information. It leverages the power of Large Language Models (LLMs), specifically Anthropic's Claude, and implements a Retrieval-Augmented Generation (RAG) pipeline to query external knowledge and provide more specific and accurate answers to drug-related inquiries in the Thai language.

## Overview

This project addresses the limitations of general-purpose LLMs by integrating them with a specific knowledge base of drug information. By employing the RAG technique, the application can retrieve relevant information from an external PDF document ("ข้อมูลยา 50 ชนิด.pdf") and use it as context to inform Claude's responses. This allows the AI to answer questions that go beyond its pre-trained knowledge, offering valuable support to pharmacists in their daily tasks.

## Key Features

* **Thai Language Support:** The entire application, including prompts and responses, is designed to operate in the Thai language.
* **RAG Implementation:** Utilizes a robust RAG pipeline to enhance the LLM's knowledge with external data.
* **Anthropic Claude Integration:** Leverages the advanced capabilities of the Claude LLM for generating informative and contextually relevant answers.
* **PDF Data Ingestion:** Reads and processes drug information from a local PDF file ("ข้อมูลยา 50 ชนิด.pdf").
* **Conversational Interface:** Provides a user-friendly graphical interface built with Tkinter for interactive querying.
* **Specific Knowledge Retrieval:** Enables the AI to answer specific questions about the drugs contained within the provided PDF document.
* **Clear and Concise Responses:** The LLM is prompted to provide answers based solely on the retrieved context, ensuring accuracy and relevance.

## Technologies Used

* **Python:** The primary programming language.
* **Langchain:** A framework for building LLM-powered applications.
* **Anthropic Claude:** A powerful Large Language Model.
* **OpenAI Embeddings:** Used for generating vector embeddings of the document chunks.
* **Chroma:** An in-memory vector store for efficient retrieval of document embeddings.
* **PyMuPDF:** A library for reading and processing PDF files.
* **Tkinter:** Python's standard GUI library for creating the user interface.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Install the required Python packages:**
    Create a `requirements.txt` file in the repository root with the following content:
    ```
    langchain_community==0.3.21    
    langchain_openai==0.3.12        
    langchain-anthropic==0.3.10    
    anthropic==0.49.0            
    pymupdf==1.25.5               
    chromadb==0.5.3            
    openai==1.68.2                 
    tiktoken==0.7.0                 
    pydantic==2.7.4                
    SQLAlchemy==2.0.40             
    PyYAML==6.0.0                  
    tenacity==9.1.2                
    requests==2.31.0                
    numpy==1.26.2                  
    ```
    Then, install the dependencies using pip:
    
    ```bash
    pip install -r requirements.txt
    ```

4.  **Place the PDF knowledge base:**
    Ensure that the PDF file containing the drug information, named `ข้อมูลยา 50 ชนิด.pdf`, is located in the same directory as the Python script.

    

5.  **Set up API Keys:**
    You need to have API keys for both Anthropic and OpenAI. Set these as environment variables before running the application.
    ```bash
    # Ensure API keys are set in environment before running
    os.environ.setdefault(
        "ANTHROPIC_API_KEY",
        "YOUR_ANTHROPIC_API_KEY",
    )
    os.environ.setdefault(
        "OPENAI_API_KEY",
        "YOUR_OPENAI_API_KEY",
    )

    ```
    *(Replace `"YOUR_ANTHROPIC_API_KEY"` and `"YOUR_OPENAI_API_KEY"` with your actual API keys.)*



## Usage

1.  **Run the Python script:**
    Assuming your main script is named `main.py`, run:
    ```bash
    python main.py
    ```

2.  **Interact with the GUI:**
    A window titled "Pharmacist Assistant AI" will appear.
    * Enter your drug-related question in Thai in the text input field.
    * Click the "Ask" button or press Enter to submit your query.
    * The assistant's response, based on the information retrieved from the PDF and processed by Claude, will be displayed in the chat log.
    * You can use the "Refresh" button to clear the chat history.
    * Type "q", "quit", or "exit" in the input field to close the application.

## Project Structure
   This project select python version  3.11.6 as a interpreter

 ```bash

├── main.py                 # The main Python script containing the application logic
├── ข้อมูลยา 50 ชนิด.pdf      # The PDF file containing the drug information
├── README.md               # This README file
└── requirements.txt        # List of Python dependencies

```

## Future Enhancements

* Support for multiple PDF files or data sources.
* Improved prompt engineering for more nuanced and accurate responses.
* Integration with a more persistent vector store (e.g., ChromaDB as a service).
* More advanced UI features, such as saving chat history.
* Error handling and logging improvements.
* Evaluation of the AI's performance and fine-tuning of parameters.

## Contributing

Contributions to this project are welcome. Please feel free to submit pull requests with bug fixes, new features, or improvements.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the `LICENSE` file for more details.

## Acknowledgements

* The Langchain library for providing a powerful framework for building LLM applications.
* Anthropic for the Claude language model.
* OpenAI for the text embedding model.
* The developers of PyMuPDF and ChromaDB for their excellent libraries.

---

**Developed with passion for empowering pharmacists.**
