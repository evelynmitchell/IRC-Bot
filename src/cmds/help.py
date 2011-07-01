try:
    import config
    import err
except ImportError:
    sys.exit(err.load_module)

def help(command):
    """Returns a string containing all the available commands

    """
    response = 'Available commands: '
    for i in config.cmds_list:
        response = response + '!' + i + ' '
    return response
