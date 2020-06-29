#!/usr/bin/python3
""" Module console """
import cmd
import sys
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    my_dictio = {
        "BaseModel": BaseModel,
        "User": User,
        "Amenity": Amenity,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State
    }
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit - Exit console"""
        return True

    def do_EOF(self, arg):
        """Quit - Exit console"""
        return True

    def emptyline(self):
        """ if enter in empty line do nothing """
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in self.my_dictio:
            print("** class doesn't exist **")
        else:
            new_object = self.my_dictio[arg]()
            new_object.save()
            print(new_object.id)
            return

    def do_show(self, arg):
        """Prints string representation instance based on the class name"""
        listarg = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
        elif listarg[0] not in self.my_dictio:
            print("** class doesn't exist **")
        elif len(arg.split(" ")) < 2:
            print("** instance id missing **")
        else:
            for value in models.storage.all().values():
                if value.id != listarg[1]:
                    print("** no instance found **")
                elif value.__class__.__name__ == listarg[0] and\
                        value.id == listarg[1]:
                    print(value.__str__())
                    return

    def do_destroy(self, arg):
        """Delete instance based on class name and id"""
        listarg = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
        elif listarg[0] not in self.my_dictio:
            print("** class doesn't exist **")
        elif len(arg.split(" ")) < 2:
            print("** instance id missing **")
        else:
            for value in models.storage.all().values():
                if value.id != listarg[1]:
                    print("** no instance found **")
                elif value.__class__.__name__ == listarg[0] and\
                        value.id == listarg[1]:
                    del models.storage.all()[listarg[0] + "." + listarg[1]]
                    models.storage.save()
                    return

    def do_all(self, arg):
            """Prints string representations of instances"""
            values_list = []
            if len(arg) == 0:
                for value in models.storage.all().values():
                    values_list.append(str(value))
                print(values_list)
            elif arg not in self.my_dictio:
                print("** class doesn't exist **")
            else:
                for Cont, value in models.storage.all().items():
                    my_class = (Cont.split(".")[0])
                    if my_class == arg:
                        values_list.append(str(value))
                print(values_list)

    def do_update(self, arg):
        models.storage.reload
        listarg = arg.split(" ")
        if len(arg) == 0:
            print ("** class name missing **")
        elif listarg[0] not in self.my_dictio:
            print("** class doesn't exist **")
        elif len(arg.split(" ")) < 2:
            print("** instance id missing **")
        elif len(arg) == 2:
            print("** attribute name missing **")
        elif len(arg) == 3:
            print("** value missing **")
            return
        elif not eval(arg[0]):
            print("** class doesn't exist **")
        else:
			Cont = arg[0] + "." + arg[1]
			my_dictio = storage.all()
        try:
            new_info = my_dictio[Cont]
        except KeyError:
            print("** no instance found **")
            return
        try:
            attr_type = type(getattr(new_info, args[2]))
            args[3] = attr_type(args[3])
        except AttributeError:
            pass
        setattr(new_info, args[2], args[3])
        new_info.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
