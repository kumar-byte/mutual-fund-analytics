--Query 1: Total number of funds
SELECT COUNT(*) AS total_funds
FROM dim_fund;


--Query 2: Top 10 funds by 5-year return
SELECT
    scheme_name,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;


--Query 3: Average NAV
SELECT AVG(nav) AS avg_nav
FROM fact_nav;


--Query 4: Total transaction amount
SELECT SUM(amount_inr) AS total_transaction_amount
FROM fact_transactions;


--Query 5: Transaction count by type
SELECT
    transaction_type,
    COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY transaction_type;


--Query 6: Category-wise average return
SELECT
    category,
    AVG(return_5yr_pct) AS avg_return
FROM fact_performance
GROUP BY category
ORDER BY avg_return DESC;


--Query 7: Top fund houses by AUM
SELECT
    fund_house,
    aum_crore
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 10;


--Query 8: Average Sharpe Ratio
SELECT AVG(sharpe_ratio) AS avg_sharpe_ratio
FROM fact_performance;


--Query 9: Investor count by gender
SELECT
    gender,
    COUNT(*) AS investor_count
FROM fact_transactions
GROUP BY gender;


--Query 10: State-wise transaction amount
SELECT
    state,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;