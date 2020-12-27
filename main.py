def naive_search(string:str, substring:str):
    result = []
    for element in range(len(string)-len(substring)+1):
        for sub_element in range(len(substring)):
            if not string[element+sub_element]==substring[sub_element]:
                break
        else:
            result.append((element, element+len(substring)))
    return result