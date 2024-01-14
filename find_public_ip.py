# Copyright
# Original author: Edino De Souza
# Repository: https://github.com/edino/Find_Public_IP
# License: GPL-3.0 license - https://github.com/edino/TCPFlagsSender/tree/main?tab=GPL-3.0-1-ov-file

# Script Summary: The script identifies the public IP address and the associated network interface with internet access.
# It utilizes the curl command to fetch the public IP address from ifconfig.me and then uses the ip command to determine the network interface bound to that IP address.

# Purpose: The purpose of the script is to determine the public IP address and the corresponding network interface with internet access on the device.

# Base command used: ip_addr=$(curl -s ifconfig.me/all | grep 'ip_addr:' | awk '{print $2}') | echo "Your IP address is: $ip_addr"

# BuildDate: 1:20 AM EST 2024-01-14

# A simple way to execute this script is using the following command: curl -s https://raw.githubusercontent.com/edino/Find_Public_IP/main/find_public_ip.py | python3 -

import subprocess

def get_public_ip():
    try:
        result = subprocess.run(['curl', '-s', 'ifconfig.me/all'], stdout=subprocess.PIPE, text=True, check=True)
        ip_addr_line = [line for line in result.stdout.split('\n') if 'ip_addr:' in line][0]
        public_ip = ip_addr_line.split()[1]
        return public_ip
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

def get_interface_for_ip(public_ip):
    try:
        result = subprocess.run(['ip', 'route', 'get', public_ip], stdout=subprocess.PIPE, text=True, check=True)
        interface = result.stdout.split('dev')[1].split()[0]
        return interface
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

def main():
    print("\nFetching public IP address...\n")

    public_ip = get_public_ip()

    print(f"Your Public IP address is: {public_ip}\n")

    print("Finding the interface for the Public IP...\n")

    bound_interface = get_interface_for_ip(public_ip)

    if not bound_interface:
        print(f"Unable to determine the network interface for {public_ip}")
    else:
        print(f"The network interface bound to {public_ip} is: {bound_interface}")

if __name__ == "__main__":
    main()
