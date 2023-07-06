import numpy as np
import pickle
from embeddingGenerator import getDocEmbeddings, getQueryEmbeddings


class VectorStore:
    def __init__(self, storage_file='vector_store.pkl'):
        self.storage_file = storage_file
        self.data = {}

        # Load existing data if any
        try:
            with open(self.storage_file, 'rb') as f:
                self.data = pickle.load(f)
        except (FileNotFoundError, EOFError):
            pass

    def add_contents(self, contents):
        embeddings = getDocEmbeddings(contents)
        for content, embedding in zip(contents, embeddings):
            self.data[content] = embedding

        # Save data to storage file
        with open(self.storage_file, 'wb') as f:
            pickle.dump(self.data, f)

    def cosine(self, a, b):
        dot_product = np.dot(a, b)
        magnitude_a = np.linalg.norm(a)
        magnitude_b = np.linalg.norm(b)
        similarity = dot_product / (magnitude_a * magnitude_b)
        return similarity

    def cosine_similarity_search(self, query, k):
        query_embedding = getQueryEmbeddings(query)
        similarities = []

        for content, embedding in self.data.items():
            similarity = self.cosine(query_embedding, embedding)
            similarities.append((similarity, content))

        # Sort by similarity in descending order and take top k results
        top_k_results = sorted(similarities, reverse=True, key=lambda x: x[0])[:k]

        return top_k_results


# vectorStore = VectorStore()
#
# contents = [
#     "Python is a high-level, interpreted programming language.",
#     "The Eiffel Tower is located in Paris, France.",
#     "Apple Inc. is an American multinational technology company.",
#     "The Great Wall of China is one of the seven wonders of the world.",
#     "Football is a popular sport played all around the world.",
#     "Microsoft Corporation is a leading global technology company.",
#     "The Sahara is the largest hot desert in the world.",
#     "The Mona Lisa is a famous painting by Leonardo da Vinci.",
#     "The Pacific Ocean is the largest and deepest of Earth's oceanic divisions.",
#     "Albert Einstein was a theoretical physicist who developed the theory of relativity."
# ]
#
# # vectorStore.add_contents(contents)
#
# query = "Programming language"
# k = 5
# results = vectorStore.cosine_similarity_search(query, k)
#
# for res in results:
#     print(res)