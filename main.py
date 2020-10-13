from timeit import default_timer as timer
from datetime import timedelta
import sys
import copy
import counter_meth
from sortPool import *

file = "basin.csv"
if len(sys.argv) != 0:
    file = sys.argv[0]

    list_of_basins = get_objects_from_csv(file)
    list_for_selection = copy.deepcopy(list_of_basins)
    print('-------------------------------------------')
    start = timer()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    selection_sort_by_volume(list_for_selection)
    elapsed_time = timedelta(((timer() - start) * 1000))
    counter_meth.print_counter_result(elapsed_time, 'SELECTION')


    for basin in list_for_selection:
        print(str(basin))
    print('--------------------------------------------')

    start = timer()
    list_of_basins = merge_sort_by_visitors(list_of_basins)
    elapsed_time = timedelta(((timer() - start) * 1000))
    counter_meth.print_counter_result(elapsed_time, 'MERGE')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    for basin in list_of_basins:
        print(str(basin))









