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
