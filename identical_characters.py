def find_longest_sequence(s: str):
    if not s:
        return "", 0
    
    # Hold the best run found so far
    max_char = s[0]
    max_len = 1

    # Hold the run currently being counted
    current_char = s[0]
    current_len = 1

    # This loop goes over EVERY character until it
    # finds a character that doesn't match.
    #
    # After characters don't match, it makes the
    # non-matching character the new character to match
    for char in s[1:]:
        # If it matches current_char, add 1 to current_len
        if char == current_char:
            current_len += 1
        # If it doesn't, reset the count and get a new character
        else:
            current_char = char
            current_len = 1
        
        # Check if the current run is longer than the best
        if current_len > max_len:
            max_len = current_len
            max_char = current_char

    return max_char * max_len, max_char, max_len


# Example usage
s = "aaabbccccdaa"
sequence, char, length = find_longest_sequence(s)

print(f"Sequence: '{sequence}'")
print(f"Character: '{char}'")
print(f"Length: {length}")
