import requests
import json

DICT_API = 'https://api.dictionaryapi.dev/api/v2/entries/en_US'


class DictionarySearch:
    __slots__ = "word"

    def __init__(self, word):
        self.word = word

    def dictionary_search_api(self):
        search_val = f"{DICT_API}/{self.word}"
        response = requests.request(
            method="GET",
            url=search_val,
        )
        meanings = json.loads(response.content)[0].get('meanings')[0]
        result = f"{self.word}. {meanings.get('partOfSpeech')}. {meanings.get('definitions')[0].get('definition')}"
        return result


if __name__ == '__main__':
    ds_instance = DictionarySearch(input("Word?  ")).dictionary_search_api()
    print(ds_instance)
