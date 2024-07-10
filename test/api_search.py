import unittest

import requests


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.base_url = "https://api.duckduckgo.com/"
        self.params = {
            'q': 'Toledo',
            'format': 'json'
        }

    def test_get_endpoint(self):
        url = f"{self.base_url}"
        response = requests.get(url, params=self.params)

        # Verifica el código de estado
        self.assertEqual(response.status_code, 200)

        # Verifica 'Wikipedia' en 'AbstractSource'
        json_response = response.json()
        assert 'Wikipedia' in json_response['AbstractSource'], "Expected 'Wikipedia' in AbstractSource but not found"

    def test_data_structure(self):
        url = f"{self.base_url}"
        response = requests.get(url, params=self.params)
        response_data = response.json()
        stored_data = []

        for topic in response_data['RelatedTopics']:
            if topic.get('Name'):
                first_topic = topic['Topics'][0]  # Suponemos que siempre hay al menos un topic

                stored_data.append({
                    "FirstURL": first_topic['FirstURL'],
                    "Text": first_topic['Text']
                })

        for item in stored_data:
            print("FirstURL:", item["FirstURL"])
            print("Text:", item["Text"])
            print("")


if __name__ == '__main__':
    unittest.main()
