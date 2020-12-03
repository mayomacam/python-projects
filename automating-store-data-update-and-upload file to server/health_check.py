#!/usr/bin/python3
import shutil
import psutil
import emails
import requests
import socket
def mail(error):
    sender = "automation@example.com"
    recipient = "student-00-b65c0c4b1b82@example.com"
    if error == 0:
        subject = "Error - CPU usage is over 80%"
    elif error == 1:
        subject = "Error - Available disk space is less than 20%"
    elif error == 2:
        subject = "Error - Available memory is less than 500MB"
    elif error == 3:
        subject = "Error - localhost cannot be resolved to 127.0.0.1"
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_email2(sender, recipient, subject, body)
    print(message)
    #emails.send_email(message)
    
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 80

def check_available_memory():
    """available memory in linux-instance, in byte"""
    available_memory = psutil.virtual_memory().available/(1024*1024)
    return available_memory > 500

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'


to_be_checked = {
    check_cpu_usage(): "CPU usage is over 80%",
    check_disk_usage("/"): "Available disk space is less than 20%",
    check_available_memory(): "Available memory is less than 500MB",
    check_localhost(): "localhost cannot be resolved to 127.0.0.1"
}

error = False
for action, message in to_be_checked.items():
    if not action: 
        error_message = message
        error = True

if error:
    mail(error_message)
