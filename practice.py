import sqlite3
import pandas as pd

connection = sqlite3.connect('data.sqlite')

product_data = pd.read_sql("""
SELECT *
    FROM products;
""", connection)

# print(product_data)

last_five_items = pd.read_sql(
    """
SELECT productCode, productName
FROM products
""", connection
).tail()
# print(last_five_items)


# planes filter
product_by_line = pd.read_sql(
    """
SELECT productName, productLine,
    CASE
    WHEN productLine = "Planes" THEN "planes"
    ELSE "NOT Planes"
    END AS Planes
FROM products
""", connection
).tail(20)
# print(product_by_line)

# Length of the product description
product_desc_len = pd.read_sql(
    """
    SELECT length(productDescription) AS description_length
    FROM products;

""", connection
).head()
# print(product_desc_len)

# all caps for vendors(first 5)
vendors = pd.read_sql(
    """
    SELECT UPPER(productVendor) AS caps_vendor
    FROM products;
""", connection
).head()

# print(vendors)

lower_names = pd.read_sql(
    """
    SELECT LOWER(productName) AS lower_name
    FROM products;
""", connection
).head()

# print(lower_names)

substring = pd.read_sql(
    """
    SELECT substr(productScale, 3, 3) AS non
    FROM products
""", connection
).tail(10)
# print(substring)


# concantinate
full_name = pd.read_sql(
    """
SELECT productVendor || " " || productName AS fullName
FROM products;
""", connection
).head(10)

# print(full_name)

round_diff = pd.read_sql(
    """
SELECT CAST(round(MSRP - buyPrice) AS INTEGER) AS round_diff
FROM products;
""", connection
)
print(round_diff)



connection.close()