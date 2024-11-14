# TODO решите задачу
import json

def task() -> float:
    with open("input.json") as f:
        data = json.load(f)
    return f"{sum([item["score"] * item["weight"] for item in data]):.3f}"

print(task())
