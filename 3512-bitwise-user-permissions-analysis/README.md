<h2><a href="https://leetcode.com/problems/bitwise-user-permissions-analysis">Bitwise User Permissions Analysis</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Table: <code>user_permissions</code></p>

<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| permissions | int     |
+-------------+---------+
user_id is the primary key.
Each row of this table contains the user ID and their permissions encoded as an integer.
</pre>

<p>Consider that each bit in the <code>permissions</code> integer represents a different access level or feature that a user has.</p>

<p>Write a solution to calculate the following:</p>

<ul>
	<li>common_perms: The access level granted to <strong>all users</strong>. This is computed using a <strong>bitwise AND</strong> operation on the <code>permissions</code> column.</li>
	<li>any_perms: The access level granted to <strong>any user</strong>. This is computed using a <strong>bitwise OR</strong> operation on the <code>permissions</code> column.</li>
</ul>

<p>Return <em>the result table in <strong>any</strong> order</em>.</p>

<p>The result format is shown in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example:</strong></p>

<div class="example-block">
<p><strong>Input:</strong></p>

<p>user_permissions table:</p>

<pre class="example-io">
+---------+-------------+
| user_id | permissions |
+---------+-------------+
| 1       | 5           |
| 2       | 12          |
| 3       | 7           |
| 4       | 3           |
+---------+-------------+
 </pre>

<p><strong>Output:</strong></p>

<pre class="example-io">
+-------------+--------------+
| common_perms | any_perms   |
+--------------+-------------+
| 0            | 15          |
+--------------+-------------+
    </pre>

<p><strong>Explanation:</strong></p>

<ul>
	<li><strong>common_perms:</strong> Represents the bitwise AND result of all permissions:

	<ul>
		<li>For user 1 (5): 5 (binary 0101)</li>
		<li>For user 2 (12): 12 (binary 1100)</li>
		<li>For user 3 (7): 7 (binary 0111)</li>
		<li>For user 4 (3): 3 (binary 0011)</li>
		<li>Bitwise AND: 5 &amp; 12 &amp; 7 &amp; 3 = 0 (binary 0000)</li>
	</ul>
	</li>
	<li><strong>any_perms:</strong> Represents the bitwise OR result of all permissions:
	<ul>
		<li>Bitwise OR: 5 | 12 | 7 | 3 = 15 (binary 1111)</li>
	</ul>
	</li>
</ul>
</div>
