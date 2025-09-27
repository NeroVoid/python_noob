# This script helps create an overview analysis of the results of an email marketing campaign

campaign_data = [
    ["alice@gmail.com", True, False],
    ["bob@yahoo.com", True, True],
    ["charlie@outlook.com", False, False],
    ["diana@gmail.com", True, False],
    ["eric@yahoo.com", False, False],
    ["fiona@gmail.com", True, True],
]

total_sent = 0 #Tracking total emails sent
opened_count = 0 #Tracking number of emails opened
clicked_count = 0 #Tracking the number of emails having clicks by recipients
domain_count = {}

for record in campaign_data:
    if len(record) == 3: #Check that the record contains all the necessary information.
        email, opened, clicked = record
       #Check the value type of each element of the record
        if (
            isinstance(email,str) and isinstance(email,str) and email.strip() != "" and
            isinstance(opened,bool) and isinstance(clicked,bool)
        ):
            total_sent += 1
            
            if opened == True:
                opened_count += 1
                
                if clicked == True:
                    clicked_count += 1
                
                domain = email.strip().split("@")[1] #Get email domain of opened emails
                #Counting emails opened by domain
                if domain in domain_count:
                    domain_count[domain] = domain_count.get(domain, 0) + 1
                else:
                    domain_count[domain] = 1
                
#Percentage of emails opened out of total emails sent
open_rate = f"{opened_count/total_sent:.0%}" 

#Percentage of emails that recipients click on the content out of total number of emails sent
click_rate = f"{clicked_count/total_sent:.0%}" 

#Find out which domain has the most opened emails out of the total opened emails and its open rate
popular_domain = max(domain_count, key=domain_count.get) 
highest_open_rate = f"{domain_count[popular_domain]/opened_count:.0%}"

print(f"Email marketing campaign report")
print(f"Total email sent: {total_sent} \n"
      f"Total email opened: {opened_count} \n"
      f"Open rate: {open_rate} \n"
      f"Total link clicked: {clicked_count} \n"
      f"Click rate: {click_rate} \n"
      f"Emails from {popular_domain} had the highest open rate, making up {highest_open_rate} of all opened emails.")