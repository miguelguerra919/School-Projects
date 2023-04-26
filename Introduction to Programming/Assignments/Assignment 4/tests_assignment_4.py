# Author: Cláudio Haupt Vieira @ NovaSBE
# License: https://creativecommons.org/licenses/by-nc/3.0/

import inspect


def is_class(AnsClass) -> bool:
    return inspect.isclass(AnsClass)


def has_constructor(AnsClass) -> bool:
    return len(inspect.signature(AnsClass).parameters) > 0


def has_variable_in_self(AnsClass, variable: str) -> bool:
    return f"self.{variable}" in get_source(AnsClass)


def is_method(ans_method) -> bool:
    return inspect.ismethod(ans_method) or inspect.isfunction(ans_method)


def get_source(ans) -> str:
    return inspect.getsource(ans)


def test_exercise_1_1(human_class, human_obj):
    not_class = "Human is not a class."
    unneeded_constructor = (
        "Human has no instance atributes, __init__() method is not required."
    )
    no_class_attribute = "Human has no class attribute 'species'."
    wrong_class_attribute = (
        "Human 'species' class attribute should be 'Homo sapiens sapiens'."
    )
    human_obj_not_instance = "human object is not an instance of the Human class."
    assert is_class(human_class), not_class
    assert not has_constructor(human_class), unneeded_constructor
    assert hasattr(human_class, "species"), no_class_attribute
    assert human_class.species == "Homo sapiens sapiens", wrong_class_attribute
    assert isinstance(human_obj, human_class), human_obj_not_instance
    print("All basic tests passed!")


def test_exercise_1_2(human_class, human_obj):
    not_class = "Human is not a class."
    no_constructor = "Human has no __init__() method."
    no_class_attribute = "Human has no class attribute 'species'."
    no_attribute_name = "Human has no instance attribute 'name'"
    no_attribute_age = "Human has no instance attribute 'age'"
    no_instance_attribute_name = (
        "Human 'name' attribute is not instance attribute. Missing self.name"
    )
    no_instance_attribute_age = (
        "Human 'age' attribute is not instance attribute. Missing self.age"
    )
    wrong_class_attribute = (
        "Human 'species' class attribute should be 'Homo sapiens sapiens'."
    )
    human_obj_not_instance = "human object is not an instance of the Human class. Try Human(name=..., age=...)"
    human_obj_wrong_age = "named_human object has the wrong age (should be 30)"
    human_obj_wrong_name = "named_human object has the wrong name (should be 'John')"

    assert is_class(human_class), not_class
    assert has_constructor(human_class), no_constructor
    assert hasattr(human_class, "species"), no_class_attribute
    assert (
        "self," in inspect.getsource(human_class.__dict__["__init__"]).rstrip().lstrip()
    ), missing_self
    assert "self.age" in inspect.getsource(
        human_class.__dict__["__init__"]
    ), no_instance_attribute_age
    assert "self.name" in inspect.getsource(
        human_class.__dict__["__init__"]
    ), no_instance_attribute_name
    assert human_class.species == "Homo sapiens sapiens", wrong_class_attribute
    assert isinstance(human_obj, human_class), human_obj_not_instance
    assert human_obj.name == "John", human_obj_wrong_name
    assert human_obj.age == 30, human_obj_wrong_age
    print("All basic tests passed!")


