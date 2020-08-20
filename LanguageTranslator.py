from ibm_watson import LanguageTranslatorV3
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from pandas import json_normalize

url_lt = 'enter-the-url-of-your-IBM-Watson-LanguageTranslator-api'
apikey_lt = 'enter-the-key-of-your-IBM-Watson-LanguageTranslator-api'
version_lt = 'enter-the-version-of-your-IBM-Watson-LanguageTranslator-api'

authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt, authenticator=authenticator)
language_translator.set_service_url(url_lt)
# print(language_translator)

# print(json_normalize(language_translator.list_identifiable_languages().get_result(), "languages"))
# Select the required languages by their codes. In this case, text is translated from English to Spanish.

textToBeTranslated = input('\nEnter text (in this case, in ENGLISH) for translation: ')
translation_response = language_translator.translate(\
    text=textToBeTranslated, model_id='en-es')
# print(translation_response)

translation = translation_response.get_result()
# print(translation)

spanish_translation = translation['translations'][0]['translation']
print('English: ' + textToBeTranslated + '\nSpanish: ' + spanish_translation + '\n')
