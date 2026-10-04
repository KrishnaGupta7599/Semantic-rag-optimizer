from sentence_transformers import SentenceTransformer

model=SentenceTransformer("all-MiniLM-L6-v2")

text="Machine learning is a branch of artificial intelligence."

embedding = model.encode(text)

print("Embedding generated!")
print("Number of dimensions:", len(embedding))
print("First 10 values:", embedding[:10])