def test_exercise_1_3(human_class, human_obj):
    not_class = "Human is not a class."
    no_constructor = "Human has no __init__() method."
    no_class_attribute = "Human has no class attribute 'species'."
    no_attribute_name = "Human has no instance attribute 'name'"
    no_attribute_age = "Human has no instance attribute 'age'"
    no_instance_attribute_name = (
        "Human 'name' attribute is not instance attribute. Missing self.name"
    )
    no_instance_attribute_age = (
        "Human 'age' attribute is not instance attribute. Missing self.age"
    )
    missing_self = "Human __init__ is missing reference to self"
    wrong_class_attribute = (
        "Human 'species' class attribute should be 'Homo sapiens sapiens'."
    )
    human_obj_not_instance = "human object is not an instance of the Human class. Try Human(name=..., age=...)"
    human_no_grow_method = "Human class does not contain a grow() method."
    human_no_self_in_grow_method = "Human grow() method should have self argument to access and increment to self.age"
    human_wrong_age = (
        "After calling the grow() method three times, human_toddler should have age 6."
    )
    human_grow_method_not_working_properly = (
        "Human grow() method is not working properly. It should increment 1 to self.age"
    )
    test = human_class(name="Test", age=1)
    try:
        test.grow()
    except UnboundLocalError:
        raise Exception(
            "In order to change the instance age, you have to change it through self.age"
        )
    except Exception:
        raise
    assert is_class(human_class), not_class
    assert has_constructor(human_class), no_constructor
    assert hasattr(human_class, "species"), no_class_attribute
    assert (
        "self," in inspect.getsource(human_class.__dict__["__init__"]).rstrip().lstrip()
    ), missing_self
    assert "self.age" in inspect.getsource(
        human_class.__dict__["__init__"]
    ), no_instance_attribute_age
    assert "self.name" in inspect.getsource(
        human_class.__dict__["__init__"]
    ), no_instance_attribute_name
    assert human_class.species == "Homo sapiens sapiens", wrong_class_attribute
    assert isinstance(human_obj, human_class), human_obj_not_instance
    assert is_method(human_obj.grow), human_no_grow_method
    assert "grow(self" in get_source(
        human_class.__dict__["grow"]
    ).replace(" ", ""), human_no_self_in_grow_method
    assert human_obj.name == "John", human_obj_wrong_name
    assert human_obj.age == 6, human_wrong_age
    assert test.age == 2, human_grow_method_not_working_properly
    if "return" in get_source(human_class.__dict__["grow"]):
        raise Warning(
            "No return is needed in grow() method, because we are simply incrementing one to an instance attribute"
        )
    print("All basic tests passed!")


def test_exercise_1_4(human_class, human_obj_1, human_obj_2):
    not_class = "Human is not a class."
    no_constructor = "Human has no __init__() method."
    no_class_attribute = "Human has no class attribute 'species'."
    no_attribute_name = "Human has no instance attribute 'name'"
    no_attribute_age = "Human has no instance attribute 'age'"
    no_instance_attribute_name = (
        "Human 'name' attribute is not instance attribute. Missing self.name"
    )
    no_instance_attribute_age = (
        "Human 'age' attribute is not instance attribute. Missing self.age"
    )
    missing_self = "Human __init__ is missing reference to self"
    wrong_class_attribute = (
        "Human 'species' class attribute should be 'Homo sapiens sapiens'."
    )
    human_obj_not_instance = "human object is not an instance of the Human class. Try Human(name=..., age=...)"
    human_no_grow_method = "Human class does not contain a grow() method."
    human_no_say_hello_method = "Human class does not contain a say_hello() method."
    human_no_self_in_grow_method = "Human grow() method should have self argument to access and increment to self.age"
    human_no_self_in_say_hello_method = "Human say_hello() method should have self argument to access self.name, as well as other Human object to access its name"
    human_grow_method_not_working_properly = (
        "Human grow() method is not working properly. It should increment 1 to self.age"
    )

    assert is_class(human_class), not_class
    assert has_constructor(human_class), no_constructor
    assert hasattr(human_class, "species"), no_class_attribute
    assert (
        "self," in inspect.getsource(human_class.__dict__["__init__"]).rstrip().lstrip()
    ), missing_self
    assert "self.age" in inspect.getsource(
        human_class.__dict__["__init__"]
    ), no_instance_attribute_age
    assert "self.name" in inspect.getsource(
        human_class.__dict__["__init__"]
    ), no_instance_attribute_name
    assert human_class.species == "Homo sapiens sapiens", wrong_class_attribute
    assert isinstance(human_obj_1, human_class), human_obj_not_instance
    assert isinstance(human_obj_2, human_class), human_obj_not_instance
    assert is_method(human_obj_1.grow), human_no_grow_method
    assert "grow(self" in get_source(
        human_class.__dict__["grow"]
    ).replace(" ", ""), human_no_self_in_grow_method
    assert "say_hello(self" in get_source(
        human_class.__dict__["say_hello"]
    ).replace(" ", ""), human_no_self_in_say_hello_method
    if not "return" in get_source(human_class.__dict__["say_hello"]):
        raise Exception(
            "Exercise requires that say_hello returns a string (eg. do not use print)"
        )
    name_1 = human_obj_1.name
    name_2 = human_obj_2.name
    error_str_return = (
        f"say_hello method should return '{name_1} says hello to {name_2}'"
    )
    assert (
        human_obj_1.say_hello(human_obj_2) == f"{name_1} says hello to {name_2}"
    ), error_str_return
    print("All basic tests passed!")


