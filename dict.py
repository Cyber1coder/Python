d = {"name": "Alice", "age": 21, "city": "Pune"}
print(d)
print(d["name"])

d["age"] = 22
d["country"] = "India"

d.pop("city")
print(d)

d.update({"name": "Bob", "city": "Mumbai"})
print(d)

d.clear()
print(d)
