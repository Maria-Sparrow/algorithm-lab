import csv
import swimmingPool

file = "basin.csv"


def get_objects_from_csv(input_file):
    csv_file = open(file, newline='')
    reader = csv.reader(csv_file)
    list_of_pool = []
    for row in reader:
        print(row)
        new_pool = swimmingPool.SwimmingPool(address=row[0], volume_of_water=int(row[1]),
                                             max_number_of_visitors=int(row[2]))
        list_of_pool.append(new_pool)
    return list_of_pool


def selection_sort_by_volume(basin_list):
    length = len(basin_list)

    for item in range(length):
        minimum = item #мінім елем

        for iteration in range(item + 1, length):
            if basin_list[iteration].volume_of_water > basin_list[minimum].volume_of_water:
                minimum = iteration

        (basin_list[item], basin_list[minimum]) = (basin_list[minimum], basin_list[item])


def merge_sort_by_visitors(basin_list, ascending=True):
    result = []
    if len(basin_list) == 1:
        return basin_list
    middle = len(basin_list) // 2

    visitors_list1 = merge_sort_by_visitors(basin_list[:middle])

    visitors_list2 = merge_sort_by_visitors(basin_list[middle:])

    first_visitor = last_visitor = 0
    while first_visitor < len(visitors_list1) and last_visitor < len(visitors_list2):
        if visitors_list1[first_visitor].max_number_of_visitors < visitors_list2[last_visitor].max_number_of_visitors:
            result.append(visitors_list2[last_visitor])
            last_visitor = last_visitor + 1

        else:
            result.append(visitors_list1[first_visitor])
            first_visitor = first_visitor + 1

    result = result + visitors_list1[first_visitor:]

    result = result + visitors_list2[last_visitor:]
    if ascending == True:
        return result
    else:
        result.reverse()
        return result
