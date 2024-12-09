## Operating Systems Terms

### 1. Operating System Basics - Sly

- Kernel
  - A kernel is the core part of an operating system that acts as a bridge between the hardware of a computer
    and the software applications that are being run. It also helps to manage system resources and handles various tasks
    like running programs, accessing files, and connecting to IO devices.
    [Source](https://www.geeksforgeeks.org/kernel-in-operating-system/)
- System Calls
  - A system call is the mechanism by which a program interacts with the underlying system to request services using the kernel.
    [Source](https://www.geeksforgeeks.org/introduction-of-system-call/)
- User Mode vs. Kernel Mode
  - User Mode and Kernel Mode refers to the way in which programs can be run. When a program is run in User Mode, it is booted up
    on an operating system level. These programs are run with limited privileges and are not allowed direct access to the system
    resources. On the contrary, Kernel Mode is when the program switches to the kernel level for the most privileged access to be
    able to interact with the hardware directly. [Soruce](https://www.geeksforgeeks.org/difference-between-user-mode-and-kernel-mode/)
- Bootstrapping/Boot Process
  - Bootstrapping refers to the process by which the hardware sequences the operations needed to load up and execute the
    operating system. The process can be seen simply as referred to in the image below.
    ![Bootstrap](https://www.tutorialspoint.com/assets/questions/media/11714/Bootstrap%20Program.PNG)
    [Source](https://www.ituonline.com/tech-definitions/what-is-bootstrapping-computing/)
- Operating System Types: [Source](https://www.geeksforgeeks.org/types-of-operating-systems/)
  - Batch Systems
    - Batch systems don't interact with the computer directly, but rather is designed to manage and execute a large number of jobs
      processed by groups. This system depends on the operator sorting the jobs with similar needs and requirements.
      ![Batch](https://media.geeksforgeeks.org/wp-content/uploads/20230511130815/types1-(1).webp)
  - Time-Sharing Systems
    - Also known as Multitasking Systems, these systems assign a set of time (quantum) to each task before moving on to the next.
      The time assigned is irregardless of the tasks being from the same user.
      ![Time-Sharing](https://media.geeksforgeeks.org/wp-content/uploads/20230512125908/Capture2210.png)
  - Real-Time Operating Systems
    - These systems are meant to serve real-time systems with minimal response times and are utilized for extremely time-sensitive
      systems requiring almost immediate deployment (e.g. missile systems, air traffic control, airbags, etc.)
      ![RTOS](https://media.geeksforgeeks.org/wp-content/uploads/20230511145635/Types8.webp)
  - Distributed Operating Systems
    - Utilizes multiple interconnected computers over a shared network, also known as distributed systems.
      ![Distributed](https://media.geeksforgeeks.org/wp-content/uploads/20230516183602/Types-of-OS-04.webp)
  - Embedded Systems
    - Systems built to be embedded into a particular application (e.g. appliances, vehicles, etc.) with specific hardware and tasks
      for that purpose. Often have limited user interface and are optimized for reliability.

### 2. Process Management - Sly

- Process
  - Program in execution
- Threads
  - Sequences of activities being executed within a process
- Process States (New, Ready, Running, Waiting, Terminated)
  - The different states in which a computer handles the processes of a program
    ![States](https://media.geeksforgeeks.org/wp-content/uploads/20241017162800402546/five-state-model.png)
- Process Control Block (PCB)
  - Data structure that keeps track of all the key information needed to manage and regulate different processes
- Context Switch
  - Process of storing the state of a process/thread to restore for use later on
- Multitasking
  - The ability of an OS to run multiple processes at once. 
- Multiprocessing
  - The utilization of multiple processors working in parallel to complete a task.
- Multithreading
  - Dividing a process into multiple threads that can be executed simultaneously.
- Process Synchronization
  - Coordinated execution of multiple processes so that there's controlled and predictable access to shared resources
- Inter-Process Communication (IPC)
  - Pipes
    - Technique that lets multiple processes communicate with each other through a uni/bi-directional channel
      [Source](https://www.geeksforgeeks.org/difference-between-pipes-and-message-queues/)
  - Message Queues
    - Linked list of messages to be shared with other processes and stored in the kernel.
      [Source](https://www.geeksforgeeks.org/difference-between-pipes-and-message-queues/)
  - Shared Memory
    - Shared block of memory that multiple processes access at the same time.
      [Source](https://www.geeksforgeeks.org/ipc-shared-memory/)
  - Sockets
    - Bidirectional pipe endpoint that allows unrelated processes to communicate with each other within the same machine or network.
      [Source](https://www.geeksforgeeks.org/advantages-of-unix-sockets-for-ipc/)

### 3. Process Scheduling - Sly

- CPU Scheduling
  - The way in which an OS decides which task gets to use the CPU
    [Source](https://www.geeksforgeeks.org/cpu-scheduling-in-operating-systems/) 
- Preemptive vs. Non-Preemptive Scheduling
  - Preemptive lets a process be booted from the running queue before it is finished, whereas Non-Preemptive waits for the
    processes to finish as needed. [Source](https://www.geeksforgeeks.org/cpu-scheduling-in-operating-systems/)
- Scheduling Algorithms: [Source](https://www.geeksforgeeks.org/cpu-scheduling-in-operating-systems/)
  - First-Come, First-Served (FCFS)
    - The prcoesses are taken in order of which ones request the CPU first.
  - Shortest Job Next (SJN)
    - Selects the waiting process that has the shortest execution time next.
  - Priority Scheduling
    - Preemptive method that works on the most important priority processes first.
  - Round Robin (RR)
    - Preemptive method where each process is cycled through with a fixed time slot (quantum).
  - Shortest Remaining Time (SRT)
    - Preemptive version of SJN
  - Multi-Level Queue Scheduling
    - Processes are divided into different classes of priority with their own scheduling needs. Processes cannot move between queues.
  - Multi-Level Feedback Queue Scheduling
    - Similar to Multi-Level Queue Scheduling, but the processes can move between queues.
  - Completely Fair Scheduler (CFS)
    - Divides the CPU time equally across all the processes based on Time Quantum/N, where N is the number of processes.

### 4. Synchronization and Concurrency - Sly

- Critical Section
  - Segment of code that accesses shared resources and is executed by multiple threads/processes at the same time.
    [Source](https://www.geeksforgeeks.org/g-fact-70/)
- Mutual Exclusion
  - Property of Process Synchronization coined by Dijkstra that states "no two processes can exist in the critical
    section at any given point of time". Usually meant to avoid simultaneous use of a common resource.
    [Source](https://www.geeksforgeeks.org/mutual-exclusion-in-synchronization/)
- Race Conditions
  - Situation in which the the result of multiple thread execution in a critical section changes according to the order the threads
    execute. [Source](https://www.geeksforgeeks.org/race-condition-vulnerability/)
- Semaphores
  - Variables used to coordinate multiple processes in a system, and are utilized to enforce mutual exclusion, avoid race conditions,
    and implement synchronization between processes. Works by using Wait (P) and Signal (V) operations to block or permit a process.
    [Source](https://www.geeksforgeeks.org/semaphores-in-process-synchronization/)
- Mutexes
  - Mainly used to provide mutual exclusion to a specific part of the code and enforces strict ownership.
    [Source](https://www.geeksforgeeks.org/mutex-vs-semaphore/)
- Monitors
  - Implemented as programming language constructs meant to simplify process synchronization by providing high-level abstraction for
    data access. Also provides mutual exclusion, condition variables, and data encapsulation within one construct.
    [Source](https://www.geeksforgeeks.org/monitors-in-process-synchronization/)
- Deadlock
  - Situation where multiple processes are stuck waiting for another to stop using a required resource.
    [Source](https://www.geeksforgeeks.org/introduction-of-deadlock-in-operating-system/)
    ![Deadlock](https://media.geeksforgeeks.org/wp-content/uploads/20190927190725/deadlock1.png)
- Starvation
  - Situation where a process keeps getting pushed down as a low-priority and is left blocked from any CPU utilization indefinitely.
    [Source](https://www.geeksforgeeks.org/difference-between-deadlock-and-starvation-in-os/)
- Busy Waiting
  - Process synchronization technique where the process waits for a condition to be satisfied before continuing with its execution.
    [Source](https://www.geeksforgeeks.org/busy-waiting-in-os/)
- Condition Variables
  - Synchronization method to make one thread wait until another has notified it that the shared resource is available to access.
    [Source](https://www.geeksforgeeks.org/cpp-multithreading-condition-variables/)
- Spinlocks
  - Synchronization method to protect shared resources being accessed by multiple threads/processes at the same time. Uses
    busy-wait method to have a thread select a lock until it becomes available.
    [Source](https://www.geeksforgeeks.org/what-is-spinlock-in-operating-system/)
- Atomic Operations
  - Operations that execute without interruption from any other process and can't be broken down any further.
    [Source](https://www.geeksforgeeks.org/atomic-operations-in-os/)
- Synchronization Problems: [Source](https://www.geeksforgeeks.org/classical-problems-of-synchronization-with-semaphore-solution/)
  - Producer-Consumer Problem
    - Problem: Both the producers and the consumers share a fixed-size buffer. In this case, the produces shouldn't be able to add
      data to a full buffer, and the consumers shouldn't pull data from an empty buffer.
      ![PC Problem](https://media.geeksforgeeks.org/wp-content/uploads/20240307124526/Producer-Consumer.jpg)
    - Solution: The options for the producer are to sleep or discard data from the full buffer, with the consumer notifying the
      producer when they've pulled data. For the consumer, they should sleep and be notified by the producer when the buffer isn't
      empty.
  - Readers-Writers Problem
    - Problem: Multiple readers can access shared data simultaneously without issue, but only one writer can access shared data at
      a time. 
    - Solution: Readers preference where writers have to wait until no readers are accessing data before a writer can. Writers
      preference where writer can still do what they need to, but there may still be someone reading the data.
  - Dining Philosophers Problem
    - Problem: Multiple processes (philosphers) share limited resources (chopsticks) they need to perform a task (eat noodles)
      ![Dining Problem](https://media.geeksforgeeks.org/wp-content/uploads/dining_philosopher_problem.png)
    - Solution: Manage the allocation of limited resources in a deadlock-free and starvation free way, letting "philosphers" eat if
      they have access to both "chopsticks"
  - Sleeping Barber Problem
    - Problem: Barber is sleeping when there are no customers and has to be woken up by a customer when they arrive, but the
      customers have to wait if there are seats open or leave if there are none.
      ![Barber](https://media.geeksforgeeks.org/wp-content/uploads/Untitled-Diagram-25.png)
    - Solution: Coordinated access so there is only one customer in the chair at a time and the barber is always working on a single
      customer in the chair

### 5. Deadlock

- Deadlock Detection
- Deadlock Prevention
- Deadlock Avoidance
- Banker’s Algorithm
- Resource Allocation Graphs
- Circular Wait
- Hold and Wait

### 6. Memory Management

- Logical Address vs. Physical Address
- Memory Allocation Techniques:
  - Contiguous Allocation
  - Non-Contiguous Allocation
- Paging
- Segmentation
- Page Tables
  - Multi-Level Page Tables
  - Inverted Page Tables
- Virtual Memory
- Page Fault
- Demand Paging
- Page Replacement Algorithms:
  - First-In-First-Out (FIFO)
  - Least Recently Used (LRU)
  - Optimal Page Replacement
  - Clock (Second-Chance) Algorithm
- Thrashing
- Fragmentation:
  - Internal Fragmentation
  - External Fragmentation

### 7. File Systems

- File Structure
- File Attributes
- File Operations
- File System Implementation
- Directory Structures:
  - Single-Level Directory
  - Two-Level Directory
  - Tree-Structured Directory
- File Allocation Methods:
  - Contiguous Allocation
  - Linked Allocation
  - Indexed Allocation
- Disk Scheduling Algorithms:
  - First-Come, First-Served (FCFS)
  - Shortest Seek Time First (SSTF)
  - SCAN/Elevator
  - Circular SCAN (C-SCAN)
  - LOOK and C-LOOK
- Journaling
- RAID Levels
- Access Control Lists (ACL)

### 8. Input/Output Management

- Device Drivers
- Device Controllers
- Interrupts
- DMA (Direct Memory Access)
- Polling
- Spooling
- Disk Structure
- Disk Scheduling Algorithms (see File Systems)

### 9. ~Security and Protection~

- Authentication
- Authorization
- Encryption
- Access Control Mechanisms
- Discretionary Access Control (DAC)
- Mandatory Access Control (MAC)
- Role-Based Access Control (RBAC)
- Privilege Levels
- Security Threats:
  - Malware (Virus, Worm, Trojan)
  - Ransomware
  - Rootkits
  - Phishing
- System Threats:
  - Buffer Overflow
  - Denial-of-Service (DoS)
- Protection Mechanisms:
  - Firewalls
  - Intrusion Detection Systems (IDS)

### 10. Advanced Topics and Algorithms (optional) - Sly

- Virtualization
- Hypervisors
- Containerization
- Distributed Systems
- Distributed File Systems
- Remote Procedure Call (RPC)
- Distributed Synchronization
- Cloud Computing
- Real-Time Systems
- Hard vs. Soft Real-Time Systems
- Algorithms:
  - Peterson’s Algorithm
  - Lamport’s Bakery Algorithm
  - Readers-Writers Variations
  - Ricart–Agrawala Algorithm (Distributed Mutual Exclusion)
  - Bully Election Algorithm
  - Ring Election Algorithm

### 11. Networking Concepts (optional)

- Network Protocols (TCP/IP)
- Socket Programming
- Network File System (NFS)
- Remote Memory Access
- Packet Scheduling
- Fair Queuing
- Weighted Fair Queuing

### 12. Miscellaneous - Sly

- System Performance
  - Benchmarking
  - Throughput
  - Latency
- System Calls (e.g., fork, exec, wait, read, write)
- Kernel Types:
  - Monolithic Kernel
  - Microkernel
  - Hybrid Kernel
  - Exokernel
- Virtual Machines (VMs)
- Resource Allocation
- Debugging Tools (strace, gdb)
- Synchronization Hardware (Test-and-Set, Compare-and-Swap)
