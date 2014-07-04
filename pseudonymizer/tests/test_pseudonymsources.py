import pytest

import pseudonymizer as psd

mynames = dict(personnames=["A B", "C D"])

def test_DictPseudonymsource():
    src = psd.DictPseudonymsource(mynames)
    assert(src.obtain("personnames") == mynames["personnames"])
    assert(not src.obtain("personnames") is mynames["personnames"]) # must be a copy

def test_DictPseudonymsource_nonexisting():
    src = psd.DictPseudonymsource(mynames)
    with pytest.raises(LookupError):
        assert(src.obtain("nonexisting") is None)

def test_FilePseudonymsource():
    src = psd.FilePseudonymsource()
    pseudonyms = src.obtain("personnames")
    assert pseudonyms[0] == "'Abd al-Ilah"
    assert pseudonyms[344] == "Antoni Stanisław Czetwertyński-Światopełk"
    assert pseudonyms[4174] == "Willia"
    assert pseudonyms[4323] == "Živojin Mišić"
    len(pseudonyms) == 4324
    assert(not src.obtain("personnames") is mynames["personnames"]) # must be a copy

def test_FilePseudonymsource_nonexisting():
    src = psd.FilePseudonymsource()
    with pytest.raises(LookupError):
        assert(src.obtain("nonexisting") is None)

