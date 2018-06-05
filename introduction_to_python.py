import csv, datetime, pprint, time
from collections import Counter


## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    cities = {'chicago': chicago, 'new york': new_york_city, 'washington': washington}
    print('\nHello! Let\'s explore some US bikeshare data!')
    while True:
        try:
            city = input('Would you like to see data for Chicago, New York, or Washington? Please type your response.\n')
        except ValueError or KeyboardInterrupt:
            break
        else:
            if city.lower() in cities:
                return cities[city.lower()]
            else:
                print('Invalid input! Please try again.')


def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        (str) Time period for a city's bikeshare data.
    '''
    time_periods = ['month', 'day', 'none']
    while True:
        try:
            time_period = input('\nWould you like to filter the data by month, day, or not at all? Type "none" for no time filter.\n')
        except ValueError or KeyboardInterrupt:
            break
        else:
            if time_period.lower() in time_periods:
                return time_period.lower()
            else:
                print('Invalid input! Please try again.')


def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        (int) Month for a city's bikeshare data.
    '''
    months = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}
    while True:
        try:
            month = input('\nWhich month? January, February, March, April, May, or June?\n')
        except ValueError or KeyboardInterrupt:
            break
        else:
            if month.lower() in months:
                return months[month.lower()]
            else:
                print('Invalid input! Please try again.')


def get_day(month):
    '''Asks the user for a day and returns the specified day.

    Args:
        (str) Month for a city's bikeshare data.
    Returns:
        (int) Day for a city's bikeshare data.
    '''
    days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30}
    while True:
        try:
            day = int(input('\nWhich day? Please type your response as an integer.\n'))
        except ValueError or KeyboardInterrupt:
            print('Invalid input! Please try again.')
        else:
            if month in days and 0 < day <= days[month] :
                return day
            else:
                print('Invalid day! Please try again.')


