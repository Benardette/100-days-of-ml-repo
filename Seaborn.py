# ============================================
# SEABORN DATA VISUALIZATION
# Healthcare Dataset
# Distribution Plots, Box Plots and Heatmaps
# ============================================

# 1. IMPORT LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2. LOAD DATASET
df = pd.read_csv("healthcare_dataset.csv")

# 3. PREPARE DATA
df["Date of Admission"] = pd.to_datetime(df["Date of Admission"])
df["Discharge Date"] = pd.to_datetime(df["Discharge Date"])

# Calculate hospital stay duration in days
df["Stay Duration"] = (
    df["Discharge Date"] - df["Date of Admission"]
).dt.days

# Set Seaborn style and blue colour palette
sns.set_theme(style="whitegrid")

gender_palette = {
    "Male": "#1769AA",
    "Female": "#75B9E7"
}

# 4. CREATE VISUALIZATION DASHBOARD
fig, axes = plt.subplots(2, 3, figsize=(20, 12))

# --------------------------------------------
# GRAPH 1: AGE DISTRIBUTION
# --------------------------------------------
sns.histplot(
    data=df,
    x="Age",
    hue="Gender",
    bins=20,
    kde=True,
    palette=gender_palette,
    alpha=0.5,
    ax=axes[0, 0]
)

axes[0, 0].set_title("Age Distribution by Gender")
axes[0, 0].set_xlabel("Age")
axes[0, 0].set_ylabel("Number of Patients")

# --------------------------------------------
# GRAPH 2: BILLING AMOUNT DISTRIBUTION
# --------------------------------------------
sns.histplot(
    data=df,
    x="Billing Amount",
    bins=30,
    color="#1769AA",
    kde=True,
    ax=axes[0, 1]
)

axes[0, 1].set_title("Distribution of Hospital Billing")
axes[0, 1].set_xlabel("Billing Amount")
axes[0, 1].set_ylabel("Frequency")

# --------------------------------------------
# GRAPH 3: BOX PLOT - BILLING BY GENDER
# --------------------------------------------
sns.boxplot(
    data=df,
    x="Gender",
    y="Billing Amount",
    hue="Gender",
    palette=gender_palette,
    legend=False,
    ax=axes[0, 2]
)

axes[0, 2].set_title("Billing Amount by Gender")
axes[0, 2].set_xlabel("Gender")
axes[0, 2].set_ylabel("Billing Amount")

# --------------------------------------------
# GRAPH 4: BOX PLOT - AGE BY MEDICAL CONDITION
# --------------------------------------------
sns.boxplot(
    data=df,
    x="Medical Condition",
    y="Age",
    color="#2685C5",
    ax=axes[1, 0]
)

axes[1, 0].set_title("Age Distribution by Medical Condition")
axes[1, 0].set_xlabel("Medical Condition")
axes[1, 0].set_ylabel("Age")
axes[1, 0].tick_params(axis="x", rotation=45)

# --------------------------------------------
# GRAPH 5: CORRELATION HEATMAP
# --------------------------------------------
numeric_columns = [
    "Age",
    "Billing Amount",
    "Stay Duration"
]

correlation = df[numeric_columns].corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="Blues",
    fmt=".2f",
    linewidths=0.5,
    vmin=-1,
    vmax=1,
    ax=axes[1, 1]
)

axes[1, 1].set_title("Correlation Between Numerical Variables")

# --------------------------------------------
# GRAPH 6: MEDICAL CONDITIONS BY GENDER
# --------------------------------------------
condition_gender = pd.crosstab(
    df["Medical Condition"],
    df["Gender"]
)

sns.heatmap(
    condition_gender,
    annot=True,
    fmt="d",
    cmap="Blues",
    linewidths=0.5,
    ax=axes[1, 2]
)

axes[1, 2].set_title("Medical Conditions by Gender")
axes[1, 2].set_xlabel("Gender")
axes[1, 2].set_ylabel("Medical Condition")

# --------------------------------------------
# 5.DASHBOARD SETTINGS
# --------------------------------------------
plt.suptitle(
    "HEALTHCARE DATA VISUALIZATION DASHBOARD",
    fontsize=18,
    fontweight="bold"
)

plt.tight_layout()

# Save dashboard as an image
plt.savefig("healthcare_seaborn_analysis.png", dpi=300)

# Display all graphs
plt.show()
