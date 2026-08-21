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

