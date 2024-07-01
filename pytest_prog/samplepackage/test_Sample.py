import pytest


@pytest.mark.smoke
def test_fun1():
    print("fun1")

@pytest.mark.xfail
def test_fun2():
    print("fun2")
    assert False


@pytest.mark.smoke
# @pytest.mark.skip
@pytest.mark.xfail
def test_fun3():
    print("fun3")

@pytest.mark.parametrize("username,pwd",[("ABC","123"),("QWE","23")])
def test_param_fun(username, pwd):
    print(f"Username:{username}, Pwd: {pwd}")