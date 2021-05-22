from jinja2 import Environment, FileSystemLoader

TEMPLATE_NAME = "ginseng"

template_loader = FileSystemLoader(searchpath="./template")
template_env = Environment(loader=template_loader)
template = template_env.get_template(f"{TEMPLATE_NAME}.html")
outputText = template.render()

with open("output/resume.html", "w") as output_file:
    print("writing!")
    output_file.write(template.render(name="Matteo Silvestro"))
