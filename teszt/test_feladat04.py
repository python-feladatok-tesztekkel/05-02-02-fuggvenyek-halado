from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TesPrimszamE(TestCase):
    def test_feladat01(self):
        parameter=1
        aktualis = feladatok.primszam_e(parameter)
        elvart = False
        self.assertEqual(elvart, aktualis,  str(parameter)+" esetén a primszámteszt nem jól működik")
    def test_feladat02(self):
        parameter=0
        aktualis = feladatok.primszam_e(parameter)
        elvart = None
        self.assertEqual(elvart, aktualis,  str(parameter)+" esetén a primszámteszt nem jól működik")
    def test_feladat03(self):
        parameter=-10
        aktualis = feladatok.primszam_e(parameter)
        elvart = None
        self.assertEqual(elvart, aktualis,  str(parameter)+" esetén a primszámteszt nem jól működik")
    def test_feladat04(self):
        parameter=2
        aktualis = feladatok.primszam_e(parameter)
        elvart = True
        self.assertEqual(elvart, aktualis,  str(parameter)+" esetén a primszámteszt nem jól működik")
    def test_feladat05(self):
        parameter=3
        aktualis = feladatok.primszam_e(parameter)
        elvart = True
        self.assertEqual(elvart, aktualis,  str(parameter)+" esetén a primszámteszt nem jól működik")
    def test_feladat05(self):
        parameter=4
        aktualis = feladatok.primszam_e(parameter)
        elvart = False
        self.assertEqual(elvart, aktualis,  str(parameter)+" esetén a primszámteszt nem jól működik")
    def test_feladat06(self):
        parameter=6
        aktualis = feladatok.primszam_e(parameter)
        elvart = False
        self.assertEqual(elvart, aktualis,  str(parameter)+" esetén a primszámteszt nem jól működik")
    def test_feladat07(self):
        parameter=7
        aktualis = feladatok.primszam_e(parameter)
        elvart = True
        self.assertEqual(elvart, aktualis,  str(parameter)+" esetén a primszámteszt nem jól működik")
    def test_feladat15(self):
        parameter=15
        aktualis = feladatok.primszam_e(parameter)
        elvart = False
        self.assertEqual(elvart, aktualis,  str(parameter)+" esetén a primszámteszt nem jól működik")
    def test_feladat101(self):
        parameter=101
        aktualis = feladatok.primszam_e(parameter)
        elvart = True
        self.assertEqual(elvart, aktualis,  str(parameter)+" esetén a primszámteszt nem jól működik")
    def test_feladat129(self):
        parameter=129
        aktualis = feladatok.primszam_e(parameter)
        elvart = False
        self.assertEqual(elvart, aktualis,  str(parameter)+" esetén a primszámteszt nem jól működik")
    def test_feladat131(self):
        parameter=131
        aktualis = feladatok.primszam_e(parameter)
        elvart = True
        self.assertEqual(elvart, aktualis,  str(parameter)+" esetén a primszámteszt nem jól működik")