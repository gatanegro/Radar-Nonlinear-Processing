# Step 2: Classifying Detected Signals (Real vs. Noise) Using AI-Based Filtering

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Prepare Data for Clustering
features = np.column_stack((peak_frequencies_standard, peak_frequencies_com))
features = np.nan_to_num(features)  # Handle NaN values

# Normalize Data for Clustering
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Apply K-Means Clustering (2 Clusters: Real Signals vs. Noise)
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
labels = kmeans.fit_predict(features_scaled)

# Assign Cluster Labels to Data
frequency_classification = pd.DataFrame({
    "Standard FFT Peaks (MHz)": np.round(peak_frequencies_standard, 3),
    "COM-Enhanced Peaks (MHz)": np.round(peak_frequencies_com, 3),
    "Signal Classification": ["Likely Real" if label == 1 else "Possible Noise" for label in labels]
})

# Display Classification Results
tools.display_dataframe_to_user(name="Signal Classification Results", dataframe=frequency_classification)
STDOUT/STDERR
/home/sandbox/.local/lib/python3.11/site-packages/pandas/core/internals/blocks.py:2323: RuntimeWarning: invalid value encountered in cast
values = values.astype(str)
