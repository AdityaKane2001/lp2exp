# Assignment 3
#
# Implement Greedy search algorithm for any of the following application:
# I. Selection Sort
# II. Minimum Spanning Tree
# III. Single-Source Shortest Path Problem
# IV. Job Scheduling Problem
# V. Prim's Minimal Spanning Tree Algorithm
# VI. Kruskal's Minimal Spanning Tree Algorithm
# VII. Dijkstra's Minimal Spanning Tree Algorithm


def job_scheduling(arr, t):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    result = [False] * t
    job = [""] * t

    for i in range(len(arr)):
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            if not result[j]:
                result[j] = True
                job[j] = arr[i][0]
                break
    print(job)


arr = [
    ['a', 2, 100],  # Job Array
    ['b', 1, 19],
    ['c', 2, 27],
    ['d', 3, 25],
    ['e', 3, 15]
]

job_scheduling(arr, 3)

# def printJobScheduling(arr, t):

#     # length of array
#     n = len(arr)

#     # Sort all jobs according to
#     # decreasing order of profit
#     for i in range(n):
#         for j in range(n - 1 - i):
#             if arr[j][2] < arr[j + 1][2]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]

#     # To keep track of free time slots
#     result = [False] * t

#     # To store result (Sequence of jobs)
#     job = ['-1'] * t

#     # Iterate through all given jobs
#     for i in range(len(arr)):

#         # Find a free slot for this job
#         # (Note that we start from the
#         # last possible slot)
#         for j in range(min(t - 1, arr[i][1] - 1), -1, -1):

#             # Free slot found
#             if result[j] is False:
#                 result[j] = True
#                 job[j] = arr[i][0]
#                 break

#     # print the sequence
#     print(job)

# # Driver Code
# arr = [
#     ['a', 2, 100],  # Job Array
#     ['b', 1, 19],
#     ['c', 2, 27],
#     ['d', 1, 25],
#     ['e', 3, 15]
# ]

# print("Following is maximum profit sequence of jobs")

# # Function Call
# printJobScheduling(arr, 3)