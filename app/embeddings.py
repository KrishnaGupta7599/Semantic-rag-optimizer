from sentence_transformers import SentenceTransformer
from ingest import load_and_chunk_pdf


# Get chunks from ingestion
chunks = load_and_chunk_pdf("docs/syllabus.pdf")

print(f"Total chunks: {len(chunks)}")


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# Generate embeddings
embeddings = model.encode(chunks)

print("Embeddings generated!")
print("Number of chunks:", len(chunks))
print("Embedding dimensions:", len(embeddings[0]))

print("\nFirst chunk:")
print(chunks[0])

print("\nFirst 10 values of its embedding:")
print(embeddings[0][:10])