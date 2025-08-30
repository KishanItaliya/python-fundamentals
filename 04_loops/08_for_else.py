staff = [("Amit", 16), ("Bob", 17), ("Charlie", 18), ("David", 19), ("Eve", 20)]

for name, age in staff:
    if age >= 18:
        print(f"{name} is an adult")
        break
else:
    print("No adult found")