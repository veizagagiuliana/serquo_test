
import requests
from behave import *


url = 'https://api.duckduckgo.com/'
params = {
    'q': 'Toledo',
    'format': 'json'
}


@given('the duckduckgo API')
def step_impl(context):
    pass


@when('I get to the API')
def step_impl(context):
    context.response = requests.get(url, params=params)


@then('the response status is 200')
def step_impl(context):
    assert context.response.status_code == 200, f"Expected status code 200, but got {context.response.status_code}"


@then('the JSON response contain "Wikipedia" in the AbstractSource')
def step_impl(context):
    json_data = context.response.json()
    assert 'Wikipedia' in json_data['AbstractSource'], "Expected 'Wikipedia' in AbstractSource but not found"


@then('by console the "FirstURL" and the "Text" of the records stored with "Name"')
def step_impl(context):
    response_data = context.response.json()
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
