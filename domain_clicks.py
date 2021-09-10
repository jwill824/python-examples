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

    return click_map


class test(unittest.TestCase):
    def test_one(self):
        domain_counts = ["900,google.com", "60,mail.yahoo.com", "10,mobile.sports.yahoo.com", "40,sports.yahoo.com", "300,yahoo.com",
                         "10,stackoverflow.com", "20,overflow.com", "5,com.com", "2,en.wikipdia.org", "1,m.wikipedia.org", "1,mobile.sports", "1,google.co.uk"]
        click_map = {'google.com': 900, 'com': 1345, 'mail.yahoo.com': 60, 'yahoo.com': 410, 'mobile.sports.yahoo.com': 10, 'sports.yahoo.com': 50, 'stackoverflow.com': 10, 'overflow.com': 20, 'com.com': 5,
                         'en.wikipdia.org': 2, 'wikipdia.org': 2, 'org': 3, 'm.wikipedia.org': 1, 'wikipedia.org': 1, 'mobile.sports': 1, 'sports': 1, 'google.co.uk': 1, 'co.uk': 1, 'uk': 1}
        self.assertEqual(click_map, countingSubDomainClicks(domain_counts))


if __name__ == '__main__':
    unittest.main()
