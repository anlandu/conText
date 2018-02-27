# HistText

## Objective
A library to download top texts from Project Gutenberg as text files, then analyze text in relation to these well-known novels and authors.

## Use
`pip install git+https://github.com/anlandu/histtext`
Run `scripts/GetGut.py` to get the top 100 books on Project Gutenberg from the past 30 days
as text files.

Run  `scripts/GetBookFromURL.py` to get the text file of a specific book from Project Gutenberg.
Takes string as command-line argument: the URL of the root directory of the book. e.g. http://www.gutenberg.org/ebooks/4300

Import `src.AvgWordLen`, `src.AvgSentLen`, or `src.FreqPOS` to use their respective methods. Note that these require the top 100 books to be downloaded already; alternatively, you can simply download your own texts of choice into the resources folder.

## Contributing
Contributions are more than welcome! Please see the  [CONTRIBUTING.md](CONTRIBUTING.md) to learn how to contribute.

## LICENSE
This project is licensed under the [MIT License](LICENSE).
