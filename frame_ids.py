import numpy as np
import re
import csv

"""
Recurrent Neural Network
"""

WORDS_LIST = np.load('wordsList.npy').tolist()
WORDS_LIST = [word.decode('UTF-8') for word in WORDS_LIST]  # Encode words as UTF-8
WORD_VECTORS = np.load('wordVectors.npy')

NUM_LINES = 988
MAX_LENGTH = 40

ids = np.zeros((NUM_LINES, MAX_LENGTH), dtype='int32')


def main():
    # WORDS_LIST = np.load('WORDS_LIST.npy')
    # print('Loaded the word list!')
    # WORDS_LIST = WORDS_LIST.tolist()  # Originally loaded as numpy array
    # WORDS_LIST = [word.decode('UTF-8') for word in WORDS_LIST]  # Encode words as UTF-8
    # wordVectors = np.load('wordVectors.npy')
    # print('Loaded the word vectors!')

    # baseballIndex = WORDS_LIST.index('india')
    # print(wordVectors[baseballIndex])])

    # while True:
    #     vectorize(clean(input()))

    read_csv()
    # maxSeqLength = 10  # Maximum length of sentence
    # numDimensions = 300  # Dimensions for each word vector
    # firstSentence = np.zeros((maxSeqLength), dtype='int32')
    # firstSentence[0] = WORDS_LIST.index("i")
    # firstSentence[1] = WORDS_LIST.index("thought")
    # firstSentence[2] = WORDS_LIST.index("the")
    # firstSentence[3] = WORDS_LIST.index("movie")
    # firstSentence[4] = WORDS_LIST.index("was")
    # firstSentence[5] = WORDS_LIST.index("incredible")
    # firstSentence[6] = WORDS_LIST.index("and")
    # firstSentence[7] = WORDS_LIST.index("inspiring")
    # # firstSentence[8] and firstSentence[9] are going to be 0
    # print(firstSentence.shape)
    # print(firstSentence)  # Shows the row index for each word

    np.save('idsMatrix', ids)

    # with tf.Session() as sess:
    #     print(tf.nn.embedding_lookup(WORD_VECTORS, firstSentence).eval().shape)


def vectorize(sentence_array, ids_index):
    for word_index, word in enumerate(sentence_array):
        if word_index <= MAX_LENGTH:
            try:
                index = WORDS_LIST.index(word)
                vector = WORD_VECTORS[index]
                ids[ids_index][word_index] = vector
            except ValueError:
                ids[ids_index][word_index] = 399999  # Unrecognized word vector


def read_csv():
    index = 0
    with open('twitter_data.csv', newline='') as file:  # 989 lines
        reader = csv.reader(file)
        for line in reader:
            print(line[0], clean(line[1]))
            vectorize(clean(line[1]), index)
            index += 1


def clean(sentence):
    special_chars = re.compile(r'[^a-zA-Z0-9]+')
    cleaned = re.sub(special_chars, ' ', sentence)
    return [cleaned_word.lower() for cleaned_word in cleaned.split()]


if __name__ == '__main__':
    main()
