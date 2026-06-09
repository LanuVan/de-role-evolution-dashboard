import duckdb

con = duckdb.connect("../de-role-evolution-dashboard/duckdb/jobs.duckdb")

print(
    con.execute(
        "select * from raw_jobs limit 5"
    ).fetchdf()
)