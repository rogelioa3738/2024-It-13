import random



def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("You did not choose a valid response")


# generate an integer between 0 and 6
# to simulate a roll of a die
def roll_die():
    roll_result = random.randint(1, 6)
    return roll_result


# rolls two dice and returns and whether we
# had a double roll
def two_rolls(who):
    double_score = "no"

    # roll two dice
    roll_1 = roll_die()
    roll_2 = roll_die()

    # check if we have a double score opportunity
    if roll_1 == roll_2:
        double_score = "yes"

    # Find th total points (so far)
    first_points = roll_1 + roll_2

    # Show the user result
    print(f"{who}: {roll_1} & {roll_2} - Total: {first_points}")

    return first_points, double_score

# checks that user enter an integer
# that is more than 13
def int_check(question):

    while True:

        error = "Please enter and integer that is 13 or more."

        try:
            response = int(input(question))

            # checks that the number is greater than / equal to 13
            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def instructions():
    print('''

**** Instructions ****

To begin, decide on a score goal (eg: The first one to get a score of 50 wins)

For each round of the game, you win points by rolling the dice.
The winner of the round is the one who gets 13 (or slightly less).

If you win the round, then your score will increase by the number of points that you earned. If you first roll of two
dice is double (eg: both dice show three), then your score will be DOUBLE the number of points.

If you lose the round, then you don't get any points.

If you tie (eg: you both get a score of 11, then you will have 11 adding to your score).

Your goal is to try to get to the target score before the computer.

Good luck.

    ''')


# finds the lowest, highest and average score from a list
def get_stats(stats_list):

    # sort the lists.
    stats_list.sort()

    # find the lowest, highest and average scores...
    lowest_score = stats_list[0]
    highest_score = stats_list[-1]
    average_score = sum(stats_list) / len(stats_list)

    return [lowest_score, highest_score, average_score]


# main routine goes here

# initiate user score and computer score
user_score = 0
comp_score = 0

num_rounds = 0

# create lists to hold user and computer scores, computer scores and game history
user_scores = []
comp_scores = []
game_history = []

# Program starts here (with a heading)
print()
print("🎲🎲Roll it 13🎲🎲")
print()

# Display instructions if user wants to see then
want_instructions = yes_no("Do you want to read instructions? ")

if want_instructions == "yes":
    instructions()

# Get target score (must be an integer more than 13)
print()
target_score = int_check("Enter a target score: ")
print()


