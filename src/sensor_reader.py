"""
Sensor Reader Stub for CropSense.
TODO: Implement actual sensor reading once hardware arrives.
"""
import time

def read_soil_moisture():
    # TODO: Read MCP3008 via SPI
    return 45.0  # Dummy value

def read_dht22():
    # TODO: Read DHT22 via GPIO
    return 22.5, 50.0  # Dummy temp, humidity

def read_bh1750():
    # TODO: Read via I2C using smbus2
    return 300.0  # Dummy lux

if __name__ == "__main__":
    print("Starting CropSense Sensor Reader (Stub)...")
    while True:
        moisture = read_soil_moisture()
        temp, hum = read_dht22()
        light = read_bh1750()
        print(f"Moisture: {moisture}%, Temp: {temp}C, Hum: {hum}%, Light: {light}lux")
        time.sleep(900) # Wait 15 minutes