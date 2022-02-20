import os


def short_name(full_name):
    return f"{full_name[1]} {full_name[0][0]}."


def average_rating(rating):
    return sum(rating)/len(rating)


def print_dict(_dict, rating=10):
    return [f"{key}".ljust(20)+f"{value}\n" for key, value in _dict.items() if value < rating]
       


def create_report_from_file(path):
    info = {}

    with open(path, encoding='utf-8') as f:

        for item in f.readlines():

            _key = short_name([x for x in item.split() if x.isalpha()])

            _value = average_rating([int(x)
                                    for x in item.split() if x.isdigit()])

            info[_key] = round(_value, 2)
    return info


def report_in_file(path, _dict):
    with open(path, 'w', encoding='utf-8') as f:
        for item in print_dict(_dict):
            f.write(item)


_report = create_report_from_file(r"HW_6\file.txt")
print(f"Учащиеся, чей средний балл меньше 5 :\n{''.join(print_dict(_report, 5))}")
print(f"Cредний балл по классу :{round(average_rating(_report.values()),2)}")
report_in_file(r"HW_6\result.txt", _report)
