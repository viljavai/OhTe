import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
    
    def test_konstruktori_toimii(self):
        self.assertEqual(str(self.kassa), "Kassassa on rahaa 1000 euroa, edullisia myyty 0, maukkaita myyty 0")

    def test_edullisesti_kateinen_toimii_riittava(self):
        self.kassa.syo_edullisesti_kateisella(250)
        self.assertEqual(str(self.kassa), "Kassassa on rahaa 1002.4 euroa, edullisia myyty 1, maukkaita myyty 0")
        assert self.kassa.syo_edullisesti_kateisella(250) == 10

    def test_edullisesti_kateinen_toimii_ei_riittava(self):
        self.kassa.syo_edullisesti_kateisella(230)
        self.assertEqual(str(self.kassa), "Kassassa on rahaa 1000 euroa, edullisia myyty 0, maukkaita myyty 0")
        assert self.kassa.syo_edullisesti_kateisella(230) == 230

    def test_maukkaasti_kateinen_toimii_riittava(self):
        self.kassa.syo_maukkaasti_kateisella(450)
        self.assertEqual(str(self.kassa), "Kassassa on rahaa 1004 euroa, edullisia myyty 0, maukkaita myyty 1")
        assert self.kassa.syo_edullisesti_kateisella(450) == 50

    def test_maukkaasti_kateinen_toimii_ei_riittava(self):
        self.kassa.syo_maukkaasti_kateisella(350)
        self.assertEqual(str(self.kassa), "Kassassa on rahaa 1000 euroa, edullisia myyty 0, maukkaita myyty 0")
        assert self.kassa.syo_edullisesti_kateisella(350) == 350