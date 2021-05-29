# PERSPECTIVEANALYZER 0.0.1

PERSPECTIVEANALYZER, is a python wrapper for the
[Google Perspective API] (https://www.perspectiveapi.com/).
PyPI: https://pypi.org/project/perspectiveAnalyzer/0.0.1/

## Installation

You can install released versions of perspectiveAnalyzer from the Python Package Index with pip or a similar tool:

**Stable Release:** `pip install perspectiveAnalyzer`<br>
**Working Version:** `pip install git+https://github.com/dassaswat/perspectiveAnalyzer.git`

```
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

  analyzeText() Method return an object containing attributes that are booleans (either True or False) .If the returned summary score falls beyond the threshold specified it return True else False.

```

## Example Usage

```python
# import the module
from perspectiveAnalyzer import Perspective

# initiate the object
api_key = "Your API Key"
textAnalyzer = Perspective(api_key, developer_name, lang, **kwargs) # Here we pass in the api_key, developerName (** Not Mandatory **), lang which is a list(defaults to just "en" ** Not Mandatory as well **) and finally we pass in the attributes with their threshold values.

res = textAnalyzer.analyzeText("Some text")
```

## Functions available

The function that is currently available with this module is:

```python
# endpoints
analyzeText("sometext")
```

## Important Links

- Register API key - [Click Here](https://docs.google.com/forms/d/e/1FAIpQLSdhBBnVVVbXSElby-jhNnEj-Zwpt5toQSCFsJerGfpXW66CuQ/viewform)
- Documentation/Endpoints - [Click Here](https://developers.perspectiveapi.com/s/)
