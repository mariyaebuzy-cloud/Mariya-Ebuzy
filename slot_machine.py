import random

symbols = ["🍒", "🍋", "🔔", "⭐", "7"]

balance = 100

print("🎰 Welcome to the Slot Machine!")

while balance > 0:
    print(f"\nCurrent Balance: ${balance}")

    try:
        bet = int(input("Enter your bet amount: $"))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if bet <= 0:
        print("Bet must be greater than 0.")
        continue

    if bet > balance:
        print("You don't have enough money!")
        continue

    reels = [random.choice(symbols) for _ in range(3)]

    print("\n|", reels[0], "|", reels[1], "|", reels[2], "|")

    if reels[0] == reels[1] == reels[2]:
        winnings = bet * 5
        balance += winnings
        print(f"🎉 JACKPOT! You won ${winnings}")
    elif reels[0] == reels[1] or reels[1] == reels[2] or reels[0] == reels[2]:
        winnings = bet * 2
        balance += winnings
        print(f"✨ Nice! You won ${winnings}")
    else:
        balance -= bet
        print("😢 Better luck next time!")

    if balance <= 0:
        print("\nGame Over! You're out of money.")
        break

    play_again = input("Play again? (y/n): ").lower()
    if play_again != "y":
        break

print(f"\nFinal Balance: ${balance}")
print("Thanks for playing!")
