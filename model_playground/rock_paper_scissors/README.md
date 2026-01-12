# semantic-forest
# Rock Paper Scissors AI Arena 🪨📄✂️

This project is a Python-based battle arena for Rock, Paper, Scissors. It allows humans, random algorithms, or AI models to compete against an OpenAI-powered opponent (`gpt-4o-mini`/'gpt-4.1-mini').

The unique feature of this script is that **the AI opponent remembers the history of the match** and the user can play via the system camera. It is fed the results of previous turns in the system prompt, allowing it to "strategise" and attempt to predict the opponent's next move.

## ✨ Features

* **Multiple Game Modes:**
    * **User vs AI:** You play manually against the LLM using the system camera to take images and a model to determine the user action for example holding your hand in a scissor shape will result in the model identifying scissors. a flat hand paper and a clenched fist, rock.
    * **AI vs AI:** Watch two different LLM instances battle.
    * **Random vs AI:** Test if the AI can beat pure randomness.
* **Strategic Memory:** The LLM receives a history of `opponent_results` and `your_results` to simulate tactical thinking.
* **Robust Error Handling:** Retries API calls automatically if the LLM returns an invalid move (something other than rock/paper/scissors).

## 📋 Prerequisites

* Python 3.12
* A valid [OpenAI API Key](https://platform.openai.com/api-keys)


## 🎮 Usage & Configuration

Open the script in your code editor to configure the game parameters before running.

### 1. Select your Player
Look for the `player` variable near the top of the file. Uncomment the mode you wish to use:

```python
# player = "gpt-4o-mini"  # AI vs AI Mode
# player = "gpt-4.1-mini" # Alternative AI Model
player = "user"           # You play manually via the laptop /computer camera
# player = "random"       # Random selection vs AI