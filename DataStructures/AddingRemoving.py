letters = ["a", "b", "c", "d", "d"]

# Add
letters.insert(0, "-")

# Remove
letters.pop(0)
# letters.remove("b")
del letters[0:3]
letters.clear()
print(letters)
