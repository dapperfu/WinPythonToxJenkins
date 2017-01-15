def test_01():
	assert 1 == 1
	
def test_02():
	import ping
	assert ping.ping() == "Pong"