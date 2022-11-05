import requests


def dev_to_modi(text):
    translated_data = requests.get(f'http://aksharamukha-plugin.appspot.com/api/public?source=Devanagari&target=Modi&text={text}')
    return translated_data.text