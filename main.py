import os
import subprocess
import tkinter as tk
from tkinter import messagebox

from generate_form import generate_form
from generate_tex import generate_tex
from generate_pdf import generate_pdf
from cleanup_folder import cleanup_folder

# Helper function to check for empty or None values
def get_default_value(value, default_value):
    return value.strip() if value and value.strip() else default_value

def on_generate_tex(company_var, role_var, url_var, city_var, country_var, color_var, filename_var):
    FILENAME = filename_var.get()
    COLOR = color_var.get()

    # Get values from Tkinter StringVars
    company = company_var.get()
    role = role_var.get()
    city =city_var.get()
    country = country_var.get()
    url = url_var.get()

    # Generate .tex file and return its path
    tex_file_path = generate_tex(company, role, url, city, country, COLOR, FILENAME)
    
    # Update the tex_file variable in the main function
    global tex_file
    tex_file = tex_file_path

    # Enable the "Generate PDF" button after .tex file is generated
    generate_pdf_button.config(state=tk.NORMAL)

def on_generate_pdf(cleanup_var):
    
    DO_CLEANUP = cleanup_var.get()

    if tex_file:
        # Generate the PDF from the .tex file
        generate_pdf(tex_file)

        if DO_CLEANUP:
            # Clean up temporary files
            cleanup_folder(delete_folder=True)
            messagebox.showinfo("Success", "PDF generated and temporary files cleaned up!")
    else:
        messagebox.showwarning("Error", "No .tex file found. Please generate it first.")

# Create the GUI and run the application
if __name__ == "__main__":
    # Initialize tex_file variable
    tex_file = None

    # Create the form and pass necessary functions
    form, generate_pdf_button = generate_form(on_generate_tex, on_generate_pdf)

    # Run the Tkinter event loop
    form.mainloop()
