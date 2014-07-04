# for py.test

import pseudonymizer as psd

mynames = dict(personnames=["A X", "B Y"])


def test_MultiPseudonymizer():
    mypsd = psd.MultiPseudonymizer(pseudonymsource=psd.DictPseudonymsource(mynames))
    assert(mypsd.pseudonym("Lutz Prechelt", "personnames") == "A X")
    assert(mypsd.pseudonym("Frank Müller", "personnames") == "B Y")

def test_Pseudonymizer_assemble_parts():
    mympsd = psd.MultiPseudonymizer(pseudonymsource=psd.DictPseudonymsource(mynames))
    mypsd = mympsd.pseudonymizer("personnames")
    assert list(map(mypsd.pseudonym, range(12))) == [
        "A X", "B Y", "A Y", "B X",
        "A X2", "B Y2", "A Y2", "B X2",
        "A X3", "B Y3", "A Y3", "B X3",
    ]

def test_Pseudonymizer_noblanks56():
    mypsd56 = psd.Pseudonymizer(["abxyz", "ABCXYZ"], "personnames")
    assert list(map(mypsd56.pseudonym, range(4))) == [
        "abxyz", "ABCXYZ", "abXYZ", "ABCxyz",
    ]

def test_Pseudonymizer_noblanks12():
    mypsd12 = psd.Pseudonymizer(["a", "AZ"], "personnames")
    assert list(map(mypsd12.pseudonym, range(4))) == [
        "a", "AZ", "Z", "Aa",
    ]

def test_Pseudonymizer_noblanks0():
    mypsd0 = psd.Pseudonymizer([""], "personnames")
    assert list(map(mypsd0.pseudonym, range(3))) == [
        "", "2", "3",
    ]

def test_Pseudonymizer_leadingtrailingblank():
    mypsdlb = psd.Pseudonymizer([" AB", "abc "], "personnames")
    assert list(map(mypsdlb.pseudonym, range(4))) == [
        " AB", "abc ", " c ", "abAB"
    ]

def test_Pseudonymizer_findmiddlefront():
    mypsdtb = psd.Pseudonymizer(["AB XYZ", "abc xyz"], "personnames")
    assert list(map(mypsdtb.pseudonym, range(4))) == [
        "AB XYZ", "abc xyz", "AB xyz", "abc XYZ"
    ]

def test_Pseudonymizer_findmiddleback():
    mypsdtb = psd.Pseudonymizer(["ABC XYZ", "abc yz"], "personnames")
    assert list(map(mypsdtb.pseudonym, range(4))) == [
        "ABC XYZ", "abc yz", "ABC yz", "abc XYZ"
    ]

def test_Pseudonymizer_findmiddleback():
    long1f = "one-but-really-long-in-comparison-to-the-rest-here "
    long1b = "Two Three"
    long4f = "one two three "
    long4b = "and-then-finally-four-but-very-late-indeed-to-be-cut-not-really-in-the-middle"
    mypsdtb = psd.Pseudonymizer([long1f+long1b, long4f+long4b], "personnames")
    assert list(map(mypsdtb.pseudonym, range(4))) == [
        long1f+long1b, long4f+long4b, long1f+long4b, long4f+long1b
    ]
