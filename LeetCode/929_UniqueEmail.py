# class Solution:
#     def numUniqueEmails(self, emails: List[str]) -> int:
#         valid_emails = set()
#         for email in emails:
#             name, domain = email.split("@")
        
#             n = ""
#             for c in name:
#                 if c == ".":
#                     continue
#                 elif c == "+":
#                     break
#                 n+=c
#             valid_emails.add(n+"@"+domain)
#         print(valid_emails)
#         return len(valid_emails)

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()

        for mail in emails:
            local, domain = mail.split("@")
            local = local.split('+')[0].replace('.', '')
            result.add(local + "@" + domain)

        return len(result)
            
# https://leetcode.com/problems/unique-email-addresses/description/
