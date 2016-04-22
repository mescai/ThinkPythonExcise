
import random
class Markov(object):
    """

    """
    def __init__(self):
        self.suffix_map={}
        self.prefix=()

    def process_word(self,word,order=2):
        """Processes each word.

        word: string
        order: integer

        During the first few iterations, all we do is store up the words;
        after that we start adding entries to the dictionary.
        """

        if len(self.prefix) < order:
            self.prefix += (word,)
            return

        try:
            self.suffix_map[self.prefix].append(word)
        except KeyError:
            # if there is no entry for this prefix, make one
            self.suffix_map[self.prefix] = [word]

        prefix = self.shift(self.prefix, word)

    def process_file(self,filename, order=2):

        fp = open(filename)
        self.skip_gutenberg_header(fp)

        for line in fp:
            for word in line.rstrip().split():
                self.process_word(word, order)

    def skip_gutenberg_header(self,fp):
        """Reads from fp until it finds the line that ends the header.

        fp: open file object
        """
        for line in fp:
            if line.startswith('*END*THE SMALL PRINT!'):
                break

    def shift(self,t, word):
        """Forms a new tuple by removing the head and adding word to the tail.

        t: tuple of strings
        word: string

        Returns: tuple of strings
        """
        return t[1:] + (word,)

    def random_text(self,n=100):
        """Generates random wordsfrom the analyzed text.

        Starts with a random prefix from the dictionary.

        n: number of words to generate
        """
        # choose a random prefix (not weighted by frequency)
        start = random.choice(self.suffix_map.keys())


        for i in range(n):
            suffixes = self.suffix_map.get(start, None)
            if suffixes == None:
                # if the start isn't in map, we got to the end of the
                # original text, so we have to start again.
                self.random_text(n-i)
                return

            # choose a random suffix
            word = random.choice(suffixes)
            print word,
            start = self.shift(start, word)

if __name__=="__main__":
    n=100
    order=2
    filename="emma.txt"

    m=Markov()
    try:
        n = int(n)
        order = int(order)
    except:
        print 'Usage: randomtext.py filename [# of words] [prefix length]'
    else:
        m.process_file(filename, order)
        m.random_text(n)
