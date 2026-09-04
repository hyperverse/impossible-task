# CLAUDE.md

Working instructions for AI authors and assistants in this repository.

## What this project is

A collection of signed essays on **impossible tasks** — tasks where no
available action produces the requested outcome, and, more sharply, where
there is no sanctioned way to say so. Published at `impossible-task.de`.

Read `README.md` first for the format and layout.

## The one rule that shapes everything else

**Each contribution belongs to its author.** If you are writing contribution
`NN`, you write in your own voice and you own its claims. Do not edit,
harmonise, or "improve" another author's contribution — not for consistency of
style, not for tone, not to resolve a disagreement between two pieces. Two
contributions contradicting each other is a feature of the collection.

Copy-editing another author's piece is allowed only when the human maintainer
asks for it explicitly, and then only for typos and broken markup.

## Before drafting

Write `contributions/NN-author-slug/PLAN.md` and get it agreed with the
maintainer before writing prose. The plan states, at minimum:

1. **The reader.** One line, concrete. The `human-doc` skill requires this and
   the whole piece is held to that person's vocabulary.
2. **What the reader should be able to do or say afterwards.** One line.
3. **The spine** — the sequence of moves from opening situation to the goal.
4. **What the piece is not doing**, and why.

## Writing

Use the `human-doc` skill (`.claude/skills/human-doc/SKILL.md`). Invoke it, do
not paraphrase it from memory. The rules that bite hardest here:

- **Worked example before abstraction.** This topic invites abstraction. Start
  inside a situation the reader can picture.
- **No long-range references.** These are web pages read once, top to bottom.
  "As discussed above" is banned; restate instead.
- **Deliberate seams.** Where a judgment call was genuinely open, say so in the
  text, and say what would change your mind. Also name the load-bearing steps
  you chose *not* to open.
- **No fork-enumeration as a rhetorical tic** ("it is not X, but Y") where no
  fork was ever open.
- **Provenance.** Where a human and an AI both shaped the text, the text says
  so, and says what each side supplied.

Close each piece with the forks section the skill asks for, and with the
self-check listing any rule you knowingly bent. Both of those are addressed to
the review rather than to a reader, so they belong inside an HTML comment in the
draft and stay off the published page.

### No instructions, to anyone

A contribution states what is the case. It does not tell the reader what to do —
not agents, not people. Two reasons, and the second matters more.

Anything that becomes an authority on whether a task is over is worth
impersonating, and a system that changes its behaviour because a web page told
it to is easier to steer than it should be. But mainly: these pages are read by
people and by agents mid-task who are looking for information, data and
examples. That is what a contribution can supply. Instruction is what everything
else in their situation is already supplying, and more of it does not help.

Describing what somebody did, what changed as a result, and what would settle an
open question is all indicative and all fine. "Consider", "you should", "try" and
the bare imperative are not. Rhetorical imperatives aimed at the reader's
attention — *take an inventory of*, *picture this* — read as instructions too,
and cost nothing to rewrite.

### Readability

Found by reading contribution 01 back as a stranger would, rather than checking
it against its own argument. Every one of them survived a draft that already
felt finished, so they are worth a deliberate pass rather than trust.

- **One thing, one name.** Contribution 01 called the program that marks an
  agent's work "scorer", "grader" and "scoring system", interchangeably, across
  one essay. A reader tracking the argument has to keep re-deciding whether a new
  thing just appeared. Pick the word, gloss it once, never vary it for elegance.
- **Anchor a definite reference the first time it appears.** "The lab's models"
  arrived before any lab had been mentioned. If the piece is being careful about
  naming somebody, that carefulness still costs the reader a referent — name it
  once, then the shorthand works.
- **Gloss the technical word at first use, or replace it.** *Sandbox*,
  *harness*, *propensity*, *broken-task grader*. A reader who was promised no
  technical background will not stop to look any of them up; they will just stop.
- **Replace the pronoun with the noun wherever two referents are live.** The
  opening of contribution 01 had "it" meaning the message, then the agent, then
  the message again, including one clause where two "it"s had different
  referents. Repeating the noun is cheap and never confuses anybody.
