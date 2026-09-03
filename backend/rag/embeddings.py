from sentence_transformers import SentenceTransformer


MODEL_NAME = "BAAI/bge-m3"

model = SentenceTransformer(MODEL_NAME)


def generate_embeddings(texts):
    return model.encode(
        texts,
        normalize_embeddings=True
    )