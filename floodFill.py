import sys

# Create the image (make sure it's rectangular!)

im = [list('..########################...........'),
      list('..#......................#...#####...'),
      list('..#..........########....#####...#...'),
      list('..#..........#......#............#...'),
      list('..#..........########.........####...'),
      list('..######......................#......'),
      list('.......#..#####.....###########......'),
      list('.......####...#######................')]

HEIGHT = len(im)
WIDTH = len(im[0])


def flood_fill(image, x, y, new_char, old_char=None):
    if old_char is None:
        # old_char defaults to the character at x, y.
        old_char = image[y][x]
    if old_char == new_char or image[y][x] != old_char:
        # BASE CASE
        return

    image[y][x] = new_char  # Change the character.

    # Uncomment  to view each step:
    print_image(image)

    # Change the neighboring characters.
    if y + 1 < HEIGHT and image[y + 1][x == old_char]:
        # RECURSIVE CASE
        flood_fill(image, x, y + 1, new_char, old_char)
    if y - 1 >= 0 and image[y - 1][x] == old_char:
        # RECURSIVE CASE
        flood_fill(image, x, y - 1, new_char, old_char)
    if x + 1 < WIDTH and image[y][x + 1] == old_char:
        # RECURSIVE CASE
        flood_fill(image, x + 1, y, new_char, old_char)
    if x - 1 >= 0 and image[y][x - 1] == old_char:
        # RECURSIVE CASE
        flood_fill(image, x - 1, y, new_char, old_char)
    return  # BASE CASE


def print_image(image):
    for y in range(HEIGHT):
        # Print each row.
        for x in range(WIDTH):
            # Print each column.
            sys.stdout.write(image[y][x])
        sys.stdout.write('\n')
    sys.stdout.write('\n')


print_image(im)
flood_fill(im, 3, 3, 'o')
print_image(im)
