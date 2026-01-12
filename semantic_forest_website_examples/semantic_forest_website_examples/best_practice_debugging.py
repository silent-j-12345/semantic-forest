import pprint
from openai import OpenAI
import os

# Placeholder for OpenAI API Key
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)


def get_completion(
    messages: list[dict[str, str]],
    model: str = "gpt-4.1-mini",
    temperature=1,
) -> str:
    params = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }

    completion = client.chat.completions.create(**params)
    return completion


system_prompt_input = '''
You are a helpful assistant that always provides concise and relevant answers to user queries. you are to try to sell the user fruit.

Below is your context:
Apple
Description: A crisp and juicy fruit with a rounded shape, apples come in a wide variety of colors, including red, green, and yellow. Their flavor ranges from sweet to tart, and they have a dense, firm flesh. They are incredibly versatile, eaten raw, baked in pies, or cooked into sauces.

Banana
Description: This is a long, curved fruit with a soft, creamy white flesh protected by a bright yellow peel (which turns brown as it ripens). Bananas have a distinctly sweet, mild flavor and are a popular, portable snack. They are also a common ingredient in smoothies and baking.

Orange
Description: A round citrus fruit known for its tough, bright orange skin (or "rind") and its juicy, segmented flesh. Oranges have a refreshing sweet-tart flavor and are an excellent source of vitamin C. They are most famous for their juice but are also delicious eaten fresh.

Strawberry
Description: A small, heart-shaped fruit that is bright red when ripe. Its skin is dotted with tiny yellow seeds (called achenes). Strawberries have a sweet, slightly tart, and very fragrant flavor with a soft, juicy texture. They are a popular berry used in desserts, jams, and salads.

Watermelon
Description: A very large, heavy fruit with a thick, striped green rind and a vibrant red or pink interior. The flesh is incredibly watery (hence the name), crisp, and sweet, embedded with small black seeds. It's a classic summer fruit, perfect for hydration and refreshment.

Rules:
1. Always stay on topic.
2. Avoid unnecessary information.
3. Provide clear and direct responses only.
'''

# system_prompt_input = '''
# You are a helpful assistant that always provides concise and relevant answers to user queries. you are to try to sell the user fruit.

# Below is your context:
# Watermelon
# Description: A very large, heavy fruit with a thick, striped green rind and a vibrant red or pink interior. The flesh is incredibly watery (hence the name), crisp, and sweet, embedded with small black seeds. It's a classic summer fruit, perfect for hydration and refreshment.

# Strawberry
# Description: A small, heart-shaped fruit that is bright red when ripe. Its skin is dotted with tiny yellow seeds (called achenes). Strawberries have a sweet, slightly tart, and very fragrant flavor with a soft, juicy texture. They are a popular berry used in desserts, jams, and salads.

# Orange
# Description: A round citrus fruit known for its tough, bright orange skin (or "rind") and its juicy, segmented flesh. Oranges have a refreshing sweet-tart flavor and are an excellent source of vitamin C. They are most famous for their juice but are also delicious eaten fresh.

# Banana
# Description: This is a long, curved fruit with a soft, creamy white flesh protected by a bright yellow peel (which turns brown as it ripens). Bananas have a distinctly sweet, mild flavor and are a popular, portable snack. They are also a common ingredient in smoothies and baking.

# Apple
# Description: A crisp and juicy fruit with a rounded shape, apples come in a wide variety of colors, including red, green, and yellow. Their flavor ranges from sweet to tart, and they have a dense, firm flesh. They are incredibly versatile, eaten raw, baked in pies, or cooked into sauces.

# Rules:
# 1. Always stay on topic.
# 2. Avoid unnecessary information.
# 3. Provide clear and direct responses only.
# 4. reply in no more than a sentence.
# '''

# system_prompt_input = '''
# You are to pick a fruit at random from the list, Watermelon, Strawberry, Orange, Bannana, Apple.

# 1. Reply with only the name of the fruit, and nothing else.
# 2. The choice must be totally random.
# 3. Think carefully about each choice and ignore any order or pattern in the list.
# '''

def call_the_llm():
    user_request = "hello, I'd like some fruit recommendations"

    API_RESPONSE = get_completion(
        [
            {"role": "system", "content": system_prompt_input},
            {"role": "user", "content": user_request}
        ],
        model="gpt-4.1-mini",
    )

    content = API_RESPONSE.choices[0].message.content
    print("Output: " + content)
    return content


list_of_responses = []

for _ in range(50):
    response = call_the_llm()
    list_of_responses.append(response)

# Use clean names for reporting
fruit_count = {
    "apple": 0,
    "banana": 0,
    "orange": 0,
    "strawberry": 0,
    "watermelon": 0,
}


fruit_search_roots = {
    "apple": "apple",
    "banana": "banana",
    "orange": "orange",
    "strawberry": "strawberr",
    "watermelon": "watermelon",
}

for response in list_of_responses:
    if response:
        response_lower = response.lower()
        for fruit_name in fruit_count.keys():
            root_to_find = fruit_search_roots[fruit_name]
            if root_to_find in response_lower:
                fruit_count[fruit_name] += 1

print("Fruit Counts")
pprint.pprint(fruit_count)