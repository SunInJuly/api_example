from api import check_lesson_name

def test_check_lesson_name():
    #lesson_url = https://stepik.org/lesson/223529
    lesson_id = 223529
    check_lesson_name(lesson_id=lesson_id, expected_name="wrong_name")
