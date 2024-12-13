# CPU Scheduler Simulation
## Overview
The purpose of this project is to simulate the way a CPU processes jobs under a variety of test conditions and algorithms. By varying the algorithms and test conditions, we can see how it effects the simulation metrics and make observations about the algorithms.

## Group Members:
- Brett Mitchell and Sly Rahimi

## Algorithms implemented:
- First Come First Serve (fcfs.py) (done)
- Shortest Job First (sjb.py)
- Round Robin (rr.py)
- Multi-Level Feedback Queue (mlfq.py) (in progress)

## Files
|   #   | File            | Description                                        |
| :---: | --------------- | -------------------------------------------------- |
|   1   | sim.py         | Main driver of project that acts as entry point for simulations.      |
|   2   | fcfs.py  | Contains FCFS simulation logic.         |
|   3   | rr.py | Contains RR simulation logic. |
|   4   | pb.py | Contains PB simulation logic. |
|   5   | mlfq.py | Contains MLFQ simulation logic. |

## Instructions:
- Receive jobs, burst types, and burst durations from 'cpu_jobs.py'.
- Choose First Come First Serve (FCFS), Round Robin (RR), Priority-Based (PB), or Multi-Level Feedback Queue (MLFQ) algorithm to run
- Run the simulation using 'sim.py' in the terminal, the entry point for simulations.
