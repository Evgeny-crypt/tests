import unittest
import requests

URL_TRNSL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'


class TestRequests(unittest.TestCase):

    def setUp(self):
        self.correct_params = {'key': API_KEY}
        self.uncorrect_params = {'key': API_KEY + '1'}

    def test_good_key(self):
        self.correct_params['lang'] = 'en'
        self.correct_params['text'] = 'Привет'
        response = requests.get(URL_TRNSL, params=self.correct_params)
        self.assertEqual(response.json()['code'], 200)
        self.assertEqual(response.json()['text'], ['Hi'])
        print(response.json())

    def test_uncorrect_lang(self):
        self.correct_params['lang'] = 'de-en'
        self.correct_params['text'] = 'Привет'
        response = requests.get(URL_TRNSL, params=self.correct_params)
        self.assertEqual(response.json()['code'], 200)
        self.assertNotEqual(response.json()['text'], ['Hi'])

    def test_bad_key(self):
        response = requests.get(URL_TRNSL, params=self.uncorrect_params)
        self.assertEqual(response.json()['code'], 401)
        self.assertEqual(response.json()['message'], 'API key is invalid')

    def test_invalid_params_text(self):
        self.correct_params['lang'] = 'en'
        response = requests.get(URL_TRNSL, params=self.correct_params)
        self.assertEqual(response.json()['code'], 502)
        self.assertEqual(response.json()['message'], 'Invalid parameter: text')

    def test_invalid_params_lang(self):
        self.correct_params['text'] = 'Привет'
        response = requests.get(URL_TRNSL, params=self.correct_params)
        self.assertEqual(response.json()['code'], 502)
        self.assertEqual(response.json()['message'], 'Invalid parameter: lang')


if __name__ == '__main__':
    TestRequests()
