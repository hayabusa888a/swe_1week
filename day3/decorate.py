import functools

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            last_exception = None
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    attempts += 1
                    print(f"Attempt {attempts} failed: {e}")
            raise last_exception
        return wrapper
    return decorator

@retry(max_attempts=3, delay=1)
def fetch_data(url):
    import random
    if random.random() < 0.7:
        raise ConnectionError("Failed to connect")
    return f"Data from {url}"


fetch_data("http://example.com")