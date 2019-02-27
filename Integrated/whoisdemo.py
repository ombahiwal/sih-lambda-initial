import whois

obj = whois.query('admin.com')
print(obj.__dict__)
