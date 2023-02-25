import os

import pytest
import time


@pytest.fixture()
def browser():
    """Какой-нибудь браузер - chrome or firefox"""
    time.sleep(1)


@pytest.mark.slow
@pytest.mark.usefixtures("browser")
def test_first():
    time.sleep(1)


# @pytest.mark.fast
# def test_second():
#     a = 5
#     b = 10
#     assert a == b

@pytest.mark.fast
def test_second():
    time.sleep(1)


@pytest.mark.skip(reason="TASK-1234 обновленная функциональность такого-то теста")
def test_skipped_test():
    pass


# @pytest.mark.skipif(os.environ["SKIP_SOMETHING"] == "true", reason="")
def test_skipped_conditional():
    if os.getenv("SKIP_SOMETHING"):
        pytest.skip("some reason")


@pytest.mark.xfail(reason="Этот тест падает из-за фазы луны")
def test_xfail():
    import random
    assert random.randint(0, 1) == 1


def test_xfail_directly():
    import random
    try:
        assert random.randint(0, 1) == 1
    except AssertionError:
        pytest.xfail("some reason")

