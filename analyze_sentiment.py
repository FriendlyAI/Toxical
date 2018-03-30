import re

import watson_developer_cloud
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
    username='5b8c3495-992b-419d-9293-e5cb7f5bd274',
    password='fD48cBk4EBiG',
    version='2017-09-26')

analyzer = SentimentIntensityAnalyzer()


def analyze(sentence):
    if sentence:
        sentence = clean(sentence)
        vs = analyzer.polarity_scores(sentence)

        watson_score = watson_analyze(sentence)

        return (f'{sentence}\nNegative: {vs["neg"]}\nPositive: {vs["pos"]}\nNeutral: {vs["neu"]}'
                f'\nCompound: {vs["compound"]}\nWith Watson: {(vs["compound"] + watson_score) / 2}',
                {'negative': vs['neg'], 'positive': vs['pos'], 'neutral': vs['neu'], 'compound': vs['compound'],
                 'watson': (vs["compound"] + watson_score) / 2})


def watson_analyze(sentence):
    bad_count = 0
    accumulate = 0
    try:
        tone_dict = tone_analyzer.tone(tone_input=sentence, content_type='text/plain')
    except watson_developer_cloud.watson_service.WatsonApiException:
        print('Error: no message given', repr(sentence))
    else:
        for emotion in tone_dict.get('document_tone').get('tones'):
            if emotion.get('tone_name') in {'Frustrated', 'Impolite', 'Anger', 'Sadness'}:
                bad_count += 1
                accumulate += emotion.get('score')
        try:
            return -accumulate / bad_count
        except ZeroDivisionError:
            return 0


def clean(sentence):
    special_chars = re.compile(r'[^a-zA-Z]+')
    cleaned = re.sub(special_chars, ' ', sentence)
    return ' '.join([cleaned_word.lower() for cleaned_word in cleaned.split()])
