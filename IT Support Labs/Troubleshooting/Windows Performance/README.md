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
