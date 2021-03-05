def test_function():
    assert sum([1,2,3]) == 6, "Should be 6"


def test_list():
    assert list(("Lista",1)) == ["Lista", 1], "Returns a list with two elements"



def custom_function(x):
    return [x for x in range(x,10)]


print(custom_function(4))

def test_custom():
    assert custom_function(4) == [4, 5, 6, 7, 8, 9], "This return a list"



if __name__ == "__main__":
    test_function()
    test_list()
    test_custom()
    print("Everything pass")