def test_exercise_2_1(client_class):
    not_class = "BankClient is not a class."
    no_constructor = (
        "BankClient requires a __init__() method to specify instance attributes."
    )
    missing_self = "BankClient __init__ is missing reference to self"
    no_inst_attribute_name = "BankClient has no instance attribute 'name'."
    no_inst_attribute_balance = "BankClient has no instance attribute 'balance'"
    no_inst_attribute_tier = "BankClient has no instance attribute 'tier'"

    assert is_class(client_class), not_class
    assert has_constructor(client_class), no_constructor
    assert (
        "self" in inspect.getsource(client_class.__dict__["__init__"]).rstrip().lstrip()
    ), missing_self
    assert (
        "self.name"
        in inspect.getsource(client_class.__dict__["__init__"]).rstrip().lstrip()
    ), no_inst_attribute_name
    assert (
        "self.balance"
        in inspect.getsource(client_class.__dict__["__init__"]).rstrip().lstrip()
    ), no_inst_attribute_balance
    assert (
        "self.tier"
        in inspect.getsource(client_class.__dict__["__init__"]).rstrip().lstrip()
    ), no_inst_attribute_tier
    test = client_class(name="Test", balance=0)
    assert test.tier == 0, "instance attribute 'tier' should be initialized as 0"
    print("All basic tests passed!")


def test_exercise_2_2(client_class):
    not_class = "BankClient is not a class."
    no_constructor = (
        "BankClient requires a __init__() method to specify instance attributes."
    )
    missing_self = "BankClient __init__ is missing reference to self"
    no_inst_attribute_name = "BankClient has no instance attribute 'name'."
    no_inst_attribute_balance = "BankClient has no instance attribute 'balance'"
    no_inst_attribute_tier = "BankClient has no instance attribute 'tier'"
    wrong_type_tier = "'tier' class attribute should be int type."
    no_method_update_tier = "BankClient does not contain 'update_tier' method"

    assert is_class(client_class), not_class
    assert has_constructor(client_class), no_constructor
    assert (
        "self" in inspect.getsource(client_class.__dict__["__init__"]).rstrip().lstrip()
    ), missing_self
    assert (
        "self.name"
        in inspect.getsource(client_class.__dict__["__init__"]).rstrip().lstrip()
    ), no_inst_attribute_name
    assert (
        "self.balance"
        in inspect.getsource(client_class.__dict__["__init__"]).rstrip().lstrip()
    ), no_inst_attribute_balance
    assert (
        "self.tier"
        in inspect.getsource(client_class.__dict__["__init__"]).rstrip().lstrip()
    ), no_inst_attribute_tier
    
    assert "self.update_tier()" in inspect.getsource(client_class.__dict__["__init__"]).rstrip().lstrip(), "update_tier() method must be called within __init__ method (hint: use self.update_tier())"
    
    if "tier" in inspect.signature(client_class.__init__).parameters:
        raise Exception(
            "BankClient objects should be instantiated with just 'name' and 'balance'. 'tier' shouldn't be argument of __init__()"
        )
    assert is_method(client_class.update_tier), no_method_update_tier
    test = client_class(name="Test", balance=0)
    assert test.tier == 0, "instance attribute 'tier' should be initialized as 0"

    if "return" in get_source(client_class.__dict__["update_tier"]):
        raise Warning(
            "No return is needed in update_tier() method, because we are directly updating an instance attribute."
        )

    test = client_class(name="Test", balance=0)
    test.update_tier()
    assert (
        test.tier == 0
    ), "update_tier() is wrong -> a client with balance less than 10000 should be tier 0"
    test1 = client_class(name="Test", balance=10001)
    test1.update_tier()
    assert (
        test1.tier == 1
    ), "update_tier() is wrong -> a client with balance greater or equal than 10000 should be tier 1"
    test2 = client_class(name="Test", balance=100000)
    test2.update_tier()
    assert (
        test2.tier == 2
    ), "update_tier() is wrong -> a client with balance greater or equal than 100000 should be tier 2"

    print("All basic tests passed!")


