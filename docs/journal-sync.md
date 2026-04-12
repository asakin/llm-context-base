# Journal Sync and Privacy

`3-Journal/` is where you write reflections, daily notes, and observations that aren't ready to share. By default, the template gitignores everything in `3-Journal/` except `README.md`, so journal entries live only on the machine where you wrote them. That's the safe default: new users don't accidentally push private reflections on the first commit. It also breaks the moment you use your wiki on more than one device. You'll write an entry on your laptop and not see it on your desktop.

Three options, from simplest to most secure. Pick one and commit to it. Don't mix them (see the warning at the bottom).

---

## Option 1: Plaintext in a private repo

Remove the `3-Journal/*` rule from `.gitignore`. Journal entries commit and sync like any other file in your repo. The content travels with the repo.

**Safe only if your repo is, and stays, private forever.** Git history is forever. Once you commit a journal entry, it sits in the repo's history. If the repo ever flips to public or leaks, every journal entry in history is exposed, including ones you later "deleted" (delete commits still sit in history behind the new HEAD).

Good fit: solo users with a private GitHub repo, comfortable betting on repo visibility never changing.

**To switch:** ask your AI to "implement option 1 from `docs/journal-sync.md`". The AI has enough spec in this doc to remove the gitignore rule, stage any existing journal files that were previously ignored, and commit.

---

## Option 2: git-crypt with a passphrase-wrapped key

Use [`git-crypt`](https://github.com/AGWA/git-crypt) to transparently encrypt journal files. Locally, the files look like regular markdown; in the repo, they're encrypted binary blobs. Your AI can still read and write them at session time (after unlock), git sees only ciphertext.

The usual `git-crypt` flow uses a binary key file that must be shipped securely between devices. A lighter variant: wrap that key with a passphrase (using `age -p` or `gpg -c`) and commit the wrapped blob to the repo. New device setup becomes "clone the repo, install `git-crypt` and `age`, decrypt the wrapped key with the passphrase, run `git-crypt unlock`."

**Safer if the repo leaks**, because the journal entries in history are encrypted blobs. An attacker with the repo still needs to crack the passphrase to read anything. **Passphrase in your head is the single point of failure.** Lose it, and every encrypted entry in history becomes unrecoverable. Binary merges can be fussy if you write the same journal file from two devices on the same day, so stick to one-file-per-day naming to minimize collisions.

Good fit: users who want cross-device sync but aren't comfortable betting on repo privacy staying intact.

**To switch:** ask your AI to "implement option 2 from `docs/journal-sync.md`". The AI has enough spec in this doc to install `git-crypt` and `age` if needed, generate the git-crypt key, wrap it with your passphrase, commit the wrapped blob, set up `.gitattributes` for `3-Journal/`, and walk you through unlocking on a second device.

---

## Option 3: Journal outside the repo

Leave `3-Journal/*` gitignored. Put the real journal in a folder that's already synced by something else (iCloud, Dropbox, Syncthing, a private NAS) and symlink it into the repo's `3-Journal/` path.

**No crypto, no git history for the journal itself, the cloud provider becomes the trust anchor.** On the plus side: zero passphrase friction, no binary merges, sync conflicts handled by the sync tool instead of by git.

Good fit: users already paying for a trusted sync service who don't want the journal mixed into git at all.

**To switch:** ask your AI to "implement option 3 from `docs/journal-sync.md`". The AI has enough spec in this doc to help you pick a location, move any existing entries, set up the symlink, and verify the gitignore still catches the symlinked path so nothing leaks into git.

---

## Don't partially migrate

Each "ask your AI" instruction above is self-contained: a fresh AI session reading this doc has enough spec to execute the chosen option without further design questions. But the options don't compose well.

If you start with Option 1 (plaintext) and later decide you want Option 2 (git-crypt), the plaintext entries stay in git history forever unless you rewrite history with [`git-filter-repo`](https://github.com/newren/git-filter-repo) to strip them out before encrypting. That's a destructive operation on your repo and will break any clones. Similarly, moving from Option 1 to Option 3 leaves the plaintext in history even after you move the live files out.

Pick once, commit to it. If you're unsure, Option 3 is the least committing: it leaves the default gitignore rule alone, so switching later costs nothing in git history.
