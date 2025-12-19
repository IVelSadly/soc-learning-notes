# System Information and Monitoring Commands

## Environment
- Virtualized Linux system
- Debian-based distribution (APT package manager)

---

## cat /proc/cpuinfo
This command provides detailed information about the processor,
including architecture, cores and flags.

### Security relevance
Understanding CPU information helps security analysts identify
virtualized environments, performance limitations and potential
resource abuse scenarios.

---

## cat /proc/meminfo
Displays memory usage and allocation details.

### Security relevance
Memory analysis is important for detecting abnormal consumption,
which may indicate misconfigured services or malicious processes.

---

## top
Displays running processes and real-time resource usage.

### Security relevance
Real-time process monitoring is essential for identifying suspicious
processes, high CPU usage and unexpected behavior on systems.

---

## apt update / apt upgrade
Used to update package lists and apply system updates.

### Security relevance
Keeping systems updated reduces exposure to known vulnerabilities
and is a basic requirement for secure system administration.
