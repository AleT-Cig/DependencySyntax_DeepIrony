import unicodedata
import Model_udpipe
import re

model = Model_udpipe.Model_udpipe(".......")


class Tweet(object):

    id = None
    text = None
    label = None
    language = None
    # topic=None

    def __init__(self, id, text, label):


        self.id=id
        self.text = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', ' ', text)
        # self.text=text
        print("text")
        print(text)
        # self.language=language
        # self.topic=topic


        self.label=label
        #print("label")
        #print(self.label)

        self.text_accents_stripped=strip_accents(self.text)

        self.upostag=model.return_upostags(self.text)
        # print("upostag")
        # print(self.upostag)

        self.deprelnegation=model.return_deprelnegations(self.text)
        #print("deprelnegation")
        #print(self.deprelnegation)


        self.deprels=model.return_deprels(self.text)
        #print("deprels")
        #print(self.deprels)


        self.relationVERB=model.return_relation(self.text,"VERB","form")
        # print("relationVERB")
        # print(self.relationVERB)

        self.relationNOUN=model.return_relation(self.text,"NOUN","form")
        # print("relationNOUN")
        # print(self.relationNOUN)

        self.relationADJ=model.return_relation(self.text,"ADJ","form")
        # print("relationADJ")
        # print(self.relationADJ)

        self.Sidorov_form=model.return_Sidorov(self.text,"form")
        #print("Sidorov_form")
        #print(self.Sidorov_form)

        self.Sidorov_upostag=model.return_Sidorov(self.text,"upostag")
        #print("Sidorov_upostag")
        #print(self.Sidorov_upostag)

        self.Sidorov_deprel=model.return_Sidorov(self.text,"deprel")
        #print("Sidorov_deprel")
        #print(self.Sidorov_deprel)

        print("\n\n")


def make_tweet(id, text, label):
    """
        Return a Tweet object.
    """
    tweet = Tweet(id, text, label)

    return tweet



def strip_accents(text):
    """
    Strip accents from input String.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :rtype: String.
    """

    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)
