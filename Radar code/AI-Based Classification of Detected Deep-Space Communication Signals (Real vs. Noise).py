# Step 2: AI-Based Classification of Detected Deep-Space Communication Signals (Real vs. Noise)

from scipy.signal import find_peaks
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Identify Frequency Peaks in Standard FFT vs. COM-Enhanced Processing
peaks_space_standard, _ = find_peaks(fft_space_adjusted, height=np.mean(fft_space_adjusted) + np.std(fft_space_adjusted))
peaks_space_com, _ = find_peaks(fft_com_space_adjusted, height=np.mean(fft_com_space_adjusted) + np.std(fft_com_space_adjusted))

# Extract Peak Frequencies
peak_frequencies_space_standard = freq_space_adjusted[peaks_space_standard] / 1e6  # Convert to MHz
peak_frequencies_space_com = freq_space_adjusted[peaks_space_com] / 1e6  # Convert to MHz

# Ensure Both Peak Arrays Are of the Same Length by Padding with NaN for Proper Comparison
max_length_space = max(len(peak_frequencies_space_standard), len(peak_frequencies_space_com))

# Pad shorter arrays with NaN values to align column lengths
peak_frequencies_space_standard = np.pad(peak_frequencies_space_standard, (0, max_length_space - len(peak_frequencies_space_standard)), constant_values=np.nan)
peak_frequencies_space_com = np.pad(peak_frequencies_space_com, (0, max_length_space - len(peak_frequencies_space_com)), constant_values=np.nan)

# Prepare Data for AI Classification
features_space = np.column_stack((peak_frequencies_space_standard, peak_frequencies_space_com))
features_space = np.nan_to_num(features_space)  # Handle NaN values

# Normalize Data for Clustering
scaler = StandardScaler()
features_space_scaled = scaler.fit_transform(features_space)

# Apply K-Means Clustering (2 Clusters: Real Signals vs. Noise)
kmeans_space = KMeans(n_clusters=2, random_state=42, n_init=10)
labels_space = kmeans_space.fit_predict(features_space_scaled)

# Assign Cluster Labels to Data
deep_space_classification = pd.DataFrame({
    "Standard FFT Peaks (MHz)": np.round(peak_frequencies_space_standard, 3),
    "COM-Enhanced Peaks (MHz)": np.round(peak_frequencies_space_com, 3),
    "Signal Classification": ["Likely Real" if label == 1 else "Possible Noise" for label in labels_space]
})

# Display Classification Results
tools.display_dataframe_to_user(name="Deep-Space Communication Signal Classification", dataframe=deep_space_classification)