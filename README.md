# RepGarden

Reference implementation for [Build My First App](https://gadirlabs.io/learn/build-my-first-app).

RepGarden is a trainer web app and an iOS/Android client app with workouts, bookings, payments, an AI content pipeline and vegetable mascots.

**Status: project preparation.** This repository currently contains the brief, agent instructions and the first three epics. There is no running application or deployment yet. Technology and branding decisions will be recorded as the course develops.

Learners should begin with [repgarden-starter](https://github.com/AhmedAGadir/repgarden-starter). This repository will hold our implementation, chosen brand assets and tagged checkpoints as they become available.

Read `CLAUDE.md`, `docs/project-brief.md` and `docs/progress.md` before working. Do only the requested epic. Never commit credentials, private design links or real client records.

## Maintaining the learner starter

`course/starter/` holds the teaching templates; `docs/` holds our reference-project execution records. They intentionally have different progress. Edit the templates here, not the generated starter repository. Keep numbered epic paths stable.

Preview drift: `python3 scripts/export-starter.py --target ../repgarden-starter --check`

Export reviewed changes: `python3 scripts/export-starter.py --target ../repgarden-starter --write`

The explicit manifest selects public learner files only. Writing requires the expected starter Git origin, its repository root and a clean working tree. Export does not commit, push, tag, delete extra files or overwrite unknown existing files. Review the resulting diff, commit both repos, tag a new starter version and update the course download link. Existing tags and learner copies stay unchanged.
