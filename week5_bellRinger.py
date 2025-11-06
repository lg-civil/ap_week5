# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
magic = "abracadabra"
# a. Retrieve the 5th character.
fifth_char = print(magic[4])
# b. Retrieve the second to last character.
second_to_last_char = print(magic[-2])
# c. Find the first occurrence of the letter 'c'.
first_c_index = print(magic.index("r"))
# find the last occurence of the letter 'a'

last_a_index = print(magic.rindex('a'))

# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# a. Extract the letters 'hij'.
# hij = print(alphabet.index[7:10])
hij = print(alphabet.index('hij'))
hij2 = print(alphabet[7:10])
# b. Extract every second letter starting from 'a' to 'm'.
# get the letter m 

m_index = print(alphabet.index('m'))
every_second = print(alphabet[0:13:2])
# c. Reverse the entire string using slicing.
reverse_alphabet = print(alphabet[ : : -1])
# example of practice

i_have_a_dream = "And when this happens, and when we allow freedom ring, when we let it ring from every village and every hamlet, from every state and every city, we will be able to speed up that day when all of God's children, black men and white men, Jews and Gentiles, Protestants and Catholics, will be able to join hands and sing in the words of the old Negro spiritual: Free at last! Free at last! Thank God Almighty, we are free at last!"

reverse_i_have_a_dream = print(i_have_a_dream[ : : -1])
# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"

famous_quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
john_f_kennedy = print(famous_quote.find('John F. Kennedy'))
extracted_name = print(famous_quote[83:])
# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
info = "Python is fun. Fun is good. Good is subjective."
len_opi_python = print(len(info))
# a. Extract the word 'subjective' without knowing its exact position.
subjective = print(info.index("subjective"))
subjective_2 = print(info[36:-1])
# b. Extract every third word.
third_word = print(info[0:47:3])
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
words = info.split() 
print(words)
reversed_words = ' '.join(reversed(words))
print(reversed_words)
# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
star_wars = "MAY THE FORCE BE WITH YOU."
low_star_wars = print(star_wars.lower())
up_star_wars = print(star_wars.upper())
# String Joining and Splitting:
# a. Convert the list into a single string.
motto = ["Make", "haste", "slowly."]
united_motto = ' '.join(motto)
print(united_motto)

# b. Now, split the string at every occurrence of the letter 'a'.
a_motto =  united_motto.split('a')
print(a_motto)
# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.

# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
# b. Count the number of times the letter 'i' appears in the same word/phrase.