import codecs


def saveMessages(msgs):
    with codecs.open('../messages.json', 'w', 'utf-8') as f:
        f.write('[')
        for data in msgs:
            f.write(str(data))
            f.write(',')
    with codecs.open('../messages.json', 'rb+', 'utf-8') as f:
        f.seek(-1, 2)
        f.truncate()
    with codecs.open('../messages.json', 'a', 'utf-8') as f:
        f.write(']')
