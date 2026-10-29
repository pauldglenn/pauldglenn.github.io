# Expanding the check-swing library

Discovery snapshot: 2026-10-29. The discovery queue has now been reviewed by six subagents. See [REVIEW.md](REVIEW.md) for 44 independently accepted additions, expanding the game to 50 clips. Raw candidate lists remain unapproved leads; only the canonical game catalog contains published entries.

## What the first search found

- 59 distinct MLB video search results across six queries. Results include false positives, commentary, injuries, and check-swing hits; none is automatically approved.
- 684 Close Call Sports articles mentioning check swings across its public archive.
- 279 higher-priority reports mention a check swing within their first 500 characters. This is a prioritization heuristic, not verified event classification.
- 263 of those higher-priority reports include a video or game link after removing commonly repeated links. Some reports cover the same game/event; link availability and side angles remain unchecked.

Sources: [MLB video search](https://www.mlb.com/search?q=check%20swing&filter=video), [Close Call Sports search](https://www.closecallsports.com/search?q=%22check+swing%22). The MLB results report non-exhaustive hit counts. These counts are not a census of all check swings and should not be added together as unique pitches.

## The route to a substantially larger library

1. Use ruling reports to identify the game, inning, batter, appeal umpire, and final swing/no-swing ruling. Keep the actual on-field ruling separate from the author's judgment of correctness. Deduplicate by game and pitch when possible.
2. Match the play to MLB game data and its play ID. Search the game's MLB highlights and publicly available source clips, including clips titled as ejections or strikeouts rather than "check swing."
3. Review the video for a first- or third-base-side replay. Mark the exact start/end window before any umpire signal, captions, commentary, or reaction gives away the answer. Reject irrelevant angles and clips where the swing itself is obscured.
4. Record video source, ruling evidence, batter handedness, base side, game/pitch IDs, and review status in one catalog. Only reviewed entries should be promoted to the game's client and scoring API together.
5. Grow the reviewed set to 100–200 first. To pursue thousands, obtain broader footage access and an appropriate reuse arrangement, then screen full-game/replay archives. A detector could rank likely check swings for review; it should not invent the recorded umpire call. Include ordinary uncontested checks to reduce the controversy bias of ejection reports.

## Why pitch data alone is insufficient

The 2021-10-14 Flores game is gamePk `660920`; its final pitch is playId `051d79eb-49a2-41e8-94f5-c395d6e823fb`.

[MLB's game feed](https://statsapi.mlb.com/api/v1.1/game/660920/feed/live) records this pitch as `S` / `Swinging Strike` and the plate appearance as "Wilmer Flores strikes out swinging." The sampled event does not contain a check-swing flag. Selecting all swinging strikes would include ordinary full swings.

[Baseball Savant's play page](https://baseballsavant.mlb.com/sporty-videos?playId=051d79eb-49a2-41e8-94f5-c395d6e823fb) resolves this play ID to a pitch video source. The direct video returned HTTP 403 in this environment, so that path has not been established as a working source for the game. A play ID also does not establish that a suitable base-side replay exists.

## Reproduce discovery

Run from the repository root:

```sh
python scripts/discover-check-swings.py --output docs/check-swing-catalog
```

Requires Python 3 and curl. The script fetches only public metadata, limits search concurrency to three requests, deduplicates URLs, retains source links, flags candidates for review, and reports fetch failures. It does not download video, infer official calls, add game clips, change the daily selection, or bypass access controls. The CSV is a compact snapshot for review; the JSON files retain discovery details.

The next content milestone is reviewed footage, not a larger unverified candidate count. Current daily results must remain reproducible when new clips are introduced.
