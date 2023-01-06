big_title = "Morphological arrhythmias systems"
headers = ["Author", "Performance", "Database", "Classes"]
data = [
    ["Raj and Ray (2018)", "Acc 0.963 \n F1 0.7606", "MIT-BIH", "16"],
    ["Mousavi and Afghah(2019)", "Acc  0.9992", "MIT-BIH", "6"],
    ["Sellami and Hwang (2018)", "F1  0.897", "MIT-BIH", "6"],
    ["Strodthoff et al. (2021).", "AUC  0.896", "MIT-BIH", "6"],
]

res = f'\\begin{{tabular}}{{{"".join(["|p{3cm}|" for i in range(len(headers))])}}} '
res += f'\n\hline \n'
res += f'\multicolumn{{{len(headers)}}}{{|c|}}{{\\textbf{{{big_title}}}}} \\\\ '
res += f'\n\hline \n'
headers = ["\\textbf{" + header + "}" for header in headers]
res += f'{" & ".join(headers)} \\\\ \n'
res += f'\hline \n'

for i, row in enumerate(data):
    v = ['\parbox[t]{3cm}{' + item.replace("\n", "\\\\") + '}' for item in row]
    res+= f'{" & ".join(v)}'
    res+= f' \\\\ \hline \n'

res += f'\\end{{tabular}}'

print(res)
