#!/usr/bin/env python3.12
# your User class goes here

class User:
    """User Class for profile information"""
    def __init__(
            self, 
            first_name, 
            last_name,
            dob, 
            email=None, 
            driver_license=None) -> None:
        
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob,
        self.email = email
        self.driver_license = driver_license

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

user_steve = User("Steve", "Murphy", "1979", "me@here.com", "113-223-123")
user_joe = User("Joe", "Stewart", "2002", "you@there.net", "345-234-532")

# print(f"Name: {user_steve.name} E-Mail: {user_steve.email_address} Driver License: {user_steve.driver_license}")
# print(f"Name: {user_joe.name} E-Mail: {user_joe.email_address} Driver License: {user_joe.driver_license}")
print(user_steve)
print(user_joe)