import os

from markdown2 import markdown
from weasyprint import HTML, CSS

# Constants
RESUME_IN_NAME: str = "adam_setapen_resume.md"
RESUME_OUT_NAME: str = "adam_setapen_resume.pdf"

images_dir = os.path.abspath('images')

# Define CSS styling
css = CSS(
    string=f"""
@page {{
    size: A4;
    margin: 1in;
}}
body {{
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    font-size: 12px;
    color: #111;
}}
h1 {{
    color: #0A66C2;
    font-size: 48px;
    margin-top: 0px;
    margin-bottom: 5px;
}}
h2 {{
    color: #2f76c9;
    font-size: 16px;
    margin-top: 0px;
    margin-bottom: 5px;
}}
h3 {{
    font-size: 14px;
    margin-top: 5px;
    margin-bottom: 0px;
}}
h4 {{
    font-size: 12px;
    margin-top: 0px;
    margin-bottom: 2px;
}}
h5 {{
    font-size: 12px;
    margin-top: 10px;
    margin-bottom: 0px;
    font-weight: normal;
}}
ul {{
    margin-top: 0;
    margin-bottom: 0;
    padding-left: 1.2em;
}}
a {{
    color: #0A66C2;
    text-decoration: none;
}}
hr {{
    border: none;
    border-top: 1px solid #ccc;
    margin: 10px 0;
}}
p {{
    margin-top: 0;
    margin-bottom: 0;
}}
.logo-container {{
    display: inline-flex;
    align-items: center;
    white-space: nowrap;
}}
#github-logo, #linkedin-logo, #www-logo {{
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    width: 12px;
    height: 12px;
    display: inline-block;
    margin-right: 4px;
    vertical-align: middle;
    margin-right: 4px;
}}
#github-logo {{
    background-image: url('file://{images_dir}/github.svg');
}}
#linkedin-logo {{
    background-image: url('file://{images_dir}/linkedin.svg');
}}
#www-logo {{
    background-image: url('file://{images_dir}/www.svg');
    width: 14px;
    height: 14px;
}}
"""
)

def main():
    print("Generating PDF from markdown...")
    # Load markdown content
    with open(RESUME_IN_NAME, "r") as f:
        markdown_content = f.read()
    # Convert to HTML
    html_resume = markdown(markdown_content)
    # Generate PDF
    HTML(string=html_resume).write_pdf(RESUME_OUT_NAME, stylesheets=[css])
    print("PDF generated successfully!")


if __name__ == "__main__":
    main()
