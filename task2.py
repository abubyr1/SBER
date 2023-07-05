def build_atm(atm_num: int, add_atm: int, distances: list) -> list:
    sorted_distances = sorted(distances, reverse=True)[0:add_atm]
    new_distances = []
    for i in range(atm_num):
        if distances[i] in sorted_distances:
            sorted_distances.remove(distances[i])
            if distances[i] % 2 == 1:
                new_distances.append(distances[i] // 2 + 1, distances[i] // 2)
            else:
                new_distances.append(distances[i] // 2, distances[i] // 2)
        else:
            new_distances.append(distances[i])
    return new_distances
