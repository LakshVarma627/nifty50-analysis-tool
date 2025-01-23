import redis

class RedisStreamConfig:
    def __init__(self, host='localhost', port=6379, db=0):
        self.client = redis.StrictRedis(host=host, port=port, db=db)

    def create_stream(self, stream_name):
        """Create a new Redis stream."""
        try:
            self.client.xadd(stream_name, {'initial': 'value'})
            return {"status": "Stream created successfully"}
        except Exception as e:
            return {"error": str(e)}

    def add_to_stream(self, stream_name, data):
        """Add data to an existing Redis stream."""
        try:
            self.client.xadd(stream_name, data)
            return {"status": "Data added to stream successfully"}
        except Exception as e:
            return {"error": str(e)}

    def read_stream(self, stream_name, count=10):
        """Read data from a Redis stream."""
        try:
            return self.client.xrange(stream_name, count=count)
        except Exception as e:
            return {"error": str(e)}
