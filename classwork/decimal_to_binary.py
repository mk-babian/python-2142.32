def decimal_to_binary(n):
    # Check if input is 0
    if n == 0:
        return "0"

    # Create an empty array to store the digits of the binary
    binary_digits = []

    # A loop checking if n is over 0
    while n > 0:
        # % 2 extracts the last digit
        # (the least significant bit)
        # of that number's bianary
        # representation
        remainder = n % 2

        # Print statement for debug purposes
        # print(remainder)

        # Append the remainder (converted to string to the array)
        binary_digits.append(str(remainder))

        # Divide n by 2 so we can move on to the next digit
        n = n // 2

    return "".join(reversed(binary_digits))

print(decimal_to_binary(10))
