class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        """
        Solution:
        - Split the string into 2 parts: valid and domain, with '@'
        - Clean local part: by replacing '.' with ''
        - Split the local part into 2 parts: before - after the '+'
        - Add those clean emails to a set -> return len(set)
        """

        emailsSet = set()

        for email in emails:
            # Split name and domain
            parts = email.split('@')
            local = parts[0]
            domain = parts[1]

            # clean name
            localParts = local.split('+')
            cleanEmail = localParts[0].replace('.', '')

            emailsSet.add(f'{cleanEmail}@{domain}')
        
        return len(emailsSet)