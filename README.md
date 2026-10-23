# CropSense: An Edge-AI System for Precision Plant Watering

CSCI 49000-AIT Midterm Progress Repository

## Project Overview
CropSense is an IoT system designed to optimize water usage for indoor plants. It uses a Raspberry Pi 4 to read soil moisture, temperature, humidity, and light data, runs a machine learning model locally (edge inference) to predict the water deficit, and triggers a pump to deliver the exact volume of water needed.

## Hardware Bill of Materials
- **Compute:** Raspberry Pi 4 Model B (2GB)
- **Sensors:** 
  - Capacitive Soil Moisture Sensor (via MCP3008 ADC using SPI)
  - DHT22 Temperature/Humidity Module (via GPIO)
  - BH1750 Light Sensor Module (via I2C)
- **Actuation:** 3.3V-compatible Relay Module + 5V Submersible Pump
- **Safety:** 1N4007 Flyback Diode

## Repository Status (Midterm - Week 9)
- [x] Hardware architecture and compatibility verified.
- [x] Raspberry Pi OS configured (SSH, I2C, SPI enabled).
- [ ] **Sensor reading implementation (In Progress)**
- [ ] **Model training and ONNX export (Planned)**
- [ ] **End-to-end actuation (Planned)**

## Setup Instructions (for when hardware arrives)
1. Connect sensors according to the wiring diagram in `docs/DIKW_Pipeline.md`.
2. Run `pip install -r requirements.txt` inside the Python virtual environment.
3. Execute `src/sensor_reader.py` to begin logging data.


#Requirements 
smbus2
spidev
onnxruntime
scikit-learn
pandas


#DIKW_Pipeline
# DIKW Pipeline Design

## 1. Data
- **Source:** Capacitive soil moisture sensor (analog), DHT22 (digital), BH1750 (I2C).
- **Sampling Rate:** Every 15 minutes.
- **Volume:** ~96 samples per day.

## 2. Information
- **Filtering:** Moving average applied to soil moisture to reduce noise.
- **Windowing:** 4-hour sliding window feature aggregation.
- **Features:** [Average Moisture, Average Temp, Average Humidity, Light, Species_ID]
- **Labels:** Water deficit (mL) calculated as `Current Moisture - Target Moisture`.

## 3. Knowledge
- **Model:** Random Forest Regressor / XGBoost.
- **Inference:** Exported to ONNX and run locally on the Raspberry Pi 4.
- **Prediction:** Outputs a continuous float representing water volume in mL.

## 4. Wisdom
- **Action:** Converts mL to pump runtime (seconds) and triggers the relay.
- **Safety:** If prediction is out of bounds, rule-based fallback prevents flooding.
- **Reporting:** Local MQTT dashboard update.
