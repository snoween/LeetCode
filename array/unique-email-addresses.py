class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        uniqueMails = set()

        for mail in emails:
            local, domain = mail.split('@')

            # clean local part
            local = local.split('+')[0]
            local = local.replace('.', '')
            # merge mail
            uniqueMails.add(f'{local}@{domain}')
        
        return len(uniqueMails)
        