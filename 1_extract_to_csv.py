# %% [markdown]
# # Extract Data from CDW and convert to CSV

# %%
import cml.data_v1 as cmldata

# Set up connection to CDW
CONNECTION_NAME = "default-impala"
conn = cmldata.get_connection(CONNECTION_NAME)

# %% [markdown]
# ## Extract Benefits Data to CSV

# %%
# Export Pandas DataFrame to CSV
SQL_QUERY = "SELECT * FROM nasheb_hl7_demo.benefits"
dataframe = conn.get_pandas_dataframe(SQL_QUERY)

# Uncomment below to observe output
# print(dataframe.head(5))
dataframe.to_csv('/home/cdsw/hl7_benefits.csv', encoding='utf-8', index=False)

# %% [markdown]
# ## Extract Care Team Data to CSV

# %%
# Export Pandas DataFrame to CSV
SQL_QUERY = "SELECT * FROM nasheb_hl7_demo.careteam"
dataframe = conn.get_pandas_dataframe(SQL_QUERY)

# Uncomment below to observe output
# print(dataframe.head(5))
dataframe.to_csv('/home/cdsw/hl7_careteam.csv', encoding='utf-8', index=False)

# %% [markdown]
# ## Extract Claims Data to CSV

# %%
# Export Pandas DataFrame to CSV
SQL_QUERY = "SELECT * FROM nasheb_hl7_demo.claims"
dataframe = conn.get_pandas_dataframe(SQL_QUERY)

# Uncomment below to observe output
# print(dataframe.head(5))
dataframe.to_csv('/home/cdsw/hl7_claims.csv', encoding='utf-8', index=False)

# %% [markdown]
# ## Extract Condition Data to CSV

# %%
# Export Pandas DataFrame to CSV
SQL_QUERY = "SELECT * FROM nasheb_hl7_demo.`condition`"
dataframe = conn.get_pandas_dataframe(SQL_QUERY)

# Uncomment below to observe output
# print(dataframe.head(5))
dataframe.to_csv('/home/cdsw/hl7_condition.csv', encoding='utf-8', index=False)

# %%
# Closing the connection
conn.close()


