def convert_time(time):
    new_time = int(time.replace(":", ""))

    return new_time


def create_obj(time):

    r_time = time[2:]

    obj = dict(
        day=time[:2],
        min_time=convert_time(r_time.split("-")[0]),
        max_time=convert_time(r_time.split("-")[1]),
    )

    return obj


def build_list_obj(v):

    list_time = []
    for item in v:
        list_time.append(create_obj(item.strip()))

    return list_time


def process_file():

    m = {}
    with open("example.txt", "r") as file:
        for line in file:
            m[line.split("=")[0]] = build_list_obj(line.split("=")[1].split(","))

    return m


def compare_list(list_1, list_2):

    count = 0
    for item in list_1:
        for time in list_2:
            if (item["day"] == time["day"]) and (
                (item["min_time"] <= time["max_time"])
                and (item["max_time"] >= time["min_time"])
            ):
                count += 1

    return count


if __name__ == "__main__":

    resp = {}
    dict = process_file()
    keys = dict.keys()
    values = dict.values()
    i = 0
    j = 0
    k = list(keys)
    v = list(values)

    for key in k:
        j = i + 1
        for value in v:
            if j < len(k):

                print(k[i], "-", k[j], ":", compare_list(v[i], v[j]))

            j += 1
        i += 1
