import duckdb

con = duckdb.connect("duckdb/jobs.duckdb")

print(con.execute("SHOW TABLES").fetchall())