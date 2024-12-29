<h2><a href="https://leetcode.com/problems/find-candidates-for-data-scientist-position-ii">Find Candidates for Data Scientist Position II</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Table: <font face="monospace"><code>Candidates</code></font></p>

<pre>
+--------------+---------+ 
| Column Name  | Type    | 
+--------------+---------+ 
| candidate_id | int     | 
| skill        | varchar |
| proficiency  | int     |
+--------------+---------+
(candidate_id, skill) is the unique key for this table.
Each row includes candidate_id, skill, and proficiency level (1-5).
</pre>

<p>Table: <font face="monospace"><code>Projects</code></font></p>

<pre>
+--------------+---------+ 
| Column Name  | Type    | 
+--------------+---------+ 
| project_id   | int     | 
| skill        | varchar |
| importance   | int     |
+--------------+---------+
(project_id, skill) is the primary key for this table.
Each row includes project_id, required skill, and its importance (1-5) for the project.
</pre>

<p>Leetcode is staffing for multiple data science projects. Write a solution to find the <strong>best candidate</strong> for<strong> each project</strong> based on the following criteria:</p>

<ol>
	<li>Candidates must have <strong>all</strong> the skills required for a project.</li>
	<li>Calculate a <strong>score</strong> for each candidate-project pair as follows:
	<ul>
		<li><strong>Start</strong> with <code>100</code> points</li>
		<li><strong>Add</strong> <code>10</code> points for each skill where <strong>proficiency &gt; importance</strong></li>
		<li><strong>Subtract</strong> <code>5</code> points for each skill where <strong>proficiency &lt; importance</strong></li>
	</ul>
	</li>
</ol>

<p>Include only the top candidate (highest score) for each project. If there&rsquo;s a <strong>tie</strong>, choose the candidate with the <strong>lower</strong> <code>candidate_id</code>. If there is <strong>no suitable candidate</strong> for a project, <strong>do not return</strong>&nbsp;that project.</p>

<p>Return a result table ordered by <code>project_id</code> in ascending order.</p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example:</strong></p>

<div class="example-block">
<p><strong>Input:</strong></p>

<p><code>Candidates</code> table:</p>

<pre class="example-io">
+--------------+-----------+-------------+
| candidate_id | skill     | proficiency |
+--------------+-----------+-------------+
| 101          | Python    | 5           |
| 101          | Tableau   | 3           |
| 101          | PostgreSQL| 4           |
| 101          | TensorFlow| 2           |
| 102          | Python    | 4           |
| 102          | Tableau   | 5           |
| 102          | PostgreSQL| 4           |
| 102          | R         | 4           |
| 103          | Python    | 3           |
| 103          | Tableau   | 5           |
| 103          | PostgreSQL| 5           |
| 103          | Spark     | 4           |
+--------------+-----------+-------------+
</pre>

<p><code>Projects</code> table:</p>

<pre class="example-io">
+-------------+-----------+------------+
| project_id  | skill     | importance |
+-------------+-----------+------------+
| 501         | Python    | 4          |
| 501         | Tableau   | 3          |
| 501         | PostgreSQL| 5          |
| 502         | Python    | 3          |
| 502         | Tableau   | 4          |
| 502         | R         | 2          |
+-------------+-----------+------------+
</pre>

<p><strong>Output:</strong></p>

<pre class="example-io">
+-------------+--------------+-------+
| project_id  | candidate_id | score |
+-------------+--------------+-------+
| 501         | 101          | 105   |
| 502         | 102          | 130   |
+-------------+--------------+-------+
</pre>

<p><strong>Explanation:</strong></p>

<ul>
	<li>For Project 501, Candidate 101 has the highest score of 105. All other candidates have the same score but Candidate 101 has the lowest candidate_id among them.</li>
	<li>For Project 502, Candidate 102 has the highest score of 130.</li>
</ul>

<p>The output table is ordered by project_id in ascending order.</p>
</div>
