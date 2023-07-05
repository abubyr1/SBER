def get_max_number(str_list: list) -> int:
    str_list.sort(reverse=True, key=lambda x: x + x[-1] * (9 - len(x)))
    result = ''.join(str_list)
    return int(result)
