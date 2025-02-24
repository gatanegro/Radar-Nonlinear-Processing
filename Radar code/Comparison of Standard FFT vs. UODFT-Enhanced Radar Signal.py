# Apply Standard FFT Processing for Baseline Analysis
fft_spectrum = np.fft.fft(received_signal)
freqs = np.fft.fftfreq(len(t), d=1/Fs)

# Compute Power Spectrum for Standard Processing
power_spectrum = np.abs(fft_spectrum) ** 2

# Apply UODFT-Based Processing (LZ Attractor & Collatz-Octave Scaling)
LZ = 1.23498  # Loop Zero as a stabilizing attractor
HQS = 0.235   # Harmonic Quantum Shift threshold

# Collatz-Octave Harmonic Scaling (Recursive Harmonic Modulation)
harmonic_scaling_factor = LZ  
collatz_harmonic = np.array([n * harmonic_scaling_factor for n in range(1, 10)])
enhanced_signal = received_signal.copy()

for h in collatz_harmonic:
    enhanced_signal += np.roll(received_signal, int(h * 10)) * 0.5  # Recursive wave folding

# Apply LZ Stabilization & HQS Adaptive Filtering
enhanced_signal *= (1 - HQS)  # Adjust energy redistribution

# Compute FFT for UODFT-Enhanced Signal
fft_uodft = np.fft.fft(enhanced_signal)
power_uodft = np.abs(fft_uodft) ** 2

# Compare Standard FFT vs. UODFT Processing
plt.figure(figsize=(12, 6))
plt.plot(freqs[:len(freqs)//2] / 1e6, power_spectrum[:len(freqs)//2], linestyle="--", label="Standard FFT")
plt.plot(freqs[:len(freqs)//2] / 1e6, power_uodft[:len(freqs)//2], linewidth=1.5, label="UODFT-Enhanced FFT")
plt.xlabel("Frequency (MHz)")
plt.ylabel("Power Spectrum (dB)")
plt.title("Comparison of Standard FFT vs. UODFT-Enhanced Radar Signal")
plt.legend()
plt.grid()
plt.show()