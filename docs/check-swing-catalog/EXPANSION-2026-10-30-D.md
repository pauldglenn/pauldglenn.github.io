# Fourth expansion batch: 2026-10-30

Adds eight independently reviewed check swings: Devers, Profar, Moniak, O’Neill, Rave, Story, Simpson, and Báez. The library now contains 143 clips. Practice access is immediate; daily eligibility starts October 31 UTC. The first 135 records are preserved exactly.

## Finding footage beyond check-swing titles

MLB Network compilations supplied distinct checks and alternate angles. Event-first review of whole-game highlights recovered an O’Neill replay omitted by the ejection edit. A Moniak HBP review contained the full side replay. Sportsnet’s public clip archive supplied a separately reviewed Rave replay. A later alternate MLB condensed-game edit matched the same pitch; it is one canonical clip. Public caption mining located Story, Simpson and Báez inside videos whose descriptions did not name the checks. Every pitch passed independent full-motion, angle, date, ruling, umpire, and duplicate checks; the provenance JSON preserves exact evidence and corrections.

## Stable broadcaster playback

Sportsnet uses public Brightcove playback metadata and expiring signed media URLs. The catalog retains a stable game API /media/clip-id URL. The API resolves the approved public video, pins the reviewed rendition by source path, dimensions, codec and duration, and redirects to a fresh signed URL. It caches links briefly and rejects changed, missing, or stale sources. Only registered catalog clips and the approved account/player/CDN are supported; requests cannot resolve arbitrary URLs. Playback resolution does not use the score database or create votes.

Media remains streamed from its publisher. Public client player configuration supplies its playback policy; no private publisher credentials or player accounts are required. No video binaries are redistributed in this repository. Provider-specific metadata is omitted from public score/statistics responses.

The 500-clip goal remains active. Further discovery now includes timestamped public captions, analytical articles, and MLB’s HBP replay index. These are review leads, never counted as playable clips until approved.
