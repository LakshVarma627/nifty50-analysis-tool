import wolframalpha

class WolframService:
    def __init__(self):
        self.client = wolframalpha.Client(settings.WOLFRAM_APP_ID)

    def query(self, question):
        """Execute a Wolfram query with free-tier limits."""
        try:
            res = self.client.query(question)
            return self._parse_response(res)
        except Exception as e:
            return {"error": "Free-tier limit exceeded or invalid query"}

    def _parse_response(self, response):
        """Extract results from Wolfram API response."""
        return {
            "pods": [{"title": pod.title, "content": pod.text} for pod in response.pods]
        }
