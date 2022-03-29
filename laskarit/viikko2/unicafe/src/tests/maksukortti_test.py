import unittest
from maksukortti import Maksukortti


class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.kortti), "saldo: 10.0")
    
    def test_lataus_toimii(self):
        self.kortti.lataa_rahaa(1000)
        self.assertEqual(str(self.kortti), "saldo: 20.0")

    def test_ottaminen_toimii_tarpeeksi(self):
        self.kortti.ota_rahaa(500)
        self.assertEqual(str(self.kortti), "saldo: 5.0")

    def test_ottaminen_toimii_ei_tarpeeksi(self):
        self.kortti.ota_rahaa(1005)
        self.assertEqual(str(self.kortti), "saldo: 10.0")
    
    def test_palauttaa_true(self):
        self.assertTrue(self.kortti.ota_rahaa(500))
    
    def test_palauttaa_false(self):
        self.assertFalse(self.kortti.ota_rahaa(1005))
