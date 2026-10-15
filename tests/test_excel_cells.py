"""Check that Excel cells reconstruct the complete PAP module."""
from pathlib import Path
import unittest

from lohnsteuer2026 import pap2026, lohnsteuer_excel

class ExcelCellsTests(unittest.TestCase):
    def test_excel_cells(self):
        files = sorted((Path(__file__).resolve().parents[1] / "excel_cells").glob("*.py"))
        self.assertEqual(len(files), 7)
        scope = {}
        for path in files:
            source = path.read_text(encoding="utf-8")
            self.assertLess(len(source), 5101, str(path))
            exec(compile(source, str(path), "exec"), scope)
        expected = pap2026(LZZ=2, RE4=500000, STKL=1, KVZ=2.5, PVZ=1)
        actual = scope["pap2026"](LZZ=2, RE4=500000, STKL=1, KVZ=2.5, PVZ=1)
        self.assertEqual(actual, expected)
        self.assertEqual(scope["lohnsteuer_excel"](5000, 1, kv_zusatzbeitrag=2.5, pv_kinderlos=1)["LSTLZZ"], lohnsteuer_excel(5000, 1, kv_zusatzbeitrag=2.5, pv_kinderlos=1)["LSTLZZ"])

if __name__ == "__main__":
    unittest.main()
