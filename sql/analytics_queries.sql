-- 1. Get total transaction volume per user
SELECT u.full_name, COUNT(t.transaction_id) AS total_transactions, SUM(t.amount) AS total_amount_transferred
FROM users u
JOIN accounts a ON u.user_id = a.user_id
JOIN transactions t ON a.account_id = t.sender_account_id
GROUP BY u.full_name
ORDER BY total_amount_transferred DESC;

-- 2. Find high-risk flagged transactions
SELECT t.transaction_id, t.amount, t.timestamp, f.risk_score, f.is_fraudulent
FROM transactions t
JOIN fraud_logs f ON t.transaction_id = f.transaction_id
WHERE f.is_fraudulent = TRUE;

-- 3. Get active account balances overview
SELECT u.full_name, a.account_type, a.balance
FROM users u
JOIN accounts a ON u.user_id = a.user_id
WHERE a.is_active = TRUE;ha complete 