# 4. Rock-Paper-Scissors Game
# ● Objective: Simulate a simple game.
# ● Task:
# ○ Accept inputs for two players (rock, paper, or scissors).
# ○ Use if conditions to determine the winner:
# ■ Rock beats Scissors
# ■ Paper beats Rock
# ■ Scissors beats Paper
# ○ Print "Player 1 Wins," "Player 2 Wins," or "It's a Tie!"
#rock paper done
#rock scissors done
#paper scissors done
#paper rock done 
#scissors rock done
#scissor paper

user1 = input("enter rock, paper, scissors")
user2 = input("enter rock, paper, scissors")
if user1 == "rock" and user2 == "scissors":
    print("rock beats scissors user 1 wins")
elif user1 == "rock" and user2 == "paper":
    print("paper beats rock user 2 win")
elif user1 == "paper" and user2 == "scissors":
    print("scissors beats paper user 2 win")
elif user1 == "paper" and user2 == "rock":
    print("paper beats rock user 1 win")
elif user1 == "scissors" and user2 == "rock":
    print("rock beats scissors user 2 win")
elif user1 == "scissors" and user2 == "paper" :
    print("scissors beats paper user1 win")   