# 0x01. Caching

## General

This project implements various caching systems with different eviction policies. A caching system stores data temporarily to provide faster access to frequently used data. The project includes implementations of FIFO, LIFO, LRU, MRU, and LFU caching strategies.

### What a caching system is
A caching system is a mechanism for temporarily storing (caching) a subset of data, typically to improve performance and reduce latency by serving future requests more quickly.

### What FIFO means
FIFO (First In, First Out) is an eviction policy where the oldest items (first added) are removed first when the cache reaches its limit.

### What LIFO means
LIFO (Last In, First Out) is an eviction policy where the most recently added items are removed first when the cache reaches its limit.

### What LRU means
LRU (Least Recently Used) is an eviction policy where the least recently accessed items are removed first when the cache reaches its limit.

### What MRU means
MRU (Most Recently Used) is an eviction policy where the most recently accessed items are removed first when the cache reaches its limit.

### What LFU means
LFU (Least Frequently Used) is an eviction policy where the least frequently accessed items are removed first when the cache reaches its limit. If multiple items have the same frequency, the least recently used item among them is removed.

### What the purpose of a caching system
The purpose of a caching system is to speed up data retrieval by temporarily storing frequently accessed data in a way that future requests for that data can be served faster.

### What limits a caching system have
Caching systems are limited by their storage capacity (maximum number of items they can hold). When the cache exceeds this capacity, items are evicted based on the implemented eviction policy (FIFO, LIFO, LRU, MRU, LFU).

## Requirements

### Python Scripts
- All files are interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file at the root of the project is mandatory.
- Code should adhere to the `pycodestyle` style (version 2.5).
- All files must be executable.
- File lengths will be tested using `wc`.
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
- All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`).
- All functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`).
- Documentation should be a complete sentence explaining the purpose of the module, class, or method.

## Parent class BaseCaching

All classes must inherit from `BaseCaching` defined below:

```python
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
