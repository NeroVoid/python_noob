logs = [
    ["192.168.1.1", "/home"],
    ["192.168.1.2", "/products"],
    ["192.168.1.1", "/products"],
    ["192.168.1.3", "/home"],
    ["192.168.1.2", "/contact"],
    ["192.168.1.1", "/about"],
]

visit_count = 0 #Tracking total visits
url_visits = {} #Tracking visits by url
ip_visits = {} #Tracking visits by IP address

for log in logs:
    ip_address, url = log
    visit_count += 1 
    url_visits[url] = url_visits.get(url, 0) + 1
    ip_visits[ip_address] = ip_visits.get(ip_address, 0) + 1 

top_visitor = max(ip_visits, key=ip_visits.get) #Find the most website visitors by IP address

print(f"Website Access Log\n")
print(f"Total visits: {visit_count}")
for url in url_visits:
    print(f"{url}: {url_visits[url]}")
print(f"Top visitor: {top_visitor} ({ip_visits[top_visitor]} visits)")