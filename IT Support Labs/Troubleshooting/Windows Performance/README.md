# Windows Performance Troubleshooting

## Overview

This lab simulates a common IT support scenario where a user reports that their computer has become slow and applications are taking a long time to open.

The goal was to investigate the system's resource usage, identify whether CPU, memory, disk, or startup applications were contributing to the issue, create a controlled high-CPU scenario, identify the process responsible, resolve the issue, and verify that system performance improved.

---

## Lab Environment

- **Host:** macOS
- **Virtualization:** Oracle VirtualBox
- **Operating System:** Windows 11
- **Issue:** Computer has become slow and applications take a long time to open
- **Tools:** Task Manager, PowerShell

---

## 1. Open Task Manager and Establish a Baseline
I started by opening **Task Manager**, a built-in Windows tool used to monitor system resources and running processes.
The initial goal was to measure the system's performance before making any changes.

### Resource Monitoring

I reviewed the following resource categories in Task Manager:

- **CPU** — Measures how much processing power is currently being used.
- **Memory** — Shows how much RAM is being used.
- **Disk** — Shows disk activity and usage.
- **Ethernet** — Shows network activity.

Rather than assuming that the computer needed more RAM or that one specific resource was causing the problem, I first collected performance data.
This is an important troubleshooting approach:

> **Measure first instead of assuming the cause of the problem.**

<img width="509" height="434" alt="Screenshot 2026-08-15 at 5 05 27 PM" src="https://github.com/user-attachments/assets/16c1f67d-cfbd-4827-9efd-5b6bc4e99ef6" />

The initial performance check did not show evidence of a major CPU, memory, disk, or network bottleneck.

---
## 2. Investigate Running Processes

I then reviewed the running processes in Task Manager and sorted them by CPU usage from highest to lowest.

The purpose was to determine whether a specific application or process was consuming an unusually large amount of CPU resources.

<img width="512" height="443" alt="Screenshot 2026-08-15 at 5 10 42 PM" src="https://github.com/user-attachments/assets/752063cd-a73d-49c2-bee7-44eb106c572d" />

At this stage, there was no obvious process causing a significant performance issue.

---

## 3. Investigate Memory Usage

I also reviewed the system's memory usage.

A percentage by itself does not necessarily indicate a problem. For example, seeing 65% memory usage would need to be considered in relation to how much RAM the computer actually has.

This reinforced the importance of looking at the available system resources rather than assuming that a percentage automatically indicates a problem.

At this point, there was no evidence that CPU, memory, or disk usage was causing a major performance problem.

> **In IT support, troubleshooting can involve ruling out potential causes rather than immediately finding a problem.**

<img width="511" height="438" alt="Screenshot 2026-08-15 at 5 14 10 PM" src="https://github.com/user-attachments/assets/20d2be2c-07df-49d0-9516-8414cac31b9d" />

---

## 4. Investigate Startup Applications

I then checked **Startup apps** in Task Manager.

Startup applications are programs that Windows automatically launches when the computer starts.

I reviewed the startup applications and their reported startup impact.

No application showed a high startup impact that would explain the reported performance problem.

<img width="518" height="440" alt="Screenshot 2026-08-15 at 5 21 56 PM" src="https://github.com/user-attachments/assets/e10c4ed3-e2ae-410f-a4fc-7a9fb68c050e" />

At this point, the investigation had ruled out several potential causes instead of randomly changing system settings.

---

## 5. Simulate High CPU Usage

To create a controlled performance problem, I intentionally generated high CPU usage using PowerShell.

PowerShell is a Windows command-line and automation tool.

I used the following command:

```powershell
while ($true) {$x = 1 + 1}
```
This command continuously repeats the calculation, creating a sustained CPU workload.

<img width="513" height="441" alt="Screenshot 2026-08-15 at 5 29 04 PM" src="https://github.com/user-attachments/assets/061668ab-fa3f-4d7a-a300-b70a037cb749" />

I then returned to Task Manager to observe the effect of the process on system performance.

<img width="512" height="444" alt="Screenshot 2026-08-15 at 5 29 16 PM" src="https://github.com/user-attachments/assets/eb334014-15c1-4426-88ed-e9cd1219a71b" />

CPU usage increased significantly, providing evidence that a process was creating a CPU bottleneck.

---
## 6. Diagnose the Performance Problem

Once the high CPU usage was observed, I investigated the process responsible for the resource consumption.

The responsible process was **PowerShell**, which was running the continuous workload created for this lab.

The troubleshooting process was:

1. Observe the performance symptoms.
2. Measure system resource usage.
3. Identify the resource experiencing high usage.
4. Identify the process responsible.
5. Determine whether the process is legitimate.
6. Take appropriate action.

### Important IT Support Consideration

A high-resource process should not automatically be terminated.

For example, if a user reports that an application is using a large amount of CPU because it is processing a large file, immediately ending the process could cause the user to lose work or interrupt an important operation.

Instead, an IT support technician should first determine:

- What application is using the resource?
- Why is it using the resource?
- Is the activity expected?
- Is the user currently working with the application?
- Can the task safely be stopped or delayed?

In this controlled lab environment, the PowerShell process was intentionally created to simulate the performance problem, so ending the process was appropriate.

---

## 7. Resolve the Issue

I ended the PowerShell process using **End Task** in Task Manager.

This stopped the continuous CPU workload.

---

## 8. Verify the Fix

After ending the process, I waited several seconds and checked Task Manager again.

CPU usage had decreased after the PowerShell process was terminated.

This confirmed that the process was responsible for the simulated CPU bottleneck and that removing it restored normal resource usage.

<img width="521" height="448" alt="Screenshot 2026-08-15 at 5 31 25 PM" src="https://github.com/user-attachments/assets/24dfc8f8-8220-4117-8a0f-f2e3b4c7036d" />

---

## Final Result

The simulated performance issue was successfully investigated and resolved.

**Problem:** Computer performance was slow due to high CPU usage.

**Investigation:** Task Manager was used to measure CPU, memory, disk, and network usage and identify the responsible process.

**Cause:** A PowerShell process was intentionally generating continuous CPU activity.

**Fix:** The simulated high-CPU process was terminated.

**Verification:** CPU usage decreased after the process was ended.

---

## Troubleshooting Approach

This lab demonstrated the importance of using evidence rather than assumptions when troubleshooting performance issues.

The process followed was:

```text
Measure → Investigate → Identify → Diagnose → Resolve → Verify
```

---

## Skills Demonstrated

- Windows performance troubleshooting
- Task Manager
- PowerShell
- CPU and memory monitoring
- Process investigation
- Resource utilization analysis
- Performance bottleneck identification
- Problem diagnosis
- Controlled troubleshooting
- Verification of corrective actions
- Customer-focused troubleshooting


