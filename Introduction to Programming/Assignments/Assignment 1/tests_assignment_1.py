import numpy.testing as npt


def test_exercise_0(o, u, k):
    assert type(o) == int, "x is not int type"
    assert type(u) == float, "y is not float type"
    assert type(k) == float, "z is not float type"
    assert k == o * u, "z is not equal to x * y"
    print("All basic tests passed! Good job!")

def test_exercise_1(first_name, last_name, birth_year, origin_city):
    assert type(first_name) == str, "brand is not str type"
    assert type(last_name) == str, "model is not str type"
    assert type(birth_year) == int, "year is not int type"
    assert type(origin_city) == float, "consumption is not float type"
    assert len(first_name) > 0, "brand is empty str"
    assert len(last_name) > 0, "model is empty str"
    print("All basic tests passed! Good job!")

def test_exercise_2(current_year, birth_year, age):
    assert type(current_year) == int, "current_year is not int type"
    assert type(birth_year) == int, "birth_year is not int type"
    assert type(age) == int, "age is not int type"
    assert age == (current_year - birth_year), "incorrect age calculation"
    print("All basic tests passed! Good job!")


def test_exercise_3(age,c, age_in_days):
    assert (type(age) == int) or (type(age) == float), "fuel is not int or float type"
    assert (type(age_in_days) == int) or (type(age_in_days) == float), "distance is not int or float type"
    assert age_in_days == (age/c*100), "incorrect calculation"
    print("All basic tests passed! Good job!")

def test_exercise_4(first_name, last_name, full_name):
    assert type(first_name) == str, "brand is not str type"
    assert type(last_name) == str, "model is not str type"
    assert type(full_name) == str, "car_name is not str type"
    assert (
        full_name == f"{first_name} {last_name}"
    ), "car_name does not equal to concatenation of brand and model"
    print("All basic tests passed! Good job!")

def test_exercise_5(first_name,age, greeting):
    assert type(age) == int, "age is not int type"
    assert type(first_name) == str, "car_name is not str type"
    assert (
        greeting == f"Hi! I drive a {first_name} that is {age} years old."
    ), "greeting string is wrongly formatted. ensure there are no extra spaces"
    print("All basic tests passed! Good job!")


def test_exercise_6(first_name, last_name, len_full_name):
    assert type(first_name) == str, "brand is not str type"
    assert type(last_name) == str, "model is not str type"
    assert type(len_full_name) == int, "len_car_name is not int"
    first_name_no_spaces = first_name.replace(" ", "")
    last_name_no_spaces = last_name.replace(" ", "")
    assert len_full_name == (
        len(first_name_no_spaces) + len(last_name_no_spaces)
    ), "incorrect amount of characters. maybe you are considering spaces?"
    print("All basic tests passed! Good job!")

def test_exercise_7(meters, inches, feet, a):
    assert type(inches) == float, "litter_gallon should be float type"
    assert type(feet) == float, "km_mile should be float type"
    measure_new = (100*feet)/inches
    npt.assert_almost_equal(a, ((1/meters)*measure_new), decimal=10, err_msg='incorrect mpg')
    print("All basic tests passed! Good job!")

def test_exercise_8_1(stock_1, stock_2, stock_3, SENOVA):
    assert stock_1[1] == SENOVA[stock_1[0]], "ingredient_1 is not correct"
    assert stock_2[1] == SENOVA[stock_2[0]], "ingredient_2 is not correct"
    assert stock_3[1] == SENOVA[stock_3[0]], "ingredient_3 is not correct"
    print('All basic tests passed! Good job!')

def test_exercise_8_2(stock_1, stock_2, stock_3, stocks):
    assert stock_1 in stocks, "ingredient_1 is not in shopping_list"
    assert stock_2 in stocks, "ingredient_2 is not in shopping_list"
    assert stock_3 in stocks, "ingredient_3 is not in shopping_list"
    print('All basic tests passed! Good job!')

def test_exercise_8_3(stocks):
    assert type(stocks)==list, "shopping_list is not list type"
    assert all([type(i)==list for i in stocks]), "shopping_list item is not list type"
    assert all([len(i) == 3 for i in stocks]), "shopping_list item has less than 3 elements (did you add quantitiy?)"
    assert all([type(i[2])==int for i in stocks]), "ingredient quantity is not int type"
    print('All basic tests passed! Good job!')

def test_exercise_8_4(stocks_dict, stocks):
         
    for idx, key in enumerate(stocks_dict.keys()):
        assert stocks_dict[key]['ingredient_name'] == stocks[idx][0], f"{key} has wrong ingredient_name"
        assert stocks_dict[key]['ingredient_price'] == stocks[idx][1], f"{key} has wrong ingredient_price"
        assert stocks_dict[key]['ingredient_quantity'] == stocks[idx][2], f"{key} has wrong ingredient_quantity"     
    print('All basic tests passed! Good job!')

def test_exercise_9_1(fausto_age, pisco_age, plutao_age, average_age):
    assert type(fausto_age) == bool, "fausto_adopted is not a boolean"
    assert type(pisco_age) == bool, "pisco_adopted is not a boolean"
    assert type(plutao_age) == bool, "plutao_adopted is not a boolean"
    assert type(average_age) == bool, "average_adopted is not a boolean"
    assert average_age == False, "available_dogs is wrong"
    print('All basic tests passed! Good job!')

def test_exercise_9_2(nr_dogs):
    assert nr_dogs == 3, "Wrong Number"
    print('All basic tests passed! Good job!')
