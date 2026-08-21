# DNS Troubleshooting

## Overview
This lab simulates a common IT support scenario where a Windows virtual machine has network connectivity but is unable to resolve domain names.

The goal was to identify whether the issue was related to network connectivity or DNS resolution, diagnose the incorrect DNS configuration, correct it, and verify that name resolution was restored 

---

## Lab Environment 

- **Host:** macOS
- **Virtualization:** Oracle VirtualBox
- **Operating System:** Windows 11
- **Network:** Virtual machine network connection
- **Tools:** Command Prompt, 'ipconfig', 'ping', 'nslookup'

---

## 1. Intial System and Network Checks 
Before troubleshooting the simulated DNS issue, I established the system's current configuration and network status.

### Hostname
The 'hostname' command was used to identify the name assigned to the Windows virtual machine.

'''cmd
hostname

### Logged-in User 
The 'whoami' command was used to identify the account currently logged into the system.

'''cmd
whoami

### IP Configuration 
The 'ipconfig' command was used to review the VM's IP configuration and determine how the system was connected to the network 

'''cmd
ipconfig

<img width="511" height="354" alt="Screenshot 2026-08-15 at 3 40 30 PM" src="https://github.com/user-attachments/assets/d8cd570e-ff1a-49c2-bf67-1dc6bd88a05b" />

These checks established the system identity and network configuration before troubleshooting began. 

## 2. Establish Network Connectivity 
Before creating the DNS failure, I tested the VM's ability to communicate with an external IP address and a domain name. 

### Test External IP Connectivity 
I used:
'''cmd
ping 8.8.8.8

A successful response demonstrated that the VM could communicate with an external IP address

### Test Domain Connectivity 
I then used:
'''cmd
ping google.com

This test verified both domain name resolution and connectivity to the resolved IP address.

<img width="509" height="156" alt="Screenshot 2026-08-15 at 3 51 05 PM" src="https://github.com/user-attachments/assets/983abf03-be35-487c-85ea-757ecd541901" />
<img width="510" height="149" alt="Screenshot 2026-08-15 at 3 51 32 PM" src="https://github.com/user-attachments/assets/08334f74-cb09-4acf-8a60-c4c08f4fd8c3" />

At this point, the VM had working network connectivity and DNS resolution 

## 3. Create the DNS Troubleshooting Scenario 



