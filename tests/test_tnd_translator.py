import unittest

from tnd_translator.translator import translate


class TestTndTranslator(unittest.TestCase):
    def test_frenchToEnglish(self):
        a = translate("bonjour", from_lang_code2="en", to_lang_code2="fr")
        trans_text = ""
        if len(a) > 0:
            trans_text = a[0]['translation'].lower()

        self.assertEqual(trans_text, "hello")
        self.assertNotEqual(trans_text, "hello1")


    def test_englishToFrench(self):
        a = translate("Hello", from_lang_code2="en", to_lang_code2="fr")
        trans_text = ""
        if len(a) > 0:
            trans_text = a[0]['translation'].lower()

        self.assertEqual(trans_text, "bonjour")
        self.assertNotEqual(trans_text, "bonjour1")


if __name__ == '__main__':
    unittest.main()
