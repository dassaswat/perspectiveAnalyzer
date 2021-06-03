from googleapiclient import discovery
import json


class Perspective:
    """
      Intialize the class with your API_KEY, Required Languages and Required Attributes and their respective thresholds in **kwargs
      You can also setup the Developer Name.

      ** Accepted attributes **
        attributes = ["TOXICITY", "SEVERE_TOXICITY", "IDENTITY_ATTACK", "INSULT",
                      "PROFANITY", "THREAT", "SEXUALLY_EXPLICIT", "FLIRTATION", "SPAM",
                      "ATTACK_ON_AUTHOR", "ATTACK_ON_COMMENTER", "INCOHERENT",
                      "INFLAMMATORY", "OBSCENE", "SPAM", "UNSUBSTANTIAL"]


      ** Accepted Languages **
      lang = ["en", "fr", "es", "de", "it", "pt", "ru"]

      For more details on the API refer to the Perspective API Documentaion
      https://developers.perspectiveapi.com/s/about-the-api-attributes-and-languages

      ** Available Methods **

      analyzeText() Method returns an object containing attributes that are booleans (either True or False) .If the returned summary score falls beyond the thresshold specified it return True else False. 
      getTextReport() Method returns an object containing probability scores for all the attributes that was passed during the initialization.
    """

    def __init__(self,
                 API_KEY: str,
                 developer_name: str = "perspectiveDeveloper",
                 lang: list = ['en'],
                 **kwargs):

        self.API_KEY = API_KEY
        self.lang = lang
        self.attributeThresholds = {}
        for key, value in kwargs.items():
            self.attributeThresholds[key] = value
        self.baseUrl = "https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1"
        self.requestedAttributes = {}
        self.analyzer = discovery.build(
            "commentanalyzer",
            "v1alpha1",
            developerKey=self.API_KEY,
            discoveryServiceUrl=self.baseUrl,
            static_discovery=False,
        )

    def getTextReport(self, text: str) -> dict:
        for key in self.attributeThresholds:
            self.requestedAttributes[key] = {}

        analyze_request = {
            'comment': {
                'text': text
            },
            'languages': self.lang,
            'requestedAttributes': self.requestedAttributes
        }

        res = self.analyzer.comments().analyze(body=analyze_request).execute()

        formatted_res = json.dumps(res, indent=2)
        return formatted_res

    def analyzeText(self, text: str) -> dict:

        for key in self.attributeThresholds:
            self.requestedAttributes[key] = {}

        analyze_request = {
            'comment': {
                'text': text
            },
            'languages': self.lang,
            'requestedAttributes': self.requestedAttributes
        }

        res = self.analyzer.comments().analyze(body=analyze_request).execute()

        data = {}
        for key in res['attributeScores']:
            data[key] = res['attributeScores'][key]['summaryScore'][
                'value'] > self.attributeThresholds[key]

        return data
