from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestOsztokSzama(TestCase):
    def test_feladat01(self):
        parameter=1
        aktualis = feladatok.osztok_szama(parameter)
        elvart = 1
        self.assertEqual(elvart, aktualis, str(parameter)+" osztóinak számát rosszul határozta meg!")
    def test_feladat02(self):
        parameter=0
        aktualis = feladatok.osztok_szama(parameter)
        elvart = None
        self.assertEqual(elvart, aktualis, str(parameter)+" osztóinak számát rosszul határozta meg!")
    def test_feladat03(self):
        parameter=-5
        aktualis = feladatok.osztok_szama(parameter)
        elvart = None
        self.assertEqual(elvart, aktualis, str(parameter)+" osztóinak számát rosszul határozta meg!")
    def test_feladat04(self):
        parameter=2
        aktualis = feladatok.osztok_szama(parameter)
        elvart = 2
        self.assertEqual(elvart, aktualis, str(parameter)+" osztóinak számát rosszul határozta meg!")
    def test_feladat05(self):
        parameter=3
        aktualis = feladatok.osztok_szama(parameter)
        elvart = 3
        self.assertEqual(elvart, aktualis, str(parameter)+" osztóinak számát rosszul határozta meg!")
    def test_feladat06(self):
        parameter=6
        aktualis = feladatok.osztok_szama(parameter)
        elvart = 4
        self.assertEqual(elvart, aktualis, str(parameter)+" osztóinak számát rosszul határozta meg!")
    def test_feladat07(self):
        parameter=7
        aktualis = feladatok.osztok_szama(parameter)
        elvart = 2
        self.assertEqual(elvart, aktualis, str(parameter)+" osztóinak számát rosszul határozta meg!")
    def test_feladat07(self):
        parameter=7
        aktualis = feladatok.osztok_szama(parameter)
        elvart = 4
        self.assertEqual(elvart, aktualis, str(parameter)+" osztóinak számát rosszul határozta meg!")
    def test_feladat12(self):
        parameter=12
        aktualis = feladatok.osztok_szama(parameter)
        elvart = 6
        self.assertEqual(elvart, aktualis, str(parameter)+" osztóinak számát rosszul határozta meg!")
    def test_feladat12(self):
        parameter=60
        aktualis = feladatok.osztok_szama(parameter)
        elvart = 12
        self.assertEqual(elvart, aktualis, str(parameter)+" osztóinak számát rosszul határozta meg!")