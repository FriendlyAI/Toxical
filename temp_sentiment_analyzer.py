from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re

analyzer = SentimentIntensityAnalyzer()


def analyze(sentence):
    sentence = clean(sentence)
    vs = analyzer.polarity_scores(sentence)

    return (f'{sentence}\nNegative: {vs["neg"]}\nPositive: {vs["pos"]}\nNeutral: {vs["neu"]}'
            f'\nCompound: {vs["compound"]}',
            {'negative': vs['neg'], 'positive': vs['pos'], 'neutral': vs['neu'], 'compound': vs['compound']})


def clean(sentence):
    special_chars = re.compile(r'[^a-zA-Z]+')
    cleaned = re.sub(special_chars, ' ', sentence)
    return ' '.join([cleaned_word.lower() for cleaned_word in cleaned.split()])
