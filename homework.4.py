# 1
def sum_numbers(num1, num2):
    sum = num1 + num2
    return sum


print(sum_numbers(1, 5))
# printing check that function work as expected

def test_1():
    assert sum_numbers(1, 10) == 11
# when sum numbers not as expected, console return assertion error
test_1()

# 2
# import pytest
# words = ['netzer', 'noa', 'gil']
# @pytest.mark.parametrize('str1', 'str2', 'str3', 'result',
#                          [
#                              ('netzer', 'noa', 'gil', 'a')
#                          ]
#                          )
# def test_a(str1, str2, str3, result ):
#     assert words == result



# 3
def search_hello():
    hello_word = open("C:\\automation course\\words.txt", 'r')
    return hello_word.read()

print(search_hello())

def test_2():
    assert 'hello' in search_hello()
    # assert 'wave' in search_hello()
    # in this line the test will return an assert error
test_2()