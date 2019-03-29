import os
import re

class Rule(object):
    name = None
    description = None
    to_fix = None

    @classmethod
    def error(cls, path, line_no):
        return [(cls.name, cls.description, path, line_no)]


class MissingLink(Rule):
    name = "MISSING-LINK"
    description = "Testcase file must have a link to a spec"
    to_fix = """
        Ensure that there is a `<link rel="help" href="[url]">` for the spec.
        `MISSING-LINK` is designed to ensure that the CSS build tool can find
        the tests. Note that the CSS build system is primarily used by
        [test.csswg.org/](http://test.csswg.org/), which doesn't use
        `wptserve`, so `*.any.js` and similar tests won't work there; stick
        with the `.html` equivalent.
    """


class Regexp(Rule):
    pattern = None
    file_extensions = None
    _re = None

    def __init__(self):
        self._re = re.compile(self.pattern)

    def applies(self, path):
        return (self.file_extensions is None or
                os.path.splitext(path)[1] in self.file_extensions)

    def search(self, line):
        return self._re.search(line)


class TrailingWhitespaceRegexp(Regexp):
    name = "TRAILING WHITESPACE"
    description = "Whitespace at EOL"
    pattern = b"[ \t\f\v]$"
    to_fix = """Remove trailing whitespace from all lines in the file."""
