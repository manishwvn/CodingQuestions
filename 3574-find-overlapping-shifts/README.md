<h2><a href="https://leetcode.com/problems/find-overlapping-shifts">Find Overlapping Shifts</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Table: <code>EmployeeShifts</code></p>

<pre>
+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| employee_id      | int     |
| start_time       | time    |
| end_time         | time    |
+------------------+---------+
(employee_id, start_time) is the unique key for this table.
This table contains information about the shifts worked by employees, including the start and end times on a specific date.
</pre>

<p>Write a solution to count the number of <strong>overlapping shifts</strong> for each employee. Two shifts are considered overlapping if one shift&rsquo;s <code>end_time</code> is <strong>later than</strong> another shift&rsquo;s <code>start_time</code>.</p>

<p><em>Return the result table ordered by</em> <code>employee_id</code> <em>in <strong>ascending</strong> order</em>.</p>

<p>The query result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example:</strong></p>

<div class="example-block">
<p><strong>Input:</strong></p>

<p><code>EmployeeShifts</code> table:</p>

<pre class="example-io">
+-------------+------------+----------+
| employee_id | start_time | end_time |
+-------------+------------+----------+
| 1           | 08:00:00   | 12:00:00 |
| 1           | 11:00:00   | 15:00:00 |
| 1           | 14:00:00   | 18:00:00 |
| 2           | 09:00:00   | 17:00:00 |
| 2           | 16:00:00   | 20:00:00 |
| 3           | 10:00:00   | 12:00:00 |
| 3           | 13:00:00   | 15:00:00 |
| 3           | 16:00:00   | 18:00:00 |
| 4           | 08:00:00   | 10:00:00 |
| 4           | 09:00:00   | 11:00:00 |
+-------------+------------+----------+
</pre>

<p><strong>Output:</strong></p>

<pre class="example-io">
+-------------+--------------------+
| employee_id | overlapping_shifts |
+-------------+--------------------+
| 1           | 2                  |
| 2           | 1                  |
| 4           | 1                  |
+-------------+--------------------+
</pre>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Employee 1 has 3 shifts:
	<ul>
		<li>08:00:00 to 12:00:00</li>
		<li>11:00:00 to 15:00:00</li>
		<li>14:00:00 to 18:00:00</li>
	</ul>
	The first shift overlaps with the second, and the second overlaps with the third, resulting in 2 overlapping shifts.</li>
	<li>Employee 2 has 2 shifts:
	<ul>
		<li>09:00:00 to 17:00:00</li>
		<li>16:00:00 to 20:00:00</li>
	</ul>
	These shifts overlap with each other, resulting in 1 overlapping shift.</li>
	<li>Employee 3 has 3 shifts:
	<ul>
		<li>10:00:00 to 12:00:00</li>
		<li>13:00:00 to 15:00:00</li>
		<li>16:00:00 to 18:00:00</li>
	</ul>
	None of these shifts overlap, so Employee 3 is not included in the output.</li>
	<li>Employee 4 has 2 shifts:
	<ul>
		<li>08:00:00 to 10:00:00</li>
		<li>09:00:00 to 11:00:00</li>
	</ul>
	These shifts overlap with each other, resulting in 1 overlapping shift.</li>
</ul>

<p>The output shows the employee_id and the count of overlapping shifts for each employee who has at least one overlapping shift, ordered by employee_id in ascending order.</p>
</div>
