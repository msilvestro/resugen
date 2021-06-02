# Resugen

A simple resume generator.

## What is it?

This is a simple tool I created for myself to quickly generate a resume from a `yaml` source file and a Jinja HTML+CSS template. It is a bit rough but it works just fine for my necessities.

## How to use it

- Install `poetry` and create a virtual environment
- Install dependencies with:
  ```sh
  poetry install
  ```
- Create a `resume.yml` file, taking inspiration from `resume.example.yml`
- Select a template creating an `.env` file, taking inspiration from `.env.example`
- Run the export and make the script look for changes:
  ```sh
  python main.py
  ```
- From this moment on, you will find the output HTML file at `output/resume.html`
  - Whenever you update the `resume.yml` or the template files the script will regenerate the output
  - To have immediate feedback on the output webpage, I recommend using VSCode extension [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)
