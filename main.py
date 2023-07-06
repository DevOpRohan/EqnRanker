# 1. Create a vector store using the VectorStore class.
import asyncio

from utils import extract_example
from vectorstore import VectorStore

vectorStore = VectorStore(storage_file="persistence/Exp2.pkl")

# 2. Create a content preprocessor using the ContentPreprocessor class.
from preprocessing import ContentPreprocessor

preprocessor = ContentPreprocessor()

##== Only run the step 3 & 4 in case of new datasource, else comments the entire step 3 & 4 ==##

# # 3. Preprocess the contents and save them into a text file.
# preprocessed_contents = preprocessor.preprocess_text_file(file_path="data/Exp2Data.txt", delimiter="====")
#
# # save the preprocessed contents into text file, each element will be seperated by "\n====NEW_QUESTION====\n"
# with open("data/pExp2Data.txt", "w") as file:
#     for content in preprocessed_contents:
#         file.write(content)
#         file.write("\n====NEW_QUESTION====\n")
#
# # 4. Add the preprocessed contents to the vector store.
# vectorStore.add_contents(preprocessed_contents)

# 5. Cosine similarity search
query = """
Solve 5x-8 = 4
"""

print(f"Search: {query}")
preprocessed_query = asyncio.run(preprocessor.preprocessQuery(query))
print(f"\nPreprocessed Query:\n {preprocessed_query} \n")

k = 10
results = vectorStore.cosine_similarity_search(preprocessed_query, k)

for res in results:
    print(f"Embedding-ProcessedContnet\n{res} \n Parsed-Question:\n{extract_example(res[1])}\n")
