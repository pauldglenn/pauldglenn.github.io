# Did He Go? — shared scoring

Game: https://pdglenn.com/check-swing/
Client: `content/check-swing/index.html`, copied unchanged by the Pelican build.
API: https://did-he-go-scores.paul-glenn280578.chatgpt.site
Sites project: `appgprj_6ae36278b2a08191bbbb67f46d67c0b0`

## Shared records

Ranked play is anonymous. On the first ranked replay, the browser completes a short SHA-256 proof-of-work challenge and receives a random player key. Keep browser data to retain that identity. No account, email, or ChatGPT sign-in is required. Unranked daily play and practice without shared voting remain available without registration. Existing account-issued keys continue working until they expire; previously saved results are preserved.

Daily answers are immutable per player/date/edition/round, submitted in order. The server validates the clip order and calculates scores; it never accepts a client-supplied score. The daily leaderboard page shows a six-bin score distribution (0–5) across every completed online attempt, without the old top-100 display cutoff. A UTC date picker and previous/next controls browse historical days. The page also shows the daily average and highlights your saved score when available. Local-only scores are labeled and excluded from global aggregates. The legacy ranked-list endpoint remains available for compatibility.

Practice votes with shared voting enabled also contribute to clip statistics. Only the first recorded vote per player key per clip counts across both modes. Retries and repeated practice do not inflate totals. Unranked play and imported friend codes do not enter global results. Earlier browser-only results cannot be recovered centrally.

Daily question distributions use the `answers` table filtered by challenge day and edition, in the original question order. They include saved answers from unfinished daily attempts, so each question has its own denominator. Practice, other dates/editions, and unverified legacy identities are excluded. Counts, percentages, the recorded ruling, and the share matching it are shown. Today’s unanswered questions are hidden unless the visitor explicitly reveals spoilers; answered questions and past dates are visible.

The separate Disagreement page uses lifetime first-vote-per-clip statistics across daily and practice. It shows strike/no-swing counts, percentages, sample sizes, split index, and disagreement with the recorded umpire. Split index equals `2 * min(strikes, noSwings) / total`; 100% means a 50/50 split. Small samples are labeled. Results sit behind a spoiler prompt.

## Submission controls and limits

- First-time registration requires a random, single-use, network-bound SHA-256 challenge with 18 leading zero bits, expiring after two minutes. The browser solves it before a player key is issued. This is computational friction, not proof that the player is human or a CAPTCHA.
- Player keys expire after one year. Existing account-issued sessions retain their original expiry. Credentials are hashed in the database and sent in authorization headers.
- Each vote requires a player-bound round ticket for its clip/mode/day, valid for 15 minutes, with a minimum delay before submission.
- The server enforces ordered rounds, one daily attempt per player key, immutable answers, and transactional deduplication. Scores are always computed on the server.
- Each network may request 30 browser challenges per hour, verify 60 per minute, and create 10 identities per UTC day. Writes are capped at 60 per player and 300 per network per minute. Shared networks may encounter these limits.
- Network limits use Cloudflare's `CF-Connecting-IP`, salted afresh each UTC day and hashed before storage. Raw addresses are not stored by application code. Expired limit/challenge rows and prior-day salts are cleaned on subsequent challenge requests. Missing network metadata fails closed for registration and writes.
- Choosing an answer immediately reveals the sourced ruling. One vote request runs while the player reads the result; the next daily round unlocks after confirmation. Ordinary choices do not re-fetch the daily scorecard.
- Pending daily choices survive reloads and stay locked. Failed saves offer an exact-choice retry, reconciling any response lost after a successful write. Expired tickets are renewed for that same locked choice. Only confirmed answers enter the saved daily scorecard.

Anonymous keys are not verified unique people: clearing browser data, using another device, or changing networks can create another identity. Determined bots can solve computational challenges and imitate valid gameplay. These checks discourage bulk abuse; they do not make the leaderboard cheating-proof. CORS is not authentication. Historical rulings are public and the curated catalog can repeat.

