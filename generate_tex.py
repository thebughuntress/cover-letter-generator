import os
import time

def generate_tex(company, role, url, city, country, color, filename, SW_PLACEHOLDER):

    if SW_PLACEHOLDER:
        # use star wars template and placeholders
        COVERLETTER_PATH = "./templates/coverletter.tex"
        PERSONAL_DATA_PATH = "../templates/personal-data-sw.tex"
        LETTER_PATH = "../templates/letter-sw.tex"
        JOB_POSTING_PATH = "../templates/job-posting.tex"
    else:
        # use local template and placeholders
        COVERLETTER_PATH = "./templates/coverletter.tex"
        PERSONAL_DATA_PATH = "../templates/personal-data.tex"
        LETTER_PATH = "../templates/letter.tex"
        JOB_POSTING_PATH = "../templates/job-posting.tex"

    # Ensure the 'tex' folder exists
    tex_folder = os.path.join(os.getcwd(), "tex")
    if not os.path.exists(tex_folder):
        os.makedirs(tex_folder)

    # Generate a the output file path
    output_file_path = os.path.join(tex_folder, f"{filename}.tex")

    if not os.path.exists(COVERLETTER_PATH):
        raise FileNotFoundError(f"Template file not found at: {COVERLETTER_PATH}")

    # Read the template content
    with open(COVERLETTER_PATH, "r") as template_file:
        tex_content = template_file.read()

    # Replace placeholders in the template
    tex_content = tex_content.replace("THISCOMPANY", company)
    tex_content = tex_content.replace("THISROLE", role)
    tex_content = tex_content.replace("THISCITY", city)
    tex_content = tex_content.replace("THISCOUNTRY", country)
    tex_content = tex_content.replace("THISURL", url)
    tex_content = tex_content.replace("PATHTOFILE1", PERSONAL_DATA_PATH)
    tex_content = tex_content.replace("PATHTOFILE2", JOB_POSTING_PATH)
    tex_content = tex_content.replace("PATHTOFILE3", LETTER_PATH)

    # Replace '#' with an empty string if it exists
    color = color.replace("#", "")
    tex_content = tex_content.replace("THISCOLOR", color)

    # Write the modified content to the .tex file
    with open(output_file_path, "w") as tex_file:
        tex_file.write(tex_content)

    print(f"Generated .tex file at: {output_file_path}")
    return output_file_path
