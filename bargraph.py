import matplotlib.pyplot as plt
import statistics as stat

CUBE_TIMES = "cubetimes.txt"
time_data = []
bins = []

# define bins every half second from 20 to 45 seconds
for i in range(40, 90):
    bins.append(i/2)


def main():
    #import data as float into time_data
    with open(CUBE_TIMES) as filestream:
        for line in filestream:
            time_data.append(float(line.rstrip()))

    plt.hist(bins=[x / 2 for x in range(44, 91)], x=time_data, color="red",
             rwidth=.6, label="solve time", range=.5)
    plt.legend()
    plt.title("Histogram of solves")
    plt.ylabel("# of solves in group")
    plt.xlabel("Solve time (.5 second steps)")
    plt.show()

    print("Standard Deviation: %.3f" % stat.stdev(time_data))
main()
