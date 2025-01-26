import tkinter as tk

def create_form(on_generate_tex, on_generate_pdf):
    # Create the main Tkinter window
    top = tk.Tk()
    top.title("Cover Letter Generator")

    # Center the window on the screen
    window_width = 600
    window_height = 400
    screen_width = top.winfo_screenwidth()
    screen_height = top.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    top.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Define variables for form inputs
    company_var = tk.StringVar()
    role_var = tk.StringVar()
    url_var = tk.StringVar()
    city_var = tk.StringVar()
    country_var = tk.StringVar()
    timestamp_var = tk.BooleanVar(value=False)  # Checkbox for timestamp (default: False)
    cleanup_var = tk.BooleanVar(value=True)    # Checkbox for cleanup (default: True)
    placeholder_var = tk.BooleanVar(value=False)  # Checkbox for placeholders

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

    # Checkboxes for additional options
    tk.Checkbutton(top, text="Filename with timestamp", variable=timestamp_var).pack(pady=5)
    tk.Checkbutton(top, text="Delete LaTeX log and auxiliary files", variable=cleanup_var).pack(pady=5)
    tk.Checkbutton(top, text="Use STARSWARS placeholders", variable=placeholder_var).pack(pady=5)

    # Buttons to trigger actions
    generate_tex_button = tk.Button(
        top, 
        text="Generate LaTeX files", 
        command=lambda: on_generate_tex(
            company_var, 
            role_var, 
            city_var, 
            country_var, 
            timestamp_var, 
            url_var, 
            placeholder_var
        )
    )
    generate_tex_button.pack(padx=20, pady=10)

    generate_pdf_button = tk.Button(
        top, 
        text="Generate PDF", 
        command=lambda: on_generate_pdf(cleanup_var), 
        state=tk.DISABLED  # Initially disabled until .tex is generated
    )
    generate_pdf_button.pack(padx=20, pady=10)

    # Return the window and PDF button
    return top, generate_pdf_button
