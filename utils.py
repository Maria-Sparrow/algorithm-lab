def wedding_func(people_list, len_of_graph):

    tribes = reboot(people_list, len_of_graph)

    boy_in_each_tribe = [boy_amount_in_tribe(tribe) for tribe in tribes]

    girl_in_each_tribe = [girl_amount_in_tribe(tribe) for tribe in tribes]

    all_possible_pairs = sum(boy_in_each_tribe) * sum(girl_in_each_tribe)

    pairs_in_one_tribe = sum(copy_couple(boy_in_each_tribe, girl_in_each_tribe))

    result = all_possible_pairs - pairs_in_one_tribe

    return result


def reboot(people_list, len_of_graph):
    tribes = []
    sorted_couple_list = sorted(people_list)
    for people in sorted_couple_list:
        if len_of_graph > 1000:
            print("Error! To much couples!")
            break
        for tribe in tribes:

            if people[0] in tribe:
                tribe.add(people[1])

                break

            elif people[1] in tribe:
                tribe.add(people[0])

                break

        else:

            tribes.append(set((people[0], people[1])))

    return tribes


def boy_amount_in_tribe(tribe):
    return len({boy_count for boy_count in tribe if boy_count % 2})


def girl_amount_in_tribe(tribes):
    return len({girl_count for girl_count in tribes if not girl_count % 2})


def copy_couple(boy_each_tribe, girl_in_each_tribe):
    return (boy * girl for boy, girl in zip(boy_each_tribe, girl_in_each_tribe))