Public responses expose chosen display names and completed daily scores, plus aggregate clip counts. They do not expose player identifiers, credentials, or individual vote histories. Sharing a scorecard copies readable text and the game URL; legacy friend codes remain a separate local import feature.

## Backend operation

Source is stored in the Sites source repository associated with the project above. The backend is a dependency-free Worker with D1 binding `DB`. Its source manifest declares `"d1": "DB"`. Drizzle-generated SQL migrations are tracked under `drizzle/` and applied by Sites publication. Do not modify already-applied migrations.

Endpoints:

- `POST /challenge`: issue an expiring computational browser challenge.
- `POST /session`: verify the challenge and issue an anonymous player key.
- `POST /name`: set public display name, authenticated.
- `POST /daily/start`: create/resume today's attempt, authenticated.
- `POST /round`: issue a player-bound round ticket, authenticated.
- `POST /vote`: persist a daily or practice vote with a valid ticket, authenticated.
- `GET /daily-stats?day=YYYY-MM-DD`: public complete score histogram, completed count, average (null when empty), and five daily answer aggregates. Defaults to the current UTC day; rejects invalid/future dates. No names, player IDs, or individual histories.
- `GET /leaderboard?day=YYYY-MM-DD`: legacy public top 100 completed scores and total, retained for older clients.
- `GET /stats`: public per-clip vote aggregates.
- `GET /health`: database availability, edition, and server UTC day.

CORS permits the game origins and the API's own origin. No server secret appears in client code. The clip edition remains v1 so old share codes still work in the local imported-card board. Public read access must only be enabled with protected registration and vote endpoints deployed.

## Verification

SQLite-backed API tests cover server scoring, locked answers, retry deduplication, aggregation, practice exclusion from rankings, credential checks, valid/invalid/expired/reused/network-bound browser challenges, honeypot rejection, registration and challenge limits, ticket binding, minimum delay, expiry, and missing-network rejection. DOM tests exercise the real Web Crypto proof solver, anonymous registration, saved-key reuse, unranked isolation, five saved daily answers, global results, statistics, and failed-save retry. Delayed-response tests verify immediate reveal before any network response, a single vote request, locked choices, navigation during saving, persisted pending choices, and reload/retry recovery. Game regressions and the Pelican production build pass. Actual browser playback and performance checks remain unavailable in this environment.

Footage and ruling evidence remain in the client catalog and Field Guide. Videos stream from MLB servers; no video files are redistributed in this repository. No MLB affiliation or video license is claimed. Scores measure agreement with historical rulings, not objective correctness, and this small curated set is not a representative sample of umpire accuracy.

## Reviewed catalog

The game now has 111 reviewed MLB swings, with [11 more in the second batch](check-swing-catalog/EXPANSION-2026-10-30-B.md), including [50 additional independently audited clips](check-swing-catalog/EXPANSION-2026-10-30.md). The initial expansion reached 50 reviewed swings (44 added after six subagents screened 338 leads and visually inspected 100 source-video candidates). Every new entry passed an independent visual/ruling audit. See [the review report](check-swing-catalog/REVIEW.md) and the lead disposition CSV. Some inspected sources overlap across batches; this is not a claim of 100 unique games.

`content/check-swing/catalog.json` is the canonical catalog. Run `python scripts/sync-check-swing-catalog.py --backend /path/to/did-he-go-api` to validate and embed it into the frontend and score API together. Add `--check` for a non-mutating consistency check. New entries carry `availableFrom`; their daily inclusion starts on their recorded activation date (October 30 for the initial expansion; October 31 for the next 50) while practice can use them immediately. Historical questions and v1 share cards remain unchanged. Never reorder, remove, or relabel entries already used by a historical daily set.

Short reviewed windows respect the existing server timing gate before the save request. The ruling still appears immediately on selection. Catalog tests compare client/API selections over 730 dates, preserve earlier daily sets, and exercise new practice votes.

Daily-distribution validation covers over 100 completed attempts, all six score bins, both supported identity types, incomplete daily answers, date/edition isolation, practice exclusion, empty and invalid dates, personal-score labels, spoiler controls, date navigation, failed-request recovery, and stale-response handling. No schema migration or changes to stored scores are required.
