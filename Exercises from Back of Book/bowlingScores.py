# A bowling score is made of 10 frames, each of which has either 1 or 2 deliveries. If all pins are bowled in the first, there is no second delivery.
# Rule A: The score of the frame is the pins bowled over in that frame, with the following exceptions:
# Rule B: If a strike, the score for that frame is 10+ the next two deliveries
# Rule C: If a spare, the score for that frame is 10+ the next delivery

# A game can be between 12 and 21 deliveries

# Each frame has two characters, appart from the last frame which has three, for a total of 21 characters
# No pins: -, Spare = n/, Strike = 'X '

# First 9 frames:
# 'X ', 'n/', or 'nm' where nm cannot equal 10
# Tenth frame:
# 'xxx', 'n/r' where n is '-' or 1-9, r is 'X', '-', or 1-9
# 'nm ' where the total is less than ten

# valid(game), scores(game), scoreCard()


# def valid(game):
#     """For example, '8/9-X X 6/4/X 8-X XXX' is a valid score"""

#     if type(game) != str:
#         print('Game is not a string')
#         return False

#     elif len(game) != 21:
#         print('Game string is not 21 characters in length')
#         return False

#     for char in game:
#         if char not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'X', '/', '-', ' ']:
#             print(f'Game string contains invalid character {char}')
#             return False
#     # need to add checking that each frame doesn't total more than 10, probably move tupling up here
#     print("Game is Valid")
#     return True


# def scores(game):
#     tuples = []
#     # Create a list of tuples, then loop through that list to get scores for each frame
#     for i in range(0, 17, 2):
#         # Loop through each score to create tuples apart from the last score
#         x, y = game[i], game[i+1]
#         tuples.append((x, y))
#     tuples.append((game[18], game[19], game[20]))

#     # convert to raw Scores to figure out scores with rules later
#     rawScores = []
#     for frame in tuples:
#         x, y = frame[0], frame[1]
#         # generator to convert - to 0
#         x, y = ((0 if n == '-' else n) for n in (x, y))

#         if x not in ['X', '/', ' '] and y not in ['X', '/', ' ']:
#             rawScores.append((int(x), int(y)))
#         elif y == '/':
#             secondNumber = 10 - int(x)
#             rawScores.append((int(x), secondNumber))
#         elif x == 'X':
#             rawScores.append((10, 0))

#     # do the same for the last frame
#     x, y, z = game[18], game[19], game[20]
#     x, y, z = ((0 if n == '-' else n) for n in (x, y, z))
#     if x not in ['X', '/', ' '] and y not in ['X', '/', ' ']:
#         rawScores.append((int(x), int(y), 0))
#     elif y == '/':
#         secondNumber = 10 - int(x)
#         rawScores.append((int(x), secondNumber, int(z)))
#     elif x == 'X' and y == 'X' and z == 'X':
#         rawScores.append((10, 10, 10))

#     # convert to scores with rules
#     # tuples = [('8', '/'), ('9', '-'), ('X', ' '), ('X', ' '), ('6', '/'), ('4', '/'), ('X', ' '), ('8', '-'), ('X', ' '), ('X', 'X', 'X')]
#     # rawScores = [(8, 2), (9, 0), (10, 0), (10, 0), (6, 4), (4, 6), (10, 0), (8, 0), (10, 0), (10, 0), (10, 10, 10)]
#     scores = []
#     total = 0

#     for i in range(0, 10):
#         pair = tuples[i]

#         if i == 9:
#             score = sum(rawScores[i])

#         elif pair[0] == 'X':
#             score = 10 + rawScores[i+1][0] + rawScores[i+1][1]
#         elif pair[1] == '/':
#             score = 10 + rawScores[i+1][0]
#         else:
#             score = rawScores[i][0] + rawScores[i][1]
#         scores.append(score)
#         total += score

#     print(scores)
#     print(total)


game = '8/9-X X 6/4/X 8-X XXX'


def valid(game):
    """For example, '8/9-X X 6/4/X 8-X XXX' is a valid score"""

    if type(game) != str:
        raise TypeError('Game is not in string format')

    frames = [game[i:i+2] for i in range(0, 18, 2)] + [game[18:]]
    if len(frames) != 10:
        raise ValueError('Must parse into exactly 10 frames')

    return frames


def framesToFlat(frames):
    """Converts frames into a flat list of roll scores"""
    rolls = []
    for frame in frames:
        for ch in frame:
            if ch == ' ':
                continue
            elif ch == 'X':
                # strike
                rolls.append(10)
            elif ch == '/':
                # spare, figures the number by subtracting the previous number from 10
                rolls.append(10 - rolls[-1])
            elif ch == '-':
                rolls.append(0)
            else:
                rolls.append(int(ch))
    return rolls


def score(rolls):
    i = 0
    scores = []
    for i in range(9):
        if rolls[i] == 10:  # strike
            frameScore = 10 + rolls[i+1] + rolls[i+2]
            scores.append(frameScore)
            i += 1
        elif rolls[i] + rolls[i+1] == 10:  # spare
            frameScore = 10 + rolls[i+2]
            scores.append(frameScore)
        else:
            frameScore = rolls[i] + rolls[i+1]
            scores.append(frameScore)
            i += 2

    tenthScore = sum(rolls[i:])
    scores.append(tenthScore)
    total = sum(scores)
    return scores, total


def main():
    try:
        frames = valid(game)
    except (TypeError, ValueError) as error:
        print('Invalid Game:', error)
        return

    rolls = framesToFlat(frames)
    frameScores, totalScore = score(rolls)

    print(frameScores)
    print(totalScore)


if __name__ == '__main__':
    main()
