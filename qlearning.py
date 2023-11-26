from tictactoe import QLearning

if __name__ == "__main__":
    qlearning = QLearning()
    qlearning.training(10000000, "quadratic", 0.0001, 0.8)
    qlearning.save_to_json("qfunction_1M_2.json")