from tictactoe.QLearning import QLearning

if __name__ == "__main__":
    qlearning = QLearning()
    qlearning.training(max_episode=10000000, decay="quadratic", lr=0.0001, discount_rate=0.8)
    qlearning.save_to_json("qfunction_1M_2.json")