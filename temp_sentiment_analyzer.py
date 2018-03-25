from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re

analyzer = SentimentIntensityAnalyzer()


def analyze(sentence):
    sentence = clean(sentence)
    vs = analyzer.polarity_scores(sentence)
    return f'{sentence}' \
           f'\nNegative: {vs["neg"]}' \
           f'\nPositive: {vs["pos"]}' \
           f'\nNeutral: {vs["neu"]}' \
           f'\nCompound: {vs["compound"]}'


def clean(sentence):
    special_chars = re.compile(r'[^a-zA-Z]+')
    cleaned = re.sub(special_chars, ' ', sentence)
    return ' '.join([cleaned_word.lower() for cleaned_word in cleaned.split()])
