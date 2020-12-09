Author: Ashley Zhang
Github: ashleyzhang216

This project is a parser that finds numerical frequencies of words used in sample texts of multiple speakers for later analysis.
The current configuration reads sample speeches of Joe Biden and Bernie Sanders that are about climate change. 

Created as part of the final paper in STS 1101 at Cornell University.

Structure of project:
> main.py
    - run to execute the program
    - each str in array politicians corresponds to a directory in data/ including texts from a unique speaker
> text_parser.py
    - contains methods used by main.py to read, parse texts, and write results from an individual source
> comparative_analysis.py
    - contains methods used by main.py to compare and write results from multiple sources
> data
    - directory that contains data used by text_parser.py
    > prepositions.txt
        - contains common words to be removed from frequency analysis
    > extra_words.txt
        - contains words/phrases entered by user to be added to frequency analysis
    > extra_removes.txt
        - contains other words, separated by new lines, entered by user to also be removed from frequency analysis
    > compare_words.txt
        - contains words/phrases entered by user to be compared between all results in comparative_analysis.py
    > Joe Biden
        - contains sample data of Joe Biden's climate change speeches
    > Bernie Sanders
        - contains sample data of Bernie Sanders' climate change speeches
> results
    > Joe Biden Results.txt
        - contains results of frequency analysis of the sample data of Joe Biden
    > Bernie Sanders Results.txt
        - contains results of frequency analysis of the sample data of Bernie Sanders
    > Comparative Results.txt
        - contains results of comparative frequency analysis of the sample data of Joe Biden and Bernie Sanders

How to use data:
- Data is organized in .txt files in directories corresponding to different speakers in the data directory
- Each file must contain a header separating documenting information and the text, for the sample data this is '--Start of Speech--'
- The documenting information is not mandatory for proper code function (the header, however, is), but may be useful

How to use results:
- Import .txt files in results folder into Google Sheets, and select '_' as the separator type.
- Results are organized as a column of words/phrases and a column(s) of use frequency, in average uses per 10,000 words.