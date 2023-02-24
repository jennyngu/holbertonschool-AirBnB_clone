#!/usr/bin/python3
"""
Program that is the entry point of the commmand interpreter
"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
"""
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
"""
import models

class HBNBCommand(cmd.Cmd):
    """
    Class that creates the hbnb console
    """
    prompt = '(hbnb) '
    class_list = ["BaseModel", "User", "State", "City", "Amenity", "Review"]

    def do_quit(self, args):
        """
        Quits the console
        """
        return True

    def do_EOF(self, args):
        """
        Exits the console on EOF
        """
        return True

    def do_help(self, args):
        cmd.Cmd.do_help(self, args)

    def do_create(self, args):
        """
        Create a new instance of args[0] and prints the ID
        """
        split_args = args.split()

        if not split_args:
            print("** class name missing **")
            return

        try:
            newInst = globals()[split_args[0]]()
        except NameError:
            print("** class doesn't exist **")
            return

        newInst.save()
        print(newInst.id)

    def do_show(self, args):
        """
        Print string representation of an instance
        of class arg[0] with id arg[1]
        """
        split_args = args.split()

        if not split_args:
            print("** class name missing **")
            return
        if split_args[0] not in self.class_list:
            print("** class doesn't exist **")
            return
        if len(split_args) < 2:
            print("** instance id missing **")
            return

        all_obj = models.storage.all()
        inst_key = split_args[0] + '.' + split_args[1]

        if inst_key in all_obj:
            inst_str = all_obj[inst_key]
            return
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """
        deletes an instance of args[0] class with args[1] id
        """
        split_args = args.split()
        if not split_args:
            print("** class name missing **")
            return
        if split_args[0] not in self.class_list:
            print("** class doesn't exist **")
            return
        if len(split_args) < 2:
            print("** instance id missing **")
            return

        all_obj = models.storage.all()
        inst_key = split_args[0] + '.' + split_args[1]

        if inst_key in all_obj:
            del all_objs[inst_key]
            models.storage.save()
            return
        else:
            print("** no instance found **")

    def do_all(self, args):
        """
        prints a string representation of all classes
        if args[0] exists, limits the output to only args[0] class
        """
        split_args = args.split()
        all_obj = models.storage.all()
        all_obj_str = []

        if not args:
            for obj in all_obj_str.values():
                all_obj_str.append(str(obj))
            print(all_obj_str)
            return
        elif split_args[0] in self.class_list:
            for obj in all_obj.values():
                if type(obj).__name__ == args[0]:
                    all_obj_str.append(str(obj))
            print (all_obj_str)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """
        update an instance of args[0] class and args[1] id
        modifies or adds args[2] attribute to arg[3] value
        """
        split_args = args.split()
        if not split_args:
            print("** class name missing **")
            return
        if split_args[0] not in self.class_list:
            print("** class doesn't exist **")
            return
        if len(split_args) < 2:
            print("** instance id missing **")
            return

        all_obj = models.storage.all()
        inst_key = split_args[0] + '.' + split_args[1]

        if inst_key not in all_obj:
            print("** no instance found **")
            return
        if len(split_args) < 3:
            print("** attribute name missing **")
            return
        if len(split_args) < 4:
            print("** value missing **")
            return
        setattr(all_obj[inst_key], split_args[2], split_args[3])
        all_obj[inst_key].save()


    def emptyline(self):
        pass

    def help_quit(self):
        print("Quits the console\n")

    def help_EOF(self):
        print("Exits on EOF\n")

    def help_help(self):
        print("A list of commands that can be used\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
