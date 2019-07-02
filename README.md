# PostgreSQL Developer

This is an awesome GUI for PostgreSQL built with python-tk and psycopg2

# About:

I was getting tired of working around the limitations of postgresql on the command line.  I had to write a small python script every time I wanted to peek at data in a table or make trivial modifications.  In addition I didn't like the implementation of postgresql in Oracle's SQL Developer so I started this application.  

Rapidly Create schemas, tables, view summary information and switch connections seamlessly with this GUI.  This makes working with your postgres environment seamless and hassle-free.

# Requirements:

You must have Python version 3.3 or higher to use the application.
I'm currently working on a branch to work with earlier versions
of Python.

Before using, you will need:

- Python 3.3 or higher
- psycopg2 2.6 or higher
- latest version of Python-tk (comes bundles with most Python3 installations)


# Starting the App

To get up and running:

    python gui.py
   
The application doesn't store environment variables.
However you can set your postgres configuration manually.
In addition, the home page allows you to use the default 
postgres connection, this is:

    localhost: 5432
    Dbname: postgres
    user: postgres
    password: password



## TODO

Currently have Viewing Data implemented, I'm working on filling in the functionality to match Oracle's SQL Developer.  

# Viewing Data

## Loading Data

## Creating Tables

### Deleting Tables


# Database Schemas:
Credentials for both the VPN and Oracle database are currently set as environment
variables.
