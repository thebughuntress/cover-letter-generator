import tkinter as tk

# Default color value
DEFAULT_COLOR = "#333333"

def create_form(on_generate_tex, on_generate_pdf):
    # Create the main Tkinter window
    root = tk.Tk()
    root.title("Cover Letter Generator")

    # Center the window on the screen
    window_width = 450
    window_height = 450
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
    timestamp_var = tk.BooleanVar(value=False)  # Checkbox for timestamp (default: False)
    cleanup_var = tk.BooleanVar(value=True)    # Checkbox for cleanup (default: True)
    placeholder_var = tk.BooleanVar(value=False)  # Checkbox for placeholders

    # CONTENT
    # Create a LabelFrame to group the inputs with a title
    frame_inputs = tk.LabelFrame(root, text="Content", padx=10, pady=10)
    frame_inputs.pack(padx=10, pady=10)

    # Use grid layout to arrange labels and entry fields side by side
    tk.Label(frame_inputs, text="Company").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    tk.Entry(frame_inputs, textvariable=company_var).grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame_inputs, text="Role").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    tk.Entry(frame_inputs, textvariable=role_var).grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame_inputs, text="URL").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    tk.Entry(frame_inputs, textvariable=url_var).grid(row=2, column=1, padx=10, pady=5)

    tk.Label(frame_inputs, text="City").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    tk.Entry(frame_inputs, textvariable=city_var).grid(row=3, column=1, padx=10, pady=5)

    tk.Label(frame_inputs, text="Country").grid(row=4, column=0, padx=10, pady=5, sticky="w")
    tk.Entry(frame_inputs, textvariable=country_var).grid(row=4, column=1, padx=10, pady=5)

    # SETTINGS
    # Create a LabelFrame to group the inputs with a title
    frame_settings = tk.LabelFrame(root, text="Settings", padx=10, pady=10)
    frame_settings.pack(padx=10, pady=10)

    # Use grid for the label and entry side by side
    tk.Label(frame_settings, text="Color", anchor="w").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    tk.Entry(frame_settings, textvariable=color_var).grid(row=0, column=1, padx=10, pady=5)

    # Checkbuttons for additional options (aligned to the left)
    tk.Checkbutton(frame_settings, text="Filename with timestamp", variable=timestamp_var, anchor="w").grid(row=1, column=0, columnspan=2, pady=5, padx=10, sticky="w")
    tk.Checkbutton(frame_settings, text="Delete LaTeX log and auxiliary files", variable=cleanup_var, anchor="w").grid(row=2, column=0, columnspan=2, pady=5, padx=10, sticky="w")
    tk.Checkbutton(frame_settings, text="Use STARSWARS placeholders", variable=placeholder_var, anchor="w").grid(row=3, column=0, columnspan=2, pady=5, padx=10, sticky="w")

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
            timestamp_var, 
            placeholder_var
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
