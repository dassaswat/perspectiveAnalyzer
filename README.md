# PERSPECTIVEANALYZER 0.0.1

PERSPECTIVEANALYZER, is a python wrapper for the
[Google Perspective API] (https://www.perspectiveapi.com/).
PyPI: https://pypi.org/project/perspectiveAnalyzer/0.0.1/

## Installation

You can install released versions of perspectiveAnalyzer from the Python Package Index with pip or a similar tool:

**Stable Release:** `pip install perspectiveAnalyzer`<br>
**Working Version:** `pip install git+https://github.com/dassaswat/perspectiveAnalyzer.git`

Intialize the class with your API_KEY, Required Languages and Required Attributes and their respective thresholds in \*\*kwargs
You can also setup the Developer Name.

** Accepted attributes **
attributes = ["TOXICITY", "SEVERE_TOXICITY", "IDENTITY_ATTACK", "INSULT",
"PROFANITY", "THREAT", "SEXUALLY_EXPLICIT", "FLIRTATION", "SPAM",
"ATTACK_ON_AUTHOR", "ATTACK_ON_COMMENTER", "INCOHERENT",
"INFLAMMATORY", "OBSCENE", "SPAM", "UNSUBSTANTIAL"]

** Accepted Languages **
lang = ["en", "fr", "es", "de", "it", "pt", "ru"]

For more details on the API refer to the Perspective API Documentation
https://developers.perspectiveapi.com/s/about-the-api-attributes-and-languages

** Available Methods **

analyzeText() Method return an object containing attributes that are booleans (either True or False) .If the returned summary score falls beyond the threshold specified it return True else False.

getTextReport() Method returns an object containing probability scores for all the attributes that was passed during the initialization.

## Example Usage

```python
# install the python Module

pip3 install perspectiveAnalyzer

```

```python
# import the module

from perspectiveAnalyzer import Perspective

# initiate the object

api_key = "Your API Key"
textAnalyzer = Perspective(api_key, "sassy", lang=["en","es"], INSULT = 0.75, TOXICITY = 0.75,SPAM= 0.75,)

"""
  Here we pass in the api_key, developerName ( ** Not Mandatory ** ), lang which is a list( defaults to just "en"
  ** Not Mandatory as well ** ) and finally we pass in the attributes with their threshold values.
"""

res = textAnalyzer.analyzeText("Some text") # Return a boolean object for the provided attribute
res = textAnalyzer.getTextReport("Some text") # Returns an object containing the probability scores for the provided attributes
```

## Functions available

The function that is currently available with this module is:

```python

# endpoints

analyzeText("Some text")
getTextReport("Some text")

```

## Sample Response

```python
# From analyzeText

{'TOXICITY': True, 'INSULT': True}

# From getTextReport

{
  "attributeScores": {
    "TOXICITY": {
      "spanScores": [
        {
          "begin": 0,
          "end": 11,
          "score": {
            "value": 0.04457423,
            "type": "PROBABILITY"
          }
        }
      ],
      "summaryScore": {
        "value": 0.04457423,
        "type": "PROBABILITY"
      }
    },
    "INSULT": {
      "spanScores": [
        {
          "begin": 0,
          "end": 11,
          "score": {
            "value": 0.01924272,
            "type": "PROBABILITY"
          }
        }
      ],
      "summaryScore": {
        "value": 0.01924272,
        "type": "PROBABILITY"
      }
    }
  },
  "languages": [
    "en"
  ],
  "detectedLanguages": [
    "en",
    "fil"
  ]
}

```

## Important Links

- Register API key - [Click Here](https://docs.google.com/forms/d/e/1FAIpQLSdhBBnVVVbXSElby-jhNnEj-Zwpt5toQSCFsJerGfpXW66CuQ/viewform)
- Documentation/Endpoints - [Click Here](https://developers.perspectiveapi.com/s/)
