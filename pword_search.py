"""
    @Author: Tolarian Ninja
    @Instructions: 1) Export data vault from password manager and copy column
                      with site URLs into a text file, save as sites.txt
                   2) Put sites.txt, breached.txt and pword_search.py into same
                      directory.
                   3) Run pword_search.py to get list of all breached sites in
                      sites.txt, google those sites to check when the breach was

"""

breached_sites = []
pword_sites = []
breached_pwords = []
    

def populate_lists():
    breached = open("breached.txt")
    pwords = open("sites.txt")
    for site in breached:
        breached_sites.append(site.strip())
    for passwrd in pwords:
        pword_sites.append(passwrd.strip())
    
def check_breach():
    for pass_site in pword_sites:
        for b_site in breached_sites:
            if pass_site.find(b_site) != -1 and len(b_site) > 0 and b_site not in breached_pwords:
                breached_pwords.append(b_site)                
    print("Sites from password site list found in MOAB:\n")
    breached_pwords.sort()
    for site in breached_pwords:
        print(site)
    print("\nGoogle for past breaches of these sites to determine age of data.")

populate_lists()
check_breach()
