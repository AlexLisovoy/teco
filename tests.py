import unittest
from teco.terms_counter import TermsCounter


class TecoTestCase(unittest.TestCase):

    def setUp(self):
        self.terms = ["is", "example term", "a term",
                      "this this", "computer science"]

        self.counter = TermsCounter(self.terms)

    def test_term_counting(self):
        counter = TermsCounter(["is", "example term"])
        answer = counter.compute_occurrences_count(
            "This is an example term")

        self.assertEqual((1, 1,), tuple(answer))

    def test_text_with_no_terms(self):
        counter = TermsCounter(["xterm"])
        answer = counter.compute_occurrences_count(
            "This is a term.")

        self.assertEqual((0,), tuple(answer))

    def test_terms_overlaps(self):
        counter = TermsCounter(["this this"])
        answer = counter.compute_occurrences_count(
            "This this this this")

        self.assertEqual((2,), tuple(answer))

    def test_case_sensitive_counting(self):
        text = "ALICE.Alice.alice"
        counter = TermsCounter(["alice"])

        self.assertEqual((3,), tuple(counter.compute_occurrences_count(text)))

    def test_terms_counting_with_new_line(self):
        text = "computer\nscience,computer\n\nscience"
        counter = TermsCounter(["computer science"])

        self.assertEqual((1,), tuple(counter.compute_occurrences_count(text)))

    def test_multiple_spaces(self):
        counter = TermsCounter(["computer science"])
        text = """computer    science is the scientific and practical
                  approach to computation and its applications"""
        self.assertEqual((1,), tuple(counter.compute_occurrences_count(text)))
