from __future__ import print_function

LIMIT=1000

def make_data():
    wordlist = []
    worddict = {}
    with open('/usr/share/dict/words') as words:
        nwords = 0
        for word in [ x.strip().replace("'", "\\'") for x in words]:
            wordlist.append(word)
            worddict[word] = '{}'.format(nwords)
            nwords+=1
            if nwords > 1000:
                break
    print("data={'biglist': [", end="")
    print(',\n'.join(['"{}"'.format(word) for word in
                    wordlist]), end="")
    print("],", end="")
    print("'worddict': {", end="")
    for k,v in worddict.items():
        print("'{}': {},\n".format(k,v), end="")
    print("}")
    print("}")

if __name__ == '__main__':
    make_data()
