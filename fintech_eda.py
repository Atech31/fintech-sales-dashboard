# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import glob

# Set visual styles
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# 1. Automatically locate the Excel file in the project folder or subfolders
excel_files = glob.glob('**/*.xlsx', recursive=True)
if not excel_files:
    raise FileNotFoundError("No .xlsx files found in this folder! Please make sure your SalesData.xlsx file is saved here.")

print(f"-> Automatically detected Excel file: {excel_files[0]}")
df = pd.read_excel(excel_files[0])

print("\n--- Dataset Info ---")
print(df.info())
print("\n--- First 5 Rows ---")
print(df.head())

# ==========================================
# 2. Automated Missing-Value Handling
# ==========================================
print("\n--- Missing Values Before Cleaning ---")
print(df.isnull().sum())

# Fill numerical missing values with median, categorical with 'Unknown'
for col in df.select_dtypes(include=[np.number]).columns:
    df[col] = df[col].fillna(df[col].median())

for col in df.select_dtypes(include=[object]).columns:
    df[col] = df[col].fillna('Unknown')

print("\n--- Missing Values After Cleaning ---")
print(df.isnull().sum())


# ==========================================
# 3. Outlier Detection via IQR (Interquartile Range)
# ==========================================
def detect_outliers_iqr(data, column):
    if column not in data.columns:
        print(f"\nColumn '{column}' not found in dataset. Skipping IQR check.")
        return pd.DataFrame()
    
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    print(f"\nOutliers detected in '{column}': {len(outliers)} rows found outside [{lower_bound:.2f}, {upper_bound:.2f}]")
    return outliers

# Safely check for transaction amount column variant
amount_col = 'Amount ($)' if 'Amount ($)' in df.columns else 'Amount'
if amount_col in df.columns:
    amount_outliers = detect_outliers_iqr(df, amount_col)


# ==========================================
# 4. Summary Statistical Calculations
# ==========================================
print("\n--- Summary Statistics (Numerical Columns) ---")
print(df.describe())


# ==========================================
# 5. Correlation Heatmap Generation
# ==========================================
plt.figure(figsize=(8, 6))
numerical_df = df.select_dtypes(include=[np.number])

if not numerical_df.empty:
    correlation_matrix = numerical_df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='Blues', fmt=".2f", linewidths=0.5)
    plt.title("FinTech Dataset - Correlation Heatmap", fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
else:
    print("\nNo numerical columns available to generate correlation heatmap.")