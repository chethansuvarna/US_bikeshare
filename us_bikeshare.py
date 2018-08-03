import time
import pandas as pd
import numpy as np
import pdb

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def city_input():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("enter chicago or new york or washington\n")
    city_lower = city.lower()
    while True:
        if city_lower=='chicago':
            return 'chicago'
        elif city_lower=='new york':
            return 'new york city' 
        elif city_lower=='washington':
            return 'washington'
        else:
            print("Please enter the city name asked above... Lets try again!!! ")
            return city_input()
    # TO DO: get user input for month (all, january, february, ... , june
def filter_input():    
    filters=input("\nHow you want to filter data by month or day of week or no filters type none for no filters\n").lower()
    if filters=='month':
        return 'month'
    elif filters =='day':
        return 'day_of_week'
    elif filters=='none':
        return 'none'
    else:
        print("\nOops!! looks like you have entered wrong filter lets try again...\n Enter month or day or none to choose filter\n")
        return filter_input()
    
def which_month(m):
    '''to get the month which user likes to filter the data by'''
    if m=='month':
        month=input("choose the month from january,february,march,april,may or june\n")
        while month.strip().lower() not in ['january','february','march','april','may','june']:
            print("oops looks like you have entered wrong input try again")
        return month.strip().lower()
    else:
        return 'none'
def which_day(d):
    '''to get the day of the week to filter the data'''
    #pdb.set_trace()
    if d=='day_of_week':
        day=input("Which day you want to filter the data by \n monday, tuesday, wednesday, thursday, friday, saturday, sunday \n").lower()
        if day not in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
            print("oops looks like you have entered wrong input lets try again")
            return which_day(d)
        return day
    else:
        return 'none'

def load_data(city):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print("\nLoading data ......\n")
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    
    return df
def load_filters(df,time,month,week_day):
    '''to load filters into dataframe'''
    if time=='month':
        months=['january','februray','march','april','may','june']
        month=months.index(month) +1
        df=df[df['month']==month]
    if time=='day_of_week':
        days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        for d in days:
            if week_day.capitalize() in d:
                day_of_week=d
        df=df[df['day_of_week']==day_of_week]
    return df
    
    

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    pop_month=df['month'].mode()[0]
    print("Most popular month is : ",pop_month)
    # TO DO: display the most common day of week
    pop_day=df['day_of_week'].mode()[0]
    print("Most popular day of week is: ",pop_day)

    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    comm_starthour=df['hour'].mode()[0]
    print("Common start time is: ",comm_starthour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    comm_start_station=df['Start Station'].mode()[0]
    print("most common start station is: ",comm_start_station)
    # TO DO: display most commonly used end station
    comm_end_station=df['End Station'].mode()[0]
    print('most common end station is: ',comm_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    trip=df.groupby(['Start Station','End Station']).size().nlargest(1)
    print("Most common start and end station combination is:\n ",trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time=df['Trip Duration'].sum()
    mean_time=round(df['Trip Duration']).mean()
    m,s=divmod(total_time,60)
    h,m=divmod(m,60)
    d,h=divmod(h,24)
    y,d=divmod(d,365)
    print("total time travel is  {}days {} hour {} minutes {} seconds".format(y,d,h,m,s)) 
    # TO DO: display mean travel time
    m,s=divmod(mean_time,60)
    h,m=divmod(m,60)
    print("Average time is {} hour {} minutes {} seconds".format(h,m,s))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    try:
        print('\nCalculating User Stats...\n')
        start_time = time.time()
          

    # TO DO: Display counts of user types
        user_types=df['User Type'].value_counts()
        print(user_types)
   
    # TO DO: Display counts of gender
        if 'Gender' in df.index:
            genders=df['Gender'].value_counts()
            print(genders)
        else:
            print("No gender data available!!")
    # TO DO: Display earliest, most recent, and most common year of birth
        if 'Birth Year' in df.index:
            earliest_birthyear=np.min(df['Birth Year'])
            print("Earliest birth year among users is: ",earliest_birthyear)
            most_recent_birthyear=np.max(df['Birth Year'])
            print("Most recent birth year among users is: ",most_recent_birthyear)
            comm_birthyear=df['Birth Year'].mode()[0]
            print("Most common birth year among users is: ",comm_birthyear)
        else:
            print("No Birth years found!!")
    except Exception as e:
        print(e)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city=city_input()
        df=load_data(city)
        filters=filter_input()
        month=which_month(filters)
        day=which_day(filters)
        df = load_filters(df,time,month,day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
