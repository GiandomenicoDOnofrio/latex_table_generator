
res = "\\documentclass{{article}} \n\\usepackage{{array}} \n\\usepackage[table]{{xcolor}} \n\\setlength{\\tabcolsep}{15pt} \n\\renewcommand{\\arraystretch}{2.5} \n\\addtolength{\\oddsidemargin}{-.875in} \n\\addtolength{\\evensidemargin}{-.875in} \n\\addtolength{\\textwidth}{1.75in} \n\\addtolength{\\topmargin}{-.875in} \n\\addtolength{\\textheight}{1.75in} \n\\begin{document}"


column_width = "2"
no_char = " "
big_title = "Morphological arrhythmias systems"
headers = ["Author", "Performance", "Database", "Classes", "Model"]
data = [
    ["Raj and Ray (2018)", "ACC 0.963 \n F1 0.7606", "MIT-BIH", "16", "SVM"],
    ["Mousavi and Afghah(2019)", "ACC  0.9992", "MIT-BIH", "6", "CNN \n RNN"],
    ["Sellami and Hwang (2018)", "F1  0.897", "MIT-BIH", "6", "CNN \n batch weighted loss"],
    ["Strodthoff et al. (2021)", "AUC  0.896", "MIT-BIH", "6", "Residual NN (xresnet)"],
    ["Yao et al. (2018)", "ACC 0.812", "CPSC 2018", "8", "CNN \n LSTM \n Attention"],
]

res += f'\\begin{{tabular}}{{{"".join([f"|p{{{column_width}cm}}|" for i in range(len(headers))])}}} '
res += f'\n\hline \n'
res += f'\multicolumn{{{len(headers)}}}{{|c|}}{{\\textbf{{{big_title}}}}} \\\\ '
res += f'\n\hline \n'
headers = ["\\textbf{" + header + "}" for header in headers]
res += f'{" & ".join(headers)} \\\\ \n'
res += f'\hline \n'

for i, row in enumerate(data):
    v = [f'\parbox[t]{{{column_width}cm}}' + '{ ' + item.replace("\n", "\\\\") + f' \\\\ {no_char}' + ' }' for item in row]
    res+= f'{" & ".join(v)}'
    res+= f' \\\\ \hline \n'

res += f'\\end{{tabular}} \n \\end{{document}}'


print(res)
