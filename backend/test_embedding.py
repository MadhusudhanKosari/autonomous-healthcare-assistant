from app.services.embedding_service import generate_embedding

text = "Patient has fever and headache"

embedding = generate_embedding(text)

print(len(embedding))
print(embedding[:5])