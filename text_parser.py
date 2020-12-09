import os
import re


def parse_file(filepath, header):
    """
    :param filepath: str
        file path of the .txt file to be read
    :param header: str
        header within the .txt file that indicates start of the data
        for all provided data, this is '--Start of Text--'
    :return: str
        data in .txt as a str
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        data_raw = file.read()

        data_raw = data_raw[data_raw.index(header) + len(header) + 1 : ]
        regex = re.compile('[,/\.!?$\n“”]')
        data_raw = regex.sub(' ', data_raw)
        data_clean = data_raw.lower()

        file.close()
        return data_clean


def analyze_data(word_count, data, extra_filepath):
    """
    :param word_count: dict
        dictionary to write word frequency data in
    :param data: str
        source str data to be analyzed
    :param extra_filepath:
        file path of .txt file containing extra words to include in frequency analysis
    :return: int
        total number of words in str data that were read
    """
    data_by_word = data.split()
    for word in data_by_word:
        if word.isnumeric():
            word = 'NUMBER'
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    with open(extra_filepath, 'r', encoding='utf-8') as file:
        for word in file.readlines():
            w = word.strip('\n')
            if w in word_count:
                word_count[w] += data.count(w)
            else:
                word_count[w] = data.count(w)

    return len(data_by_word)


def remove_fillers(word_count, filepath, extra_filepath):
    """
    :param word_count: dict
        dictionary to write word frequency data in
    :param filepath: str
        filepath of .txt file containing words to remove from word_count
        for given data, this is a list of prepositions found at:
        https://www.scrapmaker.com/download/data/wordlists/language/prepositions.txt
    :param extra_filepath:
        filepath of .txt file containing extra words to remove from word_count
    :return: none
    """
    prepositions = open(filepath, 'r', encoding='utf-8')
    extra_removes = open(extra_filepath, 'r', encoding='utf-8')

    for word in prepositions.readlines() + extra_removes.readlines():
        w = word.strip('\n')
        if w in word_count:
            del word_count[w]

    prepositions.close()
    extra_removes.close()


def print_results(results, threshold, total_words, extra_filepath):
    """
    Used for testing only. Should not be called in a normal run of the program
    :param results: dict
        word_count, whose information is to be printed to console
    :param threshold: float
        minimum frequency threshold expressed as a decimal for words/phrases to be printed
    :param total_words: int
        total number of words read whose data is in word_count
    :param extra_filepath: str
        filepath of .txt file including extra words/phrases to printed
    :return: none
    """
    extra_display = open(extra_filepath, 'r', encoding='utf-8')
    extra_list = extra_display.readlines()
    for entry in sorted(results, key=results.get, reverse=True):
        if results[entry] >= threshold or entry in extra_list:
            print(entry, 10000*round(results[entry]/total_words, 6) )
    extra_display.close()


def parse_texts(word_count, datapath, header, extra_words_filepath, remove_words_filepath, display, display_threshold):
    """
    The main function that calls most other methods in this file. 
    Called in main.py
    :param word_count: dict
        Empty dictionary passed by main.py to store word frequency data in
    :param datapath: str
        File path of the directory containing raw txt files to be parsed
    :param header: str
        String seperating header and text in each file, which is '--Start of Text--'
    :param extra_words_filepath: str
        File path of the txt file containing other words to add to the analysis
    :param remove_words_filepath: str
        File path of the txt file containing other words to remove from the analysis
    :param display: bool
        True: prints the results of the analysis following completion of parsing
        False: nothing
        Used for testing only
    :param display_threshold: float
        Threshold for frequency of words to be displayed in analysis. In decimal form
        ex: 0.001 corresponds to 0.1% usage
    :return: dict, int
        Returns dictionary containing results of analysis, total words of text processed
    """

    word_count.clear()
    total_words = 0

    for filename in os.listdir(datapath):
        if filename.endswith(".txt"):
            total_words += analyze_data(word_count, parse_file(datapath + filename, header), extra_words_filepath)

    remove_fillers(word_count, 'data/prepositions.txt', remove_words_filepath)
    if display:
        print_results(word_count, display_threshold*total_words, total_words, extra_words_filepath)

    return word_count, total_words


def export_single_result(filepath, results, total_words):
    """
    Writes results from a single speaker into a new .txt file. 
    Independent of other methods in this file. 
    Called by main.py
    :param filepath: str
        filepath of new .txt to be created and written to
    :param results: dict
        dictionary (word_count resulting from a previous execution of parse_texts()) whose results are to be written
    :param total_words: int
        total number of words read to get results. 
        used to write to the new .txt file the frequency of each word/phrase as average uses per 10,000 words
    :return: none
    """
    new_file = open(filepath, 'w')
    new_file.write('Word/Phrase_Uses per 10,000 words\n')

    for entry in sorted(results, key=results.get, reverse=True):
        new_file.write(entry + '_' + str(round(10000*results[entry]/total_words, 2)) + '\n')

    new_file.close()
