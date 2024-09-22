from hashlib import sha256

LEVELS: list[int] = list(range(3))

def save_progress(level: int):
    hash: str = level_to_hash(level)
    with open("progress.txt", "w") as f:
        f.write(hash)

def read_progress(hash: str) -> int:
    for level in LEVELS:
        if level_to_hash(level) == hash:
            return level

    raise ValueError("Progress is corrupted and can't be read")

def reset_progress():
    save_progress(0)

def level_to_hash(level: int) -> str:
    return str(sha256(str(level).encode("utf-8")).hexdigest())
