#!python3

def std_build_unicode_from_str(symbols):
    """ General function that lists unicode codepoints from string using standard logic. """
    codes = list()
    for symbol in symbols:
        codes.append(ord(symbol))
    print(codes)

def list_comp_build_unicode_from_str(symbols):
    """ General function that lists unicode codepoints from string using list comprehensions. """
    print([ord(symbol) for symbol in symbols])

def genr_build_unicode_from_str(symbols):
    """ General function that lists unicode codepoints from string using generators. """
    print(tuple(ord(symbol) for symbol in symbols))
    
    import array
    print(array.array("I", (ord(symbol) for symbol in symbols)))

def list_comp_build_higher_unicodes_from_str(symbols):
    """ General function that lists unicode codepoints above parameter from string using list comprehensions. """
    print([ord(s) for s in symbols if ord(s) > 127])

def map_build_higher_unicodes_from_str(symbols):
    """ General function that lists unicode codepoints above parameter from string using map/filter functions. """
    print(list(filter(lambda c: c > 127, map(ord, symbols))))

def list_comp_cartesian_product():
    """ General function that produces Cartesian product between two vectors. """
    colors, sizes = ["black", "white"], ["S", "M", "L"]
    
    # First Method: A * B with list comprehension
    tshirts = [(color, size) for color in colors 
                             for size in sizes]
    print(tshirts)

    # Second Method: B * A with list comprehension
    tshirts = [(color, size) for size in sizes 
                             for color in colors]
    print(tshirts)

    # Third Method: Nested For loops across vectors
    tshirts = list()
    for color in colors:
        for size in sizes:
            tshirts.append((color, size))
    print(tshirts)

def genr_cartesian_product():
    """  """
    colors, sizes = ["black", "white"], ["S", "M", "L"]
    for tshirt in ("{} {}".format(c, s) for c in colors for s in sizes):
        print(tshirt)

def tuple_unpacking_with_stars():
    """  """
    t = (20, 8)
    print(divmod(*t))

def grab_excess_items_with_stars():
    """  """
    a, *body, c, d = range(5)
    print(a, body, c, d)

    *head, b, c, d = range(5)
    print(head, b, c, d)

def use_named_tuple_for_city_data():
    """  """
    from collections import namedtuple
    City = namedtuple("City", "name country population coordinates")
    tokyo = City("Tokyo", "JP", 36.933, (35.689722, 139.691667))
    print(tokyo)
    print(tokyo.population)
    print(tokyo.coordinates)
    print(tokyo[1])
    print("\n")
    print(City._fields)
    LatLong = namedtuple("LatLong", "lat long")
    delhi_data = ("Delhi NCR", "IN", 21.935, LatLong(28.613889, 77.208889))
    delhi = City._make(delhi_data)
    print(delhi._asdict())
    for key, value in delhi._asdict().items():
        print("{}: {}".format(key, value))

def create_save_load_large_array_of_floats():
    """  """
    from array import array
    from random import random

    floats = array("d", (random() for i in range(10**7)))
    print(floats[-1])
    fp = open("floats.bin", "wb")
    floats.tofile(fp)
    fp.close()
    floats2 = array("d")
    fp = open("floats.bin", "rb")
    floats2.fromfile(fp, 10**7)
    fp.close()
    print(floats2[-1])
    print(floats2 == floats)

def deque_playground():
    """  """
    from collections import deque

    dq = deque(range(10), maxlen=10)
    print(dq)

    dq.rotate(3)
    print(dq)

    dq.rotate(-4)
    print(dq)

    dq.appendleft(-1)
    print(dq)

    dq.extend([11, 22, 33])
    print(dq)

    dq.extendleft([10, 20, 30, 40])
    print(dq)

def main():
    """ General main run function. """
    symbols = "$¢£¥€¤"

    # Test standard logic vs. list comprehensions
    """
    std_build_unicode_from_str(symbols)
    list_comp_build_unicode_from_str(symbols)
    """

    # Test list comprehensions vs. map/filter
    """
    list_comp_build_higher_unicodes_from_str(symbols)
    map_build_higher_unicodes_from_str(symbols)
    """

    # Test Cartesian product with list comprehensions
    """
    list_comp_cartesian_product()
    """

    # Test generators expressions
    """
    genr_build_unicode_from_str(symbols)
    genr_cartesian_product()
    """

    # Test tuple unpacking with star assignment
    """
    tuple_unpacking_with_stars()
    """

    # Test star assignment for grabbing excess items
    """
    grab_excess_items_with_stars()
    """

    # Test defining and using named tuples
    """
    use_named_tuple_for_city_data()
    """

    # Test large array manipulation
    """
    create_save_load_large_array_of_floats()
    """

    # Test deque manipulations
    deque_playground()
    
if __name__ == "__main__":
    main()