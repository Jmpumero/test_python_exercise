from cmath import e


def convert_time(time):
    try:
        new_time = int(time.replace(":", ""))
        if new_time >= 0 and new_time <= 2359:
            return new_time
    except Exception as e:
        print(e)
        return -1


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

    dict = {}
    with open("example.txt", "r") as file:
        for line in file:
            dict[line.split("=")[0]] = build_list_obj(line.split("=")[1].split(","))

    return dict


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
