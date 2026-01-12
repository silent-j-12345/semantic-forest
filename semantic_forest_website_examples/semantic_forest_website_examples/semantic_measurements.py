
from scipy.spatial import distance
from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()

# Placeholder for OpenAI API Key
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)


def embed_the_utterance(embedding_input):
    response = client.embeddings.create(
        input=embedding_input,
        model="text-embedding-3-small"
    )
    embedded_response = response.data[0].embedding
    return embedded_response

def compare_the_scores(embedded_test_phrase, embedded_utterance):
    return 1 - distance.cosine(embedded_test_phrase, embedded_utterance)

utterance_one = "apple"
utterance_two = ["orange", "computer", "phone", "green", "metal", "code"]

utterance_one_embedded = embed_the_utterance(utterance_one)

for word in utterance_two:
    word_embedded = embed_the_utterance(word)
    print(f"Similarity between '{utterance_one}' and '{word}': {compare_the_scores(utterance_one_embedded, word_embedded)}")
