def token_dispenser(start: int = 1):
    """
    Infinite generator that simulates a token dispenser.
 
    - Yields incrementing token numbers starting from `start`.
    - Accepts input via `send()` to optionally reset the counter to a new value.
    - Gracefully stops if `close()` is called.
    """
    current = start
    try:
        while True:
            new_start = yield current
            if new_start is not None:
                current = new_start
            else:
                current += 1
    except GeneratorExit:
        print("Dispenser closed.")

dispenser = token_dispenser()
print(next(dispenser))
print(next(dispenser))
print(dispenser.send(10))
print(next(dispenser))
print(next(dispenser))