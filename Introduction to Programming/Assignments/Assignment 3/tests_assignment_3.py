import inspect
import sys,builtins,io
from contextlib import redirect_stdout

def input(prompt=''):
    r = sys.stdin.readline()
    if not r:
        r = builtins.input(prompt)
    return r

def load_cards():
    import csv
    import os
    cards = {}
    for path in os.listdir("out/"):
        with open(f"out/{path}", mode='r',encoding="utf8") as infile:
            file_data=csv.reader(infile)
            headers=next(file_data)[1:]
            cards[path[:-4]] = [dict(zip(headers,i[1:])) for i in file_data]
    for cat in cards:
        cards[cat] = [card for card in cards[cat] if card['Correct']]
    return cards

def msg_not_a_function(var):
    return f"Variable {var} is not a function."

def msg_wrong_number_args(fun_name):
    return f"Wrong number of arguments in {fun_name}."

def msg_wrong_ret_result(expected, got):
    return f"Wrong return result.\nExpected:\n{expected}\nbut got:\n{got}"

def msg_wrong_output(expected, got):
    return f"Wrong output.\nExpected:\n{expected}\nbut got:\n{got}"

def msg_wrong_state(expected, got):
    return f"Wrong state after function call.\nExpected:\n{expected}\nbut got:\n{got}"

def assert_same_return(expected, got, tested_with=[]):
    assert got == expected, f"{msg_wrong_ret_result(expected, got)}\nTested with {tested_with}."

def assert_same_output(expected, got, tested_with=[]):
    assert got == expected, f"{msg_wrong_output(expected, got)}\nTested with {tested_with}."

def assert_same_state(expected, got, tested_with=[]):
    assert got == expected, f"{msg_wrong_state(expected, got)}\nTested with {tested_with}."

def test_remove_empty_options(func):
    assert inspect.isfunction(func), msg_not_a_function("remove_empty_options")
    assert len(inspect.signature(func).parameters) == 1, "Wrong number of arguments in remove_empty_options."
    cards = [{'A': 'True', 'B': 'False', 'C': '','D': ''}, {'A': '', 'B': '', 'C': '','D': ''}, {'A': '1', 'E': '4', 'B': '2', 'C': '','D': '3'}]
    expected = [{'A': 'True', 'B': 'False'}, {}, {'A': '1', 'E': '4', 'B': '2','D': '3'}]
    for card, output in zip(cards, expected):
        func(card)
        assert_same_state(expected=output, got=card, tested_with=[('card', card)])
    print("All basic tests passed!")

def test_remove_newline(func):
    assert inspect.isfunction(func), msg_not_a_function("remove_newlines")
    assert len(inspect.signature(func).parameters) == 1,  msg_wrong_number_args("remove_newline")
    cards = [{'Questions': 'a\n'}, {'Questions': 'a'}, {'Questions': ''}]
    expected = [{'Questions': 'a'}, {'Questions': 'a'}, {'Questions': ''}]
    for card, output in zip(cards, expected):
        test_card = dict(card)
        func(card)
        assert_same_state(expected=output, got=card, tested_with=[('card', test_card)])
    print("All basic tests passed!")

def test_answer_option(func):
    assert inspect.isfunction(func), msg_not_a_function("answer_option")
    assert len(inspect.signature(func).parameters) == 1, msg_wrong_number_args("answer_option")
    cards = [{'Correct': 'ABC', 'A': 'ABC', 'B':'x'}, {'Correct': 'x', 'A': 'ABC', 'B':'x'}]
    expected = [{'Correct': 'A', 'A': 'ABC', 'B':'x'}, {'Correct': 'B', 'A': 'ABC', 'B':'x'}]
    for card, output in zip(cards, expected):
        test_card = dict(card)
        func(card)
        assert_same_state(expected=output, got=card, tested_with=[('card', test_card)])
    print("All basic tests passed!")

