#!/usr/bin/env python3

from src.business_layer import Instagram

def main():
    username = input('Enter username: ')
    password = input('Enter password: ')
    hash_tag = input('Enter hash tag: ')

    Instagram(username, password, hash_tag)

if __name__=="__main__":
    main()