def test_exercise_2_3(client_class):
    not_class = "BankClient is not a class."
    no_constructor = (
        "BankClient requires a __init__() method to specify instance attributes."
    )
    missing_self = "BankClient __init__ is missing reference to self"
    no_inst_attribute_name = "BankClient has no instance attribute 'name'."
    no_inst_attribute_balance = "BankClient has no instance attribute 'balance'"
    no_inst_attribute_tier = "BankClient has no instance attribute 'tier'"
    wrong_type_tier = "'tier' class attribute should be int type."
    no_method_update_tier = "BankClient does not contain 'update_tier' method"
    no_method_deposit = "BankClient does not contain 'deposit' method"
    no_method_withdraw = "BankClient does not contain 'withdraw' method"

    assert is_class(client_class), not_class
    assert has_constructor(client_class), no_constructor
    assert (
        "self" in inspect.getsource(client_class.__dict__["__init__"]).rstrip().lstrip()
    ), missing_self
    assert (
        "self.name"
        in inspect.getsource(client_class.__dict__["__init__"]).rstrip().lstrip()
    ), no_inst_attribute_name
    assert (
        "self.balance"
        in inspect.getsource(client_class.__dict__["__init__"]).rstrip().lstrip()
    ), no_inst_attribute_balance
    assert (
        "self.tier"
        in inspect.getsource(client_class.__dict__["__init__"]).rstrip().lstrip()
    ), no_inst_attribute_tier
    if "tier" in inspect.signature(client_class.__init__).parameters:
        raise Exception(
            "BankClient objects should be instantiated with just 'name' and 'balance'. 'tier' shouldn't be argument of __init__()"
        )
        
    assert "self.update_tier()" in inspect.getsource(client_class.__dict__["__init__"]).rstrip().lstrip(), "update_tier() method must be called within __init__ method (hint: use self.update_tier())"
    assert is_method(client_class.update_tier), no_method_update_tier
    assert is_method(client_class.deposit), no_method_deposit
    assert is_method(client_class.withdraw), no_method_withdraw

    if len(inspect.signature(client_class.deposit).parameters) != 2:
        raise Warning("deposit method should have two arguments, self and amount")

    if len(inspect.signature(client_class.withdraw).parameters) != 2:
        raise Warning("withdraw method should have two arguments, self and amount")

    if not "self" in inspect.signature(client_class.deposit).parameters:
        raise Warning(
            "deposit method first argument should be self in order to access instance attributes"
        )

    if not "self" in inspect.signature(client_class.withdraw).parameters:
        raise Warning(
            "deposit method first argument should be self in order to access instance attributes"
        )

    if "return" in get_source(client_class.__dict__["update_tier"]):
        raise Warning(
            "No return is needed in update_tier() method, because we are directly updating an instance attribute."
        )

    if not "return" in get_source(client_class.__dict__["withdraw"]):
        raise Warning(
            "Missing a return in `withdraw` method in case of not enough balance."
        )

    if not "self.update_tier()" in get_source(client_class.__dict__["withdraw"]).replace(" ", ""):
        raise Warning(
            "Each operation (deposit, withdraw) should be followed by the update_tier() method. Use self.update_tier() to access the method"
        )

    if not "self.update_tier()" in get_source(client_class.__dict__["deposit"]).replace(" ", ""):
        raise Warning(
            "Each operation (deposit, withdraw) should be followed by the update_tier() method. Use self.update_tier() to access the method"
        )

    test_c1 = client_class(name="John", balance=1000)
    test_c1.deposit(1)
    assert (
        test_c1.balance == 1001
    ), "deposit method is not working properly. it should add the given amount to self.balance"
    test_c1.withdraw(1)
    assert (
        test_c1.balance == 1000
    ), "withdraw method is not working properly. it should subtract the given amount from self.balance"
    assert (
        test_c1.withdraw(2000) == "Failed. Not enough balance"
    ), "In case balance does not allow withdrawal, the string 'Failed. Not enough balance' should be returned"
    test_c1.deposit(10000)
    assert (
        test_c1.tier == 1
    ), "tier failed to update after deposit, are you sure you are calling self.update_tier() inside deposit() and withdraw() methods?"

    print("All basic tests passed!")
    
