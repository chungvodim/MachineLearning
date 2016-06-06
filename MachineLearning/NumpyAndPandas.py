import unicodecsv
import pandas as pd
import numpy as np
#import seaborn as sns

#def read_csv(filename):
#    with open(filename, 'rb') as f:
#        reader = unicodecsv.DictReader(f)
#        return list(reader)

#enrollments = read_csv('data\IntroToDataAnalysis\enrollments.csv')
#daily_engagement = read_csv('data\IntroToDataAnalysis\daily_engagement.csv')
#project_submissions = read_csv('data\IntroToDataAnalysis\project_submissions.csv')
#full_daily_engagement = pd.read_csv('data\IntroToDataAnalysis\daily_engagement_full.csv')

#print 'daily_engagement_full: {}'.format(len(full_daily_engagement['acct'].unique()))

# First 20 countries with employment data
countries = np.array([
    'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina',
    'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
    'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
    'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina'
])

# Employment data in 2007 for those 20 countries
employment = np.array([
    55.70000076,  51.40000153,  50.5       ,  75.69999695,
    58.40000153,  40.09999847,  61.5       ,  57.09999847,
    60.90000153,  66.59999847,  60.40000153,  68.09999847,
    66.90000153,  53.40000153,  48.59999847,  56.79999924,
    71.59999847,  58.40000153,  70.40000153,  41.20000076
])

# Change False to True for each block of code to see what it does

# Accessing elements
print 'Accessing elements'
if True:
    print countries[0]
    print countries[3]

# Slicing
print 'Slicing'
if True:
    print countries[0:3]
    print countries[:3]
    print countries[17:]
    print countries[:]

# Element types
print 'Element types'
if True:
    print countries.dtype
    print employment.dtype
    print np.array([0, 1, 2, 3]).dtype
    print np.array([1.0, 1.5, 2.0, 2.5]).dtype
    print np.array([True, False, True]).dtype
    print np.array(['AL', 'AK', 'AZ', 'AR', 'CA']).dtype

# Looping
if True:
    for country in countries:
        print 'Examining country {}'.format(country)

    for i in range(len(countries)):
        country = countries[i]
        country_employment = employment[i]
        print 'Country {} has employment {}'.format(country,
                country_employment)

# Numpy functions
if True:
    print 'mean of employment: {}'.format(employment.mean())
    print 'standard deviation of employment: {}'.format(employment.std())
    print 'max of employment: {}'.format(employment.max())
    print 'sum of employment: {}'.format(employment.sum())

def max_employment(countries, employment):
    '''
    Fill in this function to return the name of the country
    with the highest employment in the given employment
    data, and the employment in that country.
    '''
    #max_country = countries[employment.argmax()]
    max_country = countries[np.argmax(employment)]      # Replace this with your code
    max_value = employment.max()   # Replace this with your code
    print 'max_country: {}'.format(max_country)
    print 'max_value: {}'.format(max_value)
    return (max_country, max_value)

max_employment(countries,employment)

# Change False to True for each block of code to see what it does

# Arithmetic operations between 2 NumPy arrays
if True:
    a = np.array([1, 2, 3, 4])
    b = np.array([1, 2, 1, 2])
    
    print a + b
    print a - b
    print a * b
    print a / b
    print a ** b
    
# Arithmetic operations between a NumPy array and a single number
if True:
    a = np.array([1, 2, 3, 4])
    b = 2
    
    print a + b
    print a - b
    print a * b
    print a / b
    print a ** b
    
# Logical operations with NumPy arrays
if True:
    a = np.array([True, True, False, False])
    b = np.array([True, False, True, False])
    
    print 'a & b: {0}'.format(a & b)
    print 'a | b: {0}'.format(a | b)
    print '~a: {0}'.format(~a)
    
    print 'a & True: {0}'.format(a & True)
    print 'a & False: {0}'.format(a & False)
    
    print 'a | True: {0}'.format(a | True)
    print 'a | False: {0}'.format(a | False)
    
# Comparison operations between 2 NumPy Arrays
if True:
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([5, 4, 3, 2, 1])
    
    print 'a > b: {0}'.format(a > b)
    print 'a >= b: {0}'.format(a >= b)
    print 'a < b: {0}'.format(a < b)
    print 'a <= b: {0}'.format(a <= b)
    print 'a == b: {0}'.format(a == b)
    print 'a != b: {0}'.format(a != b)
    
# Comparison operations between a NumPy array and a single number
if True:
    a = np.array([1, 2, 3, 4])
    b = 2
    
    print 'a > b: {0}'.format(a > b)
    print 'a >= b: {0}'.format(a >= b)
    print 'a < b: {0}'.format(a < b)
    print 'a <= b: {0}'.format(a <= b)
    print 'a == b: {0}'.format(a == b)
    print 'a != b: {0}'.format(a != b)
    
