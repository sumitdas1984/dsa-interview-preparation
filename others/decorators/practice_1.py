# Write a decorator to enforce argument types (simple runtime check).

def enforce_types(*types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for (arg, expected) in zip(args, types):
                if not isinstance(arg, expected):
                    raise TypeError(f"Argument {arg!r} is not of type {expected.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@enforce_types(str, int)  # name must be str, age must be int
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")


# ✅ Works
greet("Alice", 30)

# ❌ Fails
greet(30, "Alice")  # TypeError
