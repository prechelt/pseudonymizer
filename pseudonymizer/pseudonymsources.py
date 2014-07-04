
import os.path

class DictPseudonymsource:
    """Manage a set of raw pseudonym lists that comes as a map from category to list."""

    def __init__(self, sourcedict):
        self._sourcedict = sourcedict

    def obtain(self, category):
        if not category in self._sourcedict:
            raise LookupError("dict-based pseudonym category '{}' is unknown".format(category))
        return list(self._sourcedict[category])  # return a copy


_datadir = os.path.join(os.path.dirname(__file__), "data")


class FilePseudonymsource:
    """Manage a set of raw pseudonym lists stored in files.

    For category x, search a list of directories for a file x.txt
    and treat each of its lines (without the linebreak) as a raw pseudonym.
    """

    def __init__(self, directories=_datadir):
        self._dirs = [directories] if type(directories) == str else directories

    def obtain(self, category):
        def findfile(filename, dirs):
            for dir in self._dirs:
                fullname = os.path.join(dir, filename)
                if os.path.isfile(fullname):
                    return fullname
            raise LookupError("file-based pseudonym category '{}' is unknown".format(category))
        with open(findfile(category + ".txt", self._dirs), encoding="utf8") as file:
            return [line.rstrip() for line in file]