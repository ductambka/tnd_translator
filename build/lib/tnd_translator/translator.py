import requests
from requests.structures import CaseInsensitiveDict

# curl -X POST --user "apikey:0IMScDSQRLy8_UDwPgU8BF9jK-z1_5eU0OAMXfVCOxqv" --header "Content-Type: application/json" --data '{"text": ["Hello, world.", "How are you?"], "model_id":"en-fr"}' "https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/353bf5d2-88c5-4b4d-a28a-8ca309ebb2fa/v3/translate?version=2018-05-01"
# New key: XZFJyPi9OLR4X4Ffe4X7Ob9E3augimo7to6ZjuKtNyMf
import requests
from requests.structures import CaseInsensitiveDict

url = "https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/353bf5d2-88c5-4b4d-a28a-8ca309ebb2fa/v3/translate?version=2018-05-01"

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Set some variables
# api_key = '<your-apikey>'
api_key = "XZFJyPi9OLR4X4Ffe4X7Ob9E3augimo7to6ZjuKtNyMf"

# api_url = '<your-url>'
# api_url = "https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/353bf5d2-88c5-4b4d-a28a-8ca309ebb2fa/v3/translate?version=2018-05-01"
api_url = "https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/353bf5d2-88c5-4b4d-a28a-8ca309ebb2fa/"


#
# headers = CaseInsensitiveDict()
# headers["Content-Type"] = "application/json"
# headers["Authorization"] = "Basic YXBpa2V5OjBJTVNjRFNRUkx5OF9VRHdQZ1U4QkY5akstejFfNWVVME9BTVhmVkNPeHF2"
#
# data = '{"text": ["Hello, world.", "How are you?"], "model_id":"en-fr"}'
#
#
# resp = requests.post(url, headers=headers, data=data)
#
# print(resp.status_code)
#


def translate(text_to_translate, from_lang_code2=None, to_lang_code2=None):
    model_id = str(f'{from_lang_code2}-{to_lang_code2}')
    # text_to_translate = 'Your content you want translate here'

    # Prepare the Authenticator
    authenticator = IAMAuthenticator(api_key)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )

    language_translator.set_service_url(api_url)

    # Translate
    translation = language_translator.translate(
        text=text_to_translate,
        model_id=model_id).get_result()

    # Print results
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    if "translations" in translation:
        return translation["translations"]
    else:
        return []

def englishToFrench(text):
    return translate(text, from_lang_code2="en", to_lang_code2="fr")


def frenchToEnglish(text):
    return translate(text, from_lang_code2="fr", to_lang_code2="en")


#
# a = englishToFrench(["Hello Guy"])
# print(a)

