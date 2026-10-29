# Did He Go? — check-swing MVP

Published at https://pdglenn.com/check-swing/ through the existing GitHub Pages workflow.

Source: `content/check-swing/index.html`. A dependency-free, buildless, responsive web game. Pelican copies it unchanged because `check-swing` is included in `STATIC_PATHS`. The personal site's homepage and theme are unchanged.

## Included

- Five date-seeded MLB calls per UTC day, one locally saved attempt, resumable progress, scorecard and completion streak.
- Six curated historical calls: Flores (2021-10-14), Ruf (2021-07-22), Hernández (2024-06-18), González (2016-06-29), Carpenter (2022-10-20), Harper (2023-09-28).
- Three first-base-side and three third-base-side broadcast replays; no synthetic footage. These approximate the umpire's perspective rather than documenting exact umpire eye position.
- Muted swing windows, playback boundary, replay, half speed, and voting unlocked after viewing. Original footage and ruling evidence links appear after a vote.
- Unlimited practice through the six-call library, baseline filtering, shuffle and skip.
- Daily leaderboard stored on device; manually import friends' scorecards. Imported scores are self-reported. Ties share rank. No invented users or global-ranking claims.
- Field guide referencing MLB rules, FanGraphs' 2026 minor-league experiments, MLB's Hawk-Eye pilot, and MapTap inspiration.

## Run and publish

Open `content/check-swing/index.html` using a static HTTP server. No package install is required for the app. Normal site publication remains:

```sh
PYTHONPATH=. pelican content -s publishconf.py
```

Pushes to main use the repository's existing build/deploy workflow.

## Content maintenance

The inline `CLIPS` array contains each official source URL, verified ruling source, game date, batter, umpire, baseline, decision, and playback start/end in seconds. View every candidate clip and verify its ruling before inclusion. Select a side angle without the umpire signal, mute audio, and leave a margin before reactions. A strike in this game is a swing ruling; not every example is strike three. González's example is strike two.

The `VERSION` constant identifies the daily selection and scorecard edition. Change it if the catalog or historical labels change, and use a new storage key if stored daily results no longer map to the same selections. Never silently reinterpret already shared scorecards.

## Verification and limits

Validated JavaScript syntax, daily selection over 365 dates, daily and practice scoring, result persistence, streaks, scorecard round trips, malformed imports, HTML escaping, voting gate, and replay-boundary logic in a DOM harness. The full Pelican production build passed and the output app matched source byte for byte. All six video sources returned video/mp4 responses. Automated visual/browser playback QA was unavailable in the authoring session.

This is an MVP with six clips, so daily selections repeat. It is not a representative sample of umpire accuracy. Browser storage is editable and can be cleared. Shared cards encode the player's answers, are not cryptographically signed, and do not prove honest play. A production global leaderboard needs a server, authentication, server-side daily scoring, abuse controls and a privacy policy.

Videos stream from MLB/broadcaster sources and may change or become unavailable. No video license or MLB affiliation is claimed. Broad public promotion needs a reliable licensed clip supply. The app does not download or redistribute video files in this repository.

The 45-degree standard described in the guide is from experimental minor-league tracking systems, not a rule used to relabel these historical MLB calls. Scores measure agreement with the recorded umpire, not objective swing truth.
