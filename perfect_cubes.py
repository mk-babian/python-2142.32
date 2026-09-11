n = int(input("Enter n: "))

count = 0
i = 1
while i ** 3 <= n:
    print(i ** 3, end=" ")
    count += 1
    i += 1

print(f"\nTotal perfect cubes: {count}")
