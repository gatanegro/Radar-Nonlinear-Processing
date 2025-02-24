
# Step 1: Analyzing Specific Frequency Bands for Hidden Signals

# Identify Frequency Peaks in COM-Enhanced Radar
from scipy.signal import find_peaks

peaks_standard, _ = find_peaks(fft_passive, height=np.mean(fft_passive) + np.std(fft_passive))
peaks_com, _ = find_peaks(fft_com_passive, height=np.mean(fft_com_passive) + np.std(fft_com_passive))

# Extract Peak Frequencies
peak_frequencies_standard = freq_passive[peaks_standard] / 1e6  # Convert to MHz
peak_frequencies_com = freq_passive[peaks_com] / 1e6  # Convert to MHz

# Compile Peak Frequency Comparisons
frequency_analysis = pd.DataFrame({
    "Standard FFT Peaks (MHz)": np.round(peak_frequencies_standard, 3),
    "COM-Enhanced Peaks (MHz)": np.round(peak_frequencies_com, 3)
})


# Ensure Both Peak Arrays Are of the Same Length by Padding with NaN for Proper Comparison
max_length = max(len(peak_frequencies_standard), len(peak_frequencies_com))

# Pad shorter arrays with NaN values to align column lengths
peak_frequencies_standard = np.pad(peak_frequencies_standard, (0, max_length - len(peak_frequencies_standard)), constant_values=np.nan)
peak_frequencies_com = np.pad(peak_frequencies_com, (0, max_length - len(peak_frequencies_com)), constant_values=np.nan)

# Compile Peak Frequency Comparisons Again
frequency_analysis_fixed = pd.DataFrame({
    "Standard FFT Peaks (MHz)": np.round(peak_frequencies_standard, 3),
    "COM-Enhanced Peaks (MHz)": np.round(peak_frequencies_com, 3)
})

# Display results
tools.display_dataframe_to_user(name="Passive Radar Frequency Analysis", dataframe=frequency_analysis_fixed)
STDOUT/STDERR
/home/sandbox/.local/lib/python3.11/site-packages/pandas/core/internals/blocks.py:2323: RuntimeWarning: invalid value encountered in cast
  values = values.astype(str)