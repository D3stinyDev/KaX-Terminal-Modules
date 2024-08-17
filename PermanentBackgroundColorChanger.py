def modify_terminal(terminal):
    terminal.terminal_display.configure(bg="darkblue") # This will change the background color
    terminal.command_entry.configure(bg="darkblue") # This will change the color of the command input bar
    terminal.terminal_display.insert("end", "Module loaded: Background color has been set\n")
