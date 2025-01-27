import os
import time

# Path to the template file
#template_path = os.path.join(os.getcwd(), "coverletter_template", "coverletter-local.tex")
template_path = os.path.join(os.getcwd(), "coverletter_template", "coverletter.tex")

def generate_tex(company, role, url, city, country, color, filename_with_timestamp):
    # Ensure the 'tex' folder exists
    tex_folder = os.path.join(os.getcwd(), "tex")
    if not os.path.exists(tex_folder):
        os.makedirs(tex_folder)

    # Generate a timestamped filename inside the 'tex' folder
    if filename_with_timestamp:
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        output_file_path = os.path.join(tex_folder, f"coverletter_{timestamp}.tex")
    else:
        output_file_path = os.path.join(tex_folder, f"coverletter.tex")

    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template file not found at: {template_path}")

    # Read the template content
    with open(template_path, "r") as template_file:
        tex_content = template_file.read()

    # Replace placeholders in the template
    tex_content = tex_content.replace("_COMPANY_", company)
    tex_content = tex_content.replace("_ROLE_", role)
    tex_content = tex_content.replace("_CITY_", city)
    tex_content = tex_content.replace("_COUNTRY_", country)
    tex_content = tex_content.replace("_URL_", url)

    # Replace '#' with an empty string if it exists
    color = color.replace("#", "")
    tex_content = tex_content.replace("_COLOR_", color)

    # Write the modified content to the .tex file
    with open(output_file_path, "w") as tex_file:
        tex_file.write(tex_content)

    print(f"Generated .tex file at: {output_file_path}")
    return output_file_path
