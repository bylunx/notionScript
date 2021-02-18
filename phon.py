"""Phonetics class for french word"""
import phonemizer

class PhoneticSentence:
    def __init__(self, word, phon_words=None):
        self.word = word.strip().lower()
        self.phon_words = phon_words

    def process_phonetic(self):
        phonetics = phonemizer.phonemize(self.word, language="fr-fr", backend="espeak").split(" ")
        self.phon_words = [PhoneticWord(p) for p in phonetics]

    @property
    def phonetic(self):
        if not self.phon_words:
            self.process_phonetic()
        return self.phon_words

    def __str__(self):
        return "".join(self.phonetic)


class PhoneticWord:

    def __init__(self, word, phon_word=None):
        self.word = word
        self.phon_word = phon_word

    def process_phonetic(self):
        self.phon_word = phonemizer.phonemize(self.word, language="fr-fr", backend="espeak")

    @property
    def phonetic(self):
        if not self.phon_word:
            self.process_phonetic()
        return self.phon_word

    def rhyme_with(self, rword):
        pass

    def __str__(self):
        return self.phonetic()