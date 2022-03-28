bill = [[7.89, "K"],
    [6.29, "A"],
    [6.29, "P"],
    [5.99, "A, K"],
    [11.99, "P"],
    [3.39, "P"],
    [3.39, "P"],
    [15.99, "A, K, T"],
    [10.99, "P"],
    [32.68, "P"],
    [32.08, "T"],
    [32.02, "K"],
    [7.49, "T, K"],
    [10.49, "K"],
    [16.99, "K"],
    [16.99, "K"],
    [4.85, "K"],
    [16.99, "K"],
    [19.99, "K, P, A, T"],
    [20.99, "T"],
    [15.49, "T"],
    [5.99, "A"],
    [15.99, "T"],
    [6.49, "T"],
    [5.99, "T"],
    [12.49, "A"],
    [10.49, "T"],
    [15.99, "T"],
    [3.99, "T"],
    [3.69, "T, K"],
    [7.99, "T"],
    [1.69, "T"],
    [1.69, "A, K"],
    [6.99, "T, A"],
    [10.99, "A"],
    [10.99, "K"],
    [10.99, "P"],
    [13.99, "K"]
]

total = 211.67 + 247.21

Individual_Totals = {"T" : 0, "P" : 0, "A" : 0, "K" : 0}

for item in bill:
    people = item[1].split(", ")
    cost_per_person = item[0] / len(people)
    for person in people:
        Individual_Totals[person] += cost_per_person

total_pre_tax = sum(Individual_Totals.values())

tax = total-total_pre_tax
for person in Individual_Totals:
    Individual_Totals[person] += Individual_Totals[person]/total_pre_tax * tax
    print(person + " owes: " + str(format(Individual_Totals[person], '.2f')))

print("Bill Total: " + str(format(sum(Individual_Totals.values()), '.2f')))
