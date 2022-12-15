import pytest


def test_validation():
    expeted_title = "google.com"
    atcual_title = "gmail.com"
    # if expeted_title==atcual_title:
    #     print("testcases passed")
    # else:
    #     print("testcase failed")
    print("beginning")
    assert expeted_title == atcual_title, "title not matching"
    assert "gmail" in expeted_title, "gmail does not exist in the title"
    assert False, "falling "
    print("ending")
