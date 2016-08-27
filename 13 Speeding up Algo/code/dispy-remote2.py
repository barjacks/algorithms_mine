# function sent to remote nodes for execution
def triple_number(n):
    return n * 3

def scrape_webpage(url):
    import requests
    from bs4 import BeautifulSoup
    response = requests.get(url)
    doc = BeautifulSoup(response.text, 'html.parser')
    headline = doc.find("h1").text
    return headline

    data = {
    'url': url,
    'headline': headline
    }
    return data

if __name__ == '__main__':
    import dispy
    # list remote nodes (here DigitalOcean instance with external IP SERVER_IP_ADDRESS)
    nodes = ['45.55.251.170']
    # use ssh to forward port 51347 for each node; e.g.,
    # 'ssh -R 51347:localhost:51347 -i ~/.ssh/do-droplet root@SERVER_IP_ADDRESS'

    # start dispynode on each node with 'dispynode.py -i SERVER_IP_ADDRESS' (so dispynode
    # uses external IP address instead of default local IP address)
    cluster = dispy.JobCluster(scrape_webpage, nodes=nodes, ip_addr='127.0.0.1')
    jobs = []
    numbers = [1, 2, 3, 4, 5, 6]
    urls = [
   'http://www.bbc.com/sport/disability-sport/37165427',
   'http://www.bbc.com/news/world-europe-37164217',
   'http://www.bbc.com/culture/story/20160819-the-21st-centurys-100-greatest-films',
   'http://www.bbc.com/future/story/20160822-the-real-risks-and-benefits-of-everyday-pleasures',
   'http://www.bbc.com/news/world-us-canada-37168165',
   'http://www.bbc.com/news/world-us-canada-37162373',
   'http://www.bbc.com/news/world-us-canada-37157478',
   'http://www.bbc.com/sport/olympics/37162798',
   ]
    #for number in numbers:
    #    job = cluster.submit(number)
    #    jobs.append(job)

    for url in urls:
        job = cluster.submit(url)
        jobs.append(job)


    for job in jobs:
        result = job()
        if result is None:
            print(job.exception)
        print('result: %s' % result)
