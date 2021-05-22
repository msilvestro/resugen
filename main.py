from jinja2 import Environment, FileSystemLoader
import yaml

TEMPLATE_NAME = "ginseng"

template_loader = FileSystemLoader(searchpath="./template")
template_env = Environment(loader=template_loader)
template = template_env.get_template(f"{TEMPLATE_NAME}.html")

with open("resume.yml", "r") as input_file:
    resume = yaml.safe_load(input_file)
with open("output/resume.html", "w") as output_file:
    output_file.write(template.render(resume=resume))
