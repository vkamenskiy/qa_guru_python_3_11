from dataclasses import dataclass

import pytest


@pytest.mark.parametrize("browser", ["chromedriver", "gekko", "webkit"],
                         ids=["Chrome", "Firefox", "Сафари"])
def test_with_param(browser):
    pass


@pytest.mark.parametrize("browser", ["Chrome", "Firefox", "Safari"])
@pytest.mark.parametrize("test_user", ["manager", "admin", "common_user"])
def test_with_matrix_param(browser, test_user):
    if browser == 'Safari' and test_user == "admin":
        pytest.skip("Админка не работает на сафари")


@pytest.mark.parametrize(["browser", "test_user"],
                         [("Chrome", "manager"), ("Firefox", "admin"), ("Safari", "common_user")],
                         ids=["Chrome with manager", "Firefox with admin", "Safari with common user"])
def test_with_matrix_param2(browser, test_user):
    pass


@pytest.mark.parametrize(["browser"],
                         [pytest.param(("Chrome", "manager"), id="Chrome with manager", marks=pytest.mark.skip("Сломано потому что сломано")),
                          pytest.param(("Firefox", "admin"), id="Firefox with admin"),
                          pytest.param(("Safari", "common_user"), id="Safari with common user"),
                          ])
def test_with_param_marks(browser):
    pass


@pytest.fixture(params=[pytest.param("Chrome", id="Chrome", marks=pytest.mark.skip),
                        "Firefox", "Safari"], scope="session")
def browser(request):
    assert request.param in ["Chrome", "Firefox", "Safari"]
    if request.param == "Chrome":
        pass
        # return Chromedriver()


def test_with_parametrized_fixture(browser):
    pass


@pytest.mark.parametrize("browser", ["Safari"], indirect=True)
def test_with_indirect_parametrization(browser):
    assert browser == "Safari"


common_user = pytest.mark.parametrize("test_user", ["common_user"], indirect=True)


@common_user
def test_with_account(test_user):
    pass



@dataclass
class User:
    id: int
    name: str
    age: int
    description: str

    def __repr__(self):
        return f"{self.name} ({self.id})"


user1 = User(id=1, name="Mario", age=32, description="something " * 10)
user2 = User(id=2, name="Wario", age=62, description="else " * 10)


def show_user(user):
    return f"{user.name} ({user.id})"


@pytest.mark.parametrize("user", [user1, user2], ids=repr)
def test_users(user):
    print()
