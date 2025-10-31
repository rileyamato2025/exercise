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
    return count_above / len(ls)
    
