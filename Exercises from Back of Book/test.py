game = '8/9-X X 6/4/X 8-X XXX'

frames = [game[i:i+2] for i in range(0, 18, 2)] + [game[18:]]
if len(frames) != 10:
    raise ValueError("Must parse into exactly 10 frames")

print(frames)
