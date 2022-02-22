from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestTokeletesSzamE(TestCase):
    def test_feladat01(self):
        parameter=1
        aktualis = feladatok.tokeletes_e(parameter)
        elvart = 1
        self.assertEqual(elvart, aktualis, str(parameter)+" tökéletességét nem jól határozta meg!")
    def test_feladat02(self):
        parameter=0
        aktualis = feladatok.tokeletes_e(parameter)
        elvart = None
        self.assertEqual(elvart, aktualis, str(parameter)+" tökéletességét nem jól határozta meg!")
    def test_feladat03(self):
        parameter=-5
        aktualis = feladatok.tokeletes_e(parameter)
        elvart = None
        self.assertEqual(elvart, aktualis, str(parameter)+" tökéletességét nem jól határozta meg!")
    def test_feladat04(self):
        parameter=2
        aktualis = feladatok.tokeletes_e(parameter)
        elvart = False
        self.assertEqual(elvart, aktualis, str(parameter)+" tökéletességét nem jól határozta meg!")
    def test_feladat05(self):
        parameter=5
        aktualis = feladatok.tokeletes_e(parameter)
        elvart = False
        self.assertEqual(elvart, aktualis, str(parameter)+" tökéletességét nem jól határozta meg!")
    def test_feladat06(self):
        parameter=6
        aktualis = feladatok.tokeletes_e(parameter)
        elvart = True
        self.assertEqual(elvart, aktualis, str(parameter)+" tökéletességét nem jól határozta meg!")
    def test_feladat12(self):
        parameter=12
        aktualis = feladatok.tokeletes_e(parameter)
        elvart = False
        self.assertEqual(elvart, aktualis, str(parameter)+" tökéletességét nem jól határozta meg!")
    def test_feladat28(self):
        parameter=12
        aktualis = feladatok.tokeletes_e(parameter)
        elvart = True
        self.assertEqual(elvart, aktualis, str(parameter)+" tökéletességét nem jól határozta meg!")
    def test_feladat56(self):
        parameter=56
        aktualis = feladatok.tokeletes_e(parameter)
        elvart = False
        self.assertEqual(elvart, aktualis, str(parameter)+" tökéletességét nem jól határozta meg!")