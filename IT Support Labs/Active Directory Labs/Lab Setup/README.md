# Active Directory Home Lab Setup

## Overview

This lab documents the setup of a Windows Server 2025 Active Directory environment and a Windows 11 client machine.

The goal was to build a small domain environment that could be used to practice Active Directory administration, Group Policy, account management, authentication security, and troubleshooting.

---

## Lab Environment

- **Server OS:** Windows Server 2025
- **Client OS:** Windows 11 Pro
- **Virtualization:** Oracle VirtualBox
- **Domain:** `corp.local`
- **Domain Controller:** `AD-SERVER`
- **Client:** Windows 11
- **Network:** VirtualBox Host-Only Network
- **Directory Services:** Active Directory Domain Services (AD DS)
- **DNS:** Active Directory-integrated DNS

---

# 1. Windows Server Setup

I downloaded the Windows Server 2025 ISO and created a virtual machine in Oracle VirtualBox.

The server was configured with an administrator password and renamed to `AD-SERVER` to make the system easily identifiable within the lab.
<img width="1194" height="669" alt="Screenshot 2026-08-15 at 7 44 58 PM" src="https://github.com/user-attachments/assets/b7ae5b19-31ad-4af9-91d0-3134bd850ab8" />

# 2. Configure the Server

After installing Windows Server, I configured the server and renamed the device to:

```text
AD-SERVER
```
<img width="511" height="429" alt="Screenshot 2026-08-15 at 8 30 04 PM" src="https://github.com/user-attachments/assets/5f3d7ca4-224c-45c6-aa37-c848d6c4f7f4" />

# 3. Install Active Directory Domain services 
I used the `Add Roles and Features Wizard` in Server Manager to install the `Active Directory Domain Services (AD DS)` role.

AD DS provides centralized management of users, computers, groups, authentication, and security policies within a Windows domain.

<img width="511" height="438" alt="Screenshot 2026-08-15 at 8 57 40 PM" src="https://github.com/user-attachments/assets/4fabccbe-ae56-49fb-b1bf-1f2f099b3f70" />

# 4. Create the Active Directory Domain
I created the Active Directory domain:
`corp.local`
The Windows Server was configured as the domain controller for this domain.

The domain provides a centralized environment for managing users, groups, computers, authentication, and security policies.

<img width="510" height="438" alt="Screenshot 2026-08-15 at 9 09 56 PM" src="https://github.com/user-attachments/assets/6d0b33cd-74f5-4916-8177-fbe6461dbe14" />

<img width="507" height="434" alt="Screenshot 2026-08-15 at 9 14 16 PM" src="https://github.com/user-attachments/assets/dcd4d429-169e-4899-b48e-729b4bb02648" />

<img width="508" height="433" alt="Screenshot 2026-08-15 at 9 36 26 PM" src="https://github.com/user-attachments/assets/44351607-ba88-4dcb-a59b-70bd2678b25e" />


# 5. Create the IT User
I created a domain user account to simulate managing an employee through Active Directory.
The account created for the lab was:
`corp\Gurleen.b`
The user was placed within the appropriate IT organizational structure.

<img width="508" height="430" alt="Screenshot 2026-08-15 at 9 48 28 PM" src="https://github.com/user-attachments/assets/00e6da10-fceb-4f4b-8594-4a01b6006e70" />


# 6. Create the IT Staff Security Group
I created an IT Staff security group and added the IT user to the group.

Using security groups allows permissions and security settings to be managed through group membership instead of configuring users individually.

<img width="511" height="438" alt="Screenshot 2026-08-15 at 9 55 59 PM" src="https://github.com/user-attachments/assets/bbac4bb4-f786-4615-93c5-dfb1fcaa9f1c" />




