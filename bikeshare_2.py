import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['all','january', 'february', 'march', 'april', 'may', 'june']

days = ['all','monday', 'tuesday', 'wednesday', 'thrusday', 'friday', 'saturday','sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = input("Choose the City (Chicago, New York city, Washington) ?\n").lower()
    while city not in(CITY_DATA ):
        try:
            print("\nInvalid input Try again\n")
        finally:
            city = input("Choose the City (Chicago, New york city, Washington) ?\n").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Which month (all, january, february, ... , june)?\n").lower()
    while month not in(months):
        try:
            print("\nInvalid input Try again\n")
        finally:
            month = input("Which month (all, january, february, ... , june)?\n").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Which day of week (all, monday, tuesday, ... sunday)?\n").lower()
    while day not in(days):
        try:
            print("\nInvalid input Try again\n")
        finally:
            day = input("Which day of week (all, monday, tuesday, ... sunday)?\n").lower()

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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("Month: ",str(months[df['month'].mode()[0]]).title(),"\n")

    # TO DO: display the most common day of week
    print ("Day: ",df['day_of_week'].mode()[0].title(),"\n")

    # TO DO: display the most common start hour
    print ("Hour:",df['hour'].mode()[0],"\n")

    print("\nThis took %s seconds." % (time.time() - start_time),"\n")
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Start station:", df['Start Station'].mode()[0],"\n")

    # TO DO: display most commonly used end station
    
    print("End station:",df['End Station'].mode()[0],"\n")
    
    # TO DO: display most frequent combination of start station and end station trip
    print("Most frequent route: ","\n")
    print(("Start Station: " + df['Start Station'] +"\n"+"End Station: " 
    + df['End Station']).mode()[0],"\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df["Trip Duration"].sum()
    
    tt_day =int(total_time//86400)
    tt_hour = int((total_time%86400)//3600)
    tt_min = int(((total_time % 86400) %3600)//60)
    tt_seg = int(((total_time % 86400) %3600)%60)
    
    print( "Total travel time:",tt_day,"d",tt_hour,"h",tt_min,"min",tt_seg,"s","\n")

    # TO DO: display mean travel time
    tm_time= df["Trip Duration"].mean()
    tm_day =int(tm_time//86400)
    tm_hour = int((tm_time%86400)//3600)
    tm_min = int(((tm_time % 86400) %3600)//60)
    tm_seg = int(((tm_time % 86400) %3600)%60)
    
    print( "Mean travel time:",tm_day,"d",tm_hour,"h",tm_min,"min",tm_seg,"s","\n")
    print("\nThis took %s seconds." % (time.time() - start_time),"\n")
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'Gender' not in df.columns:
        print("No Gender data available","\n")
    else:
        print("User per type : \n")
        print(df['User Type'].value_counts(),"\n")
    # TO DO: Display counts of gender
        print("Count per Gender : \n ")
        print(df['Gender'].value_counts(),"\n")
   
    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" not in df.columns:
        print("No Birth Year data available","\n")
    else:
        print("Birth Year details:","\n")
        print("Earliest birth year: ", int(df['Birth Year'].min()),"\n")
        print("Latest birth year: ",int(df['Birth Year'].max()),"\n")
        print("Most common birth year: ",int(df['Birth Year'].mode()[0]),"\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
 """Show raw data to the user."""
 
    start=0
    end=5
    i=0
    ans = input("Do you wanna see raw date? yes or no\n").lower()
    while ans not in ["yes","no"]:
        try:
            print("\nInvalid input Try again\n")
        finally:
            ans = input("Do you wanna see raw date? yes or no\n").lower()
    if ans == "yes":
        for i in range(len(df)):
            print(df.iloc[start:end])
            ans = input("Do you wanna see more raw date? yes or no\n").lower()
            while ans not in ["yes","no"]:
                try:
                    print("\nInvalid input Try again\n")
                finally:
                    ans = input("Do you wanna see more raw date? yes or no\n").lower()
            if ans == "yes":
                start+=5
                end+=5
            elif ans=="no":
                break
            else:
                print("\nInvalid input Try again\n")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
           break

if __name__ == "__main__":
	main()
