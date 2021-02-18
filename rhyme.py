import pyrhyme

class rhymeBrain:
    def __init__(self, word):
        self.word = word
    def get_rhymes(self):
        g = pyrhyme.RhymeBrain()
        rhymes = g.rhyming(word='bonjour', lang='fr')
        return [x for x in rhymes]
    # def __str__(self):
    #     return
r = rhymeBrain("bonjour")
rimes = r.get_rhymes()
for i in rimes:
    print(i)
