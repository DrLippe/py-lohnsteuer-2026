import unittest

from lohnsteuer2026 import pap2026, lohnsteuer_excel

class PAP2026Tests(unittest.TestCase):
    def test_official_fixture_2026(self):
        x = pap2026(LZZ=2, RE4=500000, STKL=1, KVZ=2.5, PVZ=1)
        self.assertEqual(x["LSTLZZ"], 78583)
        self.assertEqual(x["SOLZLZZ"], 0)

    def test_euro_adapter(self):
        x = lohnsteuer_excel(5000, 1, zeitraum=2,
                             kv_zusatzbeitrag=2.5, pv_kinderlos=1)
        self.assertEqual(x["LSTLZZ"], 785.83)

    def test_bad_input(self):
        with self.assertRaises(ValueError):
            pap2026(NOT_A_FIELD=1)

if __name__ == "__main__":
    unittest.main()