def test_exercise_2_4(client_class):
    not_class = "BankClient is not a class."
    no_constructor = (
        "BankClient requires a __init__() method to specify instance attributes."
    )
    missing_self = "BankClient __init__ is missing reference to self"
    no_inst_attribute_name = "BankClient has no instance attribute 'name'."
    no_inst_attribute_balance = "BankClient has no instance attribute 'balance'"
    no_inst_attribute_tier = "BankClient has no instance attribute 'tier'"
    wrong_type_tier = "'tier' class attribute should be int type."
    no_method_update_tier = "BankClient does not contain 'update_tier' method"
    no_method_deposit = "BankClient does not contain 'deposit' method"
    no_method_withdraw = "BankClient does not contain 'withdraw' method"
    no_method_transfer = "BankClient does not contain 'transfer' method"


    assert is_class(client_class), not_class
    assert has_constructor(client_class), no_constructor
    assert (
        "self" in inspect.getsource(client_class.__dict__["__init__"]).rstrip().lstrip()
    ), missing_self
    assert (
        "self.name"
        in inspect.getsource(client_class.__dict__["__init__"]).rstrip().lstrip()
    ), no_inst_attribute_name
    assert (
        "self.balance"
        in inspect.getsource(client_class.__dict__["__init__"]).rstrip().lstrip()
    ), no_inst_attribute_balance
    assert (
        "self.tier"
        in inspect.getsource(client_class.__dict__["__init__"]).rstrip().lstrip()
    ), no_inst_attribute_tier
    if "tier" in inspect.signature(client_class.__init__).parameters:
        raise Exception(
            "BankClient objects should be instantiated with just 'name' and 'balance'. 'tier' shouldn't be argument of __init__()"
        )
        
    assert "self.update_tier()" in inspect.getsource(client_class.__dict__["__init__"]).rstrip().lstrip(), "update_tier() method must be called within __init__ method (hint: use self.update_tier())"
    assert is_method(client_class.update_tier), no_method_update_tier
    assert is_method(client_class.deposit), no_method_deposit
    assert is_method(client_class.withdraw), no_method_withdraw
    assert is_method(client_class.transfer), no_method_transfer


    if len(inspect.signature(client_class.deposit).parameters) != 2:
        raise Warning("deposit method should have two arguments, self and amount")

    if len(inspect.signature(client_class.withdraw).parameters) != 2:
        raise Warning("withdraw method should have two arguments, self and amount")

    if not "self" in inspect.signature(client_class.deposit).parameters:
        raise Warning(
            "deposit method first argument should be self in order to access instance attributes"
        )

    if not "self" in inspect.signature(client_class.withdraw).parameters:
        raise Warning(
            "deposit method first argument should be self in order to access instance attributes"
        )

    if "return" in get_source(client_class.__dict__["update_tier"]):
        raise Warning(
            "No return is needed in update_tier() method, because we are directly updating an instance attribute."
        )

    if not "return" in get_source(client_class.__dict__["withdraw"]):
        raise Warning(
            "Missing a return in `withdraw` method in case of not enough balance."
        )

    if not "self.update_tier()" in get_source(client_class.__dict__["withdraw"]).replace(" ", ""):
        raise Warning(
            "Each operation (deposit, withdraw) should be followed by the update_tier() method. Use self.update_tier() to access the method"
        )

    if not "self.update_tier()" in get_source(client_class.__dict__["deposit"]).replace(" ", ""):
        raise Warning(
            "Each operation (deposit, withdraw) should be followed by the update_tier() method. Use self.update_tier() to access the method"
        )

    test_c1 = client_class(name="John", balance=1000)
    test_c1.deposit(1)
    assert (
        test_c1.balance == 1001
    ), "deposit method is not working properly. it should add the given amount to self.balance"
    test_c1.withdraw(1)
    assert (
        test_c1.balance == 1000
    ), "withdraw method is not working properly. it should subtract the given amount from self.balance"
    assert (
        test_c1.withdraw(2000) == "Failed. Not enough balance"
    ), "In case balance does not allow withdrawal, the string 'Failed. Not enough balance' should be returned"
    test_c1.deposit(10000)
    assert (
        test_c1.tier == 1
    ), "tier failed to update after deposit, are you sure you are calling self.update_tier() inside deposit() and withdraw() methods?"
    
    
    if len(inspect.signature(client_class.transfer).parameters) != 3:
        raise Warning(
            "transfer method should have three arguments, self, other_client and amount"
        )
    
    
    if not "self.update_tier()" in get_source(client_class.__dict__["transfer"]).replace(" ", ""):
        raise Warning(
            "Transfer should be followed by the update_tier() method in both the sender and the receiver objects \n Hint: use self.update_tier() and other_client.update_tier()"
        )
    
    client_1 = client_class(name="John", balance=1000)
    client_2 = client_class(name="Jane", balance=1000)
    client_1.transfer(other_client=client_2, amount=10)
    assert client_1.balance == 989, "Error in transfer() method. Ensure fee (if any) is subracted from sender balance"
    assert client_2.balance == 1010, "Error in transfer() method. Ensure receiver object"
    
    client_3 = client_class(name="Adam", balance=9999999)
    client_4 = client_class(name="Sofia", balance=0)
    client_3.transfer(client_4, 1000)
    assert client_3.balance == 9998999, "Error in transfer() method - note that clients in tier 1 and 2 do not pay transfer fees)"

    print("All basic tests passed!")
