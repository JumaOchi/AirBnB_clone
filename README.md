# AirBnB Project

## Description of the project

This is a simple copy of the AirBnB website that works using a custom shell. It contains:

 - A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)

 - File that stores data (data = objects)

 - An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## Using the Command Interpreter

Run [`console.py`](console.py "The Console Script") in the your terminal

Your shell should begin displaying

    (hbnb)

and awaiting input

### Commands

#### **Create**:

Creates a new object of `class name` and prints the `id`.

    (hbnb) create <class name>

---

#### **Show**:

Prints the string representation of an instance based on the `class name` and `id`.

    (hbnb) show <class name> <id>.

---

#### **Destroy**:

Deletes an instance based on the `class name` and `id`

    (hbnb) destroy <class name> <id>.

---

#### **All**:

Prints all string representation of all instances based or not on the `class name`.

    (hbnb) all <class name>

or

    (hbnb) all.

---

#### **Update**:

Updates an instance based on the `class name` and `id` by adding or updating attribute (save the change into the JSON file).

    (hbnb) update <class name> <id> <attribute name> "<attribute value>"

> Only one attribute can be updated at the time
All other arguments will not be used
>
>     (hbnb) update BaseModel 1234-1234-1234 email "aibnb@mail.com" first_name "Betty"
>
> is the same as
>
>     (hbnb) update BaseModel 1234-1234-1234 email "aibnb@mail.com")

> `id`, `created_at` and `updated_at` can't be updated.

---

#### **Help**

Displays all the commands when run without any arguments and specifications of each command when run with a command

    guillaume@ubuntu:~/AirBnB$ ./console.py
    (hbnb) help

    Documented commands (type help <topic>):
    ========================================
    EOF  all  create  destroy  help  quit  show  update

    (hbnb)
    (hbnb) help quit
    Quit command to exit the program

---

#### **Quit**:

Use `quit` or `EOF` to terminate the program and return to your normal shell

    guillaume@ubuntu:~/AirBnB$ ./console.py
    (hbnb)
    (hbnb) quit
    guillaume@ubuntu:~/AirBnB$
