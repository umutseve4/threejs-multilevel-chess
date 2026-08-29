from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"


class DocumentParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.lang = None
        self.title_depth = 0
        self.title = ""
        self.meta_names = {}
        self.buttons = {}
        self.import_maps = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        element_id = values.get("id")
        if element_id:
            self.ids.add(element_id)
        if tag == "html":
            self.lang = values.get("lang")
        elif tag == "title":
            self.title_depth += 1
        elif tag == "meta" and values.get("name"):
            self.meta_names[values["name"]] = values.get("content", "")
        elif tag == "button" and element_id:
            self.buttons[element_id] = values
        elif tag == "script" and values.get("type") == "importmap":
            self.import_maps.append(True)

    def handle_endtag(self, tag):
        if tag == "title":
            self.title_depth -= 1

    def handle_data(self, data):
        if self.title_depth:
            self.title += data


class StaticQualityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = INDEX.read_text(encoding="utf-8")
        cls.parser = DocumentParser()
        cls.parser.feed(cls.html)
        cls.parser.close()

    def test_document_basics(self):
        self.assertTrue(self.html.lstrip().lower().startswith("<!doctype html>"))
        self.assertEqual(self.parser.lang, "en")
        self.assertTrue(self.parser.title.strip())
        self.assertIn("width=device-width", self.parser.meta_names.get("viewport", ""))
        self.assertTrue(self.parser.meta_names.get("description", "").strip())

    def test_accessible_controls_and_status(self):
        self.assertTrue({"info", "status", "turn", "message", "actions"}.issubset(self.parser.ids))
        self.assertEqual(self.parser.buttons["resetView"].get("type"), "button")
        self.assertEqual(self.parser.buttons["resetGame"].get("type"), "button")
        self.assertRegex(self.html, r'id="status"[^>]+aria-live="polite"')

    def test_dependency_is_https_and_version_pinned(self):
        match = re.search(r'https://cdn\.jsdelivr\.net/npm/three@([^/]+)/build/three\.module\.js', self.html)
        self.assertIsNotNone(match)
        self.assertRegex(match.group(1), r'^\d+\.\d+\.\d+$')
        self.assertEqual(len(self.parser.import_maps), 1)

    def test_game_invariants_are_explicit(self):
        self.assertRegex(self.html, r'BOARD_SIZE\s*=\s*8')
        self.assertRegex(self.html, r'LEVEL_NAMES\s*=\s*\[[^]]*["\']A["\'][^]]*["\']B["\'][^]]*["\']C["\']')
        for piece in ("pawn", "rook", "knight", "bishop", "queen", "king"):
            self.assertIn(f"type === '{piece}'", self.html)

    def test_required_repository_documents_exist(self):
        for path in ("README.md", "CONTRIBUTING.md", "SECURITY.md", ".gitignore"):
            self.assertTrue((ROOT / path).is_file(), path)


if __name__ == "__main__":
    unittest.main()
