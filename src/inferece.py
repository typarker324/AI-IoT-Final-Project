"""
Model Inference Stub for CropSense.
TODO: Load ONNX model and run inference on sensor data.
"""
import numpy as np

def load_model():
    # TODO: Load ONNX model
    print("Loading ONNX model... (Stub)")
    return None

def predict_water_deficit(features):
    # TODO: Run inference
    # Dummy prediction: 150 mL
    return 150.0

if __name__ == "__main__":
    model = load_model()
    dummy_features = np.array([[45.0, 22.5, 50.0, 300.0, 1.0]]) # Moisture, Temp, Hum, Light, SpeciesID
    deficit = predict_water_deficit(dummy_features)
    print(f"Predicted Water Deficit: {deficit} mL")