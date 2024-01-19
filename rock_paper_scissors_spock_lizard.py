import random
import numpy as np

container = ["""
    _______ 
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", 
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)  
---.__(___)
""",
"""
    _______
---'   ____)____
          ______)
       __________)
        (
        (_____       
          _____)
       ______)
""",

"""

 ~~I==I>

"""]

class QLearning:
    def __init__(self, max_score=50):
        self.player_score = 0
        self.comp_score = 0
        self.max_score = max_score
        
        self.states = 50 
        self.actions = 5
        self.alpha = 0.5
        self.gamma = 0.9
        self.epsilon = 0.1
        
        self.Q = np.zeros((self.states, self.actions))
        
    def choose_action(self, state):
        if np.random.uniform(0, 1) < self.epsilon:
            action = np.random.choice(self.actions) 
        else:
            action = np.argmax(self.Q[state, :])
        return action
    
    def learn(self, player, comp, reward):
        predict = self.Q[player, comp]
        target = reward + self.gamma * np.max(self.Q[player, :])
        self.Q[player, comp] += self.alpha * (target - predict)
        
        if reward == 1:
            self.player_score += 1
        elif reward == -1:
            self.comp_score += 1
            
def game():
    # Create agent
    q_agent = QLearning()
    
    while True:
        # Agent chooses action
        comp_choice = q_agent.choose_action(q_agent.player_score)
        
        print(f"--------SCORE--------")
        print(f"YOU: {q_agent.player_score}") 
        print(f"COMP: {q_agent.comp_score}")
        
        # Get player's move
        try:
            player = int(input("Enter your move (0-4): "))
            print()
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 4.")
            continue
        
        if 0 <= player < 5:
            print("YOU: ", container[player])
            print("COMP:", container[comp_choice])
        
            if comp_choice == player:
                print("It's a tie!")
                reward = 0
            elif (player == 0 and comp_choice == 2) or (player == 1 and comp_choice == 0) or (player == 2 and comp_choice == 1) or (player == 3 and comp_choice == 4) or (player == 4 and comp_choice == 0):
                print("YOU WIN!")
                reward = 1
            else:
                print("YOU LOSE!")  
                reward = -1
        else:
            print("Invalid move. Please enter a number between 0 and 4.")
            continue
        
        # Q-learning update
        q_agent.learn(player, comp_choice, reward)
        
        # Check if max score reached
        if q_agent.player_score >= q_agent.max_score or q_agent.comp_score >= q_agent.max_score:
            print("Game over!")
            break
            
game()
