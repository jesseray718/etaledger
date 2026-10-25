"""Smoke test (added by overhaul.sh, audit R-2b).

`python -m unittest discover` exits non-zero when it discovers no tests at
all (Python 3.12+), which fails the repository's Quality gate even though
nothing is wrong. This test gives discovery something honest to run: it
compile-checks every Python source in the repository, so real syntax
breakage still fails CI.
"""
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent


class SourcesCompile(unittest.TestCase):
    def test_tracked_python_sources_compile(self):
        for p in sorted(ROOT.rglob("*.py")):
            if ".git" in p.parts or not p.is_file():
                continue
            with self.subTest(path=str(p.relative_to(ROOT))):
                compile(p.read_bytes(), str(p), "exec")


if __name__ == "__main__":
    unittest.main()
