import pytest

from terminal import Terminal

terminal = Terminal('linux')

class TestLinuxCommands:

    # Generic tests
    def test_command_does_not_exist(self):
        result = terminal.help('cool command')
        assert result == "No such command"

    def test_command_does_not_exist_and_invalid_arg(self):
        result = terminal.help('cool command', 'very nice')
        assert result == "No such command"

    # ls command tests
    def test_ls_command(self):
        result = terminal.help('ls')
        assert result == 'ls - List directory contents.'

    def test_ls_command_with_invalid_arg(self):
        result = terminal.help('ls', 'very nice')
        assert result == 'Invalid argument for command - ls'

    def test_ls_command_with_u_arg(self):
        result = terminal.help('ls', '-U')
        assert result == 'ls -U - Do not sort; list entries in directory order.'
        
    def test_ls_command_with_x_arg(self):
        result = terminal.help('ls', '-x')
        assert result == 'ls -x - List entries by lines instead of by columns.'

    # mkdir command tests 
    def test_mkdir_command(self):
        result = terminal.help('mkdir')
        assert result == 'mkdir - Creates a directory.'

    def test_mkdir_command_with_invalid_arg(self):
        result = terminal.help('mkdir', 'very nice')
        assert result == 'Invalid argument for command - mkdir'

    def test_mkdir_command_with_u_arg(self):
        result = terminal.help('mkdir', '-p')
        assert result == 'mkdir -p - No error if existing, make parent directories as needed.'

    # cat command tests 
    def test_cat_command(self):
        result = terminal.help('cat')
        assert result == 'cat - Concatenate files and print on the standard input.'

    def test_cat_command_with_invalid_arg(self):
        result = terminal.help('cat', 'very nice')
        assert result == 'Invalid argument for command - cat'

    def test_cat_command_with_D_arg(self):
        result = terminal.help('cat', '-n')
        assert result == 'cat -n - Number all output lines.'

    # Parametrized tests

    testdata_no_such_command = [
        ('ls', 'ls - List directory contents.'), ('LS', 'No such command'),
        ('mkdir', 'mkdir - Creates a directory.'), ('MKDIR', 'No such command'),
        ('cat', 'cat - Concatenate files and print on the standard input.'), ('CAT', 'No such command'),
        ('', 'No such command'), (4, 'No such command'), (None, "No such command")

    ]
    @pytest.mark.parametrize('command,expected', testdata_no_such_command)
    def test_if_command_exists(self, command, expected):
        result = terminal.help(command)
        assert result == expected


    testdata_commands_with_arg = [
        ('ls', None, 'ls - List directory contents.'),
        ('ls', '', 'ls  - List directory contents.'),
        ('ls', 'aaaaaaaaaa', 'Invalid argument for command - ls'),
        ('ls', '-u', 'Invalid argument for command - ls'),
        ('ls', '-X', 'Invalid argument for command - ls'),
        ('ls', '-U', 'ls -U - Do not sort; list entries in directory order.'),
        ('ls', '-x', 'ls -x - List entries by lines instead of by columns.'),
        ('ls', 4, 'Invalid argument for command - ls'),

        ('mkdir', None, 'mkdir - Creates a directory.'),
        ('mkdir', '', 'mkdir  - Creates a directory.'),
        ('mkdir', 'aaaaaaaaaa', 'Invalid argument for command - mkdir'),
        ('mkdir', '-P', 'Invalid argument for command - mkdir'),
        ('mkdir', '-p', 'mkdir -p - No error if existing, make parent directories as needed.'),
        ('mkdir', 4, 'Invalid argument for command - mkdir'),

        ('cat', None, 'cat - Concatenate files and print on the standard input.'),
        ('cat', '', 'cat  - Concatenate files and print on the standard input.'),
        ('cat', 'aaaaaaaaaa', 'Invalid argument for command - cat'),
        ('cat', '-N', 'Invalid argument for command - cat'),
        ('cat', '-n', 'cat -n - Number all output lines.'),
        ('cat', 4, 'Invalid argument for command - cat'),
    ]
    @pytest.mark.parametrize('command,arg,expected', testdata_commands_with_arg)
    def test_commands_with_arg(self, command, arg, expected):
        result = terminal.help(command, arg)
        assert result == expected
