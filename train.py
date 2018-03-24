import numpy as np
import tensorflow as tf
import re


def main():
    # wordsList = np.load('wordsList.npy')
    # print('Loaded the word list!')
    # wordsList = wordsList.tolist()  # Originally loaded as numpy array
    # wordsList = [word.decode('UTF-8') for word in wordsList]  # Encode words as UTF-8
    # wordVectors = np.load('wordVectors.npy')
    # print('Loaded the word vectors!')
    #
    # baseballIndex = wordsList.index('india')
    # print(wordVectors[baseballIndex])
    while True:
        print(clean(input()))


def clean(sentence):
    special_chars = re.compile(r'[^a-zA-Z0-9]+')
    cleaned = re.sub(special_chars, ' ', sentence)
    return [cleaned_word.lower() for cleaned_word in cleaned.split()]


if __name__ == '__main__':
    main()
