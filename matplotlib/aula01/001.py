from matplotlib import pyplot as plt

def main():
    plt.style.use('fivethirtyeight')
    ages_x = [_ for _ in range(25, 36)]
    dev_y = [38496, 42000, 46752, 49320, 53200,
             56000, 62316, 64928, 67317, 68748, 73752]

    plt.plot(ages_x, dev_y, label='All Devs')

    py_dev_y = [45372, 48876, 53850, 57287, 63016,
                65998, 70003, 70000, 71496, 75370, 83640]

    plt.plot(ages_x, py_dev_y, label='Python')

    plt.title('Median Salaries (USD) for Ages')
    plt.xlabel('Ages')
    plt.ylabel('Median Salary (USD)')
    plt.legend()

    plt.show()


if __name__ == '__main__':
    main()