"""Example of the use of some DSU methods."""


from dsu_data_structure import DSU


def main():
    dsu = DSU(range(6))
    print(f"dsu=DSU(range(6))\ndsu == {dsu}\n")

    dsu = DSU(range(6))
    items = dsu.items()
    print(f"dsu=DSU(range(6))\ndsu.items() == {items}\n")

    dsu = DSU(range(6))
    copy_dsu = dsu.copy()
    dsu.union(*dsu.items())
    print(f"dsu=DSU(range(6))\ndsu.union(*dsu.items())\n" \
        f"before:  {copy_dsu}\nafter:   {dsu}\n"
    )

    dsu = DSU(range(6))
    dsu.union(0, 1, 2)
    print(f"dsu=DSU(range(6)); dsu.union(0, 1, 2)\ndsu == {dsu}\n" \
        f"dsu.get_sets(2, 5) == {dsu.get_sets(2, 5)}\n" \
        f"dsu.get_sets(5) == {dsu.get_sets(5)}\n"
    )

    dsu = DSU(range(6))
    dsu.union(0, 1, 2)
    print(f"dsu=DSU(range(6)); dsu.union(0, 1, 2)\ndsu == {dsu}\n" \
        f"dsu.same(0, 1, 2) == {dsu.same(0, 1, 2)}\n" \
        f"dsu.same(0, 5) == {dsu.same(0, 5)}\n"
    )

    dsu = DSU(range(6))
    dsu.union(0, 1, 2)
    copy_dsu = dsu.copy()
    dsu.make(0, 10)
    print(f"dsu=DSU(range(6)); dsu.union(0, 1, 2)\n" \
        f"dsu.make(0, 10)\nbefore:  {copy_dsu}\nafter:   {dsu}\n"
    )

    dsu = DSU(range(6))
    dsu.union(0, 1, 2)
    copy_dsu = dsu.copy()
    dsu.remove_items(1, 4)
    print(f"dsu=DSU(range(6)); dsu.union(0, 1, 2)\n" \
        f"dsu.remove_items(1, 4)\nbefore:  {copy_dsu}\nafter:   {dsu}\n"
    )

    dsu = DSU(range(6))
    dsu.union(0, 1, 2)
    copy_dsu = dsu.copy()
    dsu.remove_sets(1, 4)
    print(f"dsu=DSU(range(6)); dsu.union(0, 1, 2)\n" \
        f"dsu.remove_sets(1, 4)\nbefore:  {copy_dsu}\nafter:   {dsu}\n"
    )

    dsu = DSU(range(6))
    dsu.union(0, 1)
    print(f"dsu=DSU(range(6)); dsu.union(0, 1)\n" \
        f"dsu == {dsu}\nlen(dsu) == {len(dsu)}\n"
    )


if __name__ == "__main__":
    main()
