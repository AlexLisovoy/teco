"""
A TermsCounter class holds a large number of terms and computes the number of
occurrences of each term in a large ASCII text.
"""


__all__ = ('TermsCounter',)


class TermsCounter:

    """
    The main class
    """

    def __init__(self, terms_list):
        """
        Constructor. Creates new TermsCounter instance from a list of terms.
        """
        self.terms_list = terms_list

    def _generate_pmt(self, term):
        """
        Generates partial match table for term.
        """
        len_term = len(term)
        pi = [0] * len_term  # prefix index
        k = 0
        for q in range(1, len_term):
            while k > 0 and term[k] != term[q]:
                k = pi[k - 1]
            if term[k] == term[q]:
                k = k + 1
            pi[q] = k
        return pi

    def _count_occurrences(self, text, term):
        """
        Implement Knuth-Morris-Pratt Algorithm with modifications:
         - search terms
         - search sequence of terms
         - search sequence separated by any number of space-like characters
         - search sequence separated by only one newline characters
         - search is not case sensitive
        """
        len_text = len(text)
        term_len = len(term)
        words = 0
        k = 0
        # we need store previous symbol to determine when starting the
        # word or sequence of newline
        prev_el = ''
        #  partial match table
        pmt = self._generate_pmt(term)
        # lower char
        lower_char = lambda c: chr(ord(c) + 32) if c.isupper() else c

        for i in range(len_text):
            char = lower_char(text[i])
            while k > 0 and term[k] != char:
                if term[k - 1] == char == " ":
                    break
                if char == "\n" and prev_el != char:
                    char = " "
                    break
                k = pmt[k - 1]
            if term[k] == char:
                if (not prev_el or not prev_el.isalnum()) or k > 0:
                    k = k + 1
            if k == term_len:
                words += 1
                # we should reset k to avoid overlaps
                # need to check, maybe we can use only suffix for
                # generating partial match table
                k = 0

            prev_el = lower_char(text[i])

        return words

    def get_terms(self):
        """
        Get a list of terms, in the same order as specified
        when constructing the object.
        """
        for terms in self.terms_list:
            yield terms

    def compute_occurrences_count(self, text):
        """
        Computes the number of occurrences of each term in a text.

        Returns a list of computed number of occurrences, in the same order as
        specified when constricting the object.

        This function should not change the state of the object.  This ensures
        that one object may be reused to compute occurrences in several texts.
        """
        yield from (self._count_occurrences(text, t) for t in self.get_terms())
