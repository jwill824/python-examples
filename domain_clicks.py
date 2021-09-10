import unittest

def countingSubDomainClicks(domain_counts):
    click_map = {}
    
    for click_domain in domain_counts:
        click_count = int(click_domain.split(",")[0])
        domain = click_domain.split(",")[1]
        
        n = len(domain.split("."))
        
        subdomains = []
        
        for i in range(n):
            subdomains.append(".".join(domain.split(".")[i:]))
            
            
        for subdomain in subdomains:
            if subdomain not in click_map:
                click_map[subdomain] = click_count
            else:
                click_map[subdomain] += click_count
            
    print (click_map)

class test(unittest.TestCase):
    def test_one(self):
        domain_counts = ["900,google.com", "60,mail.yahoo.com", "10,mobile.sports.yahoo.com", "40,sports.yahoo.com", "300,yahoo.com", "10,stackoverflow.com", "20,overflow.com", "5,com.com", "2,en.wikipdia.org", "1,m.wikipedia.org", "1,mobile.sports", "1,google.co.uk"]
        subdomain_counts = []
        countingSubDomainClicks(domain_counts)
        # self.assertEqual(subdomain_counts, countingSubDomainClicks(domain_counts))

if __name__ == '__main__':
    unittest.main()