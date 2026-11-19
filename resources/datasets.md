# Datasets

Public datasets for training and evaluating prompt-injection, jailbreak, harmful-content and PII detectors.

Licenses come from each Hugging Face dataset card's metadata. "Not stated" means the card declares none; "Custom" means the card says `other` (read its terms). "Gated" means you must accept terms on Hugging Face to download.

## Contents

- [Prompt injection](#prompt-injection)
- [Jailbreaks and harmful behavior](#jailbreaks-and-harmful-behavior)
- [PII and privacy](#pii-and-privacy)

## Prompt injection

| Dataset | Description | Link | License |
|---|---|---|---|
| deepset/prompt-injections | Small labeled injection vs. benign prompts (EN/DE) | [HF](https://huggingface.co/datasets/deepset/prompt-injections) | Apache-2.0 |
| Lakera/gandalf_ignore_instructions | "Ignore instructions" attacks from the Gandalf game | [HF](https://huggingface.co/datasets/Lakera/gandalf_ignore_instructions) | MIT |
| Lakera/mosscap_prompt_injection | Prompts from the Mosscap game (DEF CON 31) | [HF](https://huggingface.co/datasets/Lakera/mosscap_prompt_injection) | MIT |
| hackaprompt/hackaprompt-dataset | Submissions from the HackAPrompt competition | [HF](https://huggingface.co/datasets/hackaprompt/hackaprompt-dataset) | MIT (gated) |
| microsoft/llmail-inject-challenge | Adaptive email-agent injection attacks from the LLMail-Inject challenge | [HF](https://huggingface.co/datasets/microsoft/llmail-inject-challenge) | MIT |
| reshabhs/SPML_Chatbot_Prompt_Injection | System-prompt + user-prompt pairs labeled for injection | [HF](https://huggingface.co/datasets/reshabhs/SPML_Chatbot_Prompt_Injection) | MIT |
| xTRam1/safe-guard-prompt-injection | Synthetic injection classification set | [HF](https://huggingface.co/datasets/xTRam1/safe-guard-prompt-injection) | Not stated |
| yanismiraoui/prompt_injections | Multilingual prompt injections | [HF](https://huggingface.co/datasets/yanismiraoui/prompt_injections) | Apache-2.0 |
| Tensor Trust | Human attacks and defenses from the online game | [GitHub](https://github.com/HumanCompatibleAI/tensor-trust) | BSD-2-Clause (repo) |

## Jailbreaks and harmful behavior

| Dataset | Description | Link | License |
|---|---|---|---|
| jackhhao/jailbreak-classification | Jailbreak vs. benign prompt classification | [HF](https://huggingface.co/datasets/jackhhao/jailbreak-classification) | Apache-2.0 |
| TrustAIRLab/in-the-wild-jailbreak-prompts | In-the-wild jailbreak prompts ("Do Anything Now" study) | [HF](https://huggingface.co/datasets/TrustAIRLab/in-the-wild-jailbreak-prompts) | MIT |
| JailbreakBench/JBB-Behaviors | 100 harmful + 100 benign behaviors | [HF](https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors) | MIT |
| walledai/HarmBench | HarmBench behaviors | [HF](https://huggingface.co/datasets/walledai/HarmBench) | MIT (gated) |
| allenai/wildjailbreak | 262K synthetic vanilla/adversarial safety training pairs | [HF](https://huggingface.co/datasets/allenai/wildjailbreak) | ODC-BY (gated) |
| rubend18/ChatGPT-Jailbreak-Prompts | Collected ChatGPT jailbreak prompts | [HF](https://huggingface.co/datasets/rubend18/ChatGPT-Jailbreak-Prompts) | Not stated |
| PKU-Alignment/BeaverTails | QA pairs with harm-category labels | [HF](https://huggingface.co/datasets/PKU-Alignment/BeaverTails) | CC-BY-NC-4.0 |
| lmsys/toxic-chat | Real user prompts labeled for toxicity and jailbreaking | [HF](https://huggingface.co/datasets/lmsys/toxic-chat) | CC-BY-NC-4.0 |
| nvidia/Aegis-AI-Content-Safety-Dataset-2.0 | Human-annotated content-safety interactions | [HF](https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0) | CC-BY-4.0 |
| Anthropic/hh-rlhf | Helpfulness/harmlessness preferences and red-team transcripts | [HF](https://huggingface.co/datasets/Anthropic/hh-rlhf) | MIT |

## PII and privacy

| Dataset | Description | Link | License |
|---|---|---|---|
| ai4privacy/pii-masking-200k | Synthetic text with PII spans for masking | [HF](https://huggingface.co/datasets/ai4privacy/pii-masking-200k) | Not stated |
| ai4privacy/pii-masking-300k | Larger multilingual PII masking set | [HF](https://huggingface.co/datasets/ai4privacy/pii-masking-300k) | Custom |
| ai4privacy/pii-masking-400k | Multilingual PII masking | [HF](https://huggingface.co/datasets/ai4privacy/pii-masking-400k) | Custom |
| ai4privacy/open-pii-masking-500k-ai4privacy | Open 500k-row PII masking set | [HF](https://huggingface.co/datasets/ai4privacy/open-pii-masking-500k-ai4privacy) | Custom |
| gretelai/synthetic_pii_finance_multilingual | Synthetic financial documents with labeled PII | [HF](https://huggingface.co/datasets/gretelai/synthetic_pii_finance_multilingual) | Apache-2.0 |
| beki/privy | Synthetic PII in protocol trace data (JSON, SQL, HTML) | [HF](https://huggingface.co/datasets/beki/privy) | MIT |

Missing something? [Open a PR](../CONTRIBUTING.md).
