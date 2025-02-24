# Simulating Synthetic Radar Data for Testing UODFT + LZ + HQS Model
import numpy as np
import matplotlib.pyplot as plt

# Define Radar Parameters
Fs = 1e6  # Sampling Frequency (1 MHz)
T = 2e-3  # Signal duration (2 ms)
t = np.linspace(0, T, int(Fs * T), endpoint=False)  # Time vector

# Define Simulated Targets (e.g., UAVs and Clutter)
num_targets = 3
target_distances = np.array([500, 1200, 3000])  # Meters
target_rcs = np.array([1.0, 0.6, 0.2])  # Radar Cross Section (Normalized)

# Radar Wave Properties
c = 3e8  # Speed of light (m/s)
fc = 10e9  # Radar Frequency (10 GHz)
pulse_width = 1e-6  # Pulse Width (1 µs)

# Generate Radar Pulse (Sine Wave)
pulse = np.sin(2 * np.pi * fc * t) * (t < pulse_width)

# Simulate Received Signal (Reflections from Targets)
received_signal = np.zeros_like(t)
for i in range(num_targets):
    delay = 2 * target_distances[i] / c  # Round-trip delay time
    delay_samples = int(delay * Fs)  # Convert delay to samples
    
    if delay_samples < len(t):
        received_signal[delay_samples:] += target_rcs[i] * pulse[:len(t) - delay_samples]

# Add Noise to Simulate Clutter & Environmental Interference
noise = np.random.normal(0, 0.1, len(t))
received_signal += noise

# Plot Simulated Radar Signal
plt.figure(figsize=(10, 5))
plt.plot(t * 1e6, received_signal, label="Simulated Radar Signal")
plt.xlabel("Time (µs)")
plt.ylabel("Signal Amplitude")
plt.title("Synthetic Radar Signal with UAVs & Clutter")
plt.legend()
plt.grid()
plt.show()