import os
import subprocess
from tkinter import messagebox
import shutil

def generate_pdf(tex_file):
    if not tex_file:
        messagebox.showerror("Error", "Please generate the LaTeX file first.")
        return

    # Get the directory of the tex file and calculate the output PDF file path
    tex_dir = os.path.dirname(tex_file)
    parent_dir = os.path.dirname(tex_dir)
    pdf_output_dir = os.path.join(parent_dir, "pdf")

    # Generate the PDF file
    pdf_output = tex_file.replace(".tex", ".pdf")  # PDF file path in the same directory as tex file
    command = f"xelatex -synctex=1 -interaction=nonstopmode -output-directory={tex_dir} --shell-escape {tex_file}"
    subprocess.run(command, shell=True, check=True)
    subprocess.run(command, shell=True, check=True)  # Second pass to resolve cross-references

    # Ensure the 'pdf' folder exists in the parent directory
    if not os.path.exists(pdf_output_dir):
        os.makedirs(pdf_output_dir)

    # Move the generated PDF to the 'pdf' folder in the parent directory
    pdf_filename = os.path.basename(pdf_output)
    moved_pdf_path = os.path.join(pdf_output_dir, pdf_filename)

    try:
        shutil.move(pdf_output, moved_pdf_path)
        #messagebox.showinfo("Success", f"PDF generated and moved to {moved_pdf_path}")
        print(f"PDF saved to: {moved_pdf_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to move PDF: {e}")
        print(f"Error moving PDF: {e}")
