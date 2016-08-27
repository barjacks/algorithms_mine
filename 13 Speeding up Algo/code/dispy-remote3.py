# function sent to remote nodes for execution
def triple_number(n):
    return n * 3

# This code is all run on the server
def scrape_webpage(url):
    import requests
    import netifaces as ni
    from bs4 import BeautifulSoup

    response = requests.get(url)
    doc = BeautifulSoup(response.text, 'html.parser')
    headline = doc.find("h1").text

    # Create a unique filename
    my_ip = ni.ifaddresses('eth0')[2][0]['addr']
    timestamp = datetime.datetime.now().strftime("%Y-%M-%d-%H-%M-%S-%f")
    filename = "{}-{}.tsv".format(timestamp, my_ip)

    # Open up that file
    with open(filename, 'w') as f:
        header = "url\theadline\n"
        f.write(header)
        # Write the content we want to the file
        content = "{}\t{}".format(url, headline)
        f.write(content)

    # Send the file back to the client (our local machine)
    #dispy_send_file(filename)

    data = {
        'url': url,
        'headline': headline
    }
    return data

# "Is this script being run from the command line?"
if __name__ == '__main__':
    # This is weird because we usually import at the very top!
    # BUT!!! This file is actually shared between our computer
    # and our server computer, so you put imports not at the top
    import dispy

    # nodes is all of the servers are we going to connect to
    # list remote nodes (here DigitalOcean instance with external IP SERVER_IP_ADDRESS)
    nodes = ['45.55.251.170', '45.55.249.223', '45.55.159.88', '104.131.55.245']
    # use ssh to forward port 51347 for each node; e.g.,
    # 'ssh -R 51347:localhost:51347 -i ~/.ssh/do-droplet root@SERVER_IP_ADDRESS'

    # start dispynode on each node with 'dispynode.py -i SERVER_IP_ADDRESS' (so dispynode
    # uses external IP address instead of default local IP address)

    # This is where the magic happens, all the important stuff
    # double_number is the name of the function we are going to run
    # nodes is the list of servers we are going to connect to
    # and we use ip_addr='127.0.0.1' because I said so
    cluster = dispy.JobCluster(scrape_webpage, nodes=nodes, ip_addr='127.0.0.1')

    # Empty list of jobs to run because we haven't created any jobs yet
    jobs = []

    # We're going to go through these numbers and submit them to the cluster
    numbers = [1, 2, 3, 4, 5, 6]
    urls = [
        'http://www.bbc.com/sport/disability-sport/37165427',
        'http://www.bbc.com/news/world-europe-37164217',
        'http://www.bbc.com/culture/story/20160819-the-21st-centurys-100-greatest-films',
        'http://www.bbc.com/future/story/20160822-the-real-risks-and-benefits-of-everyday-pleasures',
        'http://www.bbc.com/news/world-us-canada-37168165',
        'http://www.bbc.com/news/world-us-canada-37162373',
        'http://www.bbc.com/news/world-us-canada-37157478',
        'http://www.bbc.com/sport/olympics/37162798'
    ]
    for url in urls:
        # "Hey cluster, take this number and run your function on it"
        # "OK, here's a job in return"
        # "OK, I'll save that job to look at later"
        job = cluster.submit(url)
        jobs.append(job)

    # Go through the jobs and look at what we get back
    for job in jobs:
        result = job()
        # This is what you have to do to debug your server code
        # because it won't display the exception/error on the server
        # and if it encounters an error it just returns 'None'
        if result is None:
            print(job.exception)
        else:
            print('result: %s' % result)
