import csv
import matplotlib.pyplot as plt
def read_data(filename):
    hours = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            hr = row[0].strip()
            if hr != '':
                hours.append(float(hr))
    return hours

def make_histogram(data):
    plt.hist(data, bins=10, edgecolor='black')
    plt.title('Hours of Exercise per Week')
    plt.xlabel('Hours')
    plt.ylabel('Number of Students')
    plt.show()

def main():
    filename = 'StudentExercise.csv'
    hours = read_data(filename)
    print("Data read successfully:", hours)
    make_histogram(hours)

if __name__ == '__main__':
    main()

def average(ls):
    return sum(ls) / len(ls)

def prop_above(ls):
    avg = average(ls)
    count_above = 0
    for x in ls:
        if x > avg:
            count_above += 1
    return count_above/len(ls)
def median_even(ls):
    upper_idx = int(len(ls)/2)
    lower_idx = upper_idx - 1
    median = (ls[upper_idx] + ls[lower_idx])/2

    return median
def median_odd(ls):
    idx - len(ls)//2
    median = ls[idx]

    return median
ls = read_data("exercise.csv")
if len(read_data)%2 ==0:
    median_even(read_data)
else:
    median_odd(read_data)
print(main(read_data("exercise.csv")))
print(average(read_data("exercise.csv")))
print(prop_above(read_data("exercise.csv")))
print(median_even(read_data("exercise.csv")))
print(median_odd(read_data("exercise.csv")))

