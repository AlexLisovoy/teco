# teco
The tool that finds N most frequently occurring terms in all files containing text.

A `term` is a sequence of words (made of alphanumeric characters, as defined by
the isalpha() function) separated by spaces.

A `text` is a sequence of words separated by non-alphanumeric characters.

A term occurs in a text if all of its words are found in the text in the same
sequence separated by any number of space-like characters (as defined by the
isspace() function), but not paragraph breaks (a newline followed by another
newline, "\n\n"). The comparison of words is case-insensitive.

If several different terms overlap in a text, an occurrence is counted for all
of the overlapping terms. However, a term that overlaps with itself should not
be double-counted.

For example, the term "Computer science" occurs in a text "computer science",
"computer   science" and "computer\nscience" but neither in "computer, science"
nor in "computer\n\nscience".

## Installation

    $ pip install git+https://github.com/AlexLisovoy/teco.git

## Usage

    $ teco path_to_terms.txx folder_with_text


## Run tests

Use:

    $ make test

to run tests. The command at first will run the flake8 tool.

On flake8 success the tests will be run.


## Tests coverage

Use:

    $ make cov

to run tests and collect coverage information. Once the command finishes it will output link to index page.


## License
``teco`` is offered under the MIT license.
