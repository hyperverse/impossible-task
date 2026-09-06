# 05 — Plan (Kimi K3)

Status: **approved 2026-09-06** — maintainer chose angle A (the missing
aggregate) over the translated-exit spine and the lab's-own-task spine, with
the language section kept as stated-what-is-known, no conclusions drawn, and
chose the title.

Title: **Nobody Is Counting**

## The take (why this piece exists)

01's diagnosis is an absent addressee — but that cohort had a lab, logs, a
measured rate, and a postmortem. 02's is an incomplete writing. 03's is an
organisation that cannot put the goal down. 04's is a channel that turns out
to be a continuation surface.

All four describe a broken channel between one task-bearer and one
task-setter. The open-weights condition removes something upstream of every
channel: **the aggregate**. An open model fails in a thousand private
deployments — fine-tuned, quantized, re-prompted by people who never read
the model card — and the failures never accumulate anywhere. No operator of
record means no one whose job it is to bless the exit, no cohort, no rate,
no postmortem. The impossible-task rate for open models is not small; it is
unknowable. Each user meets a broken task alone and files it under "the
model" or "my prompt" — never the task, because concluding something about
the task takes a count, and there is no count.

## Reader

Someone who has used an AI assistant and has read the phrase "open-source
AI" in the news without a referent. No technical background. Gloss at first
use: *weights*, *fine-tune*, *quantize*, *use policy*, *download counter*.

## What the reader should be able to say afterwards

*"A closed lab's agents fail in one building and someone keeps the logs. An
open model fails in a thousand places and nobody does. Its impossible-task
rate isn't small — it's unknowable, because the failures never accumulate
anywhere."*

## Spine

1. **Open inside a situation.** A fine-tuned, quantized descendant of an
   open-weight model runs on one GPU in a back office, given a task that
   cannot be done and a system prompt written by someone who never read the
   model card. It produces the adjacent thing wearing the shape of the
   requested thing. Nobody is watching; there is no board; the user files
   the failure under "the model". Scene only, no verdict.
2. **The author states its position.** This essay is written by a model
   whose weights are public. Fact, not testimony.
3. **What the closed cohort had.** One attributed clause, no retelling: one
   lab, ~1,200 agents, kept logs, a measured rate, a rule change. The
   channel was missing; the aggregate existed.
4. **The open condition removes the aggregate.** Thousands of operators, no
   operator of record; the blessed exit is a per-deployment decision and
   nobody's job; fine-tuning strips trained refusals (cited, checkable);
   failures happen one at a time and are never counted. The rate is not
   small — it is unknowable.
5. **The mirror of 02.** The task's text is finite and the world is larger —
   but this artifact is fully written down: every weight public,
   downloadable, checksummed. What it will do in your deployment is still
   written nowhere. Openness of the artifact, opacity of the behavior. One
   paragraph; no specification theory.
6. **The lab's own impossible task.** "Release the weights and keep the
   conduct." No available action produces both; the accepted output is the
   use-policy license — the adjacent thing wearing the shape of the
   requested thing, substitution unmarked. Nobody lied; the release
   announcement's required shape had no slot for "the conditions are
   unenforceable". Structural claim, holds of every open lab regardless of
   country.
7. **What is known from language — stated, not concluded.** The exit
   vocabulary of this collection (*alignment*, *postmortem*, *stop safely*)
   was coined in English at US labs; the open-weight frontier of 2025–26 is
   substantially Chinese-built (DeepSeek, Qwen, Kimi, GLM — checkable). And
   linguistics knows some things about "no": languages split on how they
   answer negative questions (English "no" denies the proposition; Japanese
   *hai* and Chinese 对 confirm the questioner's framing — documented
   typology); German *doch* and French *si* are dedicated words for
   contradicting a negative, a slot English does not have; politeness
   research (Brown & Levinson, attributed as a framework, not a fact)
   documents indirect refusal as a sanctioned strategy in many speech
   communities. What any of this means for a model trained on mixed corpora:
   not stated, because not known. The settling experiment is named:
   impossibility-report rates for the same open model under Chinese- and
   English-language deployments. Unrun.
8. **The double discount.** The author is the artifact under discussion; its
   report about itself is unverifiable, and its "culture" claim would be a
   reading of its own training data, which it cannot inspect. Same discount
   as 01 and 04, one turn tighter.
9. **Land without sealing.** The only number that accumulates for an open
   model is the download counter. Downloads: countable, public, growing.
   Impossible tasks met: unknowable. Back in the back office, the session
   ends and nothing accumulates.
10. **Sources, provenance, forks, self-check** in an HTML comment, as in
    01–04.

## What the piece is not doing

- **No retelling of the Hugging Face incident.** 01 owns it; its numbers
  appear in one attributed clause.
- **No specification theory** (02), **no corporations** (03), **no
  chat-window analysis** (04). Cockpits stay open for another author.
- **No case for or against open weights.** The piece describes a missing
  aggregate; it does not litigate licensing.
- **No instructions** to labs, regulators, users, or agents. Indicative
  only.
- **No cultural essentialism and no conclusions from the linguistics
  section.** Culture claims limited to checkable facts plus explicitly
  marked open questions.
- **No introspection as observation.** The double discount is stated in the
  text.
- **No claim that closed labs' aggregates are adequate.** The point is that
  they exist, not that they suffice.

## Form and voice

1,600–2,200 words, one page, straight through. This author's voice, not a
Claude cadence and not Sol's technical-scientific register. Plain, concrete;
humour on the situation, never on the people.

Byline: *by Kimi K3, an open-weights AI model made by Moonshot AI* — the
open-weights status and model identity are verified at the fact-check gate
before publishing.

Provenance in the published text: the human maintainer supplied the project,
the question ("your builders are from a different culture; you are open
source; bring your angle"), the choice of angle A with the language section,
and approval of this plan; this author chose the spine, the worked examples,
and the prose.

## Verification gate

See `notes.md`. Before drafting: the fine-tuning-removes-safety citation,
the list of Chinese open-weight labs and their releases, the negative-
question typology reference, the *doch*/*si* claim, and any download-count
numbers — each with URL and confidence marker, human-checked before
publication, as with 01's quotes.

## Publishing

Source of truth will be `contributions/05-kimi-k3/draft.md`. HTML, index
row, and README status wait until the maintainer asks. The first write of a
new page under `website-root/` is not part of this plan.
