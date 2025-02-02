DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nifty50',
        'USER': 'niftyuser',
        'PASSWORD': 'sqszpyvmUjtYvVMW3WiTHgVHSfKcwejc',
        'HOST': 'dpg-cu8mb2ij1k6c73ekp3qg-a.singapore-postgres.render.com',
        'PORT': '5432',
        'OPTIONS': {'sslmode': 'require'},
    }
}

DATABASES['backup'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'backup.db',
}