def read_city(city_file, time_period, month=None, day=None):
    '''Asks the user for a city and returns a list of dictionaries for that city's bike share data.

    Args:
        city_file (str): File name of the selected city.
        time_period (str): Time period for a city's bikeshare data.
        month (int): Selected month if time period is set to "month" or "day".
        day (int): Selected day if time period is set to "day".
    Returns:
        (list of dicts) Selected city's bike share data.
    '''
    with open(city_file) as f:
        if time_period == 'none':
            city_data = [{k: v for k, v in row.items()}
                for row in csv.DictReader(f, skipinitialspace=True)]
        elif time_period == 'month':
            city_data = [{k: v for k, v in row.items()}
                for row in csv.DictReader(f, skipinitialspace=True)
                if datetime.datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S').month == month]
        else:
            city_data = [{k: v for k, v in row.items()}
                for row in csv.DictReader(f, skipinitialspace=True)
                if datetime.datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S').month == month
                and datetime.datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S').day == day]
    return city_data


def popular_month(city_data):
    '''Returns the most popular month for start time.

    Args:
        city_data (list of dicts): Selected city's bike share data.
    Returns:
        (int) Most popular month for start time.
    Question: What is the most popular month for start time?
    '''
    lst = (datetime.datetime.strptime(dct['Start Time'], '%Y-%m-%d %H:%M:%S').month for dct in city_data)
    return Counter(lst).most_common(1)[0][0]


def popular_day(city_data):
    '''Returns the most popular day of the week for start time.

    Args:
        city_data (list of dicts): Selected city's bike share data.
    Returns:
        (int) Most popular day of the week for start time.
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    '''
    lst = (datetime.datetime.strptime(dct['Start Time'], '%Y-%m-%d %H:%M:%S').weekday() for dct in city_data)
    return Counter(lst).most_common(1)[0][0]


def popular_hour(city_data):
    '''Returns the most popular hour of the day for start time.

    Args:
        city_data (list of dicts): Selected city's bike share data.
    Returns:
        (int) Most popular hour of the day (in military time) for start time.
    Question: What is the most popular hour of day for start time?
    '''
    lst = (datetime.datetime.strptime(dct['Start Time'], '%Y-%m-%d %H:%M:%S').hour for dct in city_data)
    return Counter(lst).most_common(1)[0][0]


def get_time(time):
    '''Returns the converted time from seconds.

    Args:
        time (int): Time in seconds to be converted.
    Returns:
        (list of ints) Converted time in years, days, hours, minutes, and seconds.
    '''
    year = time // (365 * 24 * 3600)
    time = time % (365 * 24 * 3600)
    day =  time // (24 * 3600)
    time =  time % (24 * 3600)
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time
    return [int(year), int(day), int(hour), int(minutes), int(seconds)]


def trip_duration(city_data):
    '''Returns the total trip duration and average trip duration.

    Args:
        city_data (list of dicts): Selected city's bike share data.
    Returns:
        (list of ints) Total trip duration and average trip duration.
    Question: What is the total trip duration and average trip duration?
    '''
    lst = [float(dct['Trip Duration']) for dct in city_data]
    return [get_time(sum(lst)), get_time(sum(lst)/len(lst))]


def popular_stations(city_data):
    '''Returns the most popular start station and most popular end station.

    Args:
        city_data (list of dicts): Selected city's bike share data.
    Returns:
        (list of strs) Most popular start station and most popular end station.
    Question: What is the most popular start station and most popular end station?
    '''
    start_lst = [dct['Start Station'] for dct in city_data]
    end_lst = [dct['End Station'] for dct in city_data]
    return [Counter(start_lst).most_common(1)[0][0], Counter(end_lst).most_common(1)[0][0]]


def popular_trip(city_data):
    '''Returns the most popular trip (from start station to end station).

    Args:
        city_data (list of dicts): Selected city's bike share data.
    Returns:
        (str) Most popular trip (from start station to end station).
    Question: What is the most popular trip?
    '''
    lst = [dct['Start Station'] + ' to ' + dct['End Station'] for dct in city_data]
    return Counter(lst).most_common(1)[0][0]


def users(city_data):
    '''Returns the counts of each user type.

    Args:
        city_data (list of dicts): Selected city's bike share data.
    Returns:
        (dict) The counts of each user type.
    Question: What are the counts of each user type?
    '''
    lst = [dct['User Type'] for dct in city_data]
    return Counter(lst)


def gender(city_data):
    '''Returns the counts of gender.

    Args:
        city_data (list of dicts): Selected city's bike share data.
    Returns:
        (dict) The counts of gender.
    Question: What are the counts of gender?
    '''
    lst = [dct['Gender'] for dct in city_data]
    return Counter(lst)


def birth_years(city_data):
    '''Returns the earliest, most recent, and most popular birth years.

    Args:
        city_data: (list of dicts) Selected city's bike share data.
    Returns:
        (list of ints) The earliest, most recent, and most popular birth years.
    Question: What are the earliest, most recent, and most popular birth years?
    '''
    lst = [int(float(dct['Birth Year'])) for dct in city_data if dct['Birth Year'] != '']
    return [min(Counter(lst)), max(Counter(lst)), Counter(lst).most_common(1)[0][0]]


def display_data(city_data, start=0, end=5):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        city_data (list of dicts): Selected city's bike share data.
        start (int): Starting index of the list.
        end (int): Ending index of the list.
    Returns:
        none.
    '''
    while True:
        try:
            display = input('Would you like to view individual trip data? '
                            'Type \'yes\' or \'no\'. ')
        except ValueError or KeyboardInterrupt:
            break
        else:
            if display.lower() == 'yes':
                pprint.pprint(city_data[start:end])
                start += 5
                end += 5
            elif display.lower() == 'no':
                break
            else:
                print('Invalid input! Please try again.')


def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    month_list = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June'}
    day_list = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

    # Filter by city (Chicago, New York, Washington)
    city = get_city()

    # Filter by time period (month, day, none)
    time_period = get_time_period()
    if time_period == 'none':
        print('Loading the bike share data of {} with no filters...'.format(city))
    elif time_period == 'month':
        month = get_month()
        print('Loading the bike share data of {} for the month of {}...'.format(city, month_list[month]))
    else:
        month = get_month()
        day = get_day(month)
        print('Loading the bike share data of {} for {} {}...'.format(city, month_list[month], day))

    start_time = time.time()

    # Read CSV file of the city_data
    if time_period == 'none':
        city_data = read_city(city, time_period)
    elif time_period == 'month':
        city_data = read_city(city, time_period, month)
    else:
        city_data = read_city(city, time_period, month, day)

    print('That took %s seconds.' % (time.time() - start_time))

    print('Calculating the first statistic...')
    start_time = time.time()

    # What is the most popular month for start time?
    if time_period == 'none':
        mp_month = popular_month(city_data)
        print("The most popular month is {}.".format(month_list[mp_month]))
        print('That took %s seconds.' % (time.time() - start_time))
        print('Calculating the next statistic...')
    start_time = time.time()

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        mp_day = popular_day(city_data)
        print('The most popular day is {}.'.format(day_list[mp_day]))
        print('That took %s seconds.' % (time.time() - start_time))
        print('Calculating the next statistic...')
    start_time = time.time()

    # What is the most popular hour of day for start time?
    mp_hour = popular_hour(city_data)
    print('The most popular hour is {}00 hours.'.format(mp_hour))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    trip_data = trip_duration(city_data)
    print('The sum of the trips is {} years, {} days, {} hours, {} minutes, and {} seconds.'.format(trip_data[0][0], trip_data[0][1], trip_data[0][2], trip_data[0][3], trip_data[0][4]))
    print('The average of the trips is {} minutes and {} seconds.'.format(trip_data[1][3], trip_data[1][4]))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    mp_stations = popular_stations(city_data)
    print('The most popular start station is {} and the most popular end station is {}.'.format(mp_stations[0], mp_stations[1]))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    mp_trip = popular_trip(city_data)
    print('The most popular trip is from {}.'.format(mp_trip))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    num_users = users(city_data)
    print('There are {} subcribers and {} customers.'.format(num_users['Subscriber'], num_users['Customer']))

    print("That took %s seconds." % (time.time() - start_time))
    if city == chicago or city == new_york_city:
        print("Calculating the next statistic...")
        start_time = time.time()

        # What are the counts of gender?
        num_gender = gender(city_data)
        print('There are {} males and {} females.'.format(num_gender['Male'], num_gender['Female']))
        print('{} users did not reveal their gender.'.format(num_gender['']))

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()

        # What are the earliest, most recent, and most popular birth years?
        birth_data = birth_years(city_data)
        print('Among the users who revealed their birth years, the oldest and youngest persons were born in {} and {}, respectively.'.format(birth_data[0], birth_data[1]))
        print('The most popular birth year is {}.'.format(birth_data[2]))

        print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data(city_data)

    # Restart?
    restart = input('Would you like to restart? Type \'yes\' or press any key to exit. ')
    if restart.lower() == 'yes':
        statistics()

if __name__ == "__main__":
	statistics()
