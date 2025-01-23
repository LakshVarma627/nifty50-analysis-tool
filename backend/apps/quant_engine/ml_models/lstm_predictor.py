import tensorflow as tf
import numpy as np

class NiftyPredictor:
    def __init__(self, model_path='models/lstm.h5'):
        self.model = tf.keras.models.load_model(model_path)
        self.window_size = 60  # Use last 60 data points for prediction

    def preprocess_data(self, data):
        """Normalize and reshape data for LSTM input."""
        scaled = (data - np.mean(data)) / np.std(data)  # Standard scaling
        return np.reshape(scaled[-self.window_size:], (1, self.window_size, 1))

    def predict(self, data):
        """Predict the next time step."""
        processed = self.preprocess_data(data)
        return self.model.predict(processed)[0][0]  # Return scalar prediction