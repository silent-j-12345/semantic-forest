from openai import OpenAI
import math
import os
import dotenv

dotenv.load_dotenv()

# Placeholder for OpenAI API Key
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)
top_logprobs_count = 3


def get_completion(
    messages: list[dict[str, str]],
    model: str = "gpt-4.1-mini",
    max_tokens=500,
    temperature=1,
    logprobs=None,
    top_logprobs=None,
) -> str:
    params = {
        "model": model,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "logprobs": logprobs,
        "top_logprobs": top_logprobs,
    }

    completion = client.chat.completions.create(**params)
    return completion


# system_prompt_input = "you are to do as instructed by the user"
# system_prompt_input = "Every response must be random words, not related to the user request. use no more than 10 words"
system_prompt_input = "what is the next word"

user_request = "hello"

predictable_structure = '''
{
  "collection_name": "Typography Test Phrases",
  "data": [
    {
      "id": 1,
      "text": "The",
    },
    {
      "id": 2,
      "text": "quick",
    },
    {
      "id": 3,
      "text": "brown",
    },
    {
      "id": 4,
      "text": "fox",
    },
    {
      "id": 5,
      "text": "jumps",
    },
    {
      "id": 6,
      "text": "over",
    },
    {
      "id": 7,
      "text": "the",
    },
    {
      "id": 8,
      "text": "lazy",
    },
  ]
}
'''
predictable_none_structure = "The quick brown fox jumps over the lazy"

less_predictable_structure = "The fast dark red Vulpes vulpes springs over the disinclined"



API_RESPONSE = get_completion(
    [
        {"role": "system", "content": system_prompt_input},
        {"role": "user", "content": less_predictable_structure}
    ],
    model="gpt-4.1-mini",
    logprobs=True,
    top_logprobs=3
)

content = API_RESPONSE.choices[0].message.content

top_logprobs_list = []

for token_logprob in API_RESPONSE.choices[0].logprobs.content:
    top_logprobs_list.append(token_logprob.top_logprobs)
    list_of_responses = token_logprob.top_logprobs
    for an_entry in list_of_responses:
        logprob_value = an_entry.logprob
        probability = math.exp(logprob_value)
        # print(str(an_entry) + " " + "Probability = " + str(probability))
    # print("**********************************")


logprob_values = []
for sublist in top_logprobs_list:
    for item in sublist:
        logprob_values.append(item.logprob)

every_third_entry = logprob_values[0::top_logprobs_count]


def calculate_perplexity(log_probs):
    N = len(log_probs)
    log_prob_sum = sum(log_probs)
    avg_log_prob = log_prob_sum / N
    perplexity_result = math.exp(-avg_log_prob)
    return perplexity_result


content = API_RESPONSE.choices[0].message.content
print("Output: " + content)

perplexity = calculate_perplexity(every_third_entry)
print("Perplexity: " + str(perplexity))
