# %% [markdown]
# # Analysis with CSV Extracts

# %% [markdown]
# ## This analysis identifies all patients with Prediabetes as well as those within the past year

# %%
# Step 1: Import Necessary Libraries
import pandas as pd
from datetime import datetime

# Step 2: Load Data
conditions_path = "/home/cdsw/exported-data/hl7_condition.csv"
conditions_df = pd.read_csv(conditions_path, quotechar='"')

# Load the patient metadata
patient_pii_path = "/home/cdsw/exported-data/hl7_patient_pii.csv"
patient_metadata_df = pd.read_csv(patient_pii_path, quotechar='"')

# Step 3: Data Preprocessing
def preprocess_data(df):
    for col in df.columns:
        if df[col].dtype == object:
            df[col] = df[col].str.strip('"').str.strip('\'')
    return df

conditions_df = preprocess_data(conditions_df)

# %% [markdown]
# ### Identify all patients with prediabetes

# %%
# Convert 'onsetdatetime' from string to datetime and make it timezone aware
conditions_df['onsetdatetime'] = pd.to_datetime(conditions_df['onsetdatetime'], errors='coerce', utc=True)

# Filter for Prediabetes conditions only, removing the date restriction
conditions_df = conditions_df[
    (conditions_df['condition_display'] == "Prediabetes")
]

# Preprocess the patient metadata (ensure correct data types and stripping extra quotes)
patient_metadata_df = patient_metadata_df[['fullUrl', 'resource_name_0_family', 'resource_name_0_given_0']]

# Join the dataframes
prediabetes_patient_info_df = conditions_df.merge(
    patient_metadata_df,
    left_on='subject_reference',
    right_on='fullUrl',
    how='left'
)

# Make a copy to avoid SettingWithCopyWarning when renaming columns
final_df = prediabetes_patient_info_df[['condition_display', 'subject_reference', 'onsetdatetime', 'encounter_reference', 'resource_name_0_given_0', 'resource_name_0_family']].copy()
final_df.rename(columns={
    'resource_name_0_given_0': 'First Name',
    'resource_name_0_family': 'Last Name'
}, inplace=True)

# Display the final dataframe
print(final_df)

# %% [markdown]
# ### Identify patients with prediabetes in the past year

# %%
# Convert 'onsetdatetime' from string to datetime and make it timezone aware
conditions_df['onsetdatetime'] = pd.to_datetime(conditions_df['onsetdatetime'], errors='coerce', utc=True)
current_date = pd.Timestamp.utcnow()
one_year_ago = current_date - pd.DateOffset(years=1)
conditions_df = conditions_df[
    (conditions_df['condition_display'] == "Prediabetes") &
    (conditions_df['onsetdatetime'] >= one_year_ago)
]

# # Preprocess the patient metadata (ensure correct data types and stripping extra quotes)
patient_metadata_df = patient_metadata_df[['fullUrl', 'resource_name_0_family', 'resource_name_0_given_0']]

# Join the dataframes
prediabetes_patient_info_df = conditions_df.merge(
    patient_metadata_df,
    left_on='subject_reference',
    right_on='fullUrl',
    how='left'
)

# Make a copy to avoid SettingWithCopyWarning when renaming columns
final_df = prediabetes_patient_info_df[['condition_display', 'subject_reference', 'onsetdatetime', 'encounter_reference', 'resource_name_0_given_0', 'resource_name_0_family']].copy()
final_df.rename(columns={
    'resource_name_0_given_0': 'First Name',
    'resource_name_0_family': 'Last Name'
}, inplace=True)

# Display the final dataframe
print(final_df)


