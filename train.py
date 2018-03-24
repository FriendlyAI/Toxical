import numpy as np
import tensorflow as tf
import re


WORDS_LIST = np.load('wordsList.npy').tolist()
WORDS_LIST = [word.decode('UTF-8') for word in WORDS_LIST]  # Encode words as UTF-8
WORD_VECTORS = np.load('wordVectors.npy')

def main():
    # wordsList = np.load('wordsList.npy')
    # print('Loaded the word list!')
    # wordsList = wordsList.tolist()  # Originally loaded as numpy array
    # wordsList = [word.decode('UTF-8') for word in wordsList]  # Encode words as UTF-8
    # wordVectors = np.load('wordVectors.npy')
    # print('Loaded the word vectors!')

    # baseballIndex = wordsList.index('india')
    # print(wordVectors[baseballIndex])
    while True:
        vectorize(clean(input()))


def vectorize(sentence_array):
    for word in sentence_array:
        index = WORDS_LIST.index(word)
        vector = WORD_VECTORS[index]
        print(vector)


def clean(sentence):
    special_chars = re.compile(r'[^a-zA-Z0-9]+')
    cleaned = re.sub(special_chars, ' ', sentence)
    return [cleaned_word.lower() for cleaned_word in cleaned.split()]


if __name__ == '__main__':
    main()
