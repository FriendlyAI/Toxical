from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re

analyzer = SentimentIntensityAnalyzer()

# while True:
#     sentence = input()
#     vs = analyzer.polarity_scores(sentence)
#     print("{:-<65} {}".format(sentence, str(vs)))


def analyze(sentence):
    sentence = clean(sentence)
    vs = analyzer.polarity_scores(sentence)
    return sentence + '\n' + vs


def clean(sentence):
    special_chars = re.compile(r'[^a-zA-Z]+')
    cleaned = re.sub(special_chars, ' ', sentence)
    return ' '.join([cleaned_word.lower() for cleaned_word in cleaned.split()])
