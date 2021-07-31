import random

scatter_data = {
    "x": [random.randint(100, 300) for _ in range(20)],
    "y": [random.randint(100, 300) for _ in range(20)]
}

pie_data = {
    "x": [random.randint(10, 70) for _ in range(4)],
    "type": "percentage"
}

line_data = {
    "x": [random.randint(100, 300) for _ in range(20)],
}
