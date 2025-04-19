import iterm2
# Main asynchronous function to retrieve and print session properties

async def main(connection):
    # Get the current iTerm2 app instance
    app = await iterm2.async_get_app(connection)
    window = app.current_window  # Get the current window
    if window:
        tab = window.current_tab  # Get the current tab in the window
        if tab:
            session = tab.current_session  # Get the current session in the tab
            if session:
                # Retrieve various session properties using async methods
                bellCount = await session.async_get_variable("bellCount")
                commandLine = await session.async_get_variable("commandLine")
                effective_root_pid = await session.async_get_variable("effective_root_pid")
                hostname = await session.async_get_variable("hostname")
                jobName = await session.async_get_variable("jobName")
                lastCommand = await session.async_get_variable("lastCommand")
                mouseInfo = await session.async_get_variable("mouseInfo")
                name = await session.async_get_variable("name")
                path = await session.async_get_variable("path")
                pid = await session.async_get_variable("pid")
                processTitle = await session.async_get_variable("processTitle")
                termid = await session.async_get_variable("termid")
                terminalIconName = await session.async_get_variable("terminalIconName")
                terminalWindowName = await session.async_get_variable("terminalWindowName")
                tty = await session.async_get_variable("tty")
                username = await session.async_get_variable("username")

                # Print all retrieved session properties to the console
                print(f"Bell Count: {bellCount}")
                print(f"Command Line: {commandLine}")
                print(f"Effective Root PID: {effective_root_pid}")
                print(f"Hostname: {hostname}")
                print(f"Job Name: {jobName}")
                print(f"Last Command: {lastCommand}")
                print(f"Mouse Info: {mouseInfo}")
                print(f"Session Name: {name}")
                print(f"Path: {path}")
                print(f"PID: {pid}")
                print(f"Process Title: {processTitle}")
                print(f"Term ID: {termid}")
                print(f"Terminal Icon Name: {terminalIconName}")
                print(f"Terminal Window Name: {terminalWindowName}")
                print(f"TTY: {tty}")
                print(f"Username: {username}")
            else:
                print("No current session found.")  # Handle missing session
        else:
            print("No current tab found.")  # Handle missing tab
    else:
        print("No current window found.")  # Handle missing window

# Run the main function using iTerm2's event loop
iterm2.run_until_complete(main)
