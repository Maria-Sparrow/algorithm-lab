import sys


def read_pairs(filename, couple_list):
    try:
        with open(filename, "r") as file:
            for line in file:
                first_person, second_person = line.split(" ")
                first_person = int(first_person)
                second_person = int(second_person)
                couple_list.append((first_person, second_person))
            return couple_list

    except (FileNotFoundError):
        sys.exit(f'file "{filename}" not found')


def write_result(filename, result):
    with open(filename, "w") as file:
        file.write(str(result))
