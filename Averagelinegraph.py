import matplotlib.pyplot as plt


# Set up variables
AVERAGE_LENGTH = eval(input("Enter the length of rolling average: "))
timesdoc = "cubetimes.txt"
timeslist = []
averagetimelist = []
countinglist = []
countinglistsub10 = []
rollingaveragelist10 = []

# Creates a times list of all times
with open(timesdoc) as filestream:
    for line in filestream:
        number = float(line)
        timeslist.append(number)


# Calculate and create rolling average list
for i in range(len(timeslist)):
    average = 0

    # This controls the length of the rolling average
    if len(rollingaveragelist10) > AVERAGE_LENGTH - 1:
        rollingaveragelist10.pop(0)
    rollingavertimetoappend = timeslist[i]
    rollingaveragelist10.append(rollingavertimetoappend)

    # calculates average of past AVERAGE_LENGTH number of solves and assigns it to a variable
    # Then it appends average to averagetimelist
    for e in rollingaveragelist10:
        average += e
    average = average / (len(rollingaveragelist10))
    averagetimelist.append(average)

# create line graph of average times and scatter plot of solves
plt.scatter(range(len(timeslist)), timeslist, color='blue', s=4, label="solve")
plt.plot(range(len(averagetimelist)), averagetimelist, linewidth=2.0, color='red', label="average")

# labels
plt.ylabel("Time (in seconds)")
plt.xlabel("solve #")
plt.title("My rolling average solve time")

# display
plt.legend()
plt.show()
