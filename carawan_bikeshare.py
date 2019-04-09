import time
import pandas as pd
#import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['chicago', 'new york city', 'washington']
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
def get_filters():
    city = ''
    month = ''
    day = ''
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    """while True, Stack Overflow, SethMMorton"""
    while True:
        city = input("Input city; Chicago, New York City, or Washington:\n").lower()
        if city in cities:
            break
        else:
            print("You input an invalid city!")

    # get user input for month (all, january, february, ... , june)
    while True:
        month = str(input("Input month for which you wish to see data; All, January, February, March, April, May, June:\n").lower())
        if month in months:
            break
        else:
            print("You input an invalid month.")
    # get user input for day of week (all, monday, tuesday, ... sunday)    
    while True:
        day = str(input("Input day for which you wish to see data; All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday:\n").lower())
        if day in days:
            break
        else:
            print("You input an invalid day of the week.")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour
    #print(df.head())
    
    """This filter adapted from Project Practice problems"""
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month)
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    
    # filter by day if applicable    
    if day != 'all':
        # use the index of the days list to get the corresponding int
        day = days.index(day)
        # filter by day to create the new dataframe
        df = df[df['day'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Common Month: ', months[popular_month])

    # display the most common day of week
    popular_day = df['day'].mode()[0]
    print('Most Common Day of Week: ', days[popular_day])

    # display the most common start hour
    popular_hour =  df['hour'].mode()[0]
    print('Most Frequent Start Hour: {}:00'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_st = df['Start Station'].mode()[0]
    print('Most Frequent Start Station: \n', popular_start_st)

    # display most commonly used end station
    popular_end_st = df['End Station'].mode()[0]
    print('Most Frequent End Station: \n', popular_end_st)

    # display most frequent combination of start station and end station trip
    popular_trip = df[['Start Station','End Station']].mode()
    print('Most Frequent Start/Stop Combination: \n', popular_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    travel_sum = df['Trip Duration'].sum()
    travel_sum_mins = travel_sum // 60
    travel_sum_secs = travel_sum % 60
    print("Total Travel Time {} mins and {} secs".format(int(travel_sum_mins),travel_sum_secs))

    # display mean travel time
    travel_mean = df['Trip Duration'].mean()
    travel_mean_mins = travel_mean // 60
    travel_mean_secs = travel_mean % 60
    print("Mean Travel Time {} mins and {} secs.".format(int(travel_mean_mins), travel_mean_secs))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df["User Type"].value_counts()
    print("User Types:\n", user_types)

    # Display counts of gender
    try:
        genders = df["Gender"].value_counts()
        print("Gender stats:\n", genders)
    except:
        print("Gender Statistics not available.")

    # Display earliest, most recent, and most common year of birth
    try:
        birth_min = int(df["Birth Year"].min())
        birth_max = int(df["Birth Year"].max())
        birth_common = int(df["Birth Year"].mode()[0])
        print("Birth Year Statistics\nEarliest: {}\nMost Recent: {}\nMost Common: {}".format(birth_min, birth_max, birth_common))
    except:
        print("Birth Year Statistics not available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def disp_data(df):
    """Displays raw dataframe on user request."""
    raw_start = 0
    new_start = 0
    raw_end = 0
    raw_len = 5
    while True:
        raw_data = ' '
        if raw_data.lower() != 'yes':
            raw_data = str(input("\n\nWould you like to see (more) Raw Data? Enter Yes or No.\n"))
            if raw_data.lower() == 'yes':    
                raw_len_input = int(input("\nHow many rows would you like to see?\n"),0)
                if raw_len_input > 0:
                    raw_len = raw_len_input
                    raw_end += raw_len
                    new_start += raw_len
                else:
                    raw_len = raw_len
                    raw_end += raw_len
                    new_start += raw_len
                print(df.iloc[raw_start : raw_end])
                raw_start = new_start
                """raw_end = 5"""
            else:
                break
        elif raw_data.lower() == 'no':
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        if df['Start Time'].count() != 0:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            disp_data(df)
        else:
            print("Filter results in no data.")

        restart = input('\nWould you like to restart? Enter Yes or No.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
