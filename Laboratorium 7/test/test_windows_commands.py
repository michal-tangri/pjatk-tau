import pytest

from terminal import Terminal

terminal = Terminal('windows')


class TestWindowsCommands:

    # Generic tests
    def test_command_does_not_exist(self):
        result = terminal.help('cool command')
        assert result == "No such command"

    def test_command_does_not_exist_and_invalid_arg(self):
        result = terminal.help('cool command', 'very nice')
        assert result == "No such command"

    # dir command tests
    def test_dir_command(self):
        result = terminal.help('dir')
        assert result == 'dir - Displays a list of files.'

    def test_dir_command_with_invalid_arg(self):
        result = terminal.help('dir', 'very nice')
        assert result == 'Invalid argument for command - dir'

    def test_dir_command_with_l_arg(self):
        result = terminal.help('dir', '/L')
        assert result == 'dir /L - Uses lowercase.'
        
    def test_dir_command_with_c_arg(self):
        result = terminal.help('dir', '/C')
        assert result == 'dir /C - Display the thousand separator in file sizes.'

    # mkdir command tests 
    def test_mkdir_command(self):
        result = terminal.help('mkdir')
        assert result == 'mkdir - Creates a directory.'

    def test_mkdir_command_with_invalid_arg(self):
        result = terminal.help('mkdir', 'very nice')
        assert result == 'Invalid argument for command - mkdir'

    # cd command tests 
    def test_cd_command(self):
        result = terminal.help('cd')
        assert result == 'cd - Displays current directory or changes it.'

    def test_cd_command_with_invalid_arg(self):
        result = terminal.help('cd', 'very nice')
        assert result == 'Invalid argument for command - cd'

    def test_cd_command_with_D_arg(self):
        result = terminal.help('cd', '/D')
        assert result == 'cd /D - Change current drive.'

    # Parametrized tests

    testdata_no_such_command = [
        ('dir', 'dir - Displays a list of files.'), ('DIR', 'No such command'),
        ('mkdir', 'mkdir - Creates a directory.'), ('MKDIR', 'No such command'),
        ('cd', 'cd - Displays current directory or changes it.'), ('CD', 'No such command'),
        ('', 'No such command'), (7, 'No such command'), (None, "No such command")

    ]
    @pytest.mark.parametrize('command,expected', testdata_no_such_command)
    def test_if_command_exists(self, command, expected):
        result = terminal.help(command)
        assert result == expected


    testdata_commands_with_arg = [
        ('dir', None, 'dir - Displays a list of files.'),
        ('dir', '', 'dir  - Displays a list of files.'),
        ('dir', 'aaaaaaaaaa', 'Invalid argument for command - dir'),
        ('dir', '/c', 'Invalid argument for command - dir'),
        ('dir', '/l', 'Invalid argument for command - dir'),
        ('dir', 'c', 'Invalid argument for command - dir'),
        ('dir', 'l', 'Invalid argument for command - dir'),
        ('dir', 'C', 'Invalid argument for command - dir'),
        ('dir', 'L', 'Invalid argument for command - dir'),
        ('dir', '/C', 'dir /C - Display the thousand separator in file sizes.'),
        ('dir', '/L', 'dir /L - Uses lowercase.'),
        ('dir', 7, 'Invalid argument for command - dir'),

        ('mkdir', None, 'mkdir - Creates a directory.'),
        ('mkdir', '', 'mkdir  - Creates a directory.'),
        ('mkdir', 'aaaaaaaaaa', 'Invalid argument for command - mkdir'),
        ('mkdir', 4, 'Invalid argument for command - mkdir'),

        ('cd', None, 'cd - Displays current directory or changes it.'),
        ('cd', '', 'cd  - Displays current directory or changes it.'),
        ('cd', 'aaaaaaaaaa', 'Invalid argument for command - cd'),
        ('cd', '/d', 'Invalid argument for command - cd'),
        ('cd', 'd', 'Invalid argument for command - cd'),
        ('cd', 'D', 'Invalid argument for command - cd'),
        ('cd', '/D', 'cd /D - Change current drive.'),
        ('cd', 4, 'Invalid argument for command - cd'),
    ]
    @pytest.mark.parametrize('command,arg,expected', testdata_commands_with_arg)
    def test_commands_with_arg(self, command, arg, expected):
        result = terminal.help(command, arg)
        assert result == expected