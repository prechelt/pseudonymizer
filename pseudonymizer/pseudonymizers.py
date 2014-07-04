
class MultiPseudonymizer:
    """Manages a set of term-to-pseudonym mappings."""

    def __init__(self, pseudonymsource):
        self._pseudonymsource = pseudonymsource
        self._pseudonymizers = dict()

    def _ensure_pseudonymizer(self, category):
        if not category in self._pseudonymizers:
            raw_pseudonymlist = list(self._pseudonymsource.obtain(category))
            self._pseudonymizers[category] = Pseudonymizer(raw_pseudonymlist,
                                                           category)

    def pseudonym(self, original_term, category):
        self._ensure_pseudonymizer(category)
        return self._pseudonymizers[category].pseudonym(original_term)

    def pseudonymizer(self, category):
        self._ensure_pseudonymizer(category)
        return self._pseudonymizers[category]



class Pseudonymizer:
    """Manages one set of raw pseudonyms and one term-to-pseudonym mapping."""

    def __init__(self, pseudonymlist, category):
        self._category = category
        self._pseudonympartslist = list(map(self._split, pseudonymlist))
        self._numentries = 0
        self._original_terms = dict()  # maps from term to entry index

    def _split(self, pseudonym):
        """splits pseudonym into a (frontpart, backpart) tuple near the middle"""
        middle = len(pseudonym)//2
        hasinnerspaces = pseudonym.find(" ", 1, len(pseudonym)-1) >= 0
        if not hasinnerspaces:
            return (pseudonym[0:middle], pseudonym[middle:])
        else:
            for i in range(middle):
                if pseudonym[middle+i] == " ":
                    return (pseudonym[0:middle+i], pseudonym[middle+i:])
                if pseudonym[middle-i] == " ":
                    return (pseudonym[0:middle-i], pseudonym[middle-i:])
            assert False
            return pseudonym

    def pseudonym(self, original_term):
        if not original_term in self._original_terms:
            self._original_terms[original_term] = self._numentries
            self._numentries += 1
        index = self._original_terms[original_term]
        length = len(self._pseudonympartslist)
        frontindex = index % length
        backindex = (frontindex + (index//length)) % length
        numindex = index // (length*length)
        front = self._pseudonympartslist[frontindex][0]
        back = self._pseudonympartslist[backindex][1]
        num = "" if numindex == 0 else str(numindex+1)
        return front + back + num
