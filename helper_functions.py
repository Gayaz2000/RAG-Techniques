import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from enum import Enum

class Embedding_Provider(Enum):
    GROQ = "groq"
    OLLAMA = "llama"
    GOOGLE = "google"
    HUGGINGFACE = "huggingface"

class Helpers:
    def __init__(self):
        self.list_of_documents = None
        
    def replace_t_with_space(self, list_of_documents):
        """
        Replace all the tab ('\t') keys with white space in the page content of list of documents.

        Args:
            list_of_documents: A list of document obj, each with 'page_content' attribute.
        Return:
            The modified list of documents with tab characters replaced by white spaces
        """
        for doc in list_of_documents:
            doc.page_content = doc.page_content.replace('\t', " ")
        return self.list_of_documents

    def show_context(self, context):
        """
        Display the contents of the provided context list.

        Args:
            context (list): A list of context items to be displayed.

        Prints each context item in the list with a heading indicating its position.
        """
        for i, c in enumerate(context):
            print(f"Context {i + 1}:")
            print(c)
            print("\n")