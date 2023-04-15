import sys

img = [list('...................................................'),
       list('...........##################......................'),
       list('...........#................#......................'),
       list('...........#.......#........#......................'),
       list('...........#.......#........#......................'),
       list('...........#.......#........#......................'),
       list('...........##################......................'),
       list('...................................................')]

new_symbol = "o"
y = 4
x = 12
HEIGHT = len(img)
LENGTH = len(img[0])


def flood_fill(img, y, x, new_symbol, old_symbol=None):
    if old_symbol is None:
        old_symbol = img[y][x]
    if img[y][x] == new_symbol or img[y][x] != old_symbol:
        return
    img[y][x] = new_symbol

    piring_image(img)

    if y + 1 < HEIGHT:
        flood_fill(img, (y + 1), x, new_symbol, old_symbol)
    if y - 1 >= 0:
        flood_fill(img, (y - 1), x, new_symbol, old_symbol)
    if x + 1 < LENGTH:
        flood_fill(img, y, (x + 1), new_symbol, old_symbol)
    if x - 1 >= 0:
        flood_fill(img, y, (x - 1), new_symbol, old_symbol)


def piring_image(img):
    for y in img:
        for x in y:
            sys.stdout.write(x[0])
        sys.stdout.write("\n")
    sys.stdout.write("\n")


flood_fill(img, y, x, new_symbol)
piring_image(img)
