### Handles API Interactions

import requests
import json 
import os
from rich import print

def getConfig(client_id):
    return {
        "client_id": "brett",
        "min_jobs": 10, # Generate 5 jobs
        "max_jobs":10,  # Ensure exactly 5 jobs
        "min_bursts": 5,  # Each job has at least 2 bursts
        "max_bursts": 5,  # At most 3 bursts per job
        "min_job_interval": 10,  # New jobs arrive quickly (1 clock tick)
        "max_job_interval": 12,  # Max interval between job arrivals
        "burst_type_ratio": 0.8,  # Higher chance of CPU bursts (70%)
        "min_cpu_burst_interval": 40,  # Short CPU bursts (3 ticks)
        "max_cpu_burst_interval": 45,  # Max CPU burst duration (5 ticks)
        "min_io_burst_interval": 2,  # Short IO bursts (2 ticks)
        "max_io_burst_interval": 4,  # Max IO burst duration (4 ticks)
        "min_ts_interval": 5,  # Short timeslice intervals for preemption testing
        "max_ts_interval": 10,  # Upper bound for timeslice intervals
        "priority_levels": [3],  # 3 priority levels for clear preemption
    }

def init(config):
    """
    This function will initialize the client and return the `client_id` and `session_id`
    """
    route = f"http://profgriffin.com:8000/init"
    r = requests.post(route,json=config)
    if r.status_code == 200:
        response = r.json()
        return response
    else:
        print(f"Error: {r.status_code}")
        return None


def getJob(client_id,session_id,clock_time):  
    route = f"http://profgriffin.com:8000/job?client_id={client_id}&session_id={session_id}&clock_time={clock_time}"
    r = requests.get(route)
    if r.status_code == 200:
        response = r.json()
        return response
    else:
        print(f"Error: {r.status_code}")
        return None
    
def getBurst(client_id, session_id, job_id):
    route = f"http://profgriffin.com:8000/burst?client_id={client_id}&session_id={session_id}&job_id={job_id}"
    r = requests.get(route)
    if r.status_code == 200:
        response = r.json()
        return response
    else:
        print(f"Error: {r.status_code}")
        return None
    
def getBurstsLeft(client_id, session_id, job_id):
    route = f"http://profgriffin.com:8000/burstsLeft?client_id={client_id}&session_id={session_id}&job_id={job_id}"
    r = requests.get(route)
    if r.status_code == 200:
        response = r.json()
        return response
    else:
        print(f"Error: {r.status_code}")
        return None

def getJobsLeft(client_id, session_id):
    route = f"http://profgriffin.com:8000/jobsLeft?client_id={client_id}&session_id={session_id}"
    r = requests.get(route)
    if r.status_code == 200:
        response = r.json()
        return response
    else:
        print(f"Error: {r.status_code}")
        return None


if __name__ == '__main__':
    do_init = False;
    do_job = False;
    do_burst = False;

    jobs = {}

    client_id = "sgtrock"
    config = getConfig(client_id)
    base_url = 'http://profgriffin.com:8000/'
    response = init(config)

    start_clock = response['start_clock']
    session_id = response['session_id']

    clock = start_clock

    while(clock):
        #print(f"Clock: {clock}")
        jobsLeft = getJobsLeft(client_id, session_id)
        if not jobsLeft:
            break
        response = getJob(client_id,session_id,clock)
        if response and response['success']:
            if response['data']:
                for data in response['data']:
                    job_id = data['job_id']
                    print(f"Job {job_id} received at {clock}...")
                    if job_id not in jobs:
                        jobs[job_id] = {'data':data,'bursts':{}}
        
        print(jobs)

        for job_id in jobs:
            #print(f"cid: {client_id}, sid: {session_id}, jid: {job_id}")
            burstsLeft = getBurstsLeft(client_id, session_id, job_id)
            if not burstsLeft:
                print(f"No bursts left for job {job_id} at {clock}")
                continue
            bresp = getBurst(client_id, session_id, job_id)
            if isinstance(bresp, dict) and 'success' in bresp and bresp['success']:
                burst = bresp['data']
                bid = burst['burst_id']
                print(f"Burst {bid} received ...")
                jobs[job_id]['bursts'][bid] = burst

      
        clock += 1
