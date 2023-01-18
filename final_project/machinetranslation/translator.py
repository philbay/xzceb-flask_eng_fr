import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

""" create an instance of the IBM Watson Language translator"""
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='{version}',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    frenchText = "Hello, world"
    translation = language_translator.translate( text=frenchText, model_id='en-fr').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    return frenchText