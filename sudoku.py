import random as rand
import copy


def pattern(r, c):
    """
    Returns a valid pattern for a tile in a sudoku field.
    If this function is used on an unshuffled 9x9 list,
    the result will be:
    [[1, 2, 3, 4, 5, 6, 7, 8, 9],
     [4, 5, 6, 7, 8, 9, 1, 2, 3],
     [7, 8, 9, 1, 2, 3, 4, 5, 6],
     [2, 3, 4, 5, 6, 7, 8, 9, 1],
     [5, 6, 7, 8, 9, 1, 2, 3, 4],
     [8, 9, 1, 2, 3, 4, 5, 6, 7],
     [3, 4, 5, 6, 7, 8, 9, 1, 2],
     [6, 7, 8, 9, 1, 2, 3, 4, 5],
     [9, 1, 2, 3, 4, 5, 6, 7, 8]]

    :param r int - number of row
    :param c int - number of column
    :return int - value for the respective tile
    """
    return (3 * (r % 3) + r // 3 + c) % 9


def shuffle(s):
    """
    Returns a random sample of a list.

    :param s list - a list
    :return list - shuffled list
    """
    return rand.sample(s, len(s))


def draw(field):
    """
    Prints the sudoku field.

    :param field list - sudoku field
    """
    for i in range(10):
        if i == 0:
            print("   ", end="")
        elif i == 9:
            print(chr(ord('A') + (i - 1)), end=" ")
        else:
            print(chr(ord('A') + (i - 1)), end=" ")
    print()
    for i in range(9):
        if i == 3 or i == 6:
            print("   ", end="")
            for j in range(9):
                if j != 8:
                    print("--", end="")
                else:
                    print("-", end="")
            print()
        print(i + 1, end=": ")
        for j in range(9):
            val = "."
            if field[i][j] != val:
                val = str(field[i][j])
            if j == 2 or j == 5:
                print(val, end="|")
            else:
                print(val, end=" ")
        print()


jokes = ["I'm afraid for the calendar. Its days are numbered.",
         "What do you call a factory that makes okay products? A satisfactory.",
         "What kind of drink can be bitter and sweet? Reali-tea.",
         "What did Tennessee? The same thing as Arkansas.",
         "Why do bees have sticky hair? Because they use a honeycomb.",
         "What’s the most detail-oriented ocean? The Pacific.",
         "Want to know why nurses like red crayons? "
         "Sometimes they have to draw blood.",
         "Why do some couples go to the gym? "
         "Because they want their relationship to work out.",
         "How does a man on the moon cut his hair? Eclipse it."]
jokes = shuffle(jokes)


def update(pos, value, field, correct, blank):
    """
    Updates the field and quantity of blank tiles by analysing the user response.

    :param pos string - coordinates in form "A1"
    :param value int - number from 1 to 9, user input value for tile
    :param field list - sudoku field
    :param correct list - correct field without blanks
    :param blank int - number of blank fields

    :return list [True/False, blank, field] - True if game is continued,
    False if not.
    """
    letter = pos[0]
    number = int(str(pos[1]))
    letter_pos = ord(letter) - ord('A')
    if correct[number - 1][letter_pos] != int(value):
        print("Whoops! You did not pass mathematical analysis."
              " Now you will be expelled from UCU! What a shame!")
        return False, blank, field
    else:
        field[number - 1][letter_pos] = value
        blank -= 1
        if blank == 0:
            print("Congratulations!!! You won!\n"
                  "You passed mathematical analysis! Now you have 61.\n"
                  "You are lucky, "
                  "but next time there will not be such an offer!")
        else:
            if blank == 1:
                print("Good job! Only 1 tile left to fill!")
            else:
                print(f"Good job! Only {blank} tiles left to fill!")
            print(f"And here is a joke from the professor:\n"
                  f"{jokes[blank - 1]}")
    return True, blank, field


def play():
    """
    Function that is used to run the game.
    Here, the playing field is created and user's inputs are
    checked.
    """
    rows = [g * 3 + r for g in shuffle(range(3)) for r in shuffle(range(3))]
    cols = [g * 3 + r for g in shuffle(range(3)) for r in shuffle(range(3))]
    nums = shuffle(range(1, 10))

    field = [[nums[pattern(r, c)] for c in cols] for r in rows]
    correct = copy.deepcopy(field)

    diff = 8
    blank = 81 // diff
    for tile in rand.sample(range(81), blank):
        field[tile // 9][tile % 9] = "."

    draw(field)

    while blank > 0:
        while True:
            change = input(">>> ").split()
            if not change[1].isnumeric() \
                    or not (0 <= ord(change[0][0]) - ord('A') < 9) \
                    or not change[0][1].isnumeric() \
                    or field[int(change[0][1]) - 1][ord(change[0][0]) - ord('A')] != ".":
                print("Invalid input!")
            else:
                break
        updates = update(change[0], change[1], field, correct, blank)
        if updates[0]:
            blank = updates[1]
            field = updates[2]
            if blank == 0:
                break
            draw(field)
        else:
            return


if __name__ == "__main__":
    print("Welcome to Sudoku!\n"
          "You failed to pass the exam in mathematical analysis and\n"
          "Stepan Fedynyak has just given you the last chance to pass\n"
          "this course: win at Sudoku.\n"
          "In this game, you need to fill out the blank tiles so that\n"
          "all numbers in each column, row and 3x3 square are unique.\n"
          "To fill a tile, write the coordinates of the tile and value\n"
          "in this form: A1 1")
    print("Let's start!")
    play()
