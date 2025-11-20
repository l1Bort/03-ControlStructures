computer_science = input("Are you interested in computer science? (y/n): ") == "y"
computer_games = input("Do you like playing computer games? (y/n): ") == "y"
instagram =  input("Do you have an Instagram account? (y/n): ") == "y"

print("Results:")
print("Interested in computer science:", "Yes" if computer_science else "No")
print("Playing computer games:", "Yes" if computer_games else "No")
print("Has an Instagram account:", "Yes" if instagram else "No")