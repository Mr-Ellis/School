import statistics

examResults = [63, 92, 84, 57, 72, 94, 63]
candidates = ["Diya", "Ali", "Charles", "Eric", "Hanna", "Gabriel", "Delores"]

print("Lowest result: ", min(examResults))
print("Highest result: ", max(examResults))
print("Total of all results: ", sum(examResults))
print("(Mean) average result: ", statistics.mean(examResults))

candidates.sort()

for i in range(0,len(candidates)):
    print("Candidate", i+1, ":", candidates[i])
