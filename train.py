import numpy as np
import tensorflow as tf


def main():
    wordsList = np.load('wordsList.npy')
    print('Loaded the word list!')
    wordsList = wordsList.tolist()  # Originally loaded as numpy array
    wordsList = [word.decode('UTF-8') for word in wordsList]  # Encode words as UTF-8
    wordVectors = np.load('wordVectors.npy')
    print('Loaded the word vectors!')

    baseballIndex = wordsList.index('india')
    print(wordVectors[baseballIndex])


if __name__ == '__main__':
    main()
