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

<img width="509" height="440" alt="Screenshot 2026-08-15 at 4 28 45 PM" src="https://github.com/user-attachments/assets/c2d1ef7c-cf38-4dc0-b22f-2c61686b5210" />

**jsmith configured as a Standard User**

<img width="515" height="441" alt="Screenshot 2026-08-15 at 4 30 57 PM" src="https://github.com/user-attachments/assets/7e7dd1cf-acb3-402c-93d5-4ad5302b35de" />

---
### 2. Simulate the Login Problem 
To create the troubleshooting scenario, I intentionally disabled the `jsmith` account.
I used the following command:
```cmd
net user jsmith /active:no
```
The `net user` command is a built-in Windows tool used to manage local user accounts.
- `jsmith` identifies the account being modified.
- `/active:no` disables the account.
This simulated a situation where a user is unable to log in because their account has been disabled.
<img width="492" height="184" alt="Screenshot 2026-08-15 at 4 37 26 PM" src="https://github.com/user-attachments/assets/7fd7b6bc-5f8a-44c6-b2bd-1440a27ee996" />

---
 ## 3. Test the User Login 
 I then attempted to reproduce the user's login problem.
 I signed out of the ITAdmin account and attempted to log in as jsmith.

 The `jsmith` account was not available as expected, so I continued the investigation using Command Prompt.
 
 I used:

```cmd
net user jsmith
```
The command displayed the current configuration and status of the account.

<img width="494" height="304" alt="Screenshot 2026-08-15 at 4 49 07 PM" src="https://github.com/user-attachments/assets/72d169a9-0a79-41b4-8a9a-873fa26e35cc" />

 
 The output showed:

```text
Account active               No
```

This confirmed that the account was currently disabled.

---

## 4. Diagnose the Problem

The investigation showed that the computer itself was not necessarily the problem. The issue was with the status of the user's local account.

Using:

```cmd
net user jsmith
```

I confirmed that:

```text
Account active               No
```


### Diagnosis
The `jsmith` account was disabled, preventing the user from logging in.
This narrowed the problem down to the local user account rather than the computer's general functionality.

---

## 5. Fix the Account
I re-enabled the `jsmith` account using:

```cmd
net user jsmith /active:yes
```

The `/active:yes` parameter changes the account status back to active.
<img width="493" height="77" alt="Screenshot 2026-08-15 at 4 53 00 PM" src="https://github.com/user-attachments/assets/958d9378-2e52-4a9c-9d40-d91a596910f7" />

---

## 6. Verify the Fix 
After re-enabling the account, I verified the account status using:

```cmd
net user jsmith
```

The output showed:

```text
Account active               Yes
```

This confirmed that the account was active again and should now be able to authenticate.
<img width="489" height="299" alt="Screenshot 2026-08-15 at 4 54 32 PM" src="https://github.com/user-attachments/assets/d7c21939-ef66-45d2-be5b-7fb6d4a56849" />

---

## Final Result

The simulated login issue was successfully diagnosed and resolved.

**Problem:** User account was disabled  
**Cause:** `jsmith` had been set to inactive  
**Fix:** Re-enabled the account using `net user jsmith /active:yes`  
**Verification:** `Account active` changed from `No` to `Yes`

---

## Skills Demonstrated

- Windows user account management
- Local account troubleshooting
- Command Prompt
- `net user`
- Account status verification
- User privilege configuration
- Problem diagnosis
- Troubleshooting methodology
- Principle of least privilege






