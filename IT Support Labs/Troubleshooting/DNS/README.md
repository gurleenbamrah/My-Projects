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
