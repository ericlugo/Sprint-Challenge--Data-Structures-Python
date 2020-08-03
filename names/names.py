import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# ORIGINAL RUNTIME: 5.341 seconds ============================================================
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# NEW RUNTIME: 1.020 seconds =================================================================
# for name_1 in names_1:
#     if name_1 in names_2:
#         duplicates.append(name_1)
# NEW RUNTIME: 0.011 seconds =================================================================
names_1.extend(names_2)
names_1.sort()
for i in range(1, len(names_1)):
    if names_1[i] == names_1[i-1]:
        duplicates.append(names_1[i])

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish? There are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
