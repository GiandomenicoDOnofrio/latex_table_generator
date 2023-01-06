big_title = "Big title"
headers = ["header 1", "header 2", "header 3", "header 4"]
data = [
    ["Data 1", "Data 2", "3", "Data 4"],
    ["Data 1", "Data 2", "3", "Data 4"],
]

res = f'\\begin{{tabular}}{{{"".join(["|p{3cm}|" for i in range(len(headers))])}}} \n\hline \n\multicolumn{{{len(headers)}}}{{|c|}}{{{big_title}}} \\\\ \n\hline \n{" & ".join(headers)} \\\\ \n\hline \n'

for i, row in enumerate(data):
    res+= f'{" & ".join(row)}'
    res+= f' \\\\ \hline \n'

res += f'\\end{{tabular}}'
print(res)
