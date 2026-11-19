# Contributing

Thanks for helping make agents safer. This list stays useful only if it stays **neutral, accurate and current**.

## Add a resource

1. Put it in the right file under [`resources/`](resources), in the right section, in **alphabetical order**.
2. Use the format of that file. For tools:
   `- [Name](url) — one factual line on what it does. \`OSS\` \`License\`` (or `\`Commercial\``, `\`Free tier\``).
3. Link to the **primary source**: the repo, paper or official page, not a blog about it.
4. No marketing language ("best", "leading", "revolutionary"), and no star counts.
5. **Vendors are welcome**, including competitors of the maintainer. List your own product once per relevant section, and say in the PR that you are affiliated.
6. Mark unmaintained projects `Archived`.

## Add a lab scenario

The most valuable PR is **an attack that gets past the current guards**. Add it to the lab's corpus or scenarios, mark it `known_gap` if the local rules miss it, and include the expected outcome.

## Add a guard backend

Write a class in [`guards/`](guards) with one method:

```python
class MyGuard(Guard):
    name = "myguard"
    def check(self, text: str, checkpoint: str = "input") -> Decision:
        # checkpoint: input | tool_call | tool_result | output
        return Decision("ALLOW" | "MASK" | "REVIEW" | "BLOCK", text_or_None, reasons)
```

Register it in `get_guard()`, keep optional dependencies out of the default install, and post your lab results (`labs/01` metrics, `labs/05` attack-success rate) in the PR. Fail closed on errors.

## Before you open a PR

```bash
python3 run_tests.py
```

Links are checked in CI. If a link is dead, remove the entry or point it to the new location.

## Code of conduct

By taking part you agree to the [Code of Conduct](CODE_OF_CONDUCT.md). Report security issues in this repo's code as described in [SECURITY.md](SECURITY.md).
