import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
from ibm_watson import ApiException

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
#language_translator.set_disable_ssl_verification(True) # disabling ssl verification

def englishToFrench(englishText):
    """ This method translates from english to french """
    frenchText=''
    try:
    # Invoke a method
        translation = language_translator.translate(
        text=englishText, 
        model_id='en-fr').get_result()
        frenchText = json.dumps(translation, indent=2, ensure_ascii=False)
    except ApiException as ex:
        print 
        "Method failed with status code " + str(ex.code) + ": " + ex.message
   
    return frenchText

def frenchToEnglish(frenchText):
    """ This method translates from french to english """
    englishText=''
    try:
    # Invoke a method
        translation = language_translator.translate(
        text=frenchText, 
        model_id='fr-en').get_result()
        englishText = json.dumps(translation, indent=2, ensure_ascii=False)
    except ApiException as ex:
        print 
        "Method failed with status code " + str(ex.code) + ": " + ex.message
    
    return englishText

print(englishToFrench("Good morning sir"))
print(frenchToEnglish("Fatigue, nervosité, fatigue musculaire sont souvent les premiers signes d'un apport alimentaire insuffisant en magnésium"))