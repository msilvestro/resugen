import os
import re
import time
from pathlib import Path

import markdown
import yaml
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

load_dotenv()

TEMPLATE_NAME = os.getenv("TEMPLATE_NAME", "minimal")

template_loader = FileSystemLoader(searchpath="./template")
template_env = Environment(loader=template_loader)

month_date_pattern = re.compile(r"^([0-9]{4})-([0-9]{2})$")


def format_date(input, format):
    if not input:
        return "now"
    year, month = month_date_pattern.findall(input)[0]
    return format.format(year=year, month=month)


def markdown_converter(input):
    return markdown.markdown(input)


template_env.filters["format_date"] = format_date
template_env.filters["markdown"] = markdown_converter


def export():
    template = template_env.get_template(f"{TEMPLATE_NAME}.html")

    with open("resume.yml", "r", encoding="utf-8") as input_file:
        resume = yaml.safe_load(input_file)
    with open("output/resume.html", "w", encoding="utf-8") as output_file:
        output_file.write(template.render(resume=resume))


class TemplateHandler(PatternMatchingEventHandler):
    patterns = ["template/*.html", "template/*.css", "resume*.yml"]
    ignore_directories = True
    case_sensitive = False

    def on_modified(self, event):
        try:
            export()
            print(f"File '{event.src_path}' has been modified, output regenerated...")
        except Exception as exc:
            print(exc)


def generate():
    Path("output").mkdir(exist_ok=True)

    print(f"Using template '{TEMPLATE_NAME}'")
    try:
        export()
    except Exception as exc:
        print(exc)
    print("Output generated in 'output/resume.html', waiting for changes...")

    observer = Observer()
    observer.schedule(TemplateHandler(), path=".", recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
