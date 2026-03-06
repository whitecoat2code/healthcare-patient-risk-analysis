import pandas as pd

# Read
df = pd.read_csv("dataset.csv")

print("Total patients:", len(df))
print("\nFirst 5 rows:")
print(df.head())

# High risk
high_risk = df[(df["age"] > 50) & (df["bp"] > 140)]
print("\nHigh Risk Patients (age>50 and bp>140):")
print(high_risk.to_string(index=False))

# Counts
print("\nOutcome distribution (all patients):")
print(df["outcome"].value_counts().to_string())

print("\nOutcome distribution (high risk patients):")
print(high_risk["outcome"].value_counts().to_string())

# Simple aggregate: average BP by age group buckets (decades)
df["age_decade"] = (df["age"] // 10) * 10
avg_bp = df.groupby("age_decade")["bp"].mean().reset_index()
print("\nAverage BP by age decade:")
print(avg_bp.to_string(index=False))

# Save high_risk to CSV for reference
high_risk.to_csv("high_risk_patients.csv", index=False)
print("\nSaved high_risk_patients.csv")