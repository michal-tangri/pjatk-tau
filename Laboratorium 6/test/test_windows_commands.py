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