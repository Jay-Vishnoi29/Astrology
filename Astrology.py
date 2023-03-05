# Chaldean Name Numerology Program

# Assigning numerical values to the letters of the alphabet
letters = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 8, 'G': 3, 'H': 5, 'I': 1, 'J': 1, 'K': 2, 'L': 3, 'M': 4,
           'N': 5, 'O': 7, 'P': 8, 'Q': 1, 'R': 2, 'S': 3, 'T': 4, 'U': 6, 'V': 6, 'W': 6, 'X': 5, 'Y': 1, 'Z': 7}

# Function to calculate the Chaldean name numerology of a given name
def chaldean_name_numerology(name):
    name = name.upper()
    print("\nYou Given Name is : " , name , "\n")
    total = 0
    for letter in name:
        if letter in letters:
            total += letters[letter]
    return total

# Example usage
name = input("Enter your name: ")
print("Your name numerology is:", chaldean_name_numerology(name),"\n\n")