# Welcome to HBNB!
**HBNB** is a project to make an Airbnb clone.
It is a project in its first part of creation called **THE CONSOLE**

![enter image description here](https://rogerimages.s3.amazonaws.com/HBNB.png)

## Description of the project
HBNB is a project that allows us to know how the creation of a WEB is from its beginning, in this first part it begins with the construction of **THE CONSOLE**, where we will have a shell with the basic commands for the control of file information.

This is used to command-line manage the information required for optimal functionality, In the main functionalities it is:

 - Creation of new BaseModel and User objects
 - Recovering BaseModel and Users from a file
 - Destroy the object, such as delete functionality.

### Scope of the project
The following diagram shows the scope of the first part of this project.


![enter image description here](https://rogerimages.s3.amazonaws.com/FirstPart.png)

Mainly the creation of the console begins where it will be connected through JSON to a storage to have the ability to save and retrieve information.

# How to start it
To start the console, just type in the command line of the main shell of your operating system the command:
``` console.py ```

You will see this when you enter the console:

# How to use it
## Examples
### Help
in the example you will find the console start word $ ./console.py,
In it you can enter a command that allows the help of the commands that can be performed.
Typing help and the command you want will receive help for this command to be used.
``` 
$ ./console.py 
(hbnb)
(hbnb)help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show

(hbnb)help quit
Quit - Exit console
(hbnb)
(hbnb)help show
Prints string representation instance based on the class name
(hbnb)
(hbnb)help destroy
Delete instance based on class name and id
(hbnb)
```
### Exit console
A simple command to return to the operating system shell, "quit", this allows you to exit the console.
```
(hbnb)
(hbnb)quit
virtual@DESKTOP:~/AirBnB_clone$ 
```
## Create BaseModel
With the command "create BaseModel" you can create a new model that is saved in the file by means of JSON.
```
(hbnb)create BaseModel
3f7606ff-e5f5-4d5a-8148-829674c353e9
(hbnb)
```
## Show Base Model
With the command "show BaseModel <id-model>" you can retrieve the information stored in the BaseModel file saved in the file.
```
(hbnb)show BaseModel 3f7606ff-e5f5-4d5a-8148-829674c353e9
[BaseModel] (3f7606ff-e5f5-4d5a-8148-829674c353e9) {'id': '3f7606ff-e5f5-4d5a-8148-829674c353e9', 'created_at': datetime.datetime(2020, 6, 30, 12, 55, 35, 572984), 'updated_at': datetime.datetime(2020, 6, 30, 12, 55, 35, 573010)}
(hbnb)
```
## Destroy Base Model
With the command "destroy BaseModel <id-model>" you can delete the information stored in the BaseModel file.
```
(hbnb)destroy BaseModel 3f7606ff-e5f5-4d5a-8148-829674c353e9
(hbnb)
```
Now again with "show BaseModel <id-model> you can check if this was removed."
```
(hbnb)show BaseModel 3f7606ff-e5f5-4d5a-8148-829674c353e9
** no instance found **
(hbnb)
```
it was effectively removed from the file.
## All Base Model
With the command "all BaseModel" the information stored in the file is obtained.
if it is empty the following is observed
```
(hbnb)all BaseModel
[]
(hbnb)
```
now let's see with information stored with 3 BaseModel
```
(hbnb)create BaseModel
95fefb0d-d73a-42f0-82cb-782708cfd6af
(hbnb)create BaseModel
686e4d9d-4255-4e73-bc09-98c189f8495f
(hbnb)create BaseModel
ba42431a-3f3d-45f4-9385-dadb5aa24667
(hbnb)
(hbnb)all BaseModel
["[BaseModel] (95fefb0d-d73a-42f0-82cb-782708cfd6af) {'id': '95fefb0d-d73a-42f0-82cb-782708cfd6af', 'created_at': datetime.datetime(2020, 6, 30, 13, 19, 56, 553920), 'updated_at': datetime.datetime(2020, 6, 30, 13, 19, 56, 553955)}", "[BaseModel] (686e4d9d-4255-4e73-bc09-98c189f8495f) {'id': '686e4d9d-4255-4e73-bc09-98c189f8495f', 'created_at': datetime.datetime(2020, 6, 30, 13, 19, 58, 617067), 'updated_at': datetime.datetime(2020, 6, 30, 13, 19, 58, 617088)}", "[BaseModel] (ba42431a-3f3d-45f4-9385-dadb5aa24667) {'id': 'ba42431a-3f3d-45f4-9385-dadb5aa24667', 'created_at': datetime.datetime(2020, 6, 30, 13, 19, 59, 288827), 'updated_at': datetime.datetime(2020, 6, 30, 13, 19, 59, 288848)}"]
(hbnb)
```
## Update Base Model
To update the information of one of the models is done with the command "update BaseModel <id-model>", in the following one of the models will be updated with the first_name "Juan".
```
(hbnb)
(hbnb)update BaseModel 95fefb0d-d73a-42f0-82cb-782708cfd6af first_name "Juan"
(hbnb)
```
now with the command "show BaseModel <id-model>" we can see how it has been updated, also see how it looks with all models.
```
(hbnb)show BaseModel 95fefb0d-d73a-42f0-82cb-782708cfd6af
[BaseModel] (95fefb0d-d73a-42f0-82cb-782708cfd6af) {'id': '95fefb0d-d73a-42f0-82cb-782708cfd6af', 'created_at': datetime.datetime(2020, 6, 30, 13, 19, 56, 553920), 'updated_at': datetime.datetime(2020, 6, 30, 13, 19, 56, 553955), 'first_name': '"Juan"'}
(hbnb)
```
# Files
This is the project file structure according to requirements.
```
AirBnB_clone/
├── AUTHORS
├── console.py
├── models
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── engine
│   │   ├── file_storage.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── place.py
│   ├── review.py
│   ├── state.py
│   └── user.py
├── README.md
└── tests
    ├── __init__.py
    └── test_models
        ├── __init__.py
        ├── test_amenity.py
        ├── test_base_model.py
        ├── test_city.py
        ├── test_engine
        │   ├── __init__.py
        │   └── test_file_storage.py
        ├── test_place.py
        ├── test_review.py
        ├── test_state.py
        └── test_user.py
```

## Testing
```
$ python3 -m unittest discover tests
```
