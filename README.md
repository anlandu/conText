# HistText

## Objective
A library dedicated to downloading, analyzing, and comparing well-known texts on Project Gutenberg using natural language processing.

## Use
`pip install git+https://github.com/anlandu/histtext`

Run `scripts/GetGut.py` to get the top 100 books on Project Gutenberg from the past 30 days
as text files.

Run  `scripts/GetBookFromURL.py` to get the text file of a specific book from Project Gutenberg.
Takes string as command-line argument: the URL of the root directory of the book. e.g. http://www.gutenberg.org/ebooks/4300

Import `src.AvgWordLen`, `src.AvgSentLen`, or `src.FreqPOS` to use their methods. AvgWordLen enables you to get the average word length of a given file, or all files in the resources folder, or compare all stored word lengths to an inputted one. AvgSentLen does the same for sentence lengths. FreqPOS counts the number of times each part of speech is used in a text.

(Note that these three files assume the top 100 books are already downloaded using `GetGut.py`; alternatively, you can simply download your own texts of choice into the resources folder.)

## Contributing
Contributions are more than welcome! Please see the  [CONTRIBUTING.md](CONTRIBUTING.md) to learn how to contribute. Check out issues for some starting points!

## LICENSE
This project is licensed under the [MIT License](LICENSE).
