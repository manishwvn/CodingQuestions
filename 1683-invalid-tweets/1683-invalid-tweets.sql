SELECT 
    TWEET_ID AS 'tweet_id'
FROM 
    TWEETS
WHERE 
    LENGTH(CONTENT) > 15;
    
    