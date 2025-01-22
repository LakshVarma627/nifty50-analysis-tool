import os

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': os.getenv('MONGO_DB_NAME', 'nifty50'),
        'CLIENT': {
            'host': os.getenv('MONGO_URI', 'mongodb://localhost:27017'),
            'port': 27017,
            'username': os.getenv('MONGO_USER'),  # For Atlas
            'password': os.getenv('MONGO_PASS'),  # For Atlas
            'authSource': 'admin',
            'authMechanism': 'SCRAM-SHA-1',
            'ssl': True,  # Required for Atlas
            'tlsAllowInvalidCertificates': True  # For self-signed certs
        },
        'OPTIONS': {
            'connectTimeoutMS': 30000,  # 30s connection timeout
            'socketTimeoutMS': 60000,   # 1min query timeout
        }
    }
}