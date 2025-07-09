def filter_non_zero(d: dict[str, int]) -> dict[str, int]:
    result = {}
    for key in d:
        if d[key] != 0:
            result[key] = d[key]
    return result


data = {"a": 0, "b": 5, "c": 0, "d": 3}
print(filter_non_zero(data))

