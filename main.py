from lib import process_file, compare_list

if __name__ == "__main__":

    resp = {}
    dict = process_file()
    i = 0
    j = 0
    list_key = list(dict.keys())
    list_value = list(dict.values())

    for key in list_key:
        j = i + 1
        for value in list_value:
            if j < len(list_key):

                print(
                    list_key[i],
                    "-",
                    list_key[j],
                    ":",
                    compare_list(list_value[i], list_value[j]),
                )

            j += 1
        i += 1
