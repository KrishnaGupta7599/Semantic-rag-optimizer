
from sentence_transformers import SentenceTransformer
import chromadb
from pathlib import Path


# STEP 1: Load the same embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# STEP 2: Connect to our existing ChromaDB
db_path = Path(__file__).resolve().parent.parent / "chroma_db"

client = chromadb.PersistentClient(path=str(db_path))

collection = client.get_collection(name="syllabus")


# STEP 3: Write a function to search the database
def search_documents(query, k=3):

    # Convert the question into an embedding
    query_embedding = model.encode(query).tolist()

    # Find the most similar chunks
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    print("Distances:", results["distances"])
    return results


# STEP 4: Test our search
if __name__ == "__main__":
    question = input("Ask a question about your syllabus: ")

    results = search_documents(question)

    print("\nMost relevant chunks:\n")

    documents = results.get("documents", [[]])[0]

    if documents:
        for i, chunk in enumerate(documents, start=1):
            print(f"\n--- Result {i} ---")
            print(chunk)
    else:
        print("No relevant chunks found.")
