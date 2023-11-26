
# TicTacToe Q-Learning

Playable Tic Tac Toe game against AI Q-Learning agent.


## Installation

This project was developed with python 3.10.8. It requires only standard library. However, for unit testing it requires to install "parameterized".

```bash
  git clone https://github.com/Gratic/TicTacToe_QLearning
  cd TicTacToe_QLearning
  pip install -r requirements.txt
```
    
## Running Tests

To run tests, run the following command.

```bash
  python -m unittest discover tests -p "*test.py"
```


## Documentation

### Playing against the AI agent

Just execute the python module.

```bash
python -m tictactoe
```

### Training the AI agent

Modify as you wish the `qlearning.py` file in the root of the project.

```bash
python ./qlearning.py
```

| Parameters  | Description |
| ------------- | ------------- |
| max_episode | The number of times the QLearning algorithm will play the game.  |
| decay | Default as "linear". Possible choices are "linear" and "quadratic". The epsilon schedule as the learning progresses. Epsilon is the exploration factor, higher means more random actions and exploration, while lower means using learned knowledge. |
| lr | The learning rate. |
| discount_rate | The discount rate a.k.a. gamma. Higher means that long term rewards are taken into account while lower means to focus on short term reward. Recommended values are: 0.9, 0.95, 0.99. |

