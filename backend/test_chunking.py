from app.services.chunking_service import chunk_text

sample_text = """
Artificial Intelligence is transforming healthcare.
AI systems help doctors analyze reports.
RAG systems improve factual accuracy.
""" * 50

chunks = chunk_text(sample_text)

print(f"Total Chunks: {len(chunks)}")

print(chunks[0])