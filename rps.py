import random
choices = ["✊", "📄", "✂️"]

while True:
    user = input("Choose ✊,📄 or ✂️:" ).lower()

    if user not in choices:
        print("Invalid choice.")
        continue

    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif (
        (user == "✊" and computer == "✂️") or
        (user == "📄" and computer == "✊") or
        (user == "✂️" and computer == "📄")
    ):
        print("You win!")
    else:
        print("Computer wins!")

    play_again = input("Play again? (y/n): ")

    if play_again.lower() != "y":
        break