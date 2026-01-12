
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
    temperature=1,
    logprobs=None,
    top_logprobs=None,
) -> str:
    params = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "logprobs": logprobs,
        "top_logprobs": top_logprobs,
    }

    completion = client.chat.completions.create(**params)
    return completion

system_prompt_input = "you are to greet the user"
user_request = "hello"

API_RESPONSE = get_completion(
    [
        {"role": "system", "content": system_prompt_input},
        {"role": "user", "content": user_request}
    ],
    model="gpt-4.1-mini",
    logprobs=True,
    top_logprobs=3
)

content = API_RESPONSE.choices[0].message.content
print("Output: " + content)

top_logprobs_list = []
for token_logprob in API_RESPONSE.choices[0].logprobs.content:
    top_logprobs_list.append(token_logprob.top_logprobs)
    list_of_responses = token_logprob.top_logprobs
    for an_entry in list_of_responses:
        logprob_value = an_entry.logprob
        probability = math.exp(logprob_value)
        print(str(an_entry) + " " + "Probability = " + str(probability))
    print("**********************************")
