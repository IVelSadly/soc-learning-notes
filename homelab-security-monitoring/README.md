# Proxmox Homelab – Security & Monitoring

This repository documents my personal homelab focused on **infrastructure security, monitoring, and automation**, built on top of **Proxmox VE** using limited hardware.

## 🎯 Objectives
- Practice Linux and infrastructure hardening
- Implement monitoring and alerting (Grafana, Prometheus, Alertmanager)
- Apply basic security controls (SSH hardening, firewall, fail2ban)
- Automate operational tasks using Bash and cron
- Learn by breaking and fixing real systems

## 🧱 Architecture

Proxmox Host  
├─ VM 100 – Docker Host  
│  ├─ Portainer  
│  ├─ Prometheus  
│  ├─ Grafana  
│  ├─ Alertmanager  
│  ├─ cAdvisor  
│  
└─ (future) VM 101 – Security Labs

## 🔐 Security Practices Applied
- SSH hardening (no password auth, root login restricted)
- Firewall configuration (UFW)
- Fail2Ban for brute-force protection
- Resource limits on containers
- Log size limitation in Docker

## 📊 Monitoring Stack
- Node Exporter (host metrics)
- cAdvisor (container metrics)
- Prometheus (collection)
- Grafana (dashboards & alerts)
- Discord notifications via Alertmanager

## ⚙️ Automation
- CPU governor day/night profiles
- Automatic temperature alerts
- Weekly configuration backups
- Scheduled tasks via cron

## 🧪 Troubleshooting
All issues I encountered and fixed are documented in `/docs/guia-2-troubleshooting.md`.

## 🚀 Why this project?
I built this homelab to gain **hands-on experience in security and infrastructure**, beyond theory, using real tools and real problems.

This project reflects how I learn: **by building, breaking, fixing, and documenting**.
