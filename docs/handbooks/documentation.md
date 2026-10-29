# How the documentation is organised

RepGarden is one product with three apps and a backend, so its documentation sits at two levels. This handbook says which level owns what, so a fact is written once and found where it is expected.

## Two levels

**`repgarden/docs/`** holds what is true of the product regardless of which app you are in: the brief, the MVP scope, the roadmap, the one progress file, cross-cutting epics, the architecture (data model, roles and access, the video pipeline, notifications, environments), the brand, legal and compliance, research, and these handbooks.

**`apps/<app>/docs/`** holds what is true of one app only: its screens and navigation, how to build, run and test it, its releases and its issues. Each app uses the same folder names — `epics/`, `architecture/`, `handbooks/`, `releases/`, `issues/`, `archive/` — created on first use, not in advance. An app document links up to the product document it depends on; it never restates it.

## Rules

1. **One home per fact, decided by level.** Before writing a decision or a status, find where it already lives and edit that place. Product-level facts go up; implementation facts go down.
2. **Epics live where the work lives.** Work inside one app is an epic in that app. Work that spans apps is a root epic that links to a small epic in each app it touches. Root epics are the ones the build series tells.
3. **Names carry the date.** Epics, research sets and archived notes are named `YYYY-MM-DD-NN-name.md`: the date they were opened, a number that restarts per folder, then the name. Dated files are written once; a later decision that changes one gets a dated status line at the top, not a rewrite.
4. **One `progress.md`, at the root**, with a line per app and a link to its epics. `releases/` is per app, because each app ships on its own cadence.
5. **Instructions live in the root `AGENTS.md`.** Each app has a short `AGENTS.md` of its own — what the app is, its stack, how to run and test it — that opens by pointing to the root file. Rules are never copied down. `CLAUDE.md` at each level is one line, `@AGENTS.md`, and is never edited.
6. **Research is product research**: Benji's calls, the Fitr study, the market and the store rules. It is dated and written once. Business research about GadirLabs stays in the console.
7. **Write current state, not a diary.** Replace the old sentence; git keeps the history. Keep planned, built, checked, released and approved apart, and record a decision when it is made, not when an agent suggests it.
