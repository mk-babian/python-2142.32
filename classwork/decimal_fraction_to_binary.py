x = 0.375
p = 0

# We repeatedly multiply x by increasing powers of 2
# until the result becomes a whole integer with no
# decimal remainder
while(x * 2 ** p) % 1 != 0:
    p += 1

print("p is = ", p)

# We then convert the 'scaled' integer to binary
num = int(x * 2 ** p)
print("num is = ", num)
result = ""

# We then convert the "num" to binary
while num != 0:
    result = str(num % 2) + result
    num = num // 2

print("result is = ", result)

for i in range(p - len(result)):
    result = "0" + result

print("result is = ", result)
result = "0" + result
print("result is = ", result)
