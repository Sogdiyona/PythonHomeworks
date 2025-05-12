wo=input("Enter the word: ")
vowel="aeiouy"
consonant="bcdfghjklmnpqrstvwxyz"
vowel_s=sum(1 for char in wo if char in vowel)
consonant_s=sum(1 for char in wo if char in consonant)
print(f"Vowels: {vowel_s}, \nConsonants: {consonant_s}")