def test_rewrite_data(func):
    assert inspect.isfunction(func), msg_not_a_function("rewrite_data")
    assert len(inspect.signature(func).parameters) == 1, msg_wrong_number_args("rewrite_data")
    cards = {'category': [{'Correct': 'ABC', 'A': 'ABC', 'B':'', 'Questions': 'A\n'}]}
    expected = {'category': [{'Correct': 'A', 'A': 'ABC', 'Questions': 'A'}]}
    test_cards = dict(cards)
    func(cards)
    assert_same_state(expected=expected, got=cards, tested_with=[('cards', test_cards)])
    print("All basic tests passed!")

def test_pick_card(func):
    assert inspect.isfunction(func), msg_not_a_function("pick_card")
    assert len(inspect.signature(func).parameters) == 1, msg_wrong_number_args("pick_card")
    cards = {'category': [{'Correct': 'A', 'A': 'ABC', 'B':'', 'Questions': 'A'}]}
    expected_cards = {'category': []}
    expected_ret = ('category', {'Correct': 'A', 'A': 'ABC', 'B':'', 'Questions': 'A'})
    ret = func(cards)
    assert_same_return(expected_ret, ret, [('cards', cards)])
    assert cards == expected_cards, f"The function should remove the card from the dictionary."
    print("All basic tests passed!")

def test_question(func):
    assert inspect.isfunction(func), msg_not_a_function("question")
    assert len(inspect.signature(func).parameters) == 3, msg_wrong_number_args("question")
    team = 'beta'
    category = 'world'
    card = {'Correct': 'A', 'A': 'One', 'B':'Two', 'Questions': 'Silly question?'}
    expected_ret = f'''Question for team {team} in category {category}:

Silly question?

A. One
B. Two
'''
    ret = func(team, category, card)
    assert_same_return(expected=expected_ret, got=ret, tested_with=[('card', card)])
    print("All basic tests passed!")

def test_valid_answer(func):
    assert inspect.isfunction(func), msg_not_a_function("valid_answer")
    assert len(inspect.signature(func).parameters) == 2,msg_wrong_number_args("valid_answer")

    card = {'A': 'ABC', 'B': 'XYZ'}
    answers = ['a', 'A', 'b', 'B', 'x', 'ABC', '3', '4']
    expected = [True, True, True, True, False, False, False, False]
    for answer, expected_ret in zip(answers, expected):
        ret = func(answer, card)
        assert_same_return(expected=expected_ret, got=ret, tested_with=[('card', card), ('answer', answer)])
    print("All basic tests passed!")

def test_ask_answer(func):
    assert inspect.isfunction(func), msg_not_a_function("ask_answer")
    assert len(inspect.signature(func).parameters) == 1, msg_wrong_number_args("ask_answer")

    card = {'A': 'ABC', 'B':'XYZ', 'C': ''}
    answers = "\n".join(['v', '3', 'c', 'a'])
    expected_ret = 'a'
    sys.stdin = io.StringIO(answers)
    buf = io.StringIO()
    old = sys.stdout
    sys.stdout = buf
    ret = func(card)
    output = buf.getvalue()
    sys.stdin = sys.__stdin__
    sys.stdout = old
    expected_out = "".join(['Please input a valid answer.\n' for _ in range(3)])
    assert_same_return(expected=expected_ret, got=ret, tested_with=[('card', card)])
    assert_same_output(expected=expected_out, got=output, tested_with=[('card', card)])
    print("All basic tests passed!")

def test_check_answer(func):
    assert inspect.isfunction(func), msg_not_a_function("check_answer")
    assert len(inspect.signature(func).parameters) == 2, msg_wrong_number_args("check_answer")
    card = {'Correct': 'A', 'A': 'ABC', 'B': 'XYZ'}
    answers = ['a', 'A', 'b', 'B', 'x', 'ABC', '3', '4']
    expected = [True, True, False, False, False, False, False, False]
    for answer, expected_ret in zip(answers, expected):
        ret = func(answer, card)
        assert_same_return(expected=expected_ret, got=ret, tested_with=[('card', card), ('answer', answer)])
    print("All basic tests passed!")
