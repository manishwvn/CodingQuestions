
-- A detailed explanation of the following regular expression solution:

-- '^[A-Za-z]+[A-Za-z0-9\_\.\-]*@leetcode.com'

-- 1. ^ means the beginning of the string
--     - This is important because without it, we can have something like
--     '.shapiro@leetcode.com'
--     This is because *part* of the regex matches the pattern perfectly. 
--     The part that is 'shapiro@leetcode.com'.
--     This is how I understand it: regex will return the whole 
--     thing as long as part of it matches. By adding ^ we are saying: you have to
--     match FROM THE START.
	
-- 2. [] means character set. [A-Z] means any upper case chars. In other words, 
--     the short dash in the character set means range.
	
-- 3. After the first and the second character set, there is a notation: + or *.
--     + means at least one of the character from the preceding charset, and * means 
--     0 or more. 
	
-- 4. \ inside the charset mean skipping. In other words, \. means we want the dot as 
--     it is. Remember, for example, - means range in the character set. So what if
--      we would like to find - itself as a character? use \-. 
	 
-- 5. Everything else, like @leetcode.com refers to exact match.

SELECT * 
FROM Users
WHERE REGEXP_LIKE(mail, '^[a-zA-Z][a-zA-Z0-9._-]*@leetcode\\.com$', 'c');