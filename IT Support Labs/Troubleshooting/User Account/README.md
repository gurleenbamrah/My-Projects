# User Account Troubleshooting

## Overview 

This lab simulated a common IT support scenario where a user is unable to log into their Windows computer because their because their local user account has been disabled.

The goal was to create a standard test user, simulate an account-related login problem, investigate the account status, identify the cause, re-enable the account, and verify that the user account was active again.

---

## Lab Environment 

- **Host:** macOS
- **Virtualization:** Oracle VirtualBox
- **Operating System:** Windows 11
- **Account Used for Administration:** ITAdmin
- **Test User:** jsmith
- **Tools:** Windows Settings, Command Prompt, `net user`

---

## 1. Create a Test User
I first created a local test account named `jsmith` to simulate a user experiencing a login problem. 

### Creating the User Account 
I initially checked **Computer Management** for the Local Users and Groups option. Since this windows 11 edition did not provide that option , I used the Windows Settings interface instead. 
The account was created through:
**Settings -> Accounts -> Other users -> Add account**
I selected **"I don't have this person's sign-in information"** and created the local account.

### Configure User Privileges 
The `jsmith` account was configured as a **Standard User** rather than an administrator.

This better represent a typical employee account and follows the principle of least privilege. 
**Adding the test user**

![Add User](<img width="509" height="440" alt="Screenshot 2026-08-15 at 4 28 45 PM" src="https://github.com/user-attachments/assets/e013d7cc-b471-44d1-88af-bc13b1136a44" />
)
