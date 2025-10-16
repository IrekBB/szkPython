import unittest

# Definicja testowanej funkcji
def funkcja_silni(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * funkcja_silni(n - 1)


class TestSilnia(unittest.TestCase):
    """
    Klasa testowa, dziedzicząca po klasie TestCase z modułu unittest.
    Zawiera testy weryfikujące poprawność działania funkcji silni.
    """

    def test_silnia_dodatnie(self):
        """ Sprawdź wynik silni dla liczby dodatniej >= 2. """
        self.assertEqual(funkcja_silni(5), 120, "Powinno być: 120")

    def test_silnia_ujemne(self):
        """ Sprawdź wynik silni dla liczby ujemnej. """
        self.assertEqual(funkcja_silni(-5), None, "Powinno być: None")

    def test_silnia_0(self):
        """ Sprawdź wynik silni dla liczby dodatniej, mniejszej niż 2
        """
        self.assertEqual(funkcja_silni(0), 1, "Powinno być: 1")

    def test_silnia_string(self):
        """ Sprawdź błąd funkcji silni dla wprowadzenia stringa. """
        self.assertRaises(TypeError, funkcja_silni, "0")


if __name__ == '__main__':
    unittest.main