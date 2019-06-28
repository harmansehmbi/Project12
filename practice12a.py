"""
    DataBase : MySQL
    Prog Lang : SQL -> Structured Query Language
    Relational DataBase management System | RDBMS
    1. Create DataBase
        DataBase is collection of Tables
        Tables can be related to each other : 1 to 1 or 1 to many | has-a or is-a
    2. Create Table in DataBase
        Table is a collection of rows and columns eg: excel sheet
        ORM : Object Relational Mapping
        Your Object's Attributes should be Table's Column Names
        But in Table we can have 1 additional column and we call it as Primary Key and Auto Increment
        1 2 3 4 5 6....
        class Customer:
            def __init__(self, name, phone, email):
                self.name = name
                self.phone = phone
                self.email = email
        create table Customer(
            cid int primary key auto_increment,
            name varchar(256),
            phone varchar(20),
            email varchar(256)
        )
    3. Insert Data in Table
    cRef = Customer('John', '+91 99999 88888', 'john@example.com')
    insert into Customer values(null, 'John', '+91 99999 88888', 'john@example.com')
    4. Install Library mysql-connector
    5. Create a DBHelper which will be accessing database
"""

