import duckdb

con = duckdb.connect("duckdb/jobs.duckdb")

con.execute("""
CREATE OR REPLACE TABLE raw_jobs AS
SELECT *
FROM read_csv_auto('data/bronze/jobs.csv')
""")

print("Loaded")