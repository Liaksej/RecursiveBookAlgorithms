# Set up towers A, B and C. The ned of the list of the top of the tower.
import sys

TOTAL_DISKS = 6

# Populate Tower A:
TOWERS = {"A": list(reversed(range(1, TOTAL_DISKS + 1))), "B": [], "C": []}


def printDick(diskNum):
    # Print a single disk of width diskNum.
    emptySpace = " " * (TOTAL_DISKS - diskNum)
    if diskNum == 0:
        # Just draw a pole
        sys.stdout.write(emptySpace + "||" + emptySpace)
    else:
        # Draw the disk.
        diskSpace = "@" * diskNum
        diskNumLabel = str(diskNum).rjust(2, "_")
        sys.stdout.write(emptySpace + diskSpace + diskNumLabel + diskSpace + emptySpace)


def printTowers():
    # Print all three towers.
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (TOWERS["A"], TOWERS["B"], TOWERS["C"]):
            if level >= len(tower):
                printDick(0)
            else:
                printDick(tower[level])
        sys.stdout.write("\n")
    # Print the tower labels A, B and C.
    emptySpace = " " * (TOTAL_DISKS)
    print(
        "%s A%s%s B%s%s C\n"
        % (emptySpace, emptySpace, emptySpace, emptySpace, emptySpace)
    )


def moveOneDisc(startTower, endTower):
    # Move the top disk from startTower to endTower.
    disk = TOWERS[startTower].pop()
    TOWERS[endTower].append(disk)


def solve(numberOfDisks, startTower, endTower, tempTower):
    # Move the top numberOfDisk disks from startTower to endTower.
    if numberOfDisks == 1:
        # BASE CASE
        moveOneDisc(startTower, endTower)
        printTowers()
        return
    else:
        # RECURSIVE CASE
        solve(numberOfDisks - 1, startTower, tempTower, endTower)
        moveOneDisc(startTower, endTower)
        printTowers()
        solve(numberOfDisks - 1, tempTower, endTower, startTower)
        return


# Solve:
printTowers()
solve(TOTAL_DISKS, "A", "B", "C")

# Uncomment to enable interactive mode:
# while True:
#     printTowers()
#     print('Enter letter of start tower and the end tower. (A, B, C) Or Q to quit.')
#     move = input().upper()
#     if move == 'Q':
#         sys.exit()
#     elif move[0] in 'ABC' and move[1] in 'ABC' and move[0] != move[1]:
#         moveOneDisc(move[0], move[1])
