"""Floor of a building of size n x m. There are always external walls.
Internal ones may be missing. Return the number of rooms and their area."""


from dsu_data_structure import DSU


def main():
    n, m = 4, 3
    floor = \
"""
+-+-+-+
|   | |
+-+ +-+
| | | |
+ +-+ +
| |   |
+ +-+ +
| | | |
+-+-+-+
"""

    arr = [x for x in floor.split('\n') if x]

    dsu = DSU(range(n * m))

    # horizontal bypass of walls
    for i in range(n):
        for j in range(m - 1):
            if arr[1 + i * 2][2 + j * 2] == ' ':
                dsu.union(i * m + j, i * m + (j + 1))

    # vertical bypass of walls
    for j in range(m):
        for i in range(n - 1):
            if arr[2 + i * 2][1 + j * 2] == ' ':
                dsu.union(i * m + j, (i + 1) * m + j)

    count_area = dict()

    for set_ in dsu.get_sets(*dsu.items()):
        area = len(set_)
        if area not in count_area:
            count_area[area] = 0
        count_area[area] += 1

    print("room statistic:")
    for k, v in count_area.items():
        print(f"area: {k}, count: {v}")


if __name__ == "__main__":
    main()
