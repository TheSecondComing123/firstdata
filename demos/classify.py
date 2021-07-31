from typing import Mapping, Sequence


def classify_plot_type(data: Mapping[str, Sequence[int]]) -> str:
    if len(data.values()) == 2 and data.get("type") != "percentage":
        return "scatter"
    elif data.get("type") == "percentage":
        return "pie"
    else:
        return "line"


if __name__ == "__main__":
    print(classify_plot_type({"x": [1, 7, 5], "y": [8, 4, 1]}))  # scatter
    print(classify_plot_type({"x": [1, 7, 5], "type": "percentage"}))  # pie
    print(classify_plot_type({"x": [1, 7, 5]}))  # line
