# 🎧 Incident Troubleshooting – Swing Music on UmbrelOS

## 📌 Context
During an UmbrelOS update on a homelab environment, the **Swing Music** application
stopped playing audio files. The web interface loaded correctly and the music library
was indexed successfully, but every track failed with the message **"Can't load"**.

This case documents the investigation, root cause analysis, and lessons learned.

---

## 🖥️ Environment
- OS: UmbrelOS (Debian-based)
- Deployment: Docker containers managed by Umbrel
- Application: Swing Music
- Storage: Local filesystem (Downloads directory bind-mounted into container)
- Access: Local network (homelab)

---

## 🚨 Symptoms
- Swing Music UI loads normally
- Music library is indexed successfully
- Track metadata (artists, albums, covers) loads correctly
- Playback fails with repeated **"Can't load"** errors
- No explicit error messages shown in the web interface

---

## 🔍 Investigation Steps

### 1️⃣ Container & Service Validation
- Verified all containers were running using:
  ```bash
  docker ps
