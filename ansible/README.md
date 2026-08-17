# 🚀 Homelab Operations - Ansible Automation

Automating my homelab infrastructure using **Ansible** by following Infrastructure as Code (IaC) principles.

This repository is part of my **Homelab Operations** project, where I automate the deployment, configuration, and maintenance of services running across multiple Linux servers.

---

# 🎯 Project Goal

The objective is to eliminate manual server configuration by making every deployment reproducible through Ansible.

A fresh Ubuntu server should be fully configured with a single command.

```bash
ansible-playbook playbooks/site.yml
```

---

# 🖥️ Infrastructure

## Control Node

| Host | Purpose |
|------|---------|
| Ryzen Homelab | Runs Ansible and manages all servers |

## Managed Nodes

| Host | Purpose |
|------|---------|
| Pentium NAS | Monitoring services and self-hosted applications |
| Future Servers | Automatically provisioned using Ansible |

---

# 📂 Repository Structure

```text
ansible/
├── ansible.cfg
├── inventory/
├── playbooks/
├── roles/
├── group_vars/
├── host_vars/
├── templates/
├── files/
└── README.md
```

---

# 🛠️ Planned Roles

- Common Server Configuration
- Docker Installation
- Prometheus
- Grafana
- Alertmanager
- cAdvisor
- Node Exporter
- Docker Health Exporter
- Uptime Kuma
- Cloudflared

---

# 🚧 Current Progress

## Phase 1 ✅

Monitoring Platform

- Prometheus
- Grafana
- Alertmanager
- Node Exporter
- cAdvisor
- Docker Health Exporter
- Uptime Kuma
- Discord Alerts

---

## Phase 2 🚧

Ansible Automation

Current Focus:

- Repository Structure
- Inventory
- Roles
- Automated Deployment

---

# 🗺️ Roadmap

- ✅ Monitoring Stack
- 🚧 Ansible Automation
- ⏳ Terraform
- ⏳ Kubernetes
- ⏳ CI/CD
- ⏳ Datadog
- ⏳ Portfolio Website

---

# 💡 Objectives

- Infrastructure as Code
- Idempotent Deployments
- Modular Roles
- Production-style Project Structure
- Complete Documentation
- Recruiter-friendly GitHub Repository

---

# 📄 License

MIT License
