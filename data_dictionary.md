# Mutual Fund Analytics - Data Dictionary

## dim_fund

| Column             | Data Type | Source             |
| ------------------ | --------- | ------------------ |
| amfi_code          | INT       | 01_fund_master.csv |
| fund_house         | TEXT      | 01_fund_master.csv |
| scheme_name        | TEXT      | 01_fund_master.csv |
| category           | TEXT      | 01_fund_master.csv |
| sub_category       | TEXT      | 01_fund_master.csv |
| plan               | TEXT      | 01_fund_master.csv |
| launch_date        | DATE      | 01_fund_master.csv |
| benchmark          | TEXT      | 01_fund_master.csv |
| expense_ratio_pct  | FLOAT     | 01_fund_master.csv |
| exit_load_pct      | FLOAT     | 01_fund_master.csv |
| min_sip_amount     | FLOAT     | 01_fund_master.csv |
| min_lumpsum_amount | FLOAT     | 01_fund_master.csv |
| fund_manager       | TEXT      | 01_fund_master.csv |
| risk_category      | TEXT      | 01_fund_master.csv |
| sebi_category_code | TEXT      | 01_fund_master.csv |

## fact_nav

| Column    | Data Type | Source        |
| --------- | --------- | ------------- |
| amfi_code | INT       | clean_nav.csv |
| date      | DATE      | clean_nav.csv |
| nav       | FLOAT     | clean_nav.csv |

## fact_transactions

| Column             | Data Type | Source                 |
| ------------------ | --------- | ---------------------- |
| investor_id        | VARCHAR   | clean_transactions.csv |
| transaction_date   | DATE      | clean_transactions.csv |
| amfi_code          | INT       | clean_transactions.csv |
| transaction_type   | VARCHAR   | clean_transactions.csv |
| amount_inr         | FLOAT     | clean_transactions.csv |
| state              | VARCHAR   | clean_transactions.csv |
| city               | VARCHAR   | clean_transactions.csv |
| city_tier          | VARCHAR   | clean_transactions.csv |
| age_group          | VARCHAR   | clean_transactions.csv |
| gender             | VARCHAR   | clean_transactions.csv |
| annual_income_lakh | FLOAT     | clean_transactions.csv |
| payment_mode       | VARCHAR   | clean_transactions.csv |
| kyc_status         | VARCHAR   | clean_transactions.csv |

## fact_performance

| Column             | Data Type | Source                |
| ------------------ | --------- | --------------------- |
| amfi_code          | INT       | clean_performance.csv |
| scheme_name        | VARCHAR   | clean_performance.csv |
| fund_house         | VARCHAR   | clean_performance.csv |
| category           | VARCHAR   | clean_performance.csv |
| plan               | VARCHAR   | clean_performance.csv |
| return_1yr_pct     | FLOAT     | clean_performance.csv |
| return_3yr_pct     | FLOAT     | clean_performance.csv |
| return_5yr_pct     | FLOAT     | clean_performance.csv |
| benchmark_3yr_pct  | FLOAT     | clean_performance.csv |
| alpha              | FLOAT     | clean_performance.csv |
| beta               | FLOAT     | clean_performance.csv |
| sharpe_ratio       | FLOAT     | clean_performance.csv |
| sortino_ratio      | FLOAT     | clean_performance.csv |
| std_dev_ann_pct    | FLOAT     | clean_performance.csv |
| max_drawdown_pct   | FLOAT     | clean_performance.csv |
| aum_crore          | FLOAT     | clean_performance.csv |
| expense_ratio_pct  | FLOAT     | clean_performance.csv |
| morningstar_rating | INT       | clean_performance.csv |
| risk_grade         | VARCHAR   | clean_performance.csv |

## fact_aum

| Column         | Data Type | Source                   |
| -------------- | --------- | ------------------------ |
| fund_house     | VARCHAR   | 03_aum_by_fund_house.csv |
| aum_crore      | FLOAT     | 03_aum_by_fund_house.csv |
| date           | DATE      | 03_aum_by_fund_house.csv |
| aum_lakh_crore | FLOAT     | 03_aum_by_fund_house.csv |
| num_schemes    | INT       | 03_aum_by_fund_house.csv |
