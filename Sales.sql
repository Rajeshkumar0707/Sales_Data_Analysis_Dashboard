-- Total sales by category
SELECT category, SUM(Sales) AS total_sales
FROM sales_data
GROUP BY category;

-- Total profit by category
SELECT category, SUM(Profit) AS total_profit
FROM sales_data
GROUP BY category;

-- Monthly sales trend
SELECT Year, Month, SUM(Sales) AS monthly_sales
FROM sales_data
GROUP BY Year, Month
ORDER BY Year, Month;

-- Top 5 products by profit
SELECT product_name, SUM(Profit) AS profit
FROM sales_data
GROUP BY product_name
ORDER BY profit DESC
LIMIT 5;

-- Region-wise performance
SELECT region, SUM(Sales) AS total_sales
FROM sales_data
GROUP BY region;