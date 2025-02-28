import os
import time

def generate_tex(company, role, url, city, country, color, filename, SW_PLACEHOLDER):

    if SW_PLACEHOLDER:
        # use star wars template and placeholders
        PATH_TO_COVERLETTER = "./templates/coverletter.tex"
        PATH_TO_PERSONAL_DATA = "../templates/personal-data-sw.tex"
        PATH_TO_LETTER = "../templates/letter-sw.tex"
        PATH_TO_JOB_POSTING = "../templates/job-posting.tex"
    else:
        # use local template and placeholders
        PATH_TO_COVERLETTER = "./templates/coverletter.tex"
        PATH_TO_PERSONAL_DATA = "../templates/personal-data.tex"
        PATH_TO_LETTER = "../templates/letter.tex"
        PATH_TO_JOB_POSTING = "../templates/job-posting.tex"

    # Ensure the 'tex' folder exists
    tex_folder = os.path.join(os.getcwd(), "tex")
    if not os.path.exists(tex_folder):
        os.makedirs(tex_folder)

    # Generate a the output file path
    output_file_path = os.path.join(tex_folder, f"{filename}.tex")

    if not os.path.exists(PATH_TO_COVERLETTER):
        raise FileNotFoundError(f"Template file not found at: {PATH_TO_COVERLETTER}")

    # Read the template content
    with open(PATH_TO_COVERLETTER, "r") as template_file:
        tex_content = template_file.read()

    # Replace placeholders in the template
    tex_content = tex_content.replace("THISCOMPANY", company)
    tex_content = tex_content.replace("THISROLE", role)
    tex_content = tex_content.replace("THISCITY", city)
    tex_content = tex_content.replace("THISCOUNTRY", country)
    tex_content = tex_content.replace("THISURL", url)

    # Replace paths in awesome cv coverletter template
    tex_content = tex_content.replace("awesome-cv", "../templates/awesome-cv")
    tex_content = tex_content.replace("../shared/personal-data.tex", PATH_TO_PERSONAL_DATA)
    tex_content = tex_content.replace("../shared/job-posting.tex", PATH_TO_JOB_POSTING)
    tex_content = tex_content.replace("../shared/letter.tex", PATH_TO_LETTER)

    # Replace '#' with an empty string if it exists
    color = color.replace("#", "")
    tex_content = tex_content.replace("THISCOLOR", color)

    # Write the modified content to the .tex file
    with open(output_file_path, "w") as tex_file:
        tex_file.write(tex_content)

    print(f"Generated .tex file at: {output_file_path}")
    return output_file_path
