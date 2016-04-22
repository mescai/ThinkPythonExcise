import anagram_sets
import shelve
def store_anagrams(d):
    sh=shelve.open("atest.db","c")
    for keys,values in d.iteritems():
        sh[keys]=values
    sh.close()

def read_anagrams(word):
    sh=shelve.open("atest.db","r")
    for values in sh.values():
        if word in values:
            return values







