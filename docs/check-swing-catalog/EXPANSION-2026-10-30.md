# Catalog expansion: 2026-10-30

Added 50 independently reviewed MLB check swings, bringing the library to 100. Practice can use these immediately; daily eligibility starts October 31 UTC. The existing 50 entries retain their order and values, preserving previous daily challenges and saved scores.

## Discovery and verification

Public MLB search supplied 2,791 metadata leads. Historical Close Call Sports reports supplied additional named incidents and ruling evidence. The legacy MLB metadata endpoint `https://content.mlb.com/mlb/item/id/v1/{videoId}/details/web-v1.json` recovered playback links for footage whose newer landing pages were unavailable. The reusable `scripts/resolve-legacy-mlb-videos.py` resolves metadata only; its output still requires human or agent review.

Each published addition received a primary footage review and an independent second review of the playback window, full checking motion, usable side angle, actual pitch ruling, game date, and duplicate identity. Rulings were checked against official MLB pitch feeds and/or contemporary incident reports. See `expansion-2026-10-30.json` for per-clip evidence and audit decisions. Local contact-sheet paths in that record refer to research artifacts, not web assets.

The second review removed a duplicate Puig clip and held a Dietrich clip whose angle did not meet the game requirements. An Escobar candidate was withdrawn because its footage did not show the check. Corrections extended Cabrera’s window to include the full motion, verified Canó’s deciding umpire as Adam Hamari, and removed an unsupported attribution of Sánchez’s deciding call to the ejecting umpire. Unknown deciding umpires are explicitly identified as unknown.

Playback renditions can contain different edits, so the reviewed URL and timestamps are preserved together. No videos are copied into this repository; playback streams from public MLB servers. These clips are a curated sample, often involving disputed calls, and do not measure representative umpire accuracy.

## Remaining target

The target is 500; this release reaches 100. Keyword metadata does not reliably identify check swings or appeals, and many incident videos omit a complete usable side view. More metadata leads alone do not establish 400 additional playable, verified clips. A broader footage index linking pitch/play IDs to appeal flags, deciding umpires, rulings, camera views, and video timecodes would make further expansion substantially more reliable.
