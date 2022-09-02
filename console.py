#!/usr/bin/python3
"""
console for the hbnb project console.py
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    class defining console.py attributes & methods
    """
    prompt = '(hbnb)'
    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        """
        method called when 'quit' is passed by the user; provides a way of
        exiting the command line interpreter (via Ctrl+d)
        """
        # Return True to stop the command loop
        return True

    def do_EOF(self, arg):
        """EOF implementation to exit the program (via Ctrl+d)\n"""
        """
        method called when Ctrl+d is typed in; provides the standard way of
        exiting the command line interpreter (via Ctrl+d). Note: Ctrl+d sends
        an EOF (End Of File) signal and by default Cmd does not know what
        to do with it unless the do_EOF method is implemented.
        """
        # Return True to stop the command loop
        return True

    def emptyline(self):
        """
        method that disables the repetition of the last command on passing
        an empty line. Note: by default when an empty line is entered, the
        last command is repeated; one can change this behavior by overriding
        the emptyline method as shown below
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
