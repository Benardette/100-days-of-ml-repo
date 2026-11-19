
# ==============================================
# HEALTHCARE DATASET: SEABORN HEATMAP & PAIR PLOT
# Feature Correlation Analysis
# ==============================================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. LOAD DATASET
df = pd.read_csv("healthcare_dataset.csv")

print("Dataset shape:", df.shape)
print(df.head())


# 2. DATA PREPARATION
df["Date of Admission"] = pd.to_datetime(
    df["Date of Admission"], errors="coerce"
)

df["Discharge Date"] = pd.to_datetime(
    df["Discharge Date"], errors="coerce"
)

df["Billing Amount"] = pd.to_numeric(
    df["Billing Amount"], errors="coerce"
)

# Create a new feature: Length of Stay
df["Length of Stay"] = (
    df["Discharge Date"] - df["Date of Admission"]
).dt.days

# Remove invalid observations
df = df.dropna(
    subset=[
        "Age",
        "Billing Amount",
        "Length of Stay"
    ]
)

# Keep valid hospital stays
df = df[df["Length of Stay"] >= 0]


# 3. SELECT NUMERICAL FEATURES
features = df[
    [
        "Age",
        "Billing Amount",
        "Length of Stay"
    ]
]

# Calculate correlation matrix
correlation_matrix = features.corr(method="pearson")

print("\nCORRELATION MATRIX:")
print(correlation_matrix)


# ==============================================
# 4. CORRELATION HEATMAP
# ==============================================

sns.set_theme(style="whitegrid")

plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=1,
    linecolor="white",
    square=True,
    vmin=-1,
    vmax=1,
    cbar_kws={
        "label": "Correlation Coefficient"
    }
)

plt.title(
    "Healthcare Features Correlation Heatmap",
    fontsize=16,
    fontweight="bold",
    pad=20
)

plt.xticks(rotation=30, ha="right")
plt.yticks(rotation=0)

plt.tight_layout()
plt.savefig(
    "healthcare_correlation_heatmap.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==============================================
# 5. PAIR PLOT
# ==============================================

# Sample records to make visualization faster
sample_df = df.sample(
    n=min(1500, len(df)),
    random_state=42
)

sns.pairplot(
    data=sample_df,
    vars=[
        "Age",
        "Billing Amount",
        "Length of Stay"
    ],
    hue="Admission Type",
    palette="Set2",
    diag_kind="hist",
    plot_kws={
        "alpha": 0.5,
        "s": 25
    },
    diag_kws={
        "bins": 20
    }
)

plt.suptitle(
    "Healthcare Feature Relationships by Admission Type",
    fontsize=16,
    fontweight="bold",
    y=1.02
)

plt.savefig(
    "healthcare_pairplot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==============================================
# 6. ANALYTICAL SUMMARY
# ==============================================

print("\n===== CORRELATION ANALYSIS =====")

for col in correlation_matrix.columns:
    for row in correlation_matrix.index:
        if col != row:
            if col < row:
                value = correlation_matrix.loc[row, col]

                print(
                    f"{row} vs {col}: {value:.3f}"
                )

print("\nVisualization completed successfully!")

    fontsize=18,
    fontweight="bold"
)

plt.tight_layout()

# Save dashboard as an image
plt.savefig("healthcare_seaborn_analysis.png", dpi=300)

# Display all graphs
plt.show()