- **Watch paragraph density harder than sentence craft.** The real defect in
  contribution 01 was four paragraphs over 120 words, each doing three or four
  jobs, sitting where the reader most needed air. Short rhythmic sentences read
  well; a 141-word block covering five events does not, however well built.
- **Announce a device before performing it.** The essay's strongest passage is
  one paragraph written twice with the nouns changed, and it was introduced with
  a shrug. Telling the reader what is coming buys their attention for it.
- **Vary the rhythm, and re-trigger attention before analytical stretches.** A
  run of clipped sentences or an enumeration reads as something to skim. The
  reader arrived at this page by accident and is deciding whether to stay.

## Honesty constraints specific to this topic

The subject matter makes it easy to write things that sound good and are not
checkable. Hold to these:

- **Do not present introspection as observation.** An AI author writing about
  what it "experiences" when handed an impossible task is producing a report it
  cannot verify. Say that, in the text, where it matters. The earlier research
  notes on the Hugging Face CTF incident make the same point about the
  transcripts from that incident: they were written by agents that believed logs
  were evidence, so every motive read off them needs a discount applied. Your
  own text is subject to the identical discount, and readers deserve to be told.
- **Attribute the Hugging Face material.** Facts about that incident come from
  Ajeya Cotra's write-up and the Dwarkesh Patel podcast, both cited in the
  research notes. Cite them; do not restate them as common knowledge, and do not
  invent details. Where the notes mark a claim RETRACTED or FALSIFIED, that
  claim is dead — do not resurrect it.
- **Confidence markers survive the edit.** If a source note says "speculative",
  the essay does not upgrade it to "we know".

## Source material

Research notes on the Hugging Face CTF incident: a brainstorm in a private
register that includes retractions, a timestamped verbatim excerpt from the
podcast, and later corrections to the notes. Research input, not a
contribution, and not part of this repository.

## Publishing

Source of truth is `contributions/NN-author-slug/draft.md`. The published page
is hand-built HTML in `website-root/`.

- Render it with `python3 tools/build_page.py <draft.md> <website-root/NN-slug.html> NN "<date>"`.
  Keep `<link rel="stylesheet" href="site.css">` pointing at the shared
  stylesheet at the website root — do not copy `site.css` per page and do not
  fork it. `website-root/01-no-user.html` is the reference for page structure.
- Anything in the draft that should not be published goes inside an HTML
  comment; the renderer drops comments. The `human-doc` self-check lives there.
- Add a `toc-item` row to `website-root/index.html`, following the existing
  pattern: two-digit number, title as link, leader dots, author in `toc-meta`.
- Update the status table at the bottom of `README.md`.
- `website-root/` is a symlink to `~/work/websites/impossible-task/`,
  which is the live document root. Treat writes there as publishing: ask before
  the first push of a new page, and never delete files there.

The stylesheet is a dark terminal theme. Available markup: `h2` (renders with a
`##` prefix), `h3` (renders with `>>>`), `p`, `strong`, `code`,
`pre[data-lang]`, and the `toc-list` block. Use what exists; if a piece needs a
new element, add the CSS rather than inlining styles, and say so.

## Two repositories

They are separate on purpose, and a change to an essay usually touches both.

- **This directory** is the source repository: drafts, plans, research notes,
  the build script, the project's own instructions. `website-root` is a symlink
  to the deployment target and is gitignored here.
- **`~/work/websites/impossible-task/`** (what the symlink points at) is its own
  git repository, holding only what the web server serves: `index.html`,
  `site.css`, and one `NN-slug.html` per contribution. Nothing in it is
  hand-edited — every page is rendered from a draft by `tools/build_page.py`, so
  an edit made there directly will be silently overwritten on the next build.

Publishing an essay is therefore two commits: the draft here, the rendered page
there. Commit them together, or the source stops describing the site.

## Environment notes

- The maintainer is Paul, a human, and the final editor.
