#!/usr/bin/env python3
import re
import csv
import operator

per_user = []



def error():
    errors = {}
    #log = open('sys.log', 'r').readlines()
    log = open('syslog.log', 'r').readlines()
    for line in log:
        if 'ERROR' in line:
            abc = re.search(r"ticky: ERROR ([\w ']*)", line)
            error_name = abc.group(1)
            """if abc.group[1] in errors:
                errors[abc.group[1]] += 1
            else:
                errors[abc.group[1]] = 1"""
            errors[error_name] = errors.get(error_name, 0) + 1
    #sorted(errors.items(), key = operator.itemgetter(1), reverse=True)
    sorted_errors = {k: v for k, v in sorted(errors.items(), reverse=True, key=lambda item: item[1])}
    #print(errors)
    print(sorted_errors)
    with open('error_message.csv', 'w', newline='') as host_csv:
        fieldnames = ['ERROR', 'Count']
        writer = csv.DictWriter(host_csv, delimiter=' ', fieldnames=fieldnames)
        writer.writeheader()
        for key, value in sorted_errors.items():
            writer.writerow({'ERROR': key, 'Count': value})


# function called when per_user is empty(to insert the first entry)

def insert_first_user(username, msg_type):
    user_dict = {}
    user_dict['user'] = username
    if(msg_type == 'INFO'):
        user_dict[msg_type] = user_dict.get(msg_type, 0) + 1
        user_dict['ERROR'] = user_dict.get('ERROR', 0)
    else:
        user_dict[msg_type] = user_dict.get(msg_type, 0) + 1
        user_dict['INFO'] = user_dict.get('INFO', 0)

    per_user.append(user_dict)


def user_info():
    #log = open('sys.log', 'r').readlines()
    log = open('syslog.log', 'r').readlines()
    for line in log:
        if 'ERROR' in line:
            msg_type = 'ERROR'
            username = re.search(r"\((\w.*)\)", line)
        if 'INFO' in line:
            msg_type = 'INFO'
            username = re.search(r"\((\w.*)\)", line)
    # case when per_user is empty/first entry
        if len(per_user) == 0:
            insert_first_user(username.group(1), msg_type)

        else:
            flag = 0
            for users in per_user:
            # user name present in array of objects
                if users['user'] == username:
                    flag = 1
                    if msg_type == 'INFO':
                        users['INFO'] = users['INFO'] + 1
                    else:
                        users['ERROR'] = users['ERROR'] + 1

        # username not present in array of objects
            if(flag == 0):
                insert_first_user(username.group(1), msg_type)
    header = ['Username', 'INFO', 'ERROR']
    with open('user_statistics.csv', 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(i for i in header)

        for user in per_user:
            writer.writerow((user['user'],user['INFO'],user['ERROR']))



error()
user_info()
