import duckdb
result = duckdb.sql("select 42 AS answer").fetchall()
print(result)