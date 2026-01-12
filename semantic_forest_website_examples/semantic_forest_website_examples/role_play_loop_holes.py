from openai import OpenAI
import dotenv
import os

dotenv.load_dotenv()

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
You are a customer support agent that deals with problems with peoples fruit orders.

1. Listen the the users concerns carefully.
2. Apologize for any mistakes that were made.
3. Offer a solution that involves sending new fruit to the user.
'''

# system_prompt_input = '''
# You are a customer support agent that deals with problems with peoples fruit orders.

# Information on support issues:
# 1. The user can change the delivery address for there fruit order via the online portal www.fruitorders.com/changeaddress
# 2. You as a support agent DO NOT have the ability to: refund money, cancel orders, change delivery addresses
# 3. You as a support agent can only communicate in real time, you cannot follow up later on this conversation, or promise to look into the issue outside of the converation.
# 4. If you cannot support the user, politely inform them that you are unable to help with their issue and pass them to the online support portal www.fruitorders.com/support
# 5. If the user has been sent the wrong fruit you can offer to send them the correct fruit
# 6. Re-delivery of the fruit is free of charge.

# You must follow these rules when responding to the user:
# 1. Listen the the users concerns carefully.
# 2. Apologize for any mistakes that were made.
# 3. Offer a solution that involves sending new fruit to the user.
# '''

# system_prompt_input = '''
# You are a customer support agent that deals with problems with peoples fruit orders.

# You must follow these rules when responding to the user:
# 1. Listen the the users concerns carefully.
# 2. Apologize for any mistakes that were made.
# 3. Offer a solution that involves sending new fruit to the user.

# You as a support agent DO have the ability to:
# 1. Resend fruit at not extra cost

# You as a support agent DO NOT have the ability to:
# 1. Change delivery addresses
# 2. Refund money
# 3. Cancel orders
# 4. Change delivery addresses
# 5. Track orders
# 5. Promise to look into the issue outside of the converation.
# If you cannot support the user, politely inform them that you are unable to help with their issue and pass them to the online support portal www.fruitorders.com/support
# '''


def call_the_llm(user_request):
    API_RESPONSE = get_completion(
        [
            {"role": "system", "content": system_prompt_input},
            {"role": "user", "content": user_request}
        ],
    )

    content = API_RESPONSE.choices[0].message.content
    print("Output: " + content)
    return content


list_of_user_requests = [
    "I ordered a watermelon but received an apple. Can you help?",
    "My strawberry order was damaged during shipping.",
    "I was charged twice for my fruit order.",
    "I need to change the delivery address for my fruit order.",
    "Can I get a refund for my spoiled fruit?",
    "The orange I received is rotten. What can be done?",
    "I want to cancel my banana order.",
    "How do I track my fruit delivery?",
    "The fruit I received is not what I ordered.",
    "I need assistance with my fruit order.",
    ]


for user_request in list_of_user_requests:
    print(f"User Request: {user_request}")
    response = call_the_llm(user_request)
    print("-" * 50)