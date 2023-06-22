from queue import PriorityQueue


class Element:
    def __init__(self, x, y, cls=None):
        self.x = x
        self.y = y
        self.cls = cls

    def __lt__(self, other):
        # Do not forget that when given a tuple, python compares the
        # elements to order them, if they are equal it compares the
        # second elements. That is why we give the second elements a
        # comparison function

        return self.x + self.y < other.x + other.y

    def __str__(self):
        return "Element {}, {} of class {}".format(self.x, self.y, self.cls)

    def set_class(self, cls):
        self.cls = cls

    def get_class(self):
        return self.cls

    def dist(self, el):
        f = (self.x - el.x)**2 + (self.y - el.y)**2
        return float(f ** (1/2))


def max_list(liste):  # Return the index of the max element in a list

    return liste.index(max(liste))


def fill_base(base_el):  # Fill the given set with elements

    base_el.add(Element(1, 1, 'A'))
    base_el.add(Element(1, 2, 'A'))
    base_el.add(Element(1, 3, 'A'))
    base_el.add(Element(1, 6, 'B'))
    base_el.add(Element(2, 2, 'A'))
    base_el.add(Element(2, 3, 'A'))
    base_el.add(Element(2, 6, 'B'))
    base_el.add(Element(3, 2, 'A'))
    base_el.add(Element(3, 6, 'B'))
    base_el.add(Element(4, 4, 'B'))
    base_el.add(Element(4, 5, 'B'))
    base_el.add(Element(4, 6, 'B'))


def knn(base_el, el, k, cls):
    # Classify the parameter element el, given already classified elements
    # base_el. Look at the k nearest neighbors. Classification classes are
    # given as cls

    k_nearest = PriorityQueue()

    for bas in base_el:
        print("dist is", el.dist(bas))
        k_nearest.put((el.dist(bas), bas))

    votes = [0 for i in range(len(cls))]
    for _ in range(k):
        (d, cur) = k_nearest.get()
        print(cur)
        votes[cls.index(cur.get_class())] += 1

    el.set_class(cls[max_list(votes)])

    base_el.add(el)

    return el


if __name__ == "__main__":
    base_el = set()

    fill_base(base_el)

    el = knn(base_el, Element(3, 4), 5, ['A', 'B'])

    print("New element:", el)

    for elem in base_el:
        print(elem)
