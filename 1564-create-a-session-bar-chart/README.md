<h2><a href="https://leetcode.com/problems/create-a-session-bar-chart">Create a Session Bar Chart</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Table: <code>Sessions</code></p>

<pre>
+---------------------+---------+
| Column Name         | Type    |
+---------------------+---------+
| session_id          | int     |
| duration            | int     |
+---------------------+---------+
session_id is the column of unique values for this table.
duration is the time in seconds that a user has visited the application.
</pre>

<p>&nbsp;</p>

<p>You want to know how long a user visits your application. You decided to create bins of <code>&quot;[0-5&gt;&quot;</code>, <code>&quot;[5-10&gt;&quot;</code>, &quot;[10-15&gt;&quot;, and <code>&quot;15 minutes or more&quot;</code> and count the number of sessions on it.</p>

<p>Write a solution to report the <code>(bin, total)</code>.</p>

<p>Return the result table in <strong>any order</strong>.</p>

<p>The&nbsp;result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
Sessions table:
+-------------+---------------+
| session_id  | duration      |
+-------------+---------------+
| 1           | 30            |
| 2           | 199           |
| 3           | 299           |
| 4           | 580           |
| 5           | 1000          |
+-------------+---------------+
<strong>Output:</strong> 
+--------------+--------------+
| bin          | total        |
+--------------+--------------+
| [0-5&gt;        | 3            |
| [5-10&gt;       | 1            |
| [10-15&gt;      | 0            |
| 15 or more   | 1            |
+--------------+--------------+
<strong>Explanation:</strong> 
For session_id 1, 2, and 3 have a duration greater or equal than 0 minutes and less than 5 minutes.
For session_id 4 has a duration greater or equal than 5 minutes and less than 10 minutes.
There is no session with a duration greater than or equal to 10 minutes and less than 15 minutes.
For session_id 5 has a duration greater than or equal to 15 minutes.
</pre>
