import nbformat
from nbconvert import HTMLExporter
from traitlets.config import Config

class NotebookBridge:
    def __init__(self, notebook_path):
        self.notebook_path = notebook_path

    def read_notebook(self):
        with open(self.notebook_path, 'r', encoding='utf-8') as f:
            return nbformat.read(f, as_version=4)

    def convert_to_html(self, notebook):
        config = Config()
        config.HTMLExporter.preprocessors = ['nbconvert.preprocessors.ExtractOutputPreprocessor']
        html_exporter = HTMLExporter(config=config)
        body, resources = html_exporter.from_notebook_node(notebook)
        return body

    def save_html(self, html, output_path):
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)

    def convert_and_save(self, output_path):
        notebook = self.read_notebook()
        html = self.convert_to_html(notebook)
        self.save_html(html, output_path)
