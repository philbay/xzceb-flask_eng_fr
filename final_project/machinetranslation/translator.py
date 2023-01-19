""" This module uses ibm_watson API to translate fr-en and en-fr """
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_watson import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

""" create an instance of the IBM Watson Language translator"""
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """ This method translates from english to french """
    french_text=[]
    if len(english_text) == 0:
        return ""
    try:
    # Invoke a method
        translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
        french_text = json.dumps(translation, indent=2, ensure_ascii=False)
    except ApiException as ex:
        print("Method failed with status code " + str(ex.code) + ": " + ex.message)
    french_text = json.loads(french_text)
    french_text = french_text["translations"][0]['translation']
    return french_text

def french_to_english(french_text):
    """ This method translates from french to english """
    english_text=[]
    if len(french_text) == 0:
        return ""
    try:
    # Invoke a method
        translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
        english_text = json.dumps(translation, indent=2, ensure_ascii=False)
    except ApiException as ex:
        print("Method failed with status code " + str(ex.code) + ": " + ex.message)
    english_text = json.loads(english_text)
    english_text = english_text["translations"][0]['translation']
    return english_text
