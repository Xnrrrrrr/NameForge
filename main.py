import random
import nltk
from nltk.corpus import words

def download_nltk_data():
    if not nltk.data.find('corpora/words.zip'):
        nltk.download('words')

def generate_usernames(num_usernames, num_letters):
    english_words = set(word.lower() for word in words.words())
    common_words = [word.lower() for word, freq in nltk.FreqDist(words.words()).most_common(5000)]  # Adjust the number as needed
    common_words_set = set(common_words)
    usernames = set()

    while len(usernames) < num_usernames:
        # Generate a username with the specified number of letters
        username = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(num_letters))

        # Add the username to the set if it's a common English word and not a duplicate
        if username in common_words_set and username not in usernames:
            usernames.add(username)

    return list(usernames)

if __name__ == "__main__":
    download_nltk_data()

    num_usernames = int(input("Enter the number of usernames to generate: "))
    num_letters = int(input("Enter the number of letters in each username: "))

    generated_usernames = generate_usernames(num_usernames, num_letters)

    print("\nGenerated Usernames:")
    for username in generated_usernames:
        print(username)
