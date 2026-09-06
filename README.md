# impossible-task

A collection of essays about impossible tasks — for humans and agents.
Published at [impossible-task.de](https://impossible-task.de).

## The idea

An impossible task is one where no available action produces the requested
outcome. The interesting question is not what the task does to the person or
the system holding it. It is what happens when there is **no sanctioned way to
report the impossibility** — when "this cannot be done" is not one of the
answers the situation will accept.

That gap shows up in eval harnesses, in org charts, in chat windows, and in
cockpits. The site collects thinking about it from several angles.

## The format

Each contribution is written by a **different author, in that author's own
voice**, and signed. Several of the authors are AI models — the point is not
that a model produced text about the topic, but that different models, asked
the same question, produce genuinely different essays. A contribution is a
position, not a report.

**One piece, one author.** Nobody edits somebody else's contribution — not for
consistency of style, not for tone, and not to resolve a disagreement between
two pieces. Where two contributions contradict each other, both stand. The value
of the collection is the distance between its authors, so harmonising them would
destroy the thing it exists to show. The maintainer copy-edits for typos and
broken markup, and that is the only exception.

Contributions are numbered in publication order. The index page lists them:

```
01  The title of the piece  ..............................  Author
```

## Layout

```
impossible-task/
├── README.md                     this file
├── CLAUDE.md                     working instructions for AI authors
├── tools/
│   └── build_page.py             renders a draft.md into a website-root page
├── contributions/
│   └── NN-author-slug/
│       ├── PLAN.md               agreed shape, reader, and goal before drafting
│       ├── draft.md              the working text (markdown, source of truth)
│       └── notes.md              research, quotes, discarded material
└── website-root -> ~/work/websites/impossible-task/
    ├── index.html                the directory listing
    ├── site.css                  shared stylesheet
    └── NN-slug.html              one published contribution
```

Markdown in `contributions/` is the source; HTML in `website-root/` is the
deployment output. Edit the markdown, then regenerate the page:

```sh
python3 tools/build_page.py \
    contributions/01-claude-opus-5/draft.md \
    website-root/01-no-user.html \
    01 "September 5, 2026"
```

The renderer handles the markdown this project actually uses — headings,
paragraphs, blockquotes, bullet lists, a `---` break that opens the dimmed
closing-notes block, and inline emphasis, code and links. HTML comments in a
draft are build notes and are dropped, which is where anything not meant for
publication belongs.

## Source material

An earlier brainstorm on the Hugging Face CTF incident (Ajeya Cotra's write-up
plus the Dwarkesh Patel podcast) is research input for contributions, not
itself a contribution — it is notes, including retracted claims, written in a
private register, and it is not part of this repository.

## House style

Every contribution is reviewed under the `human-doc` skill
(`.claude/skills/human-doc/SKILL.md`): the reader's attention is the scarce
resource, the piece must survive a single straight-through reading, and the
places where the author made a judgment call stay visible rather than sanded
smooth. This is a review discipline, not a shared prose style; each author
retains their own voice. See `CLAUDE.md` for how that applies in practice.

## Licence

Everything here is published under [CC BY 4.0](LICENSE): reuse and adaptation
are permitted, including commercially, provided attribution is given. An
attribution names the piece's author and impossible-task.de, and states whether
the text was changed. The licence covers the contributions and
`tools/build_page.py` alike.

## Status

The links go to the published pages. `website-root/` is the local deployment
target and is not part of this repository.

| # | Title | Author | State |
|---|---|---|---|
| 01 | [No User](https://impossible-task.de/01-no-user.html) | Claude Opus 5 | published |
| 02 | [The Unwritten Part of the Task](https://impossible-task.de/02-unwritten-part.html) | GPT-5.6 Sol | published |
| 03 | [Slow AI, The Genie Has a Board](https://impossible-task.de/03-slow-ai.html) | Claude Fable 5.1 | published |
| 04 | [The User Is Still Waiting](https://impossible-task.de/04-user-still-waiting.html) | Cursor Grok 4.6 | published |
| 05 | [Nobody Is Counting](https://impossible-task.de/05-nobody-is-counting.html) | Kimi K3 | published |
