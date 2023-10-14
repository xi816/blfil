import time

time.sleep(.3)

# Player class
class Player:
    def __init__(self, pos, char):
        self.pos = pos
        self.char = char

class Anim:
    def __init__(self, frames, speed):
        self.frames = frames
        self.speed = speed


# Screen resolution
W = 40
H = 10

# Grid settings
grid = [[32 for i in range(W)] for j in range(H)]

grid[0] = grid[-1] = [126 for i in range(W)]
for i in range(1, len(grid)):
    grid[i][0] = grid[i][-1] = 124

def set_anim(grid, pos, frame):
    for i1, i2 in enumerate(frame.split("\n")):
        for j1, j2 in enumerate(i2):
            grid[i1+pos[1]][j1+pos[0]] = j2
    return grid

ANIM1 = [
        "^  \n|  \n|  ",
        "-> \n|  \n   ",
        "-->\n   \n   ",
        " -|\n  v\n   ",
        "  |\n  |\n  <",
        "   \n  |\n <-",
        "   \n   \n<--",
        "   \n^  \n|- "
]
ANIM2 = [
        "<---   >",
        "< ---  >",
        "<  --- >",
        "<   --->",
        "<-   -->",
        "<--   ->"
]

ANIM3 = [
        "~Animation  ~",
        "~ Animation ~",
        "~  Animation~",
        "~n  Animatio~",
        "~on  Animati~",
        "~ion  Animat~",
        "~tion  Anima~",
        "~ation  Anim~",
        "~mation  Ani~",
        "~imation  An~",
        "~nimation  A~"
]

t4 = "<!DOCTYPE html>\n<html>\n  <body>\n    Hello\n  </body>\n</html>"
ANIM4 = [t4[:i] for i in range(len(t4) + 1)]

# Plotting
def plot(grid):
    for i1, i2 in enumerate(grid):
        for j1, j2 in enumerate(i2):
            print((chr(j2) if type(j2) is int else j2), end = "")
        print()
    print()

# Starting
RUN = True

with open("config.anim", "r") as f:
    code = f.read()

for i in [j for j in code.split("\n") if j != ""]:
    exec(f"AC{i[-1][-1]} = 0")


while RUN:
    for i in [j for j in code.split("\n") if j != ""]:
        exec(f"grid = set_anim({i[:-7]}, ANIM{i[-1]}[AC{i[-1][-1]}])")
        exec(f"AC{i[-1][-1]} = (AC{i[-1][-1]} + 1) % len(ANIM{i[-1][-1]})")

    plot(grid)
    time.sleep(.1)

