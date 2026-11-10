# Assuming the existing program has a dictionary or a function like this:
ICAO_ALPHABET = {
    'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
    'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett',
    'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
    'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee',
    'Z': 'Zulu'
}

def get_icao_word(letter):
    """Returns the ICAO word for a given letter."""
    return ICAO_ALPHABET.get(letter.upper(), '')

# --- Complete the program below this line ---

# 1. Get the name from the keyboard
name = input("Enter a name: ")

# 2. Process each character in the name
print(f"\nPhonetic spelling for '{name}':")
for char in name:
    # Check if the character is a letter
    if char.isalpha():
        # Get the ICAO word and print it
        word = get_icao_word(char)
        print(f"{char.upper()}: {word}")
    elif char.isspace():
        # Optional: handle spaces between names
        print("[Space]")
