from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TesPrrimtenyezosFelbontas(TestCase):
    def test_feladat01(self):
        parameter=1
        aktualis = feladatok.primtenyezos_felbontas(parameter)
        elvart = None
        self.assertEqual(elvart, aktualis,  str(parameter)+" esetén a primtényezős felbtontást nem jól határozta meg!")
    def test_feladat02(self):
        parameter=2
        aktualis = feladatok.primtenyezos_felbontas(parameter)
        elvart = [2]
        self.assertEqual(elvart, aktualis,  str(parameter)+" esetén a primtényezős felbtontást nem jól határozta meg!")
    def test_feladat03(self):
        parameter=3
        aktualis = feladatok.primtenyezos_felbontas(parameter)
        elvart = [3]
        self.assertEqual(elvart, aktualis,  str(parameter)+" esetén a primtényezős felbtontást nem jól határozta meg!")
    def test_feladat04(self):
        parameter=4
        aktualis = feladatok.primtenyezos_felbontas(parameter)
        elvart = [2,2]
        self.assertEqual(elvart, aktualis,  str(parameter)+" esetén a primtényezős felbtontást nem jól határozta meg!")
    def test_feladat06(self):
        parameter=4
        aktualis = feladatok.primtenyezos_felbontas(parameter)
        elvart = [2,3]
        self.assertEqual(elvart, aktualis,  str(parameter)+" esetén a primtényezős felbtontást nem jól határozta meg!")
    def test_feladat09(self):
        parameter=9
        aktualis = feladatok.primtenyezos_felbontas(parameter)
        elvart = [3,3,3]
        self.assertEqual(elvart, aktualis,  str(parameter)+" esetén a primtényezős felbtontást nem jól határozta meg!")
    def test_feladat19(self):
        parameter=19
        aktualis = feladatok.primtenyezos_felbontas(parameter)
        elvart = [19]
        self.assertEqual(elvart, aktualis,  str(parameter)+" esetén a primtényezős felbtontást nem jól határozta meg!")
    def test_feladat24(self):
        parameter=19
        aktualis = feladatok.primtenyezos_felbontas(parameter)
        elvart = [2,2,2,3]
        self.assertEqual(elvart, aktualis,  str(parameter)+" esetén a primtényezős felbtontást nem jól határozta meg!")
    def test_feladat96(self):
        parameter=96
        aktualis = feladatok.primtenyezos_felbontas(parameter)
        elvart = [2 , 2 , 2 , 2 , 2 , 3]
        self.assertEqual(elvart, aktualis,  str(parameter)+" esetén a primtényezős felbtontást nem jól határozta meg!")
    def test_feladat300(self):
        parameter=300
        aktualis = feladatok.primtenyezos_felbontas(parameter)
        elvart = [2 , 2 , 3 , 5 , 5]
        self.assertEqual(elvart, aktualis,  str(parameter)+" esetén a primtényezős felbtontást nem jól határozta meg!")
    def test_feladat975(self):
        parameter=300
        aktualis = feladatok.primtenyezos_felbontas(parameter)
        elvart = [3 , 5 , 5 , 13]
        self.assertEqual(elvart, aktualis,  str(parameter)+" esetén a primtényezős felbtontást nem jól határozta meg!")