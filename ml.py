# Features:
# 0. highest tile
# 1. number of sets of horizontally adjacent tiles
# 2. number of sets of vertically adjacent tiles
# 3. highest tile of horizontally adjacent tiles
# 4. highest tile of vertically adjacent tiles
# 5. number of blanks in top left quadrant
# 6. number of blanks in top right quadrant
# 7. number of blanks in btm left quadrant
# 8. number of blanks in btm right quadrant

def getFeatures(b):
    feats = [max(b)] + [0]*8

    # horizontal then vertical
    strips = [b[i:i+4] for i in range(0, 16, 4)], [[b[i] for i in range(j, 16, 4)] for j in range(4)]

    # feats 1 to 4
    for i in range(2):
        for j in range(4):
            strip = strips[i][j]

            # if the whole strip is blank do nothing
            if sum(strip) == 0:
                continue

            # remove blanks
            strip = [tile for tile in strip if tile != 0]

            # get adjacent repeated tile stats
            for k in range(len(strip) - 1):
                if strip[k] == strip[k+1]:
                    strip[k+1] = 0
                    feats[1 + i] += 1
                    feats[3 + i] = max(feats[3 + i], strip[k])

    # feats 5 to 8
    pos = [0,2,8,10]
    for i in range(4):
        mark = pos[i]
        feats[5 + i] = (b[mark:mark+2] + b[mark+4:mark+6]).count(0)

    return feats