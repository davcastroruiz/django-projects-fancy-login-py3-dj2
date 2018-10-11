import json
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
    version = '2016-05-19',
    username = 'd28010de-72f9-4a46-b074-b401c051e339',
    password = 'P6NvqK1kqxU6',
    url = 'https://gateway.watsonplatform.net/tone-analyzer/api'
)

text = 'Team, I know that times are tough! Product '\
    'sales have been disappointing for the past three '\
    'quarters. We have a competitive product, but we '\
    'need to do a better job of selling it!'

tone_analysis = tone_analyzer.tone(
    {'text': text},
    'application/json').get_result()
print(json.dumps(tone_analysis, indent=2))
