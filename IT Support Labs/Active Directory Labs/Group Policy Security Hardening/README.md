# Group Policy Security Hardening Lab

## Overview

This lab demonstrates how Group Policy can be used to enforce security controls across Windows workstations in an Active Directory environment.

The scenario represents a company that wants to prevent users from using weak passwords and improve workstation security.

The lab focuses on two security controls:

- Disabling AutoPlay on Windows workstations
- Increasing the minimum password length requirement

The goal was to configure the security controls through Group Policy, apply them to a Windows 11 workstation, verify that the policies were successfully applied, and test that the password requirement was enforced.

---

## Lab Environment

- **Virtualization:** Oracle VirtualBox
- **Domain Controller:** `AD-SERVER`
- **Domain:** `corp.local`
- **Client:** Windows 11 Pro
- **Tools:** Group Policy Management, Command Prompt, Group Policy Results, Active Directory Users and Computers

---

# 1. Create the Workstation Security Policy

I created a new Group Policy Object (GPO) named:

```text
IT-Workstation-Security
```
The purpose of this policy was to apply workstation security settings to Windows computers within the Active Directory environment.

The Windows 11 workstation was configured to receive the policy.

<img width="509" height="436" alt="Screenshot 2026-08-20 at 2 33 12 PM" src="https://github.com/user-attachments/assets/d30be01c-ab56-4572-a99d-4f0031644820" />

# 2. Increase the Minimum Password Length
The minimum password length requirement was changed from:
```7 characters```
to:
```12 characters```
Increasing the minimum password length helps prevent users from choosing short and weaker passwords.

The policy was configured through Group Policy Management so that the security requirement could be centrally enforced across the domain.

<img width="512" height="442" alt="Screenshot 2026-08-20 at 3 13 50 PM" src="https://github.com/user-attachments/assets/83638ff3-cf9d-4bbc-8383-49bf2d13bae3" />

# 3. Apply the Group Policy
After changing the password requirement, I forced the updated Group Policy settings to be applied using:
```cmd
gpupdate /force
```
This command tells Windows to immediately check for updated Group Policy settings and apply them.
The Windows 11 workstation was then restarted to ensure the updated domain policy was fully applied.

# 4. Verify the Password Policy
After applying the updated Group Policy, I verified the domain password policy using:
```cmd
net accounts /domain
```
This command displays the domain account policy settings, including the minimum password length.
The results were checked to confirm that the minimum password length had been changed to 12 characters.

# 5. Test Password Enforcement
To verify that the security control was actually being enforced, I attempted to change the password for the test account:
```Lockout.Test```
I intentionally entered a password that was shorter than the required 12 characters.
Windows rejected the password because it did not meet the configured minimum password length requirement.
This confirmed that the Group Policy security control was successfully being enforced.

<img width="511" height="437" alt="Screenshot 2026-08-20 at 3 28 42 PM" src="https://github.com/user-attachments/assets/4122175d-9ea8-4fc5-ae62-d55fdf49bd1d" />

# 6. Security Control Verification

The password security control was successfully configured, applied, and tested.

| Security Control | Configuration | Result |
|---|---|---|
| Minimum Password Length | 12 characters | Successfully applied |
| Group Policy | `IT-Workstation-Security` | Applied to Windows 11 |
| Password Testing | Short password attempted | Rejected |

# 7. Troubleshooting and Verification Process
- The troubleshooting and verification process followed these steps:
- Created the IT-Workstation-Security Group Policy.
- Changed the minimum password length from 7 to 12 characters.
- Applied the updated policy using gpupdate /force.
- Restarted the Windows 11 workstation.
- Used net accounts /domain to verify the updated password requirement.
- Attempted to change the Lockout.Test password.
- Entered a password shorter than 12 characters.
- Confirmed that Windows rejected the password.

This demonstrated that the security policy was not only configured but was also being enforced by the workstation.

# 8. Skills Demonstrated
This lab demonstrated practical experience with:
- Active Directory Group Policy
- Group Policy Objects (GPOs)
- Group Policy Management
- Password security hardening
- Minimum password length configuration
- Password policy enforcement
- ```gpupdate /force```
- ```net accounts /domain```
- Windows authentication troubleshooting
- Security control verification
- Active Directory security administration
