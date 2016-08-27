# function sent to remote nodes for execution
def triple_number(n):
    return n * 3

if __name__ == '__main__':
    import dispy
    # list remote nodes (here DigitalOcean instance with external IP SERVER_IP_ADDRESS)
    nodes = ['45.55.251.170']
    # use ssh to forward port 51347 for each node; e.g.,
    # 'ssh -R 51347:localhost:51347 -i ~/.ssh/do-droplet root@SERVER_IP_ADDRESS'

    # start dispynode on each node with 'dispynode.py -i SERVER_IP_ADDRESS' (so dispynode
    # uses external IP address instead of default local IP address)
    cluster = dispy.JobCluster(triple_number, nodes=nodes, ip_addr='127.0.0.1')
    jobs = []
    numbers = [1, 2, 3, 4, 5, 6]
    for number in numbers:
        job = cluster.submit(number)
        jobs.append(job)
    for job in jobs:
        result = job()
        print('result: %s' % result)
