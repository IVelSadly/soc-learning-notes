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
  ```  
Confirmed Swing Music container was healthy and accessible.


2️⃣ Filesystem & Permissions Check
Verified music files existed inside the container.

Confirmed files were readable:

```bash
cat "/music/Downloads/Musicas Levi/example.mp3" > /dev/null
```
No permission or path issues found.


3️⃣ Volume & Path Mapping Analysis
Inspected container mounts:

```bash
docker inspect swingmusic_app_1 | grep -A 10 Mounts
```
Identified that /downloads was correctly bind-mounted from the host.

Verified indexing was reading correct paths.


4️⃣ Indexing vs Playback Behavior
Logs showed:

Successful indexing

No new files detected

No fatal errors

Conclusion: indexing worked, but streaming failed.

This narrowed the issue to audio decoding rather than file access.

---

🧠 Root Cause
The Swing Music container lacked the required audio decoding dependencies (FFmpeg).
As a result:

Metadata extraction succeeded

File access succeeded

Audio streaming failed at playback time

This issue surfaced after the UmbrelOS update due to container image changes.

---

🛠️ Workaround / Fix
Inside the Swing Music container:

```bash
apt add --no-cache ffmpeg
```
(or equivalent package manager depending on base image)

Then restart the container:

```bash
docker restart swingmusic_app_1
```
🎵 Playback functionality is restored immediately.

⚠️ Note: Changes made inside containers managed by Umbrel are not persistent across updates.
This fix is documented as a workaround rather than a permanent solution.

---

📚 Lessons Learned
Successful indexing does not guarantee playback capability

Audio applications often rely on external decoding libraries

Container updates can silently remove critical dependencies

Structured troubleshooting across filesystem, container and application layers is essential

Homelab incidents closely mirror real-world SOC / SRE troubleshooting scenarios

---

🎯 Relevance to SOC / Blue Team
This case demonstrates:

Incident triage and hypothesis testing

Root cause analysis across infrastructure layers

Differentiation between symptoms and root causes

Practical Docker and Linux troubleshooting skills

---

🖼️ Evidence

[Screenshot_2.png]

---


✅ Status
Issue understood and mitigated

Environment stabilized

Case documented for future reference

---
