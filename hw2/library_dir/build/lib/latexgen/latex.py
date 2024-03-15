def generate_latex_table(data):
    def generate_table_row(row):
        return " & ".join(map(str, row)) + " \\\\"

    rows = map(generate_table_row, data)
    
    backslash_char = '\\'
    slash_n = '\n'
    separator = f'{slash_n}{backslash_char}hline{slash_n}'
    
    latex_code = f"""
{backslash_char}begin{{table}}[h!]
{backslash_char}centering
{backslash_char}begin{{tabular}}{{|{"c|" * len(data[0])}}}
{backslash_char}hline
{separator.join(rows)}
{backslash_char}hline
{backslash_char}end{{tabular}}
{backslash_char}end{{table}}
"""    

    return latex_code

def generate_image_latex(image_filename):
    image_latex = f"""
\\begin{{table}}[h!]
\\centering
\\begin{{tabular}}{{|c|}}
\\hline
\\includegraphics[width=0.8\\textwidth]{{"{image_filename}"}}
\\\\ \\hline
\\end{{tabular}}
\\end{{table}}
"""
    return image_latex

def complete_latex_file(table_latex, image_latex):
    whole_latex = f"""
\\documentclass{{article}}
\\usepackage{{graphicx}}

\\begin{{document}}

{table_latex}

{image_latex}

\\end{{document}}
"""
    return whole_latex