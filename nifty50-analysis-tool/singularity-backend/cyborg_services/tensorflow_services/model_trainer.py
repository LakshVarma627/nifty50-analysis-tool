import joblib

def cache_model(model, filename):
    joblib.dump(model, filename)

def load_cached_model(filename):
    return joblib.load(filename)
