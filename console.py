#!/usr/bin/python3
""" This module defines class HBNBCommand"""

import cmd
from models.base_model import BaseModel
from models import storage
import shlex
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Contains the entry point of the command interpreter"""

    cls_dict = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
        }

    prompt = '(hbnb) '

    def do_quit(self, line):
        """ Type 'quit' to exit the command processor """

        return True

    def do_EOF(self, line):
        """ Press 'ctrl d' to exit the command processor gracefully. """

        print()
        return True

    def emptyline(self):
        """
        This method is called when an empty line is entered in response
        to the propmt. It stops the command processor from outputing the
        result of the last nonempty command entered when the user presses
        enetr without typing any command.
        """
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. EX: $ craete BaseModel
        """

        args = str(line)

        tokens = args.split(" ")

        if len(tokens) == 0:
            print("** class name missing **")
            return
        if len(tokens) == 1 and tokens[0] in self.cls_dict.keys():
            new_instance = self.cls_dict[tokens[0]]()
            new_instance.save()
            print(new_instance.id)
        elif len(tokens) > 1 and tokens[0] in self.cls_dict.keys():
            new_instance = self.cls_dict[tokens[0]]()
            for param in tokens:
                if param != tokens[0]:
                    words = param.split("=")
                    changed_word = ''
                    _str = 0
                    count = 0
                    _break = False
                    more_test = False
                    for char in words[1]:
                        count += 1
                        if count == 1 and char == '"':
                            _str = 1
                        if count == 1 and char != '"':
                            more_test = True
                            try:
                                int(char)
                            except ValueError:
                                _break = True
                                break
                        if more_test is True:
                            try:
                                if char == ".":
                                    pass
                                else:
                                    int(char)
                            except ValueError:
                                _break = True
                                break
                        if char == '"':
                            changed_word += ""
                        elif char == '_':
                            changed_word += " "
                        else:
                            changed_word += char
                    if _break is False and _str == 0:
                        numbers = changed_word.split(".")
                        if len(numbers) == 1:
                            setattr(new_instance, words[0], int(changed_word))
                        elif len(numbers) == 2:
                            setattr(new_instance, words[0],
                                    float(changed_word))
                        else:
                            pass
                    elif _break is False and _str == 1:
                        setattr(new_instance, words[0], changed_word)
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the
        class name and id. Ex: $ show BaseModel 1234-1234-1234.
        """

        words = shlex.split(line)

        if len(words) == 0:
            print('** class name missing **')
            return
        if words[0] not in self.cls_dict.keys():
            print("** class doesn't exist **")
            return
        if len(words) <= 1:
            print("** instance id missing **")
            return

        objs_dict = storage.all()

        key = words[0] + "." + words[1]

        if key in objs_dict:
            instance = objs_dict[key]
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id (save the
        change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.
        """

        args = shlex.split(line)

        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.cls_dict.keys():
            print("** class doesn't exist **")
            return
        if len(args) <= 1:
            print("** instance id missing **")
            return

        objs_dict = storage.all()

        key = args[0] + "." + args[1]

        if key in objs_dict:
            del objs_dict[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not
        on the class name. Ex: $ all BaseModel or $ all.
        """
        req_dict = []
        objs_dict = storage.all()

        if not line:
            for key in objs_dict:
                req_dict.append(str(objs_dict[key]))
            print(req_dict)
        else:
            args = shlex.split(line)
            if args[0] not in self.cls_dict.keys():
                print("** class doesn't exist **")
                return
            for key in objs_dict:
                req_dict.append(str(objs_dict[key]))
            print(req_dict)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """

        args = shlex.split(line)

        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.cls_dict.keys():
            print("** class doesn't exist **")
            return
        if len(args) <= 1:
            print("** instance id missing **")
            return

        objs_dict = storage.all()

        key = args[0] + "." + args[1]

        if key not in objs_dict:
            print("** no instance found **")
            return

        if key in objs_dict and len(args) <= 2:
            print("** attribute name missing **")
            return

        if key in objs_dict and len(args) <= 3:
            print("** value missing **")
            return

        if key in objs_dict and len(args) >= 4:
            if args[2] == 'id' or args[2] == 'created_at' or args[2] == 'updated_at':
                print(f"Can't update {args[2]}")
                return
            instance = objs_dict[key]
            if args[2] in dir(instance):
                dataType = type(getattr(instance, args[2]))
                setattr(instance, args[2], dataType(args[3]))
                instance.save()
            else:
                setattr(instance, args[2], args[3])
                instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
