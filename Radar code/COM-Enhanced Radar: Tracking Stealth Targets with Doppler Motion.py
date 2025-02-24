# Simulating Stealth Targets with Motion (Low RCS + Doppler Effects)

# Define Stealth Target Parameters
num_stealth_targets = 2  # Adding stealth targets
stealth_rcs = np.array([0.1, 0.05])  # Very low RCS values to simulate stealth objects
stealth_speeds = np.array([200, 800])  # Speed in m/s (maneuvering stealth aircraft)
doppler_stealth_shifts = 2 * fc * stealth_speeds / c  # Compute Doppler shifts for stealth objects

# Simulate Stealth Radar Returns with Doppler Effects
stealth_signals = np.zeros((num_stealth_targets, len(t)), dtype=complex)

for i in range(num_stealth_targets):
    stealth_signals[i] = stealth_rcs[i] * com_signal * np.exp(1j * 2 * np.pi * doppler_stealth_shifts[i] * t)

# Combine Standard Targets and Stealth Targets
received_stealth_signal = np.sum(doppler_signals, axis=0) + np.sum(stealth_signals, axis=0) + np.random.normal(0, 0.05, len(t))

# Apply FFT to Analyze Stealth Doppler Effects
fft_stealth_received = np.abs(np.fft.fft(received_stealth_signal))

# Plot COM Radar Performance Against Stealth Targets
plt.figure(figsize=(12, 6))
plt.plot(np.fft.fftshift(freq) / 1e6, np.fft.fftshift(fft_pulse), '--', label="Standard FFT")
plt.plot(np.fft.fftshift(freq) / 1e6, np.fft.fftshift(fft_com_signal), linewidth=1.5, label="COM-Enhanced FFT")
plt.plot(np.fft.fftshift(freq) / 1e6, np.fft.fftshift(fft_received), linewidth=1.5, linestyle="-.", label="Doppler-Shifted Targets")
plt.plot(np.fft.fftshift(freq) / 1e6, np.fft.fftshift(fft_stealth_received), linewidth=2, linestyle=":", label="Stealth Doppler Targets")
plt.xlabel("Frequency (MHz)")
plt.ylabel("Magnitude")
plt.title("COM-Enhanced Radar: Tracking Stealth Targets with Doppler Motion")
plt.legend()
plt.grid()
plt.show()