# Loop game until we have a winner
while user_score < target_score and comp_score < target_score:
    # Add one to the number of rounds (for our heading)
    num_rounds += 1
    print(f"🕜🕜🕜 Round {num_rounds} 🕜🕜🕜")

    # Start of a single round

    # Initialise 'pass' variables
    user_pass = "no"
    computer_pass = "no"

    # Start Round...
    print("Press <enter> to begin this round: ")
    input()

    # Get initial dice rolls for user
    user_first = two_rolls("User")
    user_points = user_first[0]
    double_points = user_first[1]

    # Tell the user id there are eligible for double points
    if double_points == "yes":
        print("If you win this round, you get double points!")

    # Get initial dice rolls for computer
    computer_first = two_rolls("computer")
    computer_points = computer_first[0]

    # print(f"The computer rolled a total of {computer_points}.")

    # Loop (while both user / computer have <= 13 points)...
    while computer_points <= 13 and user_points <= 13:

        # ask user if they want roll again, update
        # points / status
        print()

        # If the user has 13 points, we can assume they don't want to roll again!
        if user_points == 13:
            user_pass = "yes"

        if user_pass == "no":
            roll_again = input("Do you want to roll the dice (type 'no' to pass): ")
        else:
            roll_again = "no"

        if roll_again == "yes":
            user_move = roll_die()
            user_points += user_move

            # If user goes over 13 points, tell them that they lose and set points to 0
            if user_points > 13:
                print(f"✨✨✨Oops! Your rolled a {user_move} so your total is {user_points}. "
                      f"Which is over 13 points. ✨✨✨")

                # reset user points to zero so that when we update their
                # score at the end of round it is correct.
                user_points = 0

                break

            else:
                print(f"You rolled a {user_move} and have a total of {user_points}.")


        else:
            # If user passes, we don't want to roll them again!
            user_pass = "yes"

        # If computer has 10 or more (and is winning), It should pass!
        if computer_points >= 10 and computer_points >= user_points:
            computer_pass = "yes"
        elif computer_pass == "yes":
            pass

        else:
            # Roll die for computer and update computer points
            computer_move = roll_die()
            computer_points += computer_move

            # checks computer has not gone over...
            if computer_points > 13:
                print(f"✨✨✨The computer rolled a {computer_move}, taking their points"
                      f" to {computer_points}. This is over 13 points so the computer loses!✨✨✨")
                computer_points = 0
                break

            else:
                print(f"The computer rolled a {computer_move}.  The computer"
                      f" now has {computer_points}.")

        print()
        # Tell the user if they are winning, losing or having a tie.
        if user_points > computer_points:
            result = "😊😊😊 You are ahead 😊😊😊"
        elif user_points < computer_points:
            result = "😯😯😯 The computer is ahead! 😯😯😯"
        else:
            result = "💀💀💀 It's currently a tie. 💀💀💀"

        print(f"{result} \tUser: {user_points} \t | \t Computer: {computer_points}")

        # if both the user and the computer passed,
        # we need to exit the loop.
        if computer_pass == "yes" and user_pass == "yes":
            break

    # Outside loop - double user points if they won and are eligible

    # Show rounds result
    print()

    if user_points < computer_points:
        print("😫😫😫Sorry you have lost this round and no points "
              "have been added to your total score. The computer's score has "
              f"increased by {computer_points} points.😫😫😫 ")

        add_points = computer_points

    # Currently does not include loop points
    elif user_points > computer_points:
        # Double user points if they are eligible
        if double_points == "yes":
            user_points *= 2

        print(f"🥳🥳🥳 Yay! You have won the round and {user_points} points have "
              f"been added to your score 🥳🥳🥳")

        add_points = user_points

    else:
        print(f"😎😎😎The result for this round is a tie. You and the computer"
              f"both have {user_points}.😎😎😎")

        add_points = user_points

    # Record round result and add it to the game history
    round_results = f"Round {num_rounds} - User: {user_points} \t Computer: {computer_points}"
    game_history.append(round_results)

    # End of a single round

    # If the computer wins, add its points to its score
    if user_points < computer_points:
        comp_score += add_points

    # If the user wins, add their points to their score
    elif user_points > computer_points:
        user_score += add_points

    # If it's a tie, add their points to BOTH SCORES
    else:
        comp_score += add_points
        user_score += add_points

    user_scores.append(user_points)
    comp_scores.append(computer_points)

    print()
    print(f"🎲🎲🎲 User: {user_score} points | Computer: {comp_score} points 🎲🎲🎲")
    print()

if user_score > comp_score:
    print("👍👍👍 Game over - You Won!! 👍👍👍")
elif comp_score > user_score:
    print("👎👎👎 Game over - You Lost 👎👎👎")
else:
    pass
print(f"Final scores: User ({user_score}) vs Computer ({comp_score})")
print()

# Display game history if user wants to see it
show_history = yes_no("Do you want to see the game history?")
if show_history == "yes":
    print("\n ⌛⌛⌛Game History⌛⌛⌛")

    for item in game_history:
        print(item)

    print()

# calculate the lowest, highest and average
# scores and display them.

user_stats = get_stats(user_scores)
comp_stats = get_stats(comp_scores)

print("🎆🎆🎆 Game Statistics 🎆🎆🎆")
print(f"User     - Lowest Score: {user_stats[0]}\t "
      f"Highest Score: {user_stats[1]}\t"
      f"Average Scores: {user_stats[2]:.2f}")

print(f"Computer - Lowest Score: {comp_stats[0]}\t "
      f"Highest Score: {comp_stats[1]}\t"
      f"Average Scores: {comp_stats[2]:.2}")

print()
print("THANK YOU FOR PLAYING!")