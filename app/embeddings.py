from sentence_transformers import SentenceTransformer
from ingest import load_and_chunk_pdf
import chromadb
from pathlib import Path


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

db_path=Path(__file__).resolve().parent.parent / "chroma_db"
client = chromadb.PersistentClient(path=str(db_path))
collection = client.get_or_create_collection(
    name="syllabus"
)


# STEP 6: Remove previous syllabus records
existing = collection.get(
    where={"source": "syllabus.pdf"}
)

if existing["ids"]:
    collection.delete(ids=existing["ids"])


# STEP 7: Store chunks and embeddings
collection.upsert(
    ids=[f"chunk-{i}" for i in range(len(chunks))],
    documents=chunks,
    embeddings=embeddings.tolist(),
    metadatas=[
        {"source": "syllabus.pdf"}
        for _ in chunks
    ]
)


# STEP 8: Verify storage
print("\nEmbeddings saved successfully!")
print("Stored records:", collection.count())
print("Database location:", db_path)

print("\nFirst stored chunk:")

result = collection.get(
    ids=["chunk-0"],
    include=["documents"]
)

if result["documents"]:
    print(result["documents"][0])
else:
    print("Chunk not found in database.")

print("\nFirst chunk:")
print(chunks[0])

print("\nFirst 10 values of its embedding:")
print(embeddings[0][:10])