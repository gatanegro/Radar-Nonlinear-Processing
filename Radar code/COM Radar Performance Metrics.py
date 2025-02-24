# Compute Final Performance Metrics for COM-Enhanced Radar Validation

# Signal-to-Noise Ratio (SNR) Improvement
snr_standard = np.mean(fft_pulse) / np.std(fft_pulse)  # Standard FFT SNR
snr_com = np.mean(fft_com_signal) / np.std(fft_com_signal)  # COM-Enhanced SNR
snr_stealth = np.mean(fft_stealth_received) / np.std(fft_stealth_received)  # Stealth Target SNR
snr_extreme = np.mean(fft_extreme_received) / np.std(fft_extreme_received)  # Hypersonic Target SNR

# Detection Rate Improvement (Relative Power Levels)
detection_standard = np.sum(fft_pulse) / len(fft_pulse)
detection_com = np.sum(fft_com_signal) / len(fft_com_signal)
detection_stealth = np.sum(fft_stealth_received) / len(fft_stealth_received)
detection_extreme = np.sum(fft_extreme_received) / len(fft_extreme_received)

# Compute Tracking Error Reduction (Signal Peak Stability)
tracking_error_standard = np.std(np.diff(fft_pulse))  # Standard FFT tracking error
tracking_error_com = np.std(np.diff(fft_com_signal))  # COM-enhanced tracking error
tracking_error_stealth = np.std(np.diff(fft_stealth_received))  # Stealth target tracking error
tracking_error_extreme = np.std(np.diff(fft_extreme_received))  # Hypersonic tracking error

# Compile Results into a Table
import pandas as pd
performance_metrics = pd.DataFrame({
    "Metric": ["SNR", "Detection Rate", "Tracking Error"],
    "Standard FFT": [snr_standard, detection_standard, tracking_error_standard],
    "COM-Enhanced": [snr_com, detection_com, tracking_error_com],
    "Stealth Target": [snr_stealth, detection_stealth, tracking_error_stealth],
    "Hypersonic Target": [snr_extreme, detection_extreme, tracking_error_extreme]
})

# Display Results
import ace_tools as tools
tools.display_dataframe_to_user(name="COM Radar Performance Metrics", dataframe=performance_metrics)