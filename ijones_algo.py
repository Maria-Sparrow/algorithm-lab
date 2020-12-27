from collections import defaultdict
from typing import List

INPUT_FILE_NAME = "test.in"
OUTPUT_FILE_NAME = "test.out"


def read_input_data():
    with open(INPUT_FILE_NAME, "r") as input_file:
        width, height = [int(number) for number in input_file.readline().split()]
        corridor = [[letter for letter in row] for row in input_file.readlines()]
    return corridor, width, height


def write_output_data(ways: int):
    with open(OUTPUT_FILE_NAME, "w") as output_file:
        output_file.write(str(ways))


def find_ways(corridor: List[List[int]], width: int, height: int) -> int:

    ways_number_for_tile = []
    for tile in range(height):
        list_ways_number_for_tile = []
        for row in range(width):
            list_ways_number_for_tile.append(0)
        ways_number_for_tile.append(list_ways_number_for_tile)

    ways_number_for_letter = defaultdict(int)
    for row in range(height): #ітеруємося по плиточках першого стовпця
        tile_letter = corridor[row][0]
        ways_number_for_tile[row][0] = 1 # 1 шлях
        ways_number_for_letter[tile_letter] += 1 #якщо букви повторяються

    for col in range(1, width): # в двох вкладених форах, ітеруємося по стовпцях починаючи з першого
        letter_ways_number_for_current_column = defaultdict(int)
        previous_column = col - 1 # зберігаємо значення індексу попередньої колонки
        for row in range(height): # дивимося на кожну клітинку окремо
            tile_letter = corridor[row][col] # зберіг зн поточної клітинки
            ways = ways_number_for_letter[tile_letter] # глобальний словник: дивимось, скіьки в нас на даному етапі є шляхів до букви на якій ми стоїмо
            if tile_letter != corridor[row][previous_column]:# порівлюємо, що tile_letter(поточна буква) така ж як (буква, яка лівіше) в тому ж рядку
                ways += ways_number_for_tile[row][previous_column]# додаємо, якщо виконується умова, (дивимося на клітинку)
            ways_number_for_tile[row][col] = ways # сетаємо к-сть способів дістатися до клітинки
            letter_ways_number_for_current_column[tile_letter] += ways # способи потрапити в букву, з поточної колонки
        update_letter_ways(letter_ways_number_for_current_column, ways_number_for_letter)
    if height == 1: # 1 рядок
        return ways_number_for_tile[0][width - 1] # значеняя шляхів в певну клітинку
    else:
        return ways_number_for_tile[0][width - 1] + ways_number_for_tile[height - 1][width - 1]


def update_letter_ways(letter_ways_number_for_current_column: defaultdict, ways_number_for_letter: defaultdict) -> None:
    for tile_letter in letter_ways_number_for_current_column:
        ways_number_for_letter[tile_letter] += letter_ways_number_for_current_column[tile_letter]


if __name__ == "__main__":
    corridor, width, height = read_input_data()
    successful_ways_number = find_ways(corridor, width, height)
    write_output_data(successful_ways_number)
