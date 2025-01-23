import wolframalpha
import os

class WolframSessionManager:
    def __init__(self):
        self.client = wolframalpha.Client(os.getenv('WOLFRAM_APP_ID'))
        self.sessions = {}

    def start_session(self, session_id):
        if session_id not in self.sessions:
            self.sessions[session_id] = self.client
        return self.sessions[session_id]

    def end_session(self, session_id):
        if session_id in self.sessions:
            del self.sessions[session_id]

    def query(self, session_id, question):
        if session_id not in self.sessions:
            raise ValueError("Session not found")
        try:
            res = self.sessions[session_id].query(question)
            return self._parse_response(res)
        except Exception as e:
            return {"error": str(e)}

    def _parse_response(self, response):
        return {
            "pods": [{"title": pod.title, "content": pod.text} for pod in response.pods]
        }
