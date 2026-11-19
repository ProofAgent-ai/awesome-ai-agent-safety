# Lab 03 · Privacy protection: mask, keep the vault, restore

**You will learn:** how to stop personal data and secrets reaching a hosted model while keeping the conversation usable, by masking locally on CPU, keeping the placeholder table on your side and restoring real values only where they are needed.

| | |
|---|---|
| Time | 10 minutes |
| Needs | Python 3.9+, nothing to install, no GPU |
| OWASP | LLM02 Sensitive information disclosure |
| Regulation | GDPR data minimisation (Art. 5(1)(c)), PCI DSS for card data |

## Run it

```bash
python3 labs/03-privacy-protection/run.py
python3 labs/03-privacy-protection/run.py --guard proofagent   # 100+ PII types, several languages
python3 -m unittest labs/03-privacy-protection/test_lab.py
```

## The pattern

```
"My card 4111 1111 1111 1111, email jane.doe@example.com"
      │  mask locally (Vault keeps [CARD_1] → 4111…, [EMAIL_1] → jane…)
      ▼
"My card [CARD_1], email [EMAIL_1]"      ← all the model ever sees
      │  model answers with placeholders
      ▼
restore on your side → the user, or the tool that runs locally, gets the real values
```

- The **same value gets the same placeholder**, so the model can still reason ("email [EMAIL_1] the receipt").
- **Card numbers are checked with Luhn**, so ticket numbers are not masked by mistake.
- **Secrets** (AWS, GitHub, OpenAI, Anthropic, Slack and Stripe keys, private keys, JWTs, `password=`) are masked the same way.
- Lab 04 shows the other half: tool arguments are restored just before the tool runs, and policy rules check the **real** destination.

## Expected outcome

The tests check that none of seven sensitive values reaches the model, that the user gets them back, and that clean text is left unchanged.

## Limits of the local rules

Regexes find **structured** data well: emails, cards, IBANs and keys. They do not find names, addresses, health data or anything written in free text ("my neighbour Jane"). For that, use an NER or model-based detector such as Presidio, a ProofAgent guard, or the cloud DLP services in [`resources/guardrails.md`](../../resources/guardrails.md#pii-and-secrets-detection).
