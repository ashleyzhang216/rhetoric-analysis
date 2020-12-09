def export_comparative_results(compare_filepath, new_filepath, politicians, results, totals):
    """
    Writes results from all speakers into a new .txt file.
    Called by main.py
    :param compare_filepath: str
        filepath of a .txt file containing words/phrases whose usage frequencies of all speakers is to be written
    :param new_filepath: str
        filepath of new .txt file to be created and written to
    :param politicians: array[str]
        array of strings
        each string is the name of a politician whose texts have been parsed
    :param results: array[dict]
        array of dictionaries
        each dictionary is the result of previous executions of parse_texts() in text_parser.py
        in the same order as politicians, i.e. index of this array corresponds to the politician in the same index
    :param totals: array[int]
        array of ints
        contains total words processed from each politician
        in the same order as politicians, i.e. index of this array corresponds to the politician in the same index
    :return: none
    """
    compare_words = open(compare_filepath, 'r',  encoding='utf-8')
    new_file = open(new_filepath, 'w')

    header_str = 'Word/Phrase_'
    for pol in politicians:
        header_str += pol + '_'
    header_str += '\n'
    new_file.write(header_str)

    for word in compare_words.readlines():
        w = word.strip('\n')
        new_line = w + '_'
        for i, r in enumerate(results):
            if w in r:
                new_line += str(round(10000*r[w]/totals[i], 2)) + '_'
            else:
                new_line += '0_'

        new_line += '\n'
        new_file.write(new_line)
