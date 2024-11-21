# %% [markdown]
# # Extract Data from CDW and convert to CSV

# %%
import cml.data_v1 as cmldata

# Set up connection to CDW
CONNECTION_NAME = "default-impala"
conn = cmldata.get_connection(CONNECTION_NAME)

# %% [markdown]
# ## Extract Data Tables from CDW to Pandas DataFrame

# %%
BENEFITS_SQL_QUERY = "SELECT * FROM nasheb_hl7_demo.benefits"
benefits_df = conn.get_pandas_dataframe(BENEFITS_SQL_QUERY)

CARETEAM_SQL_QUERY = "SELECT * FROM nasheb_hl7_demo.careteam"
careteam_df = conn.get_pandas_dataframe(CARETEAM_SQL_QUERY)

CLAIMS_SQL_QUERY = "SELECT * FROM nasheb_hl7_demo.claims"
claims_df = conn.get_pandas_dataframe(CLAIMS_SQL_QUERY)

CONDITION_SQL_QUERY = "SELECT * FROM nasheb_hl7_demo.`condition`"
condition_df = conn.get_pandas_dataframe(CONDITION_SQL_QUERY)
print(condition_df)

# Closing the connection
conn.close()


