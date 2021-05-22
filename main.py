from jinja2 import Environment, FileSystemLoader
import yaml
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


def export():
    TEMPLATE_NAME = "ginseng"

    template_loader = FileSystemLoader(searchpath="./template")
    template_env = Environment(loader=template_loader)
    template = template_env.get_template(f"{TEMPLATE_NAME}.html")

    with open("resume.yml", "r") as input_file:
        resume = yaml.safe_load(input_file)
    with open("output/resume.html", "w") as output_file:
        output_file.write(template.render(resume=resume))


class TemplateHandler(PatternMatchingEventHandler):
    patterns = ["template/*.html", "template/*.css", "resume*.yml"]
    ignore_directories = True
    case_sensitive = False

    def on_modified(self, event):
        print(event)
        export()


if __name__ == "__main__":
    observer = Observer()
    observer.schedule(TemplateHandler(), path=".", recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
