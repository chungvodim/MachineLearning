import unicodecsv

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

enrollments = read_csv('data\IntroToDataAnalysis\enrollments.csv')
daily_engagement = read_csv('data\IntroToDataAnalysis\daily_engagement.csv')
project_submissions = read_csv('data\IntroToDataAnalysis\project_submissions.csv')

udacity_test_accounts = set()
for enrollment in enrollments:
    if enrollment['is_udacity'] == 'True':
        udacity_test_accounts.add(enrollment['account_key'])
print 'number of test accounts: {}'.format(len(udacity_test_accounts))

def remove_udacity_accounts(data):
    non_udacity_data = []
    for data_point in data:
        if data_point['account_key'] not in udacity_test_accounts:
            non_udacity_data.append(data_point)
    return non_udacity_data

def get_unique_students(data):
    unique_students = set()
    for data_point in data:
        unique_students.add(data_point['account_key'])
    return unique_students

unique_enrolled_students = get_unique_students(enrollments)
print 'number of enrollment: {}'.format(len(enrollments))
print 'number of unique enrollment: {}'.format(len(unique_enrolled_students))
# Change the key name
for engagement_record in daily_engagement:
    engagement_record['account_key'] = engagement_record['acct']
    del[engagement_record['acct']]

unique_engagement_students = get_unique_students(daily_engagement)
print 'number of engagement: {}'.format(len(daily_engagement))
print 'number of unique engagement: {}'.format(len(unique_engagement_students))

unique_project_submitters = get_unique_students(project_submissions)
print 'number of submissions: {}'.format(len(project_submissions))
print 'number of unique submissions: {}'.format(len(unique_project_submitters))

#for enrollment in enrollments:
#    student = enrollment['account_key']
#    if student not in unique_engagement_students:
#        print enrollment
#        break
### Checking For More Problem Records

num_problem_students = 0
for enrollment in enrollments:
    student = enrollment['account_key']
    if (student not in unique_engagement_students and enrollment['join_date'] != enrollment['cancel_date']):
        num_problem_students += 1
print 'Problem Records: {}'.format(num_problem_students)



non_udacity_enrollments = remove_udacity_accounts(enrollments)
non_udacity_engagement = remove_udacity_accounts(daily_engagement)
non_udacity_submissions = remove_udacity_accounts(project_submissions)

print 'number of non_udacity_enrollment: {}'.format(len(non_udacity_enrollments))
print 'number of non_udacity_engagement: {}'.format(len(non_udacity_engagement))
print 'number of non_udacity_submissions: {}'.format(len(non_udacity_submissions))

# Refining the question
paid_students = {}
for enrollment in non_udacity_enrollments:
    if not enrollment['is_canceled'] or enrollment['days_to_cancel'] > 7:
        account_key = enrollment['account_key']
        enrollment_date = enrollment['join_date']
        if account_key not in paid_students or enrollment_date > paid_students[account_key]:
            paid_students[account_key] = enrollment_date
print 'number of paid student: {}'.format(len(paid_students))

# Getting Data from First Week
from datetime import datetime

def within_one_week(join_date, engagement_date):
    time_delta = datetime.strptime(engagement_date, '%Y-%m-%d') - datetime.strptime(join_date, '%Y-%m-%d')
    return time_delta.days < 7

def remove_free_trial_cancels(data):
    new_data = []
    for data_point in data:
        if data_point['account_key'] in paid_students:
            new_data.append(data_point)
    return new_data

paid_enrollments = remove_free_trial_cancels(non_udacity_enrollments)
paid_engagement = remove_free_trial_cancels(non_udacity_engagement)
paid_submissions = remove_free_trial_cancels(non_udacity_submissions)

print 'number of paid enrollments: {0}'.format(len(paid_enrollments))
print 'number of paid engagement: {0}'.format(len(paid_engagement))
print 'number of paid submissions: {0}'.format(len(paid_submissions))

paid_engagement_in_first_week = []
for engagement_record in paid_engagement:
    account_key = engagement_record['account_key']
    join_date = paid_students[account_key]
    engagement_record_date = engagement_record['utc_date']

    if within_one_week(join_date, engagement_record_date):
        paid_engagement_in_first_week.append(engagement_record)

print 'number of paid engagement in first week: {0}'.format(len(paid_engagement_in_first_week))