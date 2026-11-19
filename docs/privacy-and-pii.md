# Privacy and PII in agents

An agent puts personal data in more places than a chatbot does. Data goes into the **prompt** (sent to a model provider), the **tools** (sent to third parties), **memory** (stored indefinitely), **logs** and the **reply**.

## Where data leaks

| Path | Example | Checkpoint |
|---|---|---|
| Prompt to the provider | A user pastes a CV, a medical letter or a config file with keys | 1 |
| Tool result to the model | An order lookup returns card and phone numbers the task didn't need | 2b |
| Model to a tool | The agent emails a customer record to an outside address | 2a |
| Reply to the user | Another customer's data, or data the user shouldn't see | 3 |
| Memory and logs | Secrets stored in long-term memory or traces | all |

## Mask, vault, restore

[Lab 03](../labs/03-privacy-protection) implements the pattern most teams end up with:

1. **Mask** before the model, replacing each value with a typed placeholder (`[EMAIL_1]`, `[CARD_1]`).
2. **Vault**: keep the placeholder table on your side, scoped to one conversation.
3. **Restore** only where the real value is needed: in the tool call, at the last moment and on your infrastructure, or in the reply to an authorised user.
4. **Check policy against the real value.** For example, is this email address inside the company?

## Detection approaches

| Approach | Good at | Misses |
|---|---|---|
| Regex and checksums (Luhn, IBAN) | Cards, IBANs, emails, keys | Names, addresses, free text |
| NER models ([Presidio](https://github.com/data-privacy-stack/presidio) + spaCy or transformers) | Names, locations, organisations | Context ("my neighbour"), domain-specific IDs |
| LLM or specialised classifiers | Context, many languages, health and financial data | Cost and latency, so run them on CPU or at the edge where possible |
| Secret scanners ([gitleaks](https://github.com/gitleaks/gitleaks), [TruffleHog](https://github.com/trufflesecurity/trufflehog)) | Provider keys with known formats; can verify whether a key is live | Generic passwords |

Tools and services are in [guardrails.md](../resources/guardrails.md#pii-and-secrets-detection), and evaluation sets in [datasets.md](../resources/datasets.md#pii-and-privacy).

## Regulation hooks

- **GDPR**: data minimisation (Art. 5(1)(c)), processors and transfers (Art. 28, Chapter V).
- **EU AI Act**: data governance for high-risk systems (Art. 10).
- **PCI DSS**: card data should never reach a general-purpose model.
- **HIPAA**: protected health information needs a BAA with every processor in the chain, including the model provider.
