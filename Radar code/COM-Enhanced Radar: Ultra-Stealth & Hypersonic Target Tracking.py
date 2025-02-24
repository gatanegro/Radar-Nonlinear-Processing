# Extreme Validation: Testing COM-Based Radar Under Ultra-Stealth & Hypersonic Conditions

# Define Extreme Test Parameters
num_extreme_targets = 3  # Number of extreme test targets
extreme_rcs = np.array([0.02, 0.01, 0.005])  # Ultra-low RCS for next-gen stealth aircraft
extreme_speeds = np.array([5000, 8000, 12000])  # Mach 10+ speeds (in m/s)

# Compute Doppler Frequency Shifts for Extreme Conditions
doppler_extreme_shifts = 2 * fc * extreme_speeds / c

# Simulate Radar Returns for Extreme Stealth & Hypersonic Targets
extreme_signals = np.zeros((num_extreme_targets, len(t)), dtype=complex)

for i in range(num_extreme_targets):
    extreme_signals[i] = extreme_rcs[i] * com_signal * np.exp(1j * 2 * np.pi * doppler_extreme_shifts[i] * t)

# Combine Standard, Stealth, and Extreme Hypersonic Targets
received_extreme_signal = (
    np.sum(doppler_signals, axis=0) + np.sum(stealth_signals, axis=0) + np.sum(extreme_signals, axis=0)
    + np.random.normal(0, 0.05, len(t))  # Adding high-noise interference
)

# Compute FFT for Standard FFT vs. COM-Enhanced Radar in Extreme Conditions
fft_extreme_received = np.abs(np.fft.fft(received_extreme_signal))

# Plot Standard FFT vs. COM-Enhanced Radar in Extreme Conditions
plt.figure(figsize=(12, 6))
plt.plot(np.fft.fftshift(freq) / 1e6, np.fft.fftshift(fft_pulse), '--', label="Standard FFT")
plt.plot(np.fft.fftshift(freq) / 1e6, np.fft.fftshift(fft_com_signal), linewidth=1.5, label="COM-Enhanced FFT")
plt.plot(np.fft.fftshift(freq) / 1e6, np.fft.fftshift(fft_received), linewidth=1.5, linestyle="-.", label="Doppler-Shifted Targets")
plt.plot(np.fft.fftshift(freq) / 1e6, np.fft.fftshift(fft_stealth_received), linewidth=2, linestyle=":", label="Stealth Doppler Targets")
plt.plot(np.fft.fftshift(freq) / 1e6, np.fft.fftshift(fft_extreme_received), linewidth=2, linestyle="--", label="Extreme Hypersonic Stealth Targets")
plt.xlabel("Frequency (MHz)")
plt.ylabel("Magnitude")
plt.title("COM-Enhanced Radar: Ultra-Stealth & Hypersonic Target Tracking")
plt.legend()
plt.grid()
plt.show()