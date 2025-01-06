<h2><a href="https://leetcode.com/problems/premier-league-table-ranking-iii">Premier League Table Ranking III</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Table: <code>SeasonStats</code></p>

<pre>
+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| season_id        | int     |
| team_id          | int     |
| team_name        | varchar |
| matches_played   | int     |
| wins             | int     |
| draws            | int     |
| losses           | int     |
| goals_for        | int     |
| goals_against    | int     |
+------------------+---------+
(season_id, team_id) is the unique key for this table.
This table contains season id, team id, team name, matches played, wins, draws, losses, goals scored (goals_for), and goals conceded (goals_against) for each team in each season.
</pre>

<p>Write a solution to calculate the <strong>points</strong>, <strong>goal difference</strong>, and <strong>rank</strong> for <strong>each team</strong> in <strong>each season</strong>. The ranking should be determined as follows:</p>

<ul>
	<li>Teams are first ranked by their total points (highest to lowest)</li>
	<li>If points are tied, teams are then ranked by their goal difference (highest to lowest)</li>
	<li>If goal difference is also tied, teams are then ranked alphabetically by team name</li>
</ul>

<p>Points are calculated as follows:</p>

<ul>
	<li><code>3</code> points for a <strong>win</strong></li>
	<li><code>1</code> point for a <strong>draw</strong></li>
	<li><code>0</code> points for a <strong>loss</strong></li>
</ul>

<p>Goal difference is calculated as: <code>goals_for - goals_against</code></p>

<p>Return <em>the result table ordered&nbsp;by</em> <code>season_id</code> <em>in <strong>ascending</strong> order, then by</em> <code>rank</code> <em>in <strong>ascending</strong> order, and finally by</em> <code>team_name</code> <em>in <strong>ascending</strong> order.</em></p>

<p>The query result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example:</strong></p>

<p><strong>Input:</strong></p>

<p><code>SeasonStats</code> table:</p>

<pre>
+------------+---------+-------------------+----------------+------+-------+--------+-----------+---------------+
| season_id  | team_id | team_name         | matches_played | wins | draws | losses | goals_for | goals_against |
+------------+---------+-------------------+----------------+------+-------+--------+-----------+---------------+
| 2021       | 1       | Manchester City   | 38             | 29   | 6     | 3      | 99        | 26            |
| 2021       | 2       | Liverpool         | 38             | 28   | 8     | 2      | 94        | 26            |
| 2021       | 3       | Chelsea           | 38             | 21   | 11    | 6      | 76        | 33            |
| 2021       | 4       | Tottenham         | 38             | 22   | 5     | 11     | 69        | 40            |
| 2021       | 5       | Arsenal           | 38             | 22   | 3     | 13     | 61        | 48            |
| 2022       | 1       | Manchester City   | 38             | 28   | 5     | 5      | 94        | 33            |
| 2022       | 2       | Arsenal           | 38             | 26   | 6     | 6      | 88        | 43            |
| 2022       | 3       | Manchester United | 38             | 23   | 6     | 9      | 58        | 43            |
| 2022       | 4       | Newcastle         | 38             | 19   | 14    | 5      | 68        | 33            |
| 2022       | 5       | Liverpool         | 38             | 19   | 10    | 9      | 75        | 47            |
+------------+---------+-------------------+----------------+------+-------+--------+-----------+---------------+
</pre>

<p><strong>Output:</strong></p>

<pre>
+------------+---------+-------------------+--------+-----------------+----------+
| season_id  | team_id | team_name         | points | goal_difference | position |
+------------+---------+-------------------+--------+-----------------+----------+
| 2021       | 1       | Manchester City   | 93     | 73              | 1        |
| 2021       | 2       | Liverpool         | 92     | 68              | 2        |
| 2021       | 3       | Chelsea           | 74     | 43              | 3        |
| 2021       | 4       | Tottenham         | 71     | 29              | 4        |
| 2021       | 5       | Arsenal           | 69     | 13              | 5        |
| 2022       | 1       | Manchester City   | 89     | 61              | 1        |
| 2022       | 2       | Arsenal           | 84     | 45              | 2        |
| 2022       | 3       | Manchester United | 75     | 15              | 3        |
| 2022       | 4       | Newcastle         | 71     | 35              | 4        |
| 2022       | 5       | Liverpool         | 67     | 28              | 5        | 
+------------+---------+-------------------+--------+-----------------+----------+
</pre>

<p><strong>Explanation:</strong></p>

<ul>
	<li>For the 2021 season:
	<ul>
		<li>Manchester City has 93 points (29 * 3 + 6 * 1) and a goal difference of 73 (99 - 26).</li>
		<li>Liverpool has 92 points (28 * 3 + 8 * 1) and a goal difference of 68 (94 - 26).</li>
		<li>Chelsea has 74 points (21 * 3 + 11 * 1) and a goal difference of 43 (76 - 33).</li>
		<li>Tottenham has 71 points (22 * 3 + 5 * 1) and a goal difference of 29 (69 - 40).</li>
		<li>Arsenal has 69 points (22 * 3 + 3 * 1) and a goal difference of 13 (61 - 48).</li>
	</ul>
	</li>
	<li>For the 2022 season:
	<ul>
		<li>Manchester City has 89 points (28 * 3 + 5 * 1) and a goal difference of 61 (94 - 33).</li>
		<li>Arsenal has 84 points (26 * 3 + 6 * 1) and a goal difference of 45 (88 - 43).</li>
		<li>Manchester United has 75 points (23 * 3 + 6 * 1) and a goal difference of 15 (58 - 43).</li>
		<li>Newcastle has 71 points (19 * 3 + 14 * 1) and a goal difference of 35 (68 - 33).</li>
		<li>Liverpool has 67 points (19 * 3 + 10 * 1) and a goal difference of 28 (75 - 47).</li>
	</ul>
	</li>
	<li>The teams are ranked first by points, then by goal difference, and finally by team name.</li>
	<li>The output is ordered by season_id ascending, then by rank ascending, and finally by team_name ascending.</li>
</ul>
