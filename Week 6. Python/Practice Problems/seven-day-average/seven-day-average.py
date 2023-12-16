import csv
import requests


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break
    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    averages = comparative_averages(new_cases, states)

    for state in averages:
        print(f"{state} had a 7-day average of {averages[state]["average"]} and ", end="")
        if (averages[state]["difference"] > 0):
            print(f"an increase of {averages[state]["difference"]}%.")
        elif (averages[state]["difference"] < 0):
            print(f"a dicrease of {averages[state]["difference"]}%.")
        else:
            print("did not change at all.")


# TODO: Create a dictionary to store 14 most recent days of new cases by state
def calculate(reader):
    new_cases = {}
    previous_cases = {}

    for row in reader:
        state = row["state"]
        cases = int(row["cases"])

        if state not in previous_cases:
            previous_cases[state] = cases
            new_cases[state] = []
            new_cases[state].append(cases)
        else:
            new_case = cases - previous_cases[state]
            previous_cases[state] = cases

            if len(new_cases[state]) >= 14:
                new_cases[state].pop(0)
            new_cases[state].append(new_case)
    print(new_cases["New York"])
    return new_cases

# TODO: Calculate and print out seven day average for given state
def comparative_averages(new_cases, states):
    averages = {}

    for state in states:
        averages[state] = {}
        previous_week = new_cases[state][0 : 7]
        last_week = new_cases[state][7 : ]
        last_week_average = 0
        previous_week_average = 0

        # calculate the average
        for case in last_week:
            last_week_average += case
        last_week_average = int(last_week_average / 7)
        averages[state]["average"] = last_week_average

        #calculate the previous week's average
        for case in previous_week:
            previous_week_average += case
        previous_week_average = int(previous_week_average / 7)

        #find the difference between the last week and the previous week
        try:
            difference = int(previous_week_average * 100 / last_week_average)
            difference = difference - 100
        except ZeroDivisionError:
            difference = last_week_average

        averages[state]["difference"] = difference

    return averages

main()
