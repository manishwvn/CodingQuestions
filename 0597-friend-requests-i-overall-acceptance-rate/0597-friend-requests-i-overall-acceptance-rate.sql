SELECT 
    IFNULL(
        ROUND((COUNT(DISTINCT REQUESTER_ID, ACCEPTER_ID)/
              COUNT(DISTINCT SENDER_ID, SEND_TO_ID)), 2), 0.0) AS 'accept_rate'
FROM
    FRIENDREQUEST,
    REQUESTACCEPTED;