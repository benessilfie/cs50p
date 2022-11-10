from hello import hello

def test_default():
    hello() == "Hello, World!"

def test_argument():
    hello("David") == "Hello, David!"