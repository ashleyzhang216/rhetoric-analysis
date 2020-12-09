from text_parser import parse_texts, export_single_result
from comparative import export_comparative_results

politicians = ['Joe Biden', 'Bernie Sanders']
results = []
total_words = []

for i, pol in enumerate(politicians):
    results.append({})
    r, t = parse_texts(results[i], 'data/' + pol + '/', '--Start of Text--', 'data/extra_words.txt', 'data/extra_removes.txt', False, 0.001)
    export_single_result('results/' + pol + ' Results.txt', r, t)

    total_words.append(t)

export_comparative_results('data/compare_words.txt', 'results/Comparative Results.txt', politicians, results, total_words)
print('Parsing of ' + str(sum(total_words)) + ' words from ' + str(len(politicians)) + ' speakers complete.')
