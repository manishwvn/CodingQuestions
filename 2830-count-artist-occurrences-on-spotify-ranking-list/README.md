<h2><a href="https://leetcode.com/problems/count-artist-occurrences-on-spotify-ranking-list">Count Artist Occurrences On Spotify Ranking List</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Table: <code><font face="monospace">Spotify</font></code></p>

<pre>
+-------------+---------+ 
| Column Name | Type    | 
+-------------+---------+ 
| id          | int     | 
| track_name  | varchar |
| artist      | varchar |
+-------------+---------+
<code>id</code> is the primary key (column with unique values) for this table.
Each row contains an id, track_name, and artist.
</pre>

<p>Write a solution to find how many times each artist appeared on the Spotify ranking list.</p>

<p>Return the result table having the artist&#39;s name along with the corresponding number of occurrences&nbsp;ordered by occurrence count in&nbsp;<strong>descending </strong>order. If the occurrences are equal, then it&rsquo;s ordered by the artist&rsquo;s name in <strong>ascending</strong> order.</p>

<p>The result format is in the following example​​​​​.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:
</strong>Spotify table: 
+---------+--------------------+------------+ 
| id      | track_name         | artist     |  
+---------+--------------------+------------+
| 303651  | Heart Won&#39;t Forget | Sia        |
| 1046089 | Shape of you       | Ed Sheeran |
| 33445   | I&#39;m the one        | DJ Khalid  |
| 811266  | Young Dumb &amp; Broke | DJ Khalid  | 
| 505727  | Happier            | Ed Sheeran |
+---------+--------------------+------------+ 
<strong>Output:
</strong>+------------+-------------+
| artist     | occurrences | 
+------------+-------------+
| DJ Khalid  | 2           |
| Ed Sheeran | 2           |
| Sia        | 1           | 
+------------+-------------+ 

<strong>Explanation: </strong>The count of occurrences is listed in descending order under the column name &quot;occurrences&quot;. If the number of occurrences is the same, the artist&#39;s names are sorted in ascending order.
</pre>
