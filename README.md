# Cold Outreach Pipeline for B2B SaaS — Research Project

## About This Project
This repository is a research project built as part of the 100Hires portfolio process.
The topic I chose: **Cold Outreach Pipeline for B2B SaaS**.

The goal is to collect, organize, and synthesize content from real practitioners — 
people who actively run cold outreach campaigns — to eventually build a working playbook.

---

## Tools Installed
- Cursor IDE
- Claude Code extension (installed via PowerShell CLI — not available in Cursor marketplace)
- Codex (OpenAI) extension (installed via OpenAI website)
- youtube-transcript-api (Python package, for YouTube transcript collection)

## Steps Completed
- Installed Cursor IDE from cursor.com
- Installed Claude Code via PowerShell after it wasn't found in the marketplace
- Installed Codex via OpenAI website which opened Cursor's extension bar
- Initialized Git and created this public GitHub repository entirely through Cursor terminal
- Identified and researched 10 practitioner experts in cold outreach for B2B SaaS
- Collected 2 YouTube transcripts from expert videos on cold email tactics
- Collected 1 LinkedIn post per expert across all 10 experts, with summaries and key takeaways
- Committed and pushed incrementally throughout the process (not as one final commit)

## Issues & Solutions
- Claude Code not found in Cursor marketplace → installed via PowerShell CLI instead
- After laptop restart, both extensions needed reinstalling → used official websites
- Git commit error ("author identity unknown") → fixed with `git config --global user.email/user.name`
- `mkdir -p` syntax failed in PowerShell (bash-only flag) → used PowerShell-native comma-separated syntax
- `youtube-transcript-api`'s `get_transcript()` method didn't exist in the installed version (1.2.4 changed 
  to an instance-based `.fetch()` method) → rewrote the script to match the new API
- YouTube blocked automated transcript requests from my IP (common anti-bot protection, not just a cloud-IP 
  issue) → switched to a free transcript-extraction website and manually saved the text instead
- Several experts initially chosen were swapped out for stronger or more specific practitioner voices as 
  research progressed (e.g., Justin Michael → Adam Robinson, Kyle Coleman → Jake Weber, 
  Trish Bertuzzi → Mohamed Elidrysy)

---

## Research Structure
## The 10 Experts
1. Alex Berman
2. Josh Braun
3. Jason Bay
4. Morgan J Ingram
5. Adam Robinson
6. Will Allred
7. Jake Weber
8. Belal Batrawy
9. Mohamed Elidrysy
10. Jed Mahrle

See `/research/sources.md` for the full annotated list with links and selection reasoning.

## Why These Experts?
I prioritized practitioners who actively run cold outreach campaigns and share specific, 
data-backed tactics rather than general theory. The list mixes well-known names (Alex Berman, 
Josh Braun) with sharper, more specific voices found through closer research, since the goal 
was finding genuinely strong signal, not just the first search results.

## What I Learned (So Far)
Across the collected content, a few repeated themes emerged:
- Targeting and deliverability matter more than clever copywriting (Alex Berman)
- Framing information as a question rather than a statement increases buyer engagement (Josh Braun)
- The first line of an email has two jobs: drive the open and build urgency (Jason Bay)
- AI is commoditizing research, so human consistency and authenticity are becoming the real 
  differentiator (Morgan J Ingram)
- Reply rates depend on minimizing reading friction and signaling genuine effort (Will Allred)
- Multi-email sequences work better as a connected narrative than as repetitive follow-ups (Belal Batrawy)
- LinkedIn content and cold outreach perform best as one integrated system, not separate channels 
  (Mohamed Elidrysy)
- Specific diagnostic questions outperform generic pain-point questions as cold openers (Jed Mahrle)

---

*This research will support a future cold outreach playbook for B2B SaaS.*