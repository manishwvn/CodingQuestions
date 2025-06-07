class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        def dfs(email, collected, account_graph, visited):
            if email in visited:
                return
            
            visited.add(email)
            collected.append(email)
            for neighbor in account_graph[email]:
                dfs(neighbor, collected, account_graph, visited)

        account_graph = defaultdict(list)
        email_to_name = {}

        for account in accounts:
            name = account[0]
            emails = account[1:]

            for email in emails:
                email_to_name[email] = name
                if email not in account_graph:
                    account_graph[email] = []

            first_email = emails[0]
            for email in emails[1:]:
                account_graph[first_email].append(email)
                account_graph[email].append(first_email)

        print(account_graph)
        print(email_to_name)

        visited = set()
        result = []

        for email in email_to_name:
            if email not in visited:
                collected = []
                dfs(email, collected, account_graph, visited)

                temp = [email_to_name[email]]
                collected.sort()
                for email in collected:
                    temp.append(email)
            
                result.append(temp)

        return result
