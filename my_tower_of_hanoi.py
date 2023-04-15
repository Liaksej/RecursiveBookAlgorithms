first_spire = [6, 5, 4, 3, 2, 1]
second_spire = []
third_spire = []


def move_one_disk(from_spire, to_spire):
    to_spire.append(from_spire.pop())


def solve_hannoi(number_of_disks, start_spire, end_spire, temp_spire):
    # BASE-CASE
    if number_of_disks == 1:
        move_one_disk(start_spire, end_spire)

    # RECURSIVE CASE
    else:
        solve_hannoi(number_of_disks - 1, start_spire, temp_spire, end_spire)
        move_one_disk(start_spire, end_spire)
        solve_hannoi(number_of_disks - 1, temp_spire, end_spire, start_spire)


solve_hannoi(len(first_spire), first_spire, second_spire, third_spire)
print(first_spire)
print(second_spire)
print(third_spire)
