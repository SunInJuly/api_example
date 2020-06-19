import requests
import json


API_LESSONS_URL  = "https://stepik.org/api/lessons/"


def check_lesson_name(lesson_id, expected_name):
    response = requests.get(API_LESSONS_URL + str(lesson_id))
    assert response.status_code == 200, "Status code is wrong, expected 200, got {}".format(response.status_code)
    source = json.loads(response.text)
    print(source)
    actual_name = source['lessons'][0]['title']
    assert actual_name == expected_name,  "Wrong name, expected {}, got {}".format(expected_name, actual_name)