# First 20 countries with school completion data
countries = np.array([
       'Algeria', 'Argentina', 'Armenia', 'Aruba', 'Austria','Azerbaijan',
       'Bahamas', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Bolivia',
       'Botswana', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi',
       'Cambodia', 'Cameroon', 'Cape Verde'
])

# Female school completion rate in 2007 for those 20 countries
female_completion = np.array([
    97.35583,  104.62379,  103.02998,   95.14321,  103.69019,
    98.49185,  100.88828,   95.43974,   92.11484,   91.54804,
    95.98029,   98.22902,   96.12179,  119.28105,   97.84627,
    29.07386,   38.41644,   90.70509,   51.7478 ,   95.45072
])

# Male school completion rate in 2007 for those 20 countries
male_completion = np.array([
     95.47622,  100.66476,   99.7926 ,   91.48936,  103.22096,
     97.80458,  103.81398,   88.11736,   93.55611,   87.76347,
    102.45714,   98.73953,   92.22388,  115.3892 ,   98.70502,
     37.00692,   45.39401,   91.22084,   62.42028,   90.66958
])

def overall_completion_rate(female_completion, male_completion):
    '''
    Fill in this function to return a NumPy array containing the overall
    school completion rate for each country. The arguments are NumPy
    arrays giving the female and male completion of each country in
    the same order.
    '''
    return (female_completion + male_completion) / 2

print overall_completion_rate(female_completion,male_completion)

# First 20 countries with employment data
countries = np.array([
    'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina',
    'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
    'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
    'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina'
])

# Employment data in 2007 for those 20 countries
employment = np.array([
    55.70000076,  51.40000153,  50.5       ,  75.69999695,
    58.40000153,  40.09999847,  61.5       ,  57.09999847,
    60.90000153,  66.59999847,  60.40000153,  68.09999847,
    66.90000153,  53.40000153,  48.59999847,  56.79999924,
    71.59999847,  58.40000153,  70.40000153,  41.20000076
])

# Change this country name to change what country will be printed when you
# click "Test Run". Your function will be called to determine the standardized
# score for this country for each of the given 5 Gapminder variables in 2007.
# The possible country names are available in the Downloadables section.

country_name = 'United States'

def standardize_data(values):
    standardized_value = (values - values.mean()) / values.std()
    return standardized_value

# Change False to True for each block of code to see what it does

# Using index arrays
if True:
    a = np.array([1, 2, 3, 4])
    b = np.array([True, True, False, False])
    
    print a[b]
    print a[np.array([True, False, True, False])]
    
# Creating the index array using vectorized operations
if True:
    a = np.array([1, 2, 3, 2, 1])
    b = (a >= 2)
    
    print a[b]
    print a[a >= 2]
    
# Creating the index array using vectorized operations on another array
if True:
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([1, 2, 3, 2, 1])
    
    print b == 2
    print a[b == 2]

def mean_time_for_paid_students(time_spent, days_to_cancel):
    return time_spent[days_to_cancel >= 7]

# Time spent in the classroom in the first week for 20 students
time_spent = np.array([
       12.89697233,    0.        ,   64.55043217,    0.        ,
       24.2315615 ,   39.991625  ,    0.        ,    0.        ,
      147.20683783,    0.        ,    0.        ,    0.        ,
       45.18261617,  157.60454283,  133.2434615 ,   52.85000767,
        0.        ,   54.9204785 ,   26.78142417,    0.
])

# Days to cancel for 20 students
days_to_cancel = np.array([
      4,   5,  37,   3,  12,   4,  35,  38,   5,  37,   3,   3,  68,
     38,  98,   2, 249,   2, 127,  35
])

#############################################
countries = ['Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda',
             'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan',
             'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
             'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia']

life_expectancy_values = [74.7,  75. ,  83.4,  57.6,  74.6,  75.4,  72.3,  81.5,  80.2,
                          70.3,  72.1,  76.4,  68.1,  75.2,  69.8,  79.4,  70.8,  62.7,
                          67.3,  70.6]

gdp_values = [ 1681.61390973,   2155.48523109,  21495.80508273,    562.98768478,
              13495.1274663 ,   9388.68852258,   1424.19056199,  24765.54890176,
              27036.48733192,   1945.63754911,  21721.61840978,  13373.21993972,
                483.97086804,   9783.98417323,   2253.46411147,  25034.66692293,
               3680.91642923,    366.04496652,   1175.92638695,   1132.21387981]

# Life expectancy and gdp data in 2007 for 20 countries
life_expectancy = pd.Series(life_expectancy_values)
gdp = pd.Series(gdp_values)

# Change False to True for each block of code to see what it does

# Accessing elements and slicing
if True:
    print 'life_expectancy[0]: {0}'.format(life_expectancy[0])
    print 'gdp[3:6]: {0}'.format(gdp[3:6])
    
# Looping
if True:
    for country_life_expectancy in life_expectancy:
        print 'Examining life expectancy {}'.format(country_life_expectancy)
        
