#!/usr/bin/python3
import json
import locale
import sys
import reports
import os
import emails
import datetime

"""def load_data(data1):
  data = json.dumps(data1)
  return data"""
  
def create_data(data1):
  data2 = []
  for i in data1:
    desc = "name : {} <br/> weight : {} <br/>".format(i["name"], i["weight"])
    print(desc)
    data2.append(desc)
  return data2

def process_data():
  data = []
  ab = os.listdir("supplier-data/descriptions/")
  path = "supplier-data/descriptions/"
  print(ab)
  for i in ab:
    print(i)
    dir={}
    with open(path+i, 'r') as rf:
      rf = rf.read().split("\n")[0:3]
      name, weight, description = rf
      dir["name"] = name.replace("\n", "")
      dir["weight"] = weight.replace("\n", "")
    print(dir)
    data.append(dir)
  #data = load_data(data)
  data1 = create_data(data)
  print(data1)
  return data1


def main():
  summary = process_data()
  print(summary)
  attachment = "/tmp/processed.pdf"
  title = "Processed Update on {} {},{}".format(datetime.datetime.now().strftime("%B"),datetime.datetime.now().strftime("%d"),datetime.datetime.now().strftime("%Y"))
  paragraph = "<br/>".join(summary)
  reports.generate_report(attachment, title, paragraph)
  
  sender = "automation@example.com"
  recipient = "student-00-b65c0c4b1b82@example.com"
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  attachment_path = "/tmp/processed.pdf"
  message = emails.generate_email(sender, recipient, subject, body, attachment_path)
  print(message)
  #emails.send_email(message)

if __name__ == "__main__":
  main()

