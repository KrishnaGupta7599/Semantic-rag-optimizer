import fitz
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer


pdf_path="docs/syllabus.pdf"
doc=fitz.open(pdf_path)

text=""

for page in doc:
    text += page.get_text() + "\n"

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_text(text)

print(f"Total chunks: {len(chunks)}")

model=SentenceTransformer("all-MiniLM-L6-v2")

embedding = model.encode(chunks)

print("Embedding generated!")
print("Number of chunks:", len(chunks))
print("Embedding dimensions:", len(embedding[0]))

print("\nFirst chunk:")
print(chunks[0])

print("\nFirst 10 values of its embedding:")
print(embedding[0][:10])