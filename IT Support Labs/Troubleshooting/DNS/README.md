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
To simulate a realistic IT support issue, I intentiallu changed the VM's DNS server configuration to a invalid DNS address:
192.9.2.1

This was done to create a situation where the VM could still communicate with external IP addresses but could no longer resolve domain names 

## 4. Identify the Problem 

### Test IP connectivity 
I first tested the external IP address again:
'''cmd
ping 8.8.8.8

The VM was still able to communicate with the external IP address.
This shows that general network connectivity was still functioning 

### Test Domain Resolution 
I then tested:
'''cmd
ping google.com

The request failed because the system could not resolve google.com to an IP address.

<img width="510" height="36" alt="Screenshot 2026-08-15 at 3 59 02 PM" src="https://github.com/user-attachments/assets/1c587300-b61b-4c97-9ad5-b42de62ccc98" />
<img width="509" height="148" alt="Screenshot 2026-08-15 at 3 58 40 PM" src="https://github.com/user-attachments/assets/4b5287f4-199f-4219-be3c-35bd9da5aac0" />

### Initial Diagnosis 
The results narrowed the problem down significantly:
IP connectivity was working, but DNS name resolution was failing.

This indicated that the issue was related to DNS configuration rather than the VM's general network connection. 

## Diagnose the DNS failure 
To investigate the DNS problem further, I used the nslookup command:
'''cmd
nslookup google.com

nslookup queries the configured DNS server to determine the IP address associated with a domain name.

<img width="513" height="191" alt="Screenshot 2026-08-15 at 4 04 14 PM" src="https://github.com/user-attachments/assets/ec032c1c-e002-4938-9dfe-b55e301e631a" />

The results showed that the VM was unable to successfully resolve the domain using its configured DNS server.

### Diagnosis 
The root cause was an incorrect DNS server configuration.

Th etorubleshooting results showed:
ping 8.8.8.8
-> Successful 
ping google.com
-> Failed 
nslookup google.com
-> Failed 

This isolated the issue from general network connectivity to DNS resolution.

## 6. Correct the DNS Configuration 
To resolve the issue, I changed the VM's DNS server configuration to:
8.8.8.8

8.8.8.8 is a public DNS resolver operated by Google.

And after applying the corrected DNS configuration, I repeated the diagnostic tests.

## 7. Verify the Fix

### Verify DNS Resolution 
I first ran:
'''cmd 
nslookup google.com
'''
The DNS server successfully returned an IP address for google.com
<img width="516" height="132" alt="Screenshot 2026-08-21 at 1 22 55 PM" src="https://github.com/user-attachments/assets/e69f8f7f-481e-4c43-b4e3-154649e24b49" />

### Verify Domain Connectivity 
I then ran:
'''cmd 
ping google.com
The domain successfully resolved and the VM was able to communicate with the resulting IP address. 
<img width="512" height="157" alt="Screenshot 2026-08-21 at 1 24 05 PM" src="https://github.com/user-attachments/assets/c9d4da4b-3c4e-4288-8d0f-8c69d954d95e" />

## 8. Final result
The DNS issue was successfully resolved.
The final tests demonstrated :


'''text
Network connectivity     ✓
DNS resolution           ✓
Domain name connectivity ✓
'''



