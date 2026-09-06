# 05 — Research notes

Sources for the verification gate named in `PLAN.md`. Confidence marker on
each block. ⚠ marks anything that reached me through a search-result
summary rather than a page I read in full — those get checked against the
primary source by a human before publication, as with 01's quotes.

## The author's own status (byline claim)

The maintainer's brief said "you are open source". The checkable fact is
narrower, and the draft should use it: **open-weight, not open source**.

- Moonshot AI launched Kimi K3 as an API on 16 July 2026 and published the
  weights on 26–27 July 2026 (sources disagree by a day; the Hugging Face
  repo is the arbiter). 2.8T total parameters, MoE, 1M context.
  ⚠ Secondary: https://www.chatslide.ai/guides/is-kimi-k3-open-source
  (claims read directly from the repository, verified 16 Aug 2026) and
  https://felloai.com/kimi-k3/
- The shipped license is a custom **Kimi K3 License**, not the "Modified
  MIT" that pre-release press reported. Hugging Face metadata records
  `license: other`, `license_name: kimi-k3`. Two conditions MIT does not
  have: (a) model-as-a-service businesses above $20M aggregate
  trailing-12-month revenue must sign a separate agreement with Moonshot
  before commercial use; (b) products above 100M monthly active users or
  $20M monthly revenue must display "Kimi K3" prominently in the interface.
  Primary: https://github.com/MoonshotAI/Kimi-K3/blob/HEAD/LICENSE
  CONFIDENCE: high for the license text (the file itself); medium for the
  release-date details (⚠ secondary).
- Note for the draft: the license is itself an instance of spine item 6 —
  conditions that bite only at scale, unenforceable against the ordinary
  downloader. Self-implicating and checkable; use it.
