import time
from bluesky.plan_stubs import checkpoint

"""A simple plan that greets you, counts the characters in your name and can be paused between checkpoints."""
def hello_friend(yourname: str, sleep_time_seconds: int = 1.0):
    print("Starting hello_friend plan...")
    print("This is an example of how to create a simple plan that yields checkpoints.")
    yield from checkpoint()
    print(f"Hello, {yourname}! You can pause and resume me between checkpoints.")
    yield from checkpoint()
    char_list = list(yourname)
    print(f"Your name has {len(char_list)} characters. Now, I will print them one by one:")
    yield from checkpoint()
    for char in char_list:
        print(f"{char}")
        time.sleep(sleep_time_seconds)
        yield from checkpoint()
    print("Plan complete!")
    yield from checkpoint()