import os
import time

def generate_tex(company, role, url, city, country, color, filename, SW_PLACEHOLDER):

    if SW_PLACEHOLDER:
        # use star wars template and placeholders
        PERSONAL_DATA_FILE = "../coverletter_template/personal-data-sw.tex"
        COVERLETTER_FILENAME = "coverletter-sw.tex"
    else:
        # use local template and placeholders
        PERSONAL_DATA_FILE = "../coverletter_template/personal-data.tex"
        COVERLETTER_FILENAME = "coverletter.tex"
    
    # Path to the template file
    template_path = os.path.join(os.getcwd(), "coverletter_template", COVERLETTER_FILENAME)

    # Ensure the 'tex' folder exists
    tex_folder = os.path.join(os.getcwd(), "tex")
    if not os.path.exists(tex_folder):
        os.makedirs(tex_folder)

    # Generate a the output file path
    output_file_path = os.path.join(tex_folder, f"{filename}.tex")

    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template file not found at: {template_path}")

    # Read the template content
    with open(template_path, "r") as template_file:
        tex_content = template_file.read()

    # Replace placeholders in the template
    tex_content = tex_content.replace("COMPANYX", company)
    tex_content = tex_content.replace("ROLEX", role)
    tex_content = tex_content.replace("CITYX", city)
    tex_content = tex_content.replace("COUNTRYX", country)
    tex_content = tex_content.replace("URLX", url)
    tex_content = tex_content.replace("PATHTOFILEX", PERSONAL_DATA_FILE)

    # Replace '#' with an empty string if it exists
    color = color.replace("#", "")
    tex_content = tex_content.replace("COLORX", color)

    # Write the modified content to the .tex file
    with open(output_file_path, "w") as tex_file:
        tex_file.write(tex_content)

    print(f"Generated .tex file at: {output_file_path}")
    return output_file_path
