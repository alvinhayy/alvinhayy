<img src="assets/banner.png" alt="Alvin Dhiya'ul H — mobile security, reverse engineering, Android" width="100%">

<p align="center">
  <a href="https://hayyvin.my.id"><img src="https://img.shields.io/badge/site-hayyvin.my.id-111111?style=flat-square"></a>
  <a href="https://blog.hayyvin.my.id"><img src="https://img.shields.io/badge/blog-writing-d6201c?style=flat-square"></a>
  <a href="https://writeup.hayyvin.my.id"><img src="https://img.shields.io/badge/writeups-HTB%20%2F%20CTF-111111?style=flat-square"></a>
  <a href="https://notes.hayyvin.my.id"><img src="https://img.shields.io/badge/notes-reference-6c6c6c?style=flat-square"></a>
</p>

I take apart Android applications, and I automate the parts of offensive work
that should not need a human.

Most of my time goes to the awkward middle of mobile security — the part after
static analysis stops being useful and before you can actually reach the
application logic. Packers, RASP SDKs, emulator detection, TLS pinning, Flutter
apps that ignore the system trust store entirely.

The tooling here exists because I hit a wall and the existing write-ups were
wrong about why.

### Currently

- Reverse engineering Android apps — packers, RASP, Flutter/Dart AOT binaries
- Building multi-agent tooling for engagement work, with scope and phase gates
  rather than a model left to its own judgement
- Writing it down, including the approaches that **didn't** work

### Projects

| | |
|---|---|
| **[Mobile-Pentest-Setup](https://github.com/alvinhayy/Mobile-Pentest-Setup)** | Build an anti-detection rooted Android AVD in one command — KernelSU root, system-wide device identity spoofing, proxy CA into the APEX trust store |
| **RedDelta-TA416** <sub>`private`</sub> | AI red team orchestrator — 22 specialist agents over an isolated Kali execution plane, RAG-backed knowledge, persistent engagement state, and phase gates that stop for human approval before exploitation. SvelteKit control plane, Python MCP servers |
| **[URL-Status-Checker](https://github.com/alvinhayy/URL-Status-Checker)** | Bulk URL status checker for bug bounty recon |
| **[Scanning-Malware](https://github.com/alvinhayy/Scanning-Malware)** | Scan a directory against VirusTotal |
| **[MageR-Scripts](https://github.com/alvinhayy/MageR-Scripts)** | Small scripts for things I got tired of doing by hand |

### Writing

- [Building an Anti-Detection Rooted AVD (Android 16 + KernelSU)](https://blog.hayyvin.my.id/mobile-hacking-anti-detection-rooted-avd-kernelsu) — why `emulator -prop` cannot touch `ro.*`, why `skip_mount` silently voids `system.prop`, and why a CA has to be mounted into zygote
- [Bypass SSL Pinning with Frida & Objection](https://blog.hayyvin.my.id/mobile-hacking-bypass-ssl-android-ssl-pinning-with-frida-objection)
- [Install a Burp CA Certificate on Android 11](https://blog.hayyvin.my.id/mobile-hacking-install-burp-certificate)

More at **[blog.hayyvin.my.id](https://blog.hayyvin.my.id)** · HTB and CTF writeups at
**[writeup.hayyvin.my.id](https://writeup.hayyvin.my.id)**

### Working with

<p>
  <img src="https://img.shields.io/badge/Frida-e0759a?style=flat-square&logo=frida&logoColor=white">
  <img src="https://img.shields.io/badge/Ghidra-ff6b00?style=flat-square">
  <img src="https://img.shields.io/badge/radare2-1a1a1a?style=flat-square">
  <img src="https://img.shields.io/badge/Burp%20Suite-ff6633?style=flat-square&logo=burpsuite&logoColor=white">
  <img src="https://img.shields.io/badge/Android-3ddc84?style=flat-square&logo=android&logoColor=white">
  <img src="https://img.shields.io/badge/Python-3776ab?style=flat-square&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Bash-4eaa25?style=flat-square&logo=gnubash&logoColor=white">
  <img src="https://img.shields.io/badge/Docker-2496ed?style=flat-square&logo=docker&logoColor=white">
  <img src="https://img.shields.io/badge/TypeScript-3178c6?style=flat-square&logo=typescript&logoColor=white">
  <img src="https://img.shields.io/badge/Svelte-ff3e00?style=flat-square&logo=svelte&logoColor=white">
  <img src="https://img.shields.io/badge/MCP-111111?style=flat-square">
</p>

<sub>Yogyakarta, Indonesia · everything published here comes from systems I own or was authorised to test</sub>
