class Terminal:

    def __init__(self, os):
        self.os = os

        if os == 'linux':
            self.commands = {
                'ls': {
                    '': 'List directory contents.',
                    '-U': 'Do not sort; list entries in directory order.',
                    '-x': 'List entries by lines instead of by columns.'
                },
                'mkdir': {
                    '': 'Creates a directory.',
                    '-p': 'No error if existing, make parent directories as needed.',
                },
                'cat': {
                    '': 'Concatenate files and print on the standard input.',
                    '-n': 'Number all output lines.'
                },
            }

        if os == 'windows':
            self.commands = {
                'dir': {
                    '': 'Displays a list of files.',
                    '/C': 'Display the thousand separator in file sizes.',
                    '/L': 'Uses lowercase.',
                },
                'mkdir': {
                    '': 'Creates a directory.',
                },
                'cd': {
                    '': 'Displays current directory or changes it.',
                    '/D': 'Change current drive.'
                },
            }

    def help(self, command, arg=None):
        if command not in self.commands:
            return "No such command"

        if arg is not None:
            if arg not in self.commands[command]:
                return "Invalid argument for command - %s" % (command)
            return "%s %s - %s" % (command, arg, self.commands[command][arg])

        return "%s - %s" % (command, self.commands[command][''])