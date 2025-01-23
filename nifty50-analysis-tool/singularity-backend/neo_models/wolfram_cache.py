from django.core.cache import cache

def cache_wolfram_query(query, result):
    cache.set(query, result, timeout=3600)  # Cache for 1 hour

def get_cached_wolfram_query(query):
    return cache.get(query)
