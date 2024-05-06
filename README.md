# PDF_AI

PDF_AI is a powerful tool for processing and extracting information from PDF documents using state-of-the-art natural language processing techniques. Whether you need to search for specific content within PDFs or analyze and manipulate text data, PDF_AI has got you covered.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

PDF documents are a ubiquitous format for sharing information, but they can be challenging to work with programmatically. PDF_AI simplifies the process by allowing you to upload PDFs, extract text from them, and perform advanced operations on the text data.

## Features

- Upload and process PDF documents.
- Extract text from PDFs with high accuracy.
- Split extracted text into manageable chunks.
- Create embeddings to search for content within PDFs.
- Perform similarity searches on PDF documents.
- Utilize advanced natural language processing for question-answering tasks.

## Installation

To use PDF_AI, follow these installation instructions:

1. Clone this repository to your local machine.

   ```shell
   git clone https://github.com/yourusername/PDF_AI.git

2. Navigate to the project directory.

   ```shell
   cd PDF_AI

3. Create a virtual environment (recommended) to isolate project dependencies.

   ```shell
   python -m venv venv
4. Activate the virtual environment.
*On Windows:*
   ```shell
   .\venv\Scripts\Activate
   ```
   *On macOS and Linux:*
      ```bash
      source venv/bin/activate
      ```
5. Install the required Python packages from `requirements.txt`.
   ```bash
   pip install -r requirements.txt
   ```
6. Create HuggingFace account and Generate a new API token.
   Create a .env file in the project directory and add your access token as follows:
   ```shell
   HUGGINGFACE_TOKEN=your-access-token-goes-here
   ```
7. You are now ready to run the PDF_AI tool. Start the application with the following command:
   ```bash
   streamlit run app.py
   ```

## Usage

- Run the PDF_AI tool by following the installation instructions.
- Upload your PDF document.
- PDF_AI will extract text from the document.
- You can split the text into manageable chunks for further processing.
- Perform similarity searches to find relevant content within the document.
- Utilize the built-in question-answering capabilities to get answers to your questions.

## Contributing

If you would like to contribute to PDF_AI, feel free to open issues, submit pull requests, or provide suggestions. We welcome contributions from the community.
