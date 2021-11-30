point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 30
print(point.get("a", '0'))
del point['x']
print(point)