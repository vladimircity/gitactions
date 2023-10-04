from app import ipv4_or_localhost_regex_type

def test_ipv4_or_localhost_regex_type():
    assert ipv4_or_localhost_regex_type('localhost') == 'localhost'