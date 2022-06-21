def rev_sent(sentence):
    """
    :param sentence:
    :return:
    """
    words = sentence.split(" ")     # split the string into words
    reverse_sentence = ' '.join(reversed(words))    # then reverse the split list and join using space
    return reverse_sentence


if __name__ == '__main__':
    input_data = " python with practice code"
    print(rev_sent(input_data))
