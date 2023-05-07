# Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# Initialize a variable to count vowels
vowel_count = 0

# Loop over each character in the sentence
for char in sentence:
    # Check if the character is a vowel
    if char.lower() in "aeiou":
        # If it is, increment the vowel count
        vowel_count += 1

# Print the total number of vowels found
print("The total number of vowels in the sentence is:", vowel_count)
