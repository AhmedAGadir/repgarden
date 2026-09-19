# Epic 02 — Save your work with Git

Outcome: an inspected local checkpoint and a matching copy in the learner's own private GitHub repository.

## Phase 1 — Prepare

- [ ] Read project instructions and progress. Confirm the project folder; inspect existing Git history and remotes before changing anything. Never reinitialise or replace an existing remote blindly.
- [ ] Check Git is available. If absent, guide the learner using https://git-scm.com/install/ for their OS. Explain any installation permission requests.
- [ ] Explain repository (tracked project), commit (local checkpoint) and push (sending commits to a remote).
- [ ] Ask for commit author name/email if needed; configure them for this project only. Explain that commits contain this identity and offer GitHub's noreply address option. Never invent an identity.
- [ ] Initialise a local repository if needed. Inspect files and .gitignore. Exclude secrets, real client records and private design links. A .gitignore rule does not untrack previously committed files.

Stop and show the learner the proposed file list and a short change summary. Wait for approval before committing or sending files.

## Phase 2 — Save locally

- [ ] After the learner approves the reviewed files, create a commit named Prepare RepGarden workspace. If existing work already has a suitable checkpoint, explain and reuse it rather than fabricate changes.
- [ ] Verify the commit and report remaining uncommitted changes. Explain that future work is not saved to Git automatically.

## Phase 3 — Save on GitHub

- [ ] Guide account creation/sign-in using GitHub's own interface. Do not request passwords or access tokens in chat. Consult https://docs.github.com/en/get-started/start-your-journey/about-github-and-git as needed.
- [ ] Ask the learner to create or approve creation of their own private repgarden repository. Confirm account, repository name and private visibility. Do not push to the course author's repositories or replace existing history. If creating manually, use an empty repo without an initial README, license or gitignore.
- [ ] Connect the intended remote and push only reviewed commits after learner approval. No force push. Verify the remote commit matches the local commit and return the repository URL.
- [ ] Learner opens GitHub, checks private visibility, project files and commit message. Do not claim this human check until confirmed.

## Completion and stop

After confirmation, update this epic and docs/progress.md with evidence and any blockers. Ask to include these record changes in a final commit and push, then verify a clean working tree and matching remote. Stop with docs/epics/03-figma.md next. Never claim setup, recovery or sync was tested when it was not. Explain how to request another checkpoint after future reviewed work; do not perform a destructive rollback demonstration.
