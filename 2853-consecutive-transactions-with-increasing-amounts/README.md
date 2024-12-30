<h2><a href="https://leetcode.com/problems/consecutive-transactions-with-increasing-amounts">Consecutive Transactions with Increasing Amounts</a></h2> <img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' /><hr><p>Table: <code>Transactions</code></p>

<pre>
+------------------+------+
| Column Name      | Type |
+------------------+------+
| transaction_id   | int  |
| customer_id      | int  |
| transaction_date | date |
| amount           | int  |
+------------------+------+
transaction_id is the primary key of this table. 
Each row contains information about transactions that includes unique (customer_id, transaction_date) along with the corresponding customer_id and amount.  
</pre>

<p>Write an SQL query to find the customers who have made consecutive transactions with increasing <code>amount</code>&nbsp;for at least three consecutive days. Include the <code>customer_id</code>,&nbsp;start date of the consecutive transactions&nbsp;period and the end date of the consecutive transactions period. There can be multiple consecutive transactions by a customer.</p>

<p>Return <em>the result table ordered by</em> <code>customer_id</code> <em>in <strong>ascending</strong> order.</em></p>

<p>The query result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong>&nbsp;
Transactions table:
+----------------+-------------+------------------+--------+
| transaction_id | customer_id | transaction_date | amount |
+----------------+-------------+------------------+--------+
| 1 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;| 101 &nbsp; &nbsp; &nbsp; &nbsp; | 2023-05-01 &nbsp; &nbsp; &nbsp; | 100 &nbsp; &nbsp;|
| 2 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;| 101 &nbsp; &nbsp; &nbsp; &nbsp; | 2023-05-02 &nbsp; &nbsp; &nbsp; | 150 &nbsp; &nbsp;|
| 3 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;| 101 &nbsp; &nbsp; &nbsp; &nbsp; | 2023-05-03 &nbsp; &nbsp; &nbsp; | 200 &nbsp; &nbsp;|
| 4 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;| 102 &nbsp; &nbsp; &nbsp; &nbsp; | 2023-05-01 &nbsp; &nbsp; &nbsp; | 50 &nbsp; &nbsp; |
| 5 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;| 102 &nbsp; &nbsp; &nbsp; &nbsp; | 2023-05-03 &nbsp; &nbsp; &nbsp; | 100 &nbsp; &nbsp;|
| 6 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;| 102 &nbsp; &nbsp; &nbsp; &nbsp; | 2023-05-04 &nbsp; &nbsp; &nbsp; | 200 &nbsp; &nbsp;|
| 7 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;| 105 &nbsp; &nbsp; &nbsp; &nbsp; | 2023-05-01 &nbsp; &nbsp; &nbsp; | 100 &nbsp; &nbsp;|
| 8 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;| 105 &nbsp; &nbsp; &nbsp; &nbsp; | 2023-05-02 &nbsp; &nbsp; &nbsp; | 150 &nbsp; &nbsp;|
| 9 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;| 105 &nbsp; &nbsp; &nbsp; &nbsp; | 2023-05-03 &nbsp; &nbsp; &nbsp; | 200 &nbsp; &nbsp;|
| 10 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | 105 &nbsp; &nbsp; &nbsp; &nbsp; | 2023-05-04 &nbsp; &nbsp; &nbsp; | 300 &nbsp; &nbsp;|
| 11 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | 105 &nbsp; &nbsp; &nbsp; &nbsp; | 2023-05-12 &nbsp; &nbsp; &nbsp; | 250 &nbsp; &nbsp;|
| 12 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | 105 &nbsp; &nbsp; &nbsp; &nbsp; | 2023-05-13 &nbsp; &nbsp; &nbsp; | 260 &nbsp; &nbsp;|
| 13 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | 105 &nbsp; &nbsp; &nbsp; &nbsp; | 2023-05-14 &nbsp; &nbsp; &nbsp; | 270 &nbsp; &nbsp;|
+----------------+-------------+------------------+--------+
<strong>Output:</strong>&nbsp;
+-------------+-------------------+-----------------+
| customer_id | consecutive_start | consecutive_end |&nbsp;
+-------------+-------------------+-----------------+
| 101 &nbsp; &nbsp; &nbsp; &nbsp; |&nbsp; 2023-05-01 &nbsp; &nbsp; &nbsp; |&nbsp;2023-05-03 &nbsp; &nbsp; &nbsp;|&nbsp;
| 105 &nbsp; &nbsp; &nbsp; &nbsp; |&nbsp; 2023-05-01 &nbsp; &nbsp; &nbsp; |&nbsp;2023-05-04 &nbsp; &nbsp; &nbsp;|
| 105 &nbsp; &nbsp; &nbsp; &nbsp; |&nbsp; 2023-05-12 &nbsp; &nbsp; &nbsp; |&nbsp;2023-05-14 &nbsp; &nbsp; &nbsp;|&nbsp;
+-------------+-------------------+-----------------+
<strong>Explanation:</strong>&nbsp;
- customer_id 101 has made consecutive transactions with increasing amounts from May 1st, 2023, to May 3rd, 2023
- customer_id 102 does not have any consecutive transactions for at least 3 days.&nbsp;
- customer_id 105 has two sets of consecutive transactions: from May 1st, 2023, to May 4th, 2023, and from May 12th, 2023, to May 14th, 2023.&nbsp;
customer_id is sorted in ascending order.
</pre>

<p>&nbsp;</p>
