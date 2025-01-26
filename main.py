import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess
import time

from generate_tex import generate_tex
from generate_pdf import generate_pdf
from cleanup_folder import cleanup_folder

# Helper function to check for empty or None values
def get_default_value(value, default_value):
    return value.strip() if value and value.strip() else default_value

def on_generate_tex():

    # Get the actual values from the Tkinter StringVars
    company = get_default_value(company_var.get(), "R2-D2 TECHNOLOGIES, LTD.").upper()
    role = get_default_value(role_var.get(), "ASTROMECH DROID ENGINEER").upper()
    city = get_default_value(city_var.get(), "CORUSCANT,").upper()
    country = get_default_value(country_var.get(), "GALACTIC REPUBLIC").upper()
    url = get_default_value(url_var.get(), "https://www.esa.int/About_Us/Careers_at_ESA/Apply_now_to_become_an_ESA_astronaut")

    filename_with_timestamp = timestamp_var.get()

    # Generate the .tex file with the user inputs (updated function call)
    tex_file_path = generate_tex(company, role, city, country, filename_with_timestamp, url)  # Corrected to use user inputs

    # Save the tex file path globally for later use (e.g., PDF generation)
    global tex_file
    tex_file = tex_file_path

    # Enable the "Generate PDF" button after generating .tex
    generate_pdf_button.config(state=tk.NORMAL)

def on_generate_pdf():
    if tex_file:
        # Generate the PDF
        generate_pdf(tex_file)

        if cleanup_var.get():
            # Perform cleanup automatically after PDF generation
            cleanup_folder()
            messagebox.showinfo("Success", "PDF generated and temporary files cleaned up!")
    else:
        messagebox.showwarning("Error", "No .tex file found. Please generate it first.")

top = tk.Tk()
top.title("Cover Letter Generator")

# Center the window on the screen
window_width = 600
window_height = 400
screen_width = top.winfo_screenwidth()
screen_height = top.winfo_screenheight()

# Calculate position for the window to be centered
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
top.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Define variables
company_var = tk.StringVar()
role_var = tk.StringVar()
url_var = tk.StringVar()
city_var = tk.StringVar()
country_var = tk.StringVar()

# Create labels and entry fields with padding
tk.Label(top, text="Company").pack(padx=20)
tk.Entry(top, textvariable=company_var).pack(padx=20)
tk.Label(top, text="Role").pack(padx=20)
tk.Entry(top, textvariable=role_var).pack(padx=20)
tk.Label(top, text="URL").pack(padx=20)
tk.Entry(top, textvariable=url_var).pack(padx=20)
tk.Label(top, text="City").pack(padx=20)
tk.Entry(top, textvariable=city_var).pack(padx=20)
tk.Label(top, text="Country").pack(padx=20)
tk.Entry(top, textvariable=country_var).pack(padx=20)

# Checkbox for adding timestamp to filename
# This initializes the checkbox state to unchecked (False)
timestamp_var = tk.BooleanVar(value=False)  
tk.Checkbutton(top, text="Filename with timestamp", variable=timestamp_var).pack(pady=10)

# Checkbox for deleting all LaTeX log and auxiliary files
# This initializes the checkbox state to checked (True)
cleanup_var = tk.BooleanVar(value=True)
tk.Checkbutton(top, text="Delete LaTeX log and auxiliary files", variable=cleanup_var).pack(pady=10)

# Buttons with padding
tk.Button(top, text="Generate LaTeX files", command=on_generate_tex).pack(padx=20, pady=10)
generate_pdf_button = tk.Button(top, text="Generate PDF", command=on_generate_pdf, state=tk.DISABLED)
generate_pdf_button.pack(padx=20, pady=10)

# Initialize tex_file variable
tex_file = None

top.mainloop()
