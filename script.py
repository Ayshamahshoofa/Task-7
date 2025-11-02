import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# connect
conn = sqlite3.connect("sales_data.db")

# SQL query: total quantity and revenue per product
query = """
SELECT 
    product, 
    SUM(quantity) AS total_quantity,
    SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY product
ORDER BY total_revenue DESC
"""

# load to pandas
df = pd.read_sql_query(query, conn)

print("✅ Sales Summary:")
print(df.to_string(index=False))

# plot revenue by product
ax = df.plot(kind="bar", x="product", y="total_revenue", legend=False)
ax.set_title("Revenue by Product")
ax.set_xlabel("Product")
ax.set_ylabel("Revenue (INR)")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()

conn.close()
