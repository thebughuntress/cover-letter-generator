import tkinter as tk
import time

# Default color value
DEFAULT_COLOR = "#333333"
DEFAULT_FILENAME = "coverletter"

def generate_form(on_generate_tex, on_generate_pdf):
    # Create the main Tkinter window
    root = tk.Tk()
    root.title("Cover Letter Generator")
    root.iconbitmap("images/favicon.ico")

    # Center the window on the screen
    window_width = 500
    window_height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Define variables for form inputs
    company_var = tk.StringVar()
    role_var = tk.StringVar()
    url_var = tk.StringVar()
    city_var = tk.StringVar()
    country_var = tk.StringVar()

    # Initialize the color variable with the default value
    color_var = tk.StringVar(value=DEFAULT_COLOR)
    filename_var = tk.StringVar(value=DEFAULT_FILENAME)
    timestamp_var = tk.BooleanVar(value=False)  # Checkbox for timestamp (default: False)
    cleanup_var = tk.BooleanVar(value=True)    # Checkbox for cleanup (default: True)
    placeholder_var = tk.BooleanVar(value=False)  # Checkbox for placeholders

    # Function to update company name based on checkbox state
    def update_entries():
        if placeholder_var.get():  # If the checkbox is checked
            company_var.set("R2-D2 TECHNOLOGIES, LTD.")
            role_var.set("ASTROMECH DROID ENGINEER")  
            city_var.set("CORUSCANT") 
            country_var.set("GALACTIC REPUBLIC")
            url_var.set("https://www.esa.int/About_Us/Careers_at_ESA")
            color_var.set("#1d146e")
        else:
            company_var.set("")  # Clear the company name if not checked
            role_var.set("")  # Clear role
            city_var.set("")  # Clear city
            country_var.set("")  # Clear country
            url_var.set("")  # Clear URL
            color_var.set(DEFAULT_COLOR)
            filename_var.set(DEFAULT_FILENAME)

    def update_filename():
        if timestamp_var.get():  # Check the actual checkbox variable
            timestamp = time.strftime("%Y%m%d_%H%M")
            filename = filename_var.get()
            filename_var.set(f"{filename}_{timestamp}")
        else:
            filename = filename_var.get().split('_20')[0]
            filename_var.set(filename)

    # CONTENT
    # Create a LabelFrame to group the inputs with a title
    frame_inputs = tk.LabelFrame(root, text="Job Posting", padx=10, pady=10)
    frame_inputs.pack(padx=10, pady=10, fill="both", expand=True)

    # Use grid layout to arrange labels and entry fields side by side
    tk.Label(frame_inputs, text="Company").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    tk.Entry(frame_inputs, textvariable=company_var, width=40).grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame_inputs, text="Role").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    tk.Entry(frame_inputs, textvariable=role_var, width=40).grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame_inputs, text="URL").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    tk.Entry(frame_inputs, textvariable=url_var, width=40).grid(row=2, column=1, padx=10, pady=5)

    tk.Label(frame_inputs, text="City").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    tk.Entry(frame_inputs, textvariable=city_var, width=40).grid(row=3, column=1, padx=10, pady=5)

    tk.Label(frame_inputs, text="Country").grid(row=4, column=0, padx=10, pady=5, sticky="w")
    tk.Entry(frame_inputs, textvariable=country_var, width=40).grid(row=4, column=1, padx=10, pady=5)

    # SETTINGS
    # Create a LabelFrame to group the inputs with a title
    frame_settings = tk.LabelFrame(root, text="Settings", padx=10, pady=10)
    frame_settings.pack(padx=10, pady=10, fill="both", expand=True)

    # Use grid for the label and entry side by side
    tk.Label(frame_settings, text="Color", anchor="w").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    tk.Entry(frame_settings, textvariable=color_var, width=30).grid(row=0, column=1, padx=10, pady=5)

    # Use grid for the label and entry side by side
    tk.Label(frame_settings, text="Filename", anchor="w").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    tk.Entry(frame_settings, textvariable=filename_var, width=30).grid(row=1, column=1, padx=10, pady=5) 

    # Checkbuttons for additional options (aligned to the left)
    tk.Checkbutton(frame_settings, text="Filename with timestamp", variable=timestamp_var, anchor="w", command=update_filename).grid(row=2, column=0, columnspan=2, pady=2, padx=10, sticky="w")
    tk.Checkbutton(frame_settings, text="Use STARSWARS placeholders", variable=placeholder_var, anchor="w", command=update_entries).grid(row=3, column=0, columnspan=2, pady=2, padx=10, sticky="w")
    tk.Checkbutton(frame_settings, text="Delete LaTeX log and auxiliary files", variable=cleanup_var, anchor="w").grid(row=4, column=0, columnspan=2, pady=2, padx=10, sticky="w")

    # Create a frame for the buttons at the bottom
    button_frame = tk.Frame(root)
    button_frame.pack(side="bottom", pady=10)

    # Buttons to trigger actions
    generate_tex_button = tk.Button(
        button_frame, 
        text="Generate LaTeX files", 
        command=lambda: on_generate_tex(
            company_var, 
            role_var,
            url_var,
            city_var, 
            country_var, 
            color_var,
            filename_var
        )
    )
    generate_tex_button.pack(side="left", padx=10)

    generate_pdf_button = tk.Button(
        button_frame, 
        text="Generate PDF", 
        command=lambda: on_generate_pdf(cleanup_var), 
        state=tk.DISABLED  # Initially disabled until .tex is generated
    )
    generate_pdf_button.pack(side="left", padx=10)

    # Return the window and PDF button
    return root, generate_pdf_button