# Pandas functions
if True:
    print life_expectancy.mean()
    print life_expectancy.std()
    print gdp.max()
    print gdp.sum()

# Vectorized operations and index arrays
if True:
    a = pd.Series([1, 2, 3, 4])
    b = pd.Series([1, 2, 1, 2])
  
    print 'a + b: {0}'.format(a + b)
    print 'a * 2: {0}'.format(a * 2)
    print 'a >= 3: {0}'.format(a >= 3)
    print 'a[a >= 3]: {0}'.format(a[a >= 3])
   
def variable_correlation(variable1, variable2):
    
    num_same_direction = None        # Replace this with your code
    num_different_direction = None   # Replace this with your code
    
    return (num_same_direction, num_different_direction)
##############################################
countries = [
    'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina',
    'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
    'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
    'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina'
]


employment_values = [
    55.70000076,  51.40000153,  50.5       ,  75.69999695,
    58.40000153,  40.09999847,  61.5       ,  57.09999847,
    60.90000153,  66.59999847,  60.40000153,  68.09999847,
    66.90000153,  53.40000153,  48.59999847,  56.79999924,
    71.59999847,  58.40000153,  70.40000153,  41.20000076
]

# Employment data in 2007 for 20 countries
employment = pd.Series(employment_values, index=countries)
print employment.argmax()
print employment.max()
def max_employment(employment):

    max_country = employment.argmax()      # Replace this with your code
    max_value = employment.loc[max_country]   # Replace this with your code

    return (max_country, max_value)

############################################################

# Change False to True for each block of code to see what it does

# Addition when indexes are the same
if True:
    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
    print 'indexes are the same: {0}'.format(s1 + s2)

# Indexes have same elements in a different order
if True:
    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([10, 20, 30, 40], index=['b', 'd', 'a', 'c'])
    print 'Indexes have same elements in a different order: {0}'.format(s1 + s2)

# Indexes overlap, but do not have exactly the same elements
if True:
    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([10, 20, 30, 40], index=['c', 'd', 'e', 'f'])
    print 'Indexes overlap: {0}'.format(s1 + s2)
    print 'Indexes overlap without NAN: {0}'.format((s1 + s2).dropna())
# Indexes do not overlap
if True:
    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([10, 20, 30, 40], index=['e', 'f', 'g', 'h'])
    print 'Indexes do not overlap: {0}'.format(s1 + s2)
    print 'Indexes do not overlap without NAN: {0}'.format((s1 + s2).dropna())

##########################################################

s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([10, 20, 30, 40], index=['c', 'd', 'e', 'f'])
print s1.add(s2, fill_value=0)

##########################################################
if True:
    s = pd.Series([1, 2, 3, 4, 5])
    def add_one(x):
        return x + 1
    print s.apply(add_one)

names = pd.Series([
    'Andre Agassi',
    'Barry Bonds',
    'Christopher Columbus',
    'Daniel Defoe',
    'Emilio Estevez',
    'Fred Flintstone',
    'Greta Garbo',
    'Humbert Humbert',
    'Ivan Ilych',
    'James Joyce',
    'Keira Knightley',
    'Lois Lane',
    'Mike Myers',
    'Nick Nolte',
    'Ozzy Osbourne',
    'Pablo Picasso',
    'Quirinus Quirrell',
    'Rachael Ray',
    'Susan Sarandon',
    'Tina Turner',
    'Ugueth Urbina',
    'Vince Vaughn',
    'Woodrow Wilson',
    'Yoji Yamada',
    'Zinedine Zidane'
])

def reverse_name(name):
    last_name = name.split()[1]
    first_name = name.split()[0]
    return last_name + ', ' + first_name

def reverse_names(names):
    return names.apply(reverse_name)

print reverse_names(names)

#############################################################

# The following code reads all the Gapminder data into Pandas DataFrames. You'll
# learn about DataFrames next lesson.

path = 'data/NumpyAndPandas/'
employment = pd.read_csv(path + 'employment_above_15.csv', index_col='Country')
female_completion = pd.read_csv(path + 'female_completion_rate.csv', index_col='Country')
male_completion = pd.read_csv(path + 'male_completion_rate.csv', index_col='Country')
life_expectancy = pd.read_csv(path + 'life_expectancy.csv', index_col='Country')
gdp = pd.read_csv(path + 'gdp_per_capita.csv', index_col='Country')

# The following code creates a Pandas Series for each variable for the United States.
# You can change the string 'United States' to a country of your choice.

employment_us = employment.loc['United States']
female_completion_us = female_completion.loc['United States']
male_completion_us = male_completion.loc['United States']
life_expectancy_us = life_expectancy.loc['United States']
gdp_us = gdp.loc['United States']

# Uncomment the following line of code to see the available country names
print employment.index.values
employment_us.plot()
# Use the Series defined above to create a plot of each variable over time for
# the country of your choice. You will only be able to display one plot at a time
# with each "Test Run".