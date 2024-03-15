import subprocess
import os
from latexgen import generate_latex_table, generate_image_latex, complete_latex_file

def generate_pdf_from_latex(latex_filename, output_dir):
    os.chdir(output_dir)
    
    try:
        subprocess.run(["pdflatex", "-interaction=batchmode", latex_filename], check=True)
        print("PDF generated successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error generating PDF: {e}")


def save_latex_to_file(latex_code, filename):
    with open(filename, 'w') as file:
        file.write(latex_code)




def main():
    data = [
        [".0 1 2 3", "4 5 6", "7 8 9"],
        ["10 11 12", "13 14", "15 16"],
        ["17 18 19 ", "20 21", "22 23"]
    ]
    latex_table = generate_latex_table(data)
    # print(latex_table)

    image_filename = "../test_samples/label.png"  
    image_latex = generate_image_latex(image_filename)
    # print(image_latex)

    whole_latex = complete_latex_file(latex_table, image_latex)
    # print(whole_latex)


    latex_filename = '../output/table_with_picture.tex'

    save_latex_to_file(whole_latex, latex_filename)

    generate_pdf_from_latex(latex_filename, '../output')



if __name__ == "__main__":
    main()
