import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
from ibm_watson import ApiException


apikey='izqT1UEaG3Wft_my4QZ5o5b5dUaETwRJ6Aym34iMxM9S'
url='https://api.eu-de.language-translator.watson.cloud.ibm.com/instances/2f5bc655-b802-4f69-8eb5-5ebfb6058d8b'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

"""translation = language_translator.translate(
    text='I understand',
    model_id='en-es').get_result()
print(json.dumps(translation, indent=2, ensure_ascii=False))"""

def englishToFrench(englishText):
    print('start test')
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
    #write the code here
    englishText = ""
    return englishText

print(englishToFrench("Good morning sir"))