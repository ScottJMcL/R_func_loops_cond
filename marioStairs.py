def marioStairs(steps):
    # each level contins same number of charachers
    # top always has one X
    # each lvl has n + 1 
    # bottom has steps * X
    
    num_x = 0
    while steps > 0:
        num_x += 1
        print("X" * num_x)
        steps -= 1

marioStairs(20)