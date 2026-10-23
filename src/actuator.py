"""
Actuator Stub for CropSense.
TODO: Control relay and pump based on predicted water volume.
"""
import time

def water_plant(volume_ml, flow_rate_ml_per_sec=10):
    # TODO: Trigger GPIO relay
    duration = volume_ml / flow_rate_ml_per_sec
    print(f"Pump ON for {duration} seconds to deliver {volume_ml} mL... (Stub)")
    # time.sleep(duration) # To be uncommented when relay is attached
    print("Pump OFF.")

if __name__ == "__main__":
    # Example: Water 150 mL
    water_plant(150.0)