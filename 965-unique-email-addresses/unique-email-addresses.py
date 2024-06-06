class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        count = 0
        uniques = set()
        for email in emails:
            local, domain = email.split('@')
            s = ''
            for i in range(len(local)):
                if local[i] == '.':
                    continue
                if local[i] == '+':
                    break
                s += local[i]
            uniques.add(s + '@' + domain)
        
        print(uniques)
        return len(uniques)

                







        