<h2><a href="https://leetcode.com/problems/the-users-that-are-eligible-for-discount">The Users That Are Eligible for Discount</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Table: <code>Purchases</code></p>

<pre>
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| user_id     | int      |
| time_stamp  | datetime |
| amount      | int      |
+-------------+----------+
(user_id, time_stamp) is the primary key (combination of columns with unique values) for this table.
Each row contains information about the purchase time and the amount paid for the user with ID user_id.
</pre>

<p>&nbsp;</p>

<p>A user is eligible for a discount if they had a purchase in the inclusive interval of time <code>[startDate, endDate]</code> with at least <code>minAmount</code> amount. To convert the dates to times, both dates should be considered as the <strong>start</strong> of the day (i.e., <code>endDate = 2022-03-05</code> should be considered as the time <code>2022-03-05 00:00:00</code>).</p>

<p>Write a solution to report the IDs of the users that are eligible for a discount.</p>

<p>Return the result table ordered by <code>user_id</code>.</p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong>
Purchases table:
+---------+---------------------+--------+
| user_id | time_stamp          | amount |
+---------+---------------------+--------+
| 1       | 2022-04-20 09:03:00 | 4416   |
| 2       | 2022-03-19 19:24:02 | 678    |
| 3       | 2022-03-18 12:03:09 | 4523   |
| 3       | 2022-03-30 09:43:42 | 626    |
+---------+---------------------+--------+
startDate = 2022-03-08, endDate = 2022-03-20, minAmount = 1000
<strong>Output:</strong>
+---------+
| user_id |
+---------+
| 3       |
+---------+
<strong>Explanation:</strong>
Out of the three users, only User 3 is eligible for a discount.
 - User 1 had one purchase with at least minAmount amount, but not within the time interval.
 - User 2 had one purchase within the time interval, but with less than minAmount amount.
 - User 3 is the only user who had a purchase that satisfies both conditions.
</pre>

<p>&nbsp;</p>
<p><strong>Important Note:</strong> This problem is basically the same as <a href="https://leetcode.com/problems/the-number-of-users-that-are-eligible-for-discount/">The Number of Users That Are Eligible for Discount</a>.</p>
