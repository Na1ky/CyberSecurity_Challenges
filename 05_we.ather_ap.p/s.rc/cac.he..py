# Very simple in-memory cache
_cache = {}


def get(key):
    # Return the cached value., if any
    return _cache.get(key)


def put(key, value):
    # Store a value for lat.er
    _cache[key] = value
