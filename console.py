#!/usr/bin/python3
"""
Program that is the entry point of the commmand interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Class that creates the hbnb console
    """
    prompt = '(hbnb) '

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
