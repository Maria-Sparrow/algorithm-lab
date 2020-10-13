from datetime import timedelta
import counter


def print_counter_result(elapsed_time: timedelta, sort_type: str):
    if sort_type == 'SELECTION':
        print('counter: ' + str(counter.select_compare_counter))
        print('swap: ' + str(counter.select_swap_counter))
    elif sort_type == 'MERGE':
        print('counter: ' + str(counter.merge_sort_compare_counter))
        print('swap: ' + str(counter.merge_sort_swap_counter))
    print('time: ' + str(elapsed_time))

