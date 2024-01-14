# Find_Public_IP

Purpose:
The purpose of this script is to find the public IP address of the device executing the script and identify the network interface associated with that IP address. It utilizes the curl command to fetch the public IP address from ifconfig.me and then uses the ip route get command to determine the network interface bound to that IP address.

Requirements:
The script assumes that the curl command is available on the system for fetching the public IP address.
The ip command is required to perform route lookups to find the associated network interface.
Script Explanation:
1. get_public_ip() Function:
Uses subprocess.run to execute the curl command with the argument 'ifconfig.me/all'.
Parses the output to find the line containing 'ip_addr:'.
Extracts the public IP address from that line.
Returns the public IP address.
2. get_interface_for_ip(public_ip) Function:
Uses subprocess.run to execute the ip route get command with the provided public IP address.
Extracts the network interface from the output of the ip command.
Returns the network interface associated with the given public IP.
3. main() Function:
Calls get_public_ip() to retrieve the public IP address.
Prints the obtained public IP address.
Calls get_interface_for_ip() to find the network interface associated with the public IP.
Prints the network interface information.
How to Run:
Make sure Python is installed on your system.
Save the script to a file, for example, find_public_ip.py.
Ensure the script has execute permissions (chmod +x find_public_ip.py).
Run the script (./find_public_ip.py).
Notes:
The script may display errors if either curl or ip commands are not available or if there are issues with the network connection.
The accuracy of determining the network interface depends on the routing information available on the system.
Feel free to let me know if you have any specific questions or if you'd like further clarification on any part of the script!
