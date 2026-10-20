from backend.core.permissions import is_host
def test_host_check():
    assert is_host('a','a'); assert not is_host('b','a')
