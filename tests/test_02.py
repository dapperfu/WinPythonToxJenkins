# Pointless 
import ping
def test_ping():
    assert ping.ping == "pong"
	
def test_echo():
    assert ping.echo("hello") == "hello"