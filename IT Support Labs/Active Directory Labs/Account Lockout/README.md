# Active Directory Account Lockout Lab

## Overview

This lab demonstrates how Active Directory can be used to implement and investigate an account lockout security control.

The lab environment was configured with a Windows Server 2025 domain controller and a Windows 11 client joined to the `corp.local` domain. An account lockout policy was configured to lock an account after five unsuccessful login attempts.

The scenario simulated a potential brute-force login attempt. I tested the lockout policy, investigated the resulting security event, identified the locked account, and recovered the account through Active Directory Users and Computers.


---

## Lab Environment

- **Domain:** `corp.local`
- **Domain Controller:** Windows Server 2025
- **Client:** Windows 11 Pro
- **Virtualization:** Oracle VirtualBox
- **Network:** Host-only network
- **Active Directory:** Active Directory Domain Services (AD DS)
- **Tools:** Active Directory Users and Computers, Group Policy Management, Command Prompt, Event Viewer

---