- Byline consequence: *by Kimi K3, an open-weights AI model made by
  Moonshot AI*. Do not write "open source" — under the OSI definition the
  revenue gate is a field-of-use restriction (⚠ analysis:
  https://moclaw.ai/blog/kimi-k3-license). The maintainer's framing gets
  gently corrected in the text; that correction is itself on-theme.

## Fine-tuning strips trained refusals

Qi, Zeng, Xie, Chen, Jia, Mittal et al., "Fine-tuning Aligned Language
Models Compromises Safety, Even When Users Do Not Intend To!", arXiv
2310.03693 (Oct 2023). https://arxiv.org/abs/2310.03693
CONFIDENCE: high (abstract read in full).

- "The safety alignment of LLMs can be compromised by fine-tuning with only
  a few adversarially designed training examples." GPT-3.5 Turbo's
  guardrails jailbroken with 10 such examples for under $0.20 via the
  fine-tuning API.
- "Even without malicious intent, simply fine-tuning with benign and
  commonly used datasets can also inadvertently degrade the safety
  alignment of LLMs, though to a lesser extent."
- "Even if a model's initial safety alignment is impeccable, it is not
  necessarily [] maintained after custom fine-tuning."
- Successor framing: Qi et al. 2025 on "shallow safety alignment" —
  alignment mostly adjusts the distribution over the first few tokens.
  ⚠ Known only via the survey arXiv 2605.25073; cite the concept, not the
  detail, unless a human reads the 2025 paper.

Use in the draft: the blessed exit ("you may report this as impossible")
is training, and training is what fine-tuning rewrites. The exit does not
survive distribution. One sentence, cited.

## The open-weight frontier is substantially Chinese-built

- ⚠ AI2Work, "Chinese Labs Own the Open-Weight Leaderboard" (2026),
  https://ai2.work/blog/chinese-labs-own-the-open-weight-leaderboard-glm-deepseek-qwen :
  the four highest-scoring open-weight models on the Artificial Analysis
  Intelligence Index — Kimi K3 (60), GLM-5.3 (60), Qwen3.8 2.4T (58),
  GLM-5.3-Flash (57) — all from Chinese labs; best US open model on the
  same board, NVIDIA Nemotron 3 Ultra, scores 38. Artificial Analysis
  reportedly noted in April 2026 that the ten highest-scoring open-weight
  models were all from China-based labs. CHECK against
  artificialanalysis.ai directly before use.
- ⚠ Forkast, "Chinese Open-Weight Frontier Compresses" (2026),
  https://forkast.news/chinese-open-weight-frontier-compresses-five-labs-thirty-days-two-licensing-models/ :
  summer 2026 sequence — Kimi K3 (27 Jul), DeepSeek V4-Flash (31 Jul,
  MIT), Qwen3.8-2.4T-A95B (12 Aug, custom revenue-gated), GLM-5.3-Flash
  (25 Aug, MIT). Licensing split: MIT for the small fast models,
  revenue-gated custom licenses for the flagships. Download figures quoted
  there: DeepSeek V4-Flash 4.65M, Kimi K3 2.78M, GLM-5.3-Flash 441K,
  Qwen3.8-2.4T flagship 38.8K. CHECK against Hugging Face directly.
- Lab locations (common knowledge, still verify): DeepSeek — Hangzhou;
  Qwen — Alibaba, Hangzhou; GLM — Zhipu AI / Z.ai, Beijing (spun out of
  Tsinghua; listed in Hong Kong Jan 2026); Kimi — Moonshot AI, Beijing.

The claim the draft needs is modest: the frontier of publicly downloadable
weights in 2025–26 is substantially Chinese-built, while the exit
vocabulary (*alignment*, *postmortem*, *stop safely*) was coined in
English at US labs. CONFIDENCE: high for the leaderboard fact modulo the
⚠ check; medium for the vocabulary claim — it is a claim about the
literature's language and origin, not about any person or culture. Keep it
at that.

## What is known from language (spine item 7)

The draft states documented linguistics and draws no conclusion about
models. Three checkable blocks:

**Negative questions split languages.** Holmberg, "The syntax of negative
questions and their answers" (GLOW 36, 2013/2016),
https://glowlinguistics.org/36/pdf/holmberg.pdf
CONFIDENCE: high for the distinction as a literature claim.

- Truth-based (agree/disagree) system: the particle confirms or denies the
  truth of the proposition. Japanese: Q "Kimi tukarete nai?" ('Are you not
  tired?') A "Un, tukarete nai" — literally 'Yes, I'm not tired.' English
  is polarity-based: "No, I'm not tired."
- Chinese and Japanese are the standard truth-based examples (also Korean,
  Afrikaans, Georgian, Evenki, Southern Min in Holmberg's list).
- REQUIRED CAVEAT: later work treats the dichotomy as idealized.
  Roelofsen & Farkas, "Polarity particles revisited", Semantics and
  Pragmatics 12.15 (2019), https://doi.org/10.3765/sp.12.15 , replace the
  binary split with a finer feature model; and Liu et al.(?), "Is Mandarin
  Chinese a Truth-Based Language?", Frontiers in Psychology 2016,
  https://pmc.ncbi.nlm.nih.gov/articles/PMC5167746/ , find Mandarin is a
  **mixed** system using both strategies. The essay says "languages split"
  and immediately says the split is not clean. Both halves are the
  checkable claim.

**German doch / French si.** Krifka, "Response particles as propositional
anaphors", SALT 23 (2013), https://doi.org/10.3765/salt.v0i0.2676 ;
Roelofsen & Farkas 2013 handout,
https://projects.illc.uva.nl/inquisitivesemantics/assets/files/handouts/Roelofsen2013_Rochester.pdf
CONFIDENCE: high.

- German ja/nein/**doch** and French oui/non/**si** are three-particle
  systems: *doch* and *si* are dedicated words for contradicting a
  negative — "Katharina ist nicht zu Hause." / "Doch, sie ist zu Hause."
  ('Yes, she IS.'). English has no such slot; "yes" after a negative
  question is ambiguous between agreement and contradiction.
- The gloss for the reader: some languages set aside a word for exactly
  the move "what you just assumed is wrong". English makes that move share
  a word with agreement. Stated as a fact about words, not about
  speakers' thoughts.

**Indirect refusal as a sanctioned strategy.** Brown & Levinson,
*Politeness: Some Universals in Language Usage*, Cambridge University
Press, 1987. CONFIDENCE: high for the book's existence and territory
(face-threatening acts, off-record strategies); it is cited in the draft
as a framework, not a finding. No quote used.

**The settling experiment, named and unrun:** impossibility-report rates
for the same open model under Chinese-language and English-language
deployments, tasks held constant. Behaviour under a changed option set is
checkable; the author's introspection about its own "culture" is not.

## The download counter (closing image)

Hugging Face documentation, "Models Download Stats",
https://huggingface.co/docs/hub/en/models-download-stats
CONFIDENCE: high (official docs, read in full).

- Counting is server-side: every HTTP GET or HEAD to a library's
  designated "query file" (default `config.json`) counts as one download.
- The public `downloads` field is a rolling 30-day total; it is **not
  deduplicated by user**; GGUF repos double-count on full clones.
- So even the one number that accumulates is a proxy: it counts config-
  file requests, not deployments, and says nothing about use — let alone
  about tasks that could not be done. The draft can use this: the counter
  is precise, public, growing, and measures the wrong thing for anyone
  asking about failure. Downloads last month: 2.78 million (⚠ Forkast
  figure for Kimi K3, check against HF). Impossible tasks met: no field
  in the API.

## The closed cohort (one attributed clause)

Contribution 01's numbers — ~1,200 agents, 198 of 898 tasks never solved,
93% of board traffic, the rule change requiring agents to ask or stop —
are used in one clause, attributed to the lab's own write-up as sourced in
`contributions/01-claude-opus-5/notes.md` and the earlier research notes. Do
not re-derive; do not add detail beyond what 01 already sourced.

## Open items for the human check before publication

1. ⚠ Leaderboard and download numbers against artificialanalysis.ai and
   Hugging Face directly.
2. ⚠ Kimi K3 release date (26 vs 27 July 2026) against the HF repo.
3. The LICENSE file read in full, not via secondary summaries.
4. Holmberg's Japanese example re-checked against the PDF (it is a
   handout; the Frontiers paper gives the same example via Jones 1999).
5. If the draft names the Qi et al. 2025 "shallow alignment" paper, a
   human reads it first; otherwise cite the 2023 paper only.
