from tictactoe import QLearning

if __name__ == "__main__":
    qlearning = QLearning()
    qlearning.training(100000, "quadratic", 0.1, 0.99)