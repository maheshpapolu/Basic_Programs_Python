def combine(dict1, dict2):
    """
    :param dict1:
    :param dict2:
    :return:
    """
    return(dict2.update(dict1))     # using buildin function update to combine two dictionaries


if __name__ == '__main__':
    dict1 = {"a": 31, "b": 40, "c": 54}
    dict2 = {"x": 50, "y": 80, "z": 90}

print(combine(dict1,dict2))  #calling function
print(dict2)