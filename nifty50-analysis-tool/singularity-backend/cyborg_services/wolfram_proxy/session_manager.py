import wolframalpha
import time

class WolframSessionManager:
    def __init__(self, app_id):
        self.client = wolframalpha.Client(app_id)
        self.sessions = {}

    def start_session(self, session_id):
        if session_id not in self.sessions:
            self.sessions[session_id] = {
                "client": self.client,
                "start_time": time.time()
            }
            return {"status": "Session started", "session_id": session_id}
        else:
            return {"status": "Session already exists", "session_id": session_id}

    def end_session(self, session_id):
        if session_id in self.sessions:
            del self.sessions[session_id]
            return {"status": "Session ended", "session_id": session_id}
        else:
            return {"status": "Session not found", "session_id": session_id}

    def query(self, session_id, question):
        if session_id in self.sessions:
            try:
                res = self.sessions[session_id]["client"].query(question)
                return self._parse_response(res)
            except Exception as e:
                return {"error": str(e)}
        else:
            return {"error": "Session not found"}

    def _parse_response(self, response):
        return {
            "pods": [{"title": pod.title, "content": pod.text} for pod in response.pods]
        }
