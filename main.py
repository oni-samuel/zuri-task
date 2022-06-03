#!/usr/bin/env python
# coding: utf-8

# In[3]:


def play_game():
    import random
    outcome=('P','R','S')
    player=input("player1: enter 'R' for rock,'P' for paper and 'S' scissors").upper()
    while player not in outcome:
        print('input a valid option')
        player=input("player1: enter 'R' for rock,'P' for paper and 'S' scissors").upper()
    computer= random.choice(outcome)
    print(f"player's choice is ({player}), while computer's choice is ({computer})")
    if player==computer:
        print("it's a tie")
        return play_game()
    if (player=='R' and computer=='S') or (player=='P' and computer=='R') or (player=='S' and computer=='P'):
        print(f"you won the game")
    else:
          print(f"you lost the game")
play_game()


# In[ ]:





# In[ ]:




