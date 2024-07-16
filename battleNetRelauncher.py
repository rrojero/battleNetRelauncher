# Work around for Battle.net.exe pausing after a few minuites of downloading.
# Battle.net should be setup to Remember Login email and phone number, keep me logged in checked, Apply latest updates for recently played games
import psutil
import subprocess
import time

# Define number of times to run the script
num_loops = 10
# Define wait time between launches (seconds)
wait_time = 600

def terminate_battle_net():
    """
    Terminates any running Battle.net.exe processes.
    """
    # Get list of running processes
    for process in psutil.process_iter():
        # Check if process name matches (ignoring case)
        if "battle.net.exe" in process.name().lower():
            try:
                # Terminate the process
                process.terminate()
                print(f"Terminated Battle.net process (PID: {process.pid})")
            except psutil.NoSuchProcess:
                print(f"Process (PID: {process.pid}) already terminated")

def launch_and_terminate():
    """
    Launches Battle.net and terminates any lingering processes after wait time.
    """
    # Allow wrap up time between loops + Terminate any lingering Battle.net processes
    print("PreLaunch termination")
    time.sleep(10)
    terminate_battle_net()

    # Launch Battle.net
    subprocess.Popen("C:\Program Files (x86)\Battle.net\Battle.net.exe")  # Adjust path if needed

    # Wait for defined time
    print(f"Launched Battle.net at {time.strftime('%H:%M:%S')}")
    time.sleep(wait_time)

    # Terminate any lingering Battle.net processes
    print("PostLaunch termination")
    terminate_battle_net()

# Run the loop
for _ in range(num_loops):
    launch_and_terminate()
    print(f"Finished loop {_ + 1} out of {num_loops}")

print("Finished all loops.")
