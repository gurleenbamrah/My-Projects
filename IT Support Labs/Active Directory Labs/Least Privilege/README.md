## Overview

This lab demonstrates the principle of **least privilege** using Active Directory and NTFS permissions.

The scenario is based on a company that wants to ensure ordinary employees do not receive unnecessary access to IT resources.

The goal was to:

- Verify that `gurleen.b` does not have administrator privileges
- Review the user's Active Directory group memberships
- Create a standard employee account with limited access
- Use an Active Directory security group to control access
- Configure NTFS permissions on an IT folder
- Verify that an IT employee can access the resource
- Verify that a regular employee is denied access

---

## Lab Environment

- **Domain:** `corp.local`
- **Domain Controller:** AD-SERVER
- **Client:** Windows 11
- **IT User:** `gurleen.b`
- **Regular Employee:** `employee.test`
- **Security Group:** `IT Staff`
- **Tools:** Command Prompt, Active Directory Users and Computers, Windows File Explorer

---
# 1. Verify User Privileges

The first step was to determine what privileges and group memberships were assigned to `gurleen.b`.

### Check Group Memberships

The following command was used:

```cmd
whoami /groups
```
This command displays the security groups associated with the currently logged-in account.

The results did not show:
```
BUILTIN\Administrators
```
This indicated that gurleen.b was not a member of the local Administrators group.

<img width="514" height="434" alt="Screenshot 2026-08-20 at 4 11 01 PM" src="https://github.com/user-attachments/assets/db905021-23fa-42b1-94b6-3e7af973dc01" />

This screenshot demonstrates that gurleen.b does not have the BUILTIN\Administrators group membership.
---
# 2. Verify Administrative Access 
To further test whether the account had administrative privileges, an administrative command was attempted.
```cmd
net session
```
The command returned:
```
Access is denied.
```
This provided additional evidence that the current account did not have the required administrator privileges to perform the administrative operation.

<img width="514" height="438" alt="Screenshot 2026-08-20 at 4 43 18 PM" src="https://github.com/user-attachments/assets/8360703b-9221-4c70-bb0b-d13c4ee0dc9c" />

This demonstrated that the standard user account could not perform the administrative operation.
---
# 3. Verify Group Membership from Active Directory
The user's membership was then reviewed from the administrator side using Active Directory Users and Computers.

The purpose was to confirm which security groups the user belonged to and verify that access was being managed through group membership rather than unnecessary administrator privileges.

<img width="509" height="437" alt="Screenshot 2026-08-20 at 4 48 06 PM" src="https://github.com/user-attachments/assets/4189fb68-4c59-4879-85a6-0153577fb931" />

The user was associated with the appropriate IT security group rather than being granted administrator privileges.

This follows the principle of least privilege by giving the user access through a specific security group instead of making the user a system administrator.
---
# 4. Create a Regular Employee Account
A second user was created to represent an ordinary employee who should not have access to IT-specific resources.

## Account Created
- **Username:** employee.test
- **Account Type:** Standard domain user
- **Password:** Created for the lab

The new employee's group membership was reviewed after the account was created.
The account was intended to remain a regular employee and was not added to the IT Staff security group.

<img width="514" height="437" alt="Screenshot 2026-08-20 at 4 55 59 PM" src="https://github.com/user-attachments/assets/3f58b8d5-3373-4f5d-ab80-5f95365fd401" />

<img width="511" height="441" alt="Screenshot 2026-08-20 at 4 56 46 PM" src="https://github.com/user-attachments/assets/357b9eb2-3cd8-418d-bdd1-aeeb0ad1f78a" />
---
# 5. Create the IT Resource
A folder representing company IT resources was created on the domain controller.
The structure was organized to simulate company data and an IT-specific resource.
Example:
```
Company Data
└── IT
```
The IT folder was used as the protected resource for this access control test.
The goal was to allow members of the IT Staff security group to access the folder while preventing ordinary employees from accessing it.
---
# 6. Configure NTFS Permissions  
The permissions for the IT folder were configured using Windows NTFS security settings.

The folder's properties were opened and the Security tab was used to configure access.

The IT Staff security group was given permission to access and modify the folder.
## Permission Configuration
The IT Staff group was granted the appropriate permissions required to work with the IT resource.

This allowed access to be managed through group membership rather than by assigning permissions individually to each employee.

<img width="516" height="442" alt="Screenshot 2026-08-20 at 5 15 40 PM" src="https://github.com/user-attachments/assets/bc5cdc9d-46d7-4ebd-b77b-f47b7ea55ca7" />

This screenshot demonstrates that access to the folder was assigned to the IT Staff security group.
---







