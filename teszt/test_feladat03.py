from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestTokeletesSzamok(TestCase):
    def test_feladat01(self):
        aktualis = feladatok.tokeletes_szamok()
        elvart = [6,28,496,8182]
        self.assertEqual(elvart, aktualis, "A tökéletes számokat rosszul határozta meg!")
