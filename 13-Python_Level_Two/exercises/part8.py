import re

# patterns = ['item1', 'item2']
#
# text = 'This is a string with term1, and not the other!'
#
# for pattern in patterns:
#     print("i am looking for term: "+pattern)
#
#     if re.search(pattern, text):
#         print("match")
#     else:
#         print("not match")
#
#
# match = re.search("the", text)
# print(match.start())


#print(re.findall("match", "test phrase match in the middel and end match"))


def multi_re_find(patterns, phrase):
    for pat in patterns:
        print("searching for pattern {}".format(pat))
        print(re.findall(pat, phrase))
        print('\n')

test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'
test_pattern = ['s[sd]+']


multi_re_find(test_pattern, test_phrase)
