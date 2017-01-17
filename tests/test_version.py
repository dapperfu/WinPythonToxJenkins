import sys

def test_version1():
    assert sys.version_info >= (3,0)
	
def test_version2():
    assert sys.version_info <= (3,0)