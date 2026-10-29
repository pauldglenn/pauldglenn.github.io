# Did He Go? — shared scoring

Game: https://pdglenn.com/check-swing/
Client: `content/check-swing/index.html`, copied unchanged by the Pelican build.
API: https://did-he-go-scores.paul-glenn280578.chatgpt.site
Sites project: `appgprj_6ae36278b2a08191bbbb67f46d67c0b0`

## Shared records

Ranked play requires connecting a ChatGPT account through the score service. The service uses the platform's authenticated identity header, hashes the account identifier, and issues an expiring game session. It does not store email addresses. Reconnecting on another device resumes the same account and daily attempt. Practice and unranked daily play remain available without sign-in.

Daily answers are immutable per account/date/edition/round, submitted in order. The server validates the clip order and calculates scores; it never accepts a client-supplied score. Only completed ranked attempts enter the public daily leaderboard. Ties share a rank.

Signed-in practice votes also contribute to clip statistics. Only the first recorded vote per account per clip counts across both modes. Retries and repeated practice do not inflate totals. Anonymous play and imported friend codes do not enter global results. Earlier browser-only results cannot be recovered centrally.

Statistics show strike/no-swing counts, percentages, sample sizes, split index, and disagreement with the recorded umpire. Split index equals `2 * min(strikes, noSwings) / total`; 100% means a 50/50 split. Small samples are labeled. Results sit behind a spoiler prompt.

## Submission controls and limits

- Platform-authenticated accounts are required to issue sessions; anonymous session requests fail. Sessions expire after 30 days.
- Each vote needs an account-bound ticket for its clip/mode/day, valid for 15 minutes, with a minimum delay before submission.
- The server enforces one daily attempt per account, ordered rounds, locked answers, and transactional writes with unique keys.
- Writes are limited to 60 per account per minute; account connections to 10 per hour.
- The browser requests tickets when starting replays. Expired tickets require replaying the clip. Failed saves remain retryable.

These controls prevent unauthenticated score stuffing and arbitrary submitted totals. They cannot prove that a human watched the replay, stop a signed-in player automating valid requests, or prevent multiple accounts. CORS is a browser restriction, not authentication. Historical rulings are public, and the six-clip catalog repeats: this is a casual game, not a cheating-proof competition.

Public responses expose chosen display names and completed daily scores, plus aggregate clip counts. They do not expose account identifiers, credentials, or individual vote histories. Session credentials stay in the browser and are sent in authorization headers. Sharing a scorecard copies readable text and the game URL; legacy friend codes remain a separate local import feature.

## Backend operation

Source is stored in the Sites source repository associated with the project above. The backend is a dependency-free Worker with D1 binding `DB`. Its source manifest declares `"d1": "DB"`. Drizzle-generated SQL migrations are tracked under `drizzle/` and applied by Sites publication. Do not modify already-applied migrations.

Endpoints:

- `GET /connect`: platform sign-in and connection to the game via origin-checked popup messaging.
- `POST /session`: issue a game session for a platform-authenticated account, from the service's own origin.
- `POST /name`: set public display name, authenticated.
- `POST /daily/start`: create/resume today's attempt, authenticated.
- `POST /round`: issue an account-bound round ticket, authenticated.
- `POST /vote`: persist a daily or practice vote with a valid ticket, authenticated.
- `GET /leaderboard?day=YYYY-MM-DD`: public top 100 completed scores and total.
- `GET /stats`: public per-clip vote aggregates.
- `GET /health`: database availability, edition, and server UTC day.

CORS permits the game origins and the API's own origin. No server secret appears in client code. The clip edition remains v1 so old share codes still work in the local imported-card board. Public read access must only be enabled after deploying the account-protected API.

## Verification

SQLite-backed API tests cover server scoring, immutable answers, retry deduplication, aggregation across accounts, practice exclusion from rankings, anonymous-write rejection, input/origin checks, account reconnection, rate limits, ticket binding, minimum delay, and expiry. DOM integration tests cover five saved daily answers, global results, statistics rendering, failed-save retry, and legacy score isolation. Game regressions and the full Pelican build pass. Actual browser sign-in and visual playback testing remain unavailable in this authoring environment.

Footage and ruling evidence remain in the client catalog and Field Guide. Videos stream from MLB servers; no video files are redistributed in this repository. No MLB affiliation or video license is claimed. Scores measure agreement with historical rulings, not objective correctness, and this small curated set is not a representative sample of umpire accuracy.
