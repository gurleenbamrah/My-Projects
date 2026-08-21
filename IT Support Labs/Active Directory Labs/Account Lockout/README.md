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

# 1. Configure the Account Lockout Threshold

The Active Directory environment was configured with an account lockout policy to protect user accounts from repeated failed authentication attempts.

The **Account Lockout Threshold** was configured to:

```text
5 invalid login attempts
```

This means an account will become locked after five consecutive incorrect authentication attempts.

The setting was configured through Group Policy Management.

<img width="510" height="432" alt="Screenshot 2026-08-15 at 10 12 26 PM" src="https://github.com/user-attachments/assets/282a19a2-5056-437c-8d02-281a6ac2bd51" />

# 2. Apply the Group Policy 
After configuring the account lockout policy, I forced the updated Group Policy settings to be applied using:
```cmd
gpupdate /force
```
This command tells Windows to immediately check for updated Group Policy settings and apply them.

<img width="511" height="436" alt="Screenshot 2026-08-16 at 5 01 40 PM" src="https://github.com/user-attachments/assets/d11e7655-b2c8-41b7-8081-007575d42890" />

# 3. Verify the Account Lockout Policy 
I verified that the account lockout policy was being applied to the Windows 11 client.
The following command was used:
```cmd
net accounts /domain
```
This command displays the domain account policies applied to the computer, including the configured account lockout threshold.

The threshold initially showed as Never, indicating that the policy had not yet been applied correctly.

I returned to Group Policy Management, confirmed the account lockout setting was configured within the domain policy, and applied the policy again.

After restarting the Windows 11 client, I ran the command again to verify that the account lockout threshold was now set to 5 attempts.

<img width="508" height="440" alt="Screenshot 2026-08-20 at 1 27 47 PM" src="https://github.com/user-attachments/assets/c550ff20-95fd-4a88-8759-9bd202755976" />

# 4. Create the Test Account
To safely test the account lockout security control, I created a dedicated test account rather than using an administrative account.

The account was created through Active Directory Users and Computers.

### Test Account

```Username: Lockout.Test```
A test password was configured for the account.
The account was used specifically to simulate repeated failed login attempts.

<img width="512" height="433" alt="Screenshot 2026-08-20 at 1 39 35 PM" src="https://github.com/user-attachments/assets/8d7dd369-7e63-42bd-92f7-20b809fe39c0" />

# 5. Simulate Repeated Failed Login Attempts
I used the Windows 11 client to simulate a potential brute-force login attempt against the test account.

The account lockout threshold was configured for five invalid attempts, so I intentionally entered an incorrect password five times.

After the repeated failed attempts, Windows prevented the account from being used to sign in.

This demonstrated that the Active Directory account lockout policy was functioning as intended.

<img width="508" height="436" alt="Screenshot 2026-08-20 at 1 43 26 PM" src="https://github.com/user-attachments/assets/b1764f97-b9a3-45c4-9f52-18049fb8064a" />

# 6. Investigate the Account Lockout  
After the account became locked, I investigated the incident from the domain controller.
I opened:

```Server Manager → Tools → Event Viewer```
Event Viewer was used to identify the security event associated with the account lockout.
The relevant event ID was:
```4740```

Event ID 4740 indicates that a user account was locked out.

This provides useful information for an IT administrator investigating repeated failed authentication attempts.

<img width="517" height="439" alt="Screenshot 2026-08-20 at 1 58 31 PM" src="https://github.com/user-attachments/assets/9c9640ac-21c2-4e02-935a-c2269be488f9" />

# 7. Investigate the Lockout Details
I reviewed the account lockout event to identify the affected account and investigate the source of the lockout.

The event information can help an administrator determine which account was locked and which computer was associated with the lockout.

This type of investigation is important because repeated failed authentication attempts could be caused by:
- A user repeatedly entering an incorrect password
- A saved credential using an old password
- A service or application using outdated credentials
- A potential brute-force attack
  
The administrator should investigate the cause before simply unlocking the account.
# 8. Recover the Account 
After investigating the incident, I recovered the affected account through Active Directory Users and Computers.
I navigated to:

IT → Lockout.Test → Properties → Account

The account was unlocked using the account settings.

<img width="514" height="438" alt="Screenshot 2026-08-20 at 2 02 03 PM" src="https://github.com/user-attachments/assets/f380e1b1-9909-4a34-88e9-80fb23897cf9" />

# 9. Verify Account Recovery 
After unlocking the account, I attempted to sign in again using the correct credentials.

The successful login confirmed that the account had been recovered and was no longer locked.

<img width="507" height="433" alt="Screenshot 2026-08-20 at 2 04 40 PM" src="https://github.com/user-attachments/assets/9cd448ca-0e13-40c8-8206-68e6ea0ab96d" />

# 10. Troubleshooting Process
- The troubleshooting process followed a structured approach:
- Configure the account lockout security control.
- Apply the updated Group Policy.
- Verify that the threshold was set correctly.
- Create a dedicated test account.
- Simulate repeated failed authentication attempts.
- Confirm that the account was locked.
- Investigate the security event using Event Viewer.
- Identify Event ID 4740 as the account lockout event.
- Unlock the affected account.
- Verify successful authentication after recovery.

# 11. Skills Demonstrated 
- This lab demonstrated practical experience with:
- Active Directory Users and Computers
- Group Policy Management
- Account Lockout Policy
- Group Policy troubleshooting
- gpupdate /force
- net accounts /domain
- Windows authentication troubleshooting
- Event Viewer
- Windows Security Event IDs
- Event ID 4740
- Brute-force attack detection concepts
- User account recovery
- Active Directory security administration

  








