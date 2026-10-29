# Did He Go? — shared scoring update

Game: https://pdglenn.com/check-swing/
Client: `content/check-swing/index.html`, copied unchanged by the existing Pelican build.
API: https://did-he-go-scores.paul-glenn280578.chatgpt.site
Sites project: `appgprj_6ae36278b2a08191bbbb67f46d67c0b0`

## Deployment status

The backend has been deployed privately and its D1 tables verified. The frontend changes are prepared for launch. Public API access requires the owner's approval, requested separately; do not publish this frontend until that access is approved and public health/CORS checks pass.

## Shared records

- A server-created, random player key is stored in each browser. The database stores a hash of that credential and a generated public display name. Players can explicitly save another display name.
- Daily answers are immutable per player/date/edition/round, submitted in order. The server validates the daily clip order and calculates scores. Only completed online attempts enter the global daily leaderboard. Ties share a rank.
- Practice votes also contribute to clip statistics. Only the first recorded vote per player key per clip counts, across both modes. Retry requests and repeated practice do not inflate totals.
- Statistics show strike/no-swing counts, percentages, sample sizes, split index, and disagreement with the recorded umpire. Split index equals `2 * min(strikes, noSwings) / total`; 100% means a 50/50 split. Small samples are labeled. Results are behind a spoiler prompt.
- Existing local attempts remain local. The service cannot recover votes from earlier visitors, and imported friend codes never enter global scores or aggregate votes.
- Saving new online calls requires the API. Failed saves leave the choices available for retry. Local progress and streaks remain in the browser.

## Privacy and limits

The public API exposes display names and completed daily scores, plus aggregate clip counts; it does not expose player IDs, credential hashes, or individual vote histories. Player keys are sent as authorization headers. Browser keys are anonymous device identities, not verified accounts; clearing storage or switching devices can create another player. These are casual rankings, not cheating-resistant competition. When a trusted connection IP is available, registration is limited to 10 new keys per day. Only a daily hash is retained for that limiter, with expiry cleanup.

The game uses six historical MLB broadcast side replays. Dates repeat across days; prior familiarity can affect scores. This is not a representative sample of umpire accuracy. Scores measure agreement with historical rulings, not objective correctness.

## Backend operation

The backend source is stored in the Sites source repository associated with the project above. It is a dependency-free Worker with a D1 binding named `DB`. Its source manifest declares `"d1": "DB"`. Drizzle-generated SQL migrations are tracked under `drizzle/` and applied by Sites publication. Do not modify already-applied migrations.

Endpoints:
- `POST /session`: issue a guest credential.
- `POST /name`: set public display name, authenticated.
- `POST /daily/start`: create/resume today's attempt, authenticated.
- `POST /vote`: persist daily or practice vote, authenticated.
- `GET /leaderboard?day=YYYY-MM-DD`: top 100 completed scores plus total.
- `GET /stats`: per-clip vote aggregates.
- `GET /health`: database availability, edition, and server UTC day.

CORS permits the game origins and the API's own origin. Secrets do not appear in client code. The clip edition remains v1 so old share codes still work in the local imported-card board.

## Verification

SQLite-backed API tests cover server scoring, immutable answers, retry deduplication, vote aggregation across two players, practice exclusion from rankings, authentication, input validation, origin checks, and registration limits. DOM integration tests cover five saved daily answers, global results, statistics rendering, failed-save retry, and legacy score isolation. Existing game regressions and the full Pelican build pass. Visual/browser playback testing remains unavailable in this authoring environment.

Original footage and ruling evidence remain in the client catalog and Field Guide. Videos stream from MLB servers; no video files are redistributed in this repository. No MLB affiliation or video license is claimed.
