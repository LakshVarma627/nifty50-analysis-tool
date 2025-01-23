import nbformat
from nbconvert import HTMLExporter
from nbclient import NotebookClient

class NotebookBridge:
    def __init__(self, notebook_path):
        self.notebook_path = notebook_path
        self.notebook = None

    def load_notebook(self):
        with open(self.notebook_path, 'r') as f:
            self.notebook = nbformat.read(f, as_version=4)

    def execute_notebook(self):
        if self.notebook is None:
            self.load_notebook()
        client = NotebookClient(self.notebook)
        client.execute()

    def convert_to_html(self):
        if self.notebook is None:
            self.load_notebook()
        html_exporter = HTMLExporter()
        html_data, _ = html_exporter.from_notebook_node(self.notebook)
        return html_data
