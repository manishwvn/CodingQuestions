with cte as (
    select
        CONCAT("#", SUBSTRING_INDEX(SUBSTRING_INDEX(tweet, "#", -1), " ", 1)) AS hashtag,
        count(*) as hashtag_count
    from
        tweets
    where
        month(tweet_date) = 2 and year(tweet_date) = 2024
    group by
        hashtag
)

select * from cte order by hashtag_count desc, hashtag desc limit 3;