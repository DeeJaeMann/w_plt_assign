#!/usr/bin/env python3.12
# your User class goes here

class User:
    """User Class for profile information"""
    def __init__(self, name, email_address, driver_license):
        self.name = name
        self.email_address = email_address
        self.driver_license = driver_license

user_steve = User("Steve", "me@here.com", "113-223-123")
user_joe = User("Joe", "you@there.net", "345-234-532")

print(f"Name: {user_steve.name} E-Mail: {user_steve.email_address} Driver License: {user_steve.driver_license}")
print(f"Name: {user_joe.name} E-Mail: {user_joe.email_address} Driver License: {user_joe.driver_license}")
