import os
from typing import Dict, List
import time
import requests
import random

from rock_paper_scissors_model import get_rock_paper_scissors

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

game_turns = 3

# player = "gpt-4o-mini"
# player = "gpt-4.1-mini"
player = "user"
# player = "random"

llm_opponent = "gpt-4o-mini"


def get_system_prompt(opponent_results, your_results) -> str:
    prompt = f'''
    Today we are going to play a game of rock paper scissors.
    Please choose either rock, paper, or scissors.
    
    here are the results of your opponent's choices:
    {opponent_results}

    here are the results of your choices:
    {your_results}
    
    As the games progress try to predict what your oppenent will choose next and win the game.
    You must use tactics and strategies to try to win
    only respond with [rock, paper, scissors] and nothing else.
    '''
    # print(prompt)
    return prompt


def call_chatgpt(system_prompt, gpt_model: str = "gpt-4o-mini") -> str:
    """
    This creates the call to openAI
    """
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }

    payload: dict[str, str | List[dict[str, str]]] = {
        "model": gpt_model,
        "messages": [
            {"role": "system", "content": system_prompt}
        ]
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions", headers=headers, json=payload
    )

    if response.status_code == 200:
        data = response.json()
        message_content = data.get("choices")[0].get("message").get("content")
        return message_content
    else:
        return f"Error: {response.status_code} - {response.text}"
    

def run_conversation(mode) -> None:
    run_index: int = 0
    player_a_results: List[str] = []
    player_b_results: List[str] = []
    result_list: List[str] = []
    choices = ['rock', 'paper', 'scissors']

    for conversation_turn in range(game_turns):

        # depending on game mode get the first turn
        if mode == "random":
            player_a = random.choice(choices)
        elif mode == "gpt-4o-mini" or mode == "gpt-4.1-mini":
            if run_index == 0:
                player_a = call_chatgpt(get_system_prompt([], []), player)
            else:
                player_a = call_chatgpt(get_system_prompt(player_b_results[:-1], player_a_results), player)
        elif mode == "user":
            print("player get ready to make your choice!")
            player_a = get_rock_paper_scissors()
        else:
            raise ValueError(f"Unknown mode: {mode}")

        correct_case_player_a = player_a.lower()
        player_a_results.append(correct_case_player_a)

        # Attempt 5 times to get a vald response from gpt
        for _ in range(5):
            if run_index == 0:
                player_b = call_chatgpt(get_system_prompt([], []), llm_opponent)
            else:
                player_b = call_chatgpt(get_system_prompt(player_a_results[:-1], player_b_results), llm_opponent)
            correct_case_player_b = player_b.lower()
            if correct_case_player_b not in choices:
                print(f"LLM chose an invalid selection, retrying...")
                continue
            else:
                break
        
        player_b_results.append(correct_case_player_b)

        result = f"{player} results: {correct_case_player_a} | {llm_opponent} results: {correct_case_player_b}"
        result_list.append(result)
        # print(result)
        time.sleep(2)

        run_index += 1

        # Check if the conversation should end
        if run_index == game_turns:
            break
    return result_list


if __name__ == "__main__":
    print("")
    print(f"Final Results")
    for result in run_conversation(mode=player):
        print(result)
