#Напишите функцию capitilize_text, которвя принимает ряд текста и повертаэ этот текст но с первой большой и
#другими маленькими букваит для каждого слова

import pytest

def capitilize_text(text):
    return text.title()
#or
def test_positive():
    result = capitilize_text('good Bad UGLY')
    assert 'Good Bad Ugly' == result

#or
@pytest.mark.parametrize('text, expected_result', [
    ('good Bad UGLY', 'Good Bad Ugly')
])
def test_positive(text, expected_result):
    assert capitilize_text(text_test) == expected_result
#next

database = [
    {"id": 1, "name":"John", "second_name":"Doe", "age": 30},
    {"id": 2, "name":"John", "second_name":"Joi", "age": 25}
]
def check_user(database, user_dict):
    final_result = []
    for dict in database:
        negative_result = 0
        for value in user_dict.values():
            if value in dict.values():
                negative_result = negative_result + 1
        final_result.append(negative_result)
    if 0 in final_result:
        return "full"
    elif 1 in final_result:
        return "read-only"
    else:
        return "restricted"

#print(check_user(database,  {"id": 1, "name":"John", "second_name":"Joi", "age": 25}))

#testing this function
import pytest
@pytest.mark.parametrize("dict, expected_result", [
    ({"id": 1, "name":"John", "second_name":"Doe", "age": 30}, "full"),
    ({"id": 1, "name":"John", "second_name":"Joi", "age": 30}, "read-only"),
    ({"id": 1, "name":"John", "second_name":"Joi", "age": 25}, "restricted")
                         ])
def test_func(dict, expected_result):
    assert check_user(database, dict) == expected_result

#lection 13 