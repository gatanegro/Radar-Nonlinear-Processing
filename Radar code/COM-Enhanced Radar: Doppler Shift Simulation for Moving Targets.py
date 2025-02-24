# Simulating Doppler Shift for Moving Targets in COM-Enhanced Radar

# Define Target Motion Parameters
num_targets = 3  # Number of targets
target_speeds = np.array([150, 500, 1500])  # Speeds in m/s (including a hypersonic target)
c = 3e8  # Speed of light (m/s)

# Compute Doppler Frequency Shifts for Each Target
doppler_shifts = 2 * fc * target_speeds / c  # Doppler formula: f_d = (2 * v * f_c) / c

# Simulate Doppler-Shifted Radar Returns
doppler_signals = np.zeros((num_targets, len(t)), dtype=complex)

for i in range(num_targets):
    doppler_signals[i] = com_signal * np.exp(1j * 2 * np.pi * doppler_shifts[i] * t)  # Frequency shift

# Sum the signals to create the final received waveform
received_signal = np.sum(doppler_signals, axis=0) + np.random.normal(0, 0.05, len(t))  # Adding noise

# Apply FFT to Analyze Doppler Effects
fft_received = np.abs(np.fft.fft(received_signal))

# Plot Standard FFT vs. COM-Enhanced Doppler Radar Processing
plt.figure(figsize=(12, 6))
plt.plot(np.fft.fftshift(freq) / 1e6, np.fft.fftshift(fft_pulse), '--', label="Standard FFT")
plt.plot(np.fft.fftshift(freq) / 1e6, np.fft.fftshift(fft_com_signal), linewidth=1.5, label="COM-Enhanced FFT")
plt.plot(np.fft.fftshift(freq) / 1e6, np.fft.fftshift(fft_received), linewidth=1.5, linestyle="-.", label="Doppler-Shifted Targets")
plt.xlabel("Frequency (MHz)")
plt.ylabel("Magnitude")
plt.title("COM-Enhanced Radar: Doppler Shift Simulation for Moving Targets")
plt.legend()
plt.grid()
plt.show()