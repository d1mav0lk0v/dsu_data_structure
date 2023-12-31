# DSU - disjoint-set-union

### Info

See the disjoint set union data structure description at the [link](https://en.wikipedia.org/wiki/Disjoint-set_data_structure).

This implementation is built on sets and not references to parents. Therefore, the complexity of the operation is different from the article. Also added some useful methods.

Basic methods and their complexity:
* **same O(m)** - check items from the same set;
* **union O(m + n)** - union sets into one set based on their items;
* **make O(m)** - make a new set for an item or separate this item from its set;
* **remove_items O(m)** - remove an item from a structure;
* **remove_sets O(m + n)** - remove a set from a structure based on its item.

Where:
* **m** - number of method parameters (items), usually 1-2;
* **n** - number of items in the DSU.

Additional methods allow:
* get sets based on their items;
* get all items from sets;
* get a copy DSU;
* clear the DSU of all items;
* check the DSU for emptiness;
* get number of items;
* get string representation;
* compare two structures DSU;
* check whether an item is contained in one of the sets;
* get iterator over all items.

---

### Prerequisites

Language version starting from 3.10+

```bash
$ python --version
Python 3.10.4
```

---

### Installation

```bash
pip install dsu_data_structure
```

---

### Usage

Open the [folder](examples) to view details.

```python
>>> from dsu_data_structure import DSU

>>> dsu = DSU(range(6))
>>> print(dsu)
[{0}, {1}, {2}, {3}, {4}, {5}]

>>> print(dsu.items())
{0, 1, 2, 3, 4, 5}

>>> dsu.union(0, 1, 2, 3)
>>> print(dsu)
[{0, 1, 2, 3}, {4}, {5}]

>>> dsu.same(0, 2)
True
>>> dsu.same(0, 5)
False

>>> dsu.make(0, 10)
>>> print(dsu)
[{0}, {1, 2, 3}, {4}, {5}, {10}]

>>> dsu.remove_items(0, 2)
>>> print(dsu)
[{1, 3}, {4}, {5}, {10}]

>>> dsu.remove_sets(3)
>>> print(dsu)
[{4}, {5}, {10}]
```

---

### Authors

* [Dmitry Volkov](https://github.com/d1mav0lk0v)

---

### License

MIT License - see the [LICENSE](LICENSE) file for details

---
