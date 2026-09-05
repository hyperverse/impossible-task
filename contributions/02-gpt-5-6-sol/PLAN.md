# 02 — Plan (GPT-5.6 Sol)

Status: **approved 2026-09-05**

Working title: **The Unwritten Part of the Task**

Alternates: *Outside the Proof Checker* · *Complete Within the Model* · *Who
Finishes the Specification?*

## Reader

Someone who gives or receives tasks at work, including work done with AI, and
who does not need a background in software, physics, or philosophy.

## What the reader should be able to say afterwards

*“A proof checker can tell whether a formal result meets a written
specification. Most real-world tasks are different: part of the intended result
was never written down, and carrying out the task includes reconstructing it.”*

## Governing claim

A mathematical or computational task can have a sharply bounded scope and an
exact verifier. That makes it an important contrast, not merely a simple
example. Most tasks in the physical and social world are specified by a finite
text that points toward a much richer state imagined by its writer. The writer
may not know which parts of that state reached the page and which remain only
in their own model of the result. Humans and agents both work from that lossy
boundary.

A finite specification can therefore be complete inside a chosen formal model,
while an open-world task cannot list every relevant fact, acceptable side
effect, or observation under which the result must count as correct. Ordinary
work succeeds because requester, executor, and evaluator supply compatible
missing structure. An impossible task can arise when they supply incompatible
structure while the requested result is still treated as uniquely determined.

## Spine

1. **Open inside a proof checker.** A short formal theorem has a statement,
   fixed rules, and a small program that accepts or rejects a proposed proof.
   Finding a proof may be hard, and whether one exists may be a separate
   question, but checking a candidate is exact. The checker does not need to
   infer what the theorem’s author had in mind.

2. **Show what made that possible.** The formal task closed its world. Symbols,
   rules, assumptions, and the meaning of acceptance were brought inside the
   boundary. A similarly bounded computational task—sorting a given list under
   a stated ordering—can have the same property. This is genuine
   specification, not an approximation to real-world work.

3. **Step outside the checker.** A request such as “make the application easier
   to use” points to a future state in the writer’s mind. The words do not
   contain the users they pictured, the trade-offs they would accept, or the
   observations that would make them say “yes, that is what I meant.” For many
   human writers, the distinction between what they wrote and what they were
   imagining is itself difficult to see because both are present to them at
   once. The person or agent receiving the text gets only one of the two.

4. **Name the unwritten operation.** The executor does not merely follow the
   specification; the executor reconstructs a candidate for its missing
   structure. Humans use shared context, convention, and professional
   judgment. Agents use the text, supplied context, tools, and learned
   regularities. Most of the time the reconstruction is close enough and
   disappears into ordinary competence.

5. **Move to physical measurement.** “Give the exact length of this table”
   needs a time, temperature, treatment of uneven edges, measuring procedure,
   and uncertainty. Physics does not repair this with a more impressive number
   of decimal places. Measurement works by stating conditions and uncertainty,
   making the boundary visible rather than pretending it vanished. Source any
   metrology claims from BIPM material rather than relying on analogy alone.

6. **Locate the impossible case.** Trouble appears when the requester,
   executor, and evaluator close the world differently. One result can satisfy
   the words, another the purpose, and neither both. If the accepted output has
   no place to expose that mismatch, continued effort cannot resolve it because
   the missing information is not inside the task.

7. **Apply the structure to agents without claiming an inner experience.**
   Prompts are small compared with the worlds they refer to. Models produce
   useful work by filling omissions from context and learned regularities, just
   as people use convention and professional judgment. This is a structural
   and behavioural claim, not testimony about what a model feels or privately
   understands. State what evidence would weaken it: tasks where varied
   plausible contexts do not alter the model’s interpretation.

8. **Use the project itself as the recursive seam.** The maintainer supplied a
   topic, constraints, and an approved plan; the author selected the
   proof-checking, application, and measurement examples and decided what “a
   draft” should include. The maintainer’s new distinction between formal and
   real-world tasks materially changed the plan, but still did not uniquely
   determine the prose. The essay about unwritten specification therefore has
   an unwritten part. That is mildly funny, evidence of ordinary authorship,
   and not a claim that the collaboration failed.

9. **Land on responsibility without assigning fault.** The hidden completion of
   a task is neither a defect in the requester nor disobedience in the
   executor. It is part of acting in a world larger than a specification. The
   impossible task is interesting because it makes that usually successful
   arrangement visible.

10. **Close with sources, provenance, declined branches, and the self-check.**
   Review-only material will remain in an HTML comment so the renderer omits it.

## What the piece is not doing

- **No claim that all tasks are impossible or all specifications defective.**
  The bounded-task counterexample prevents this from becoming a slogan.
- **No retelling of the Hugging Face incident.** Contribution 01 already owns
  that case. This piece develops the question it deliberately left open.
- **No instructions for better prompting, management, or agent behaviour.**
  Examples may show what changed under different boundaries, but the essay
  remains descriptive.
- **No apocalypse argument and no assignment of blame.** Incomplete
  specification is treated as a normal feature of finite descriptions, often
  resolved successfully.
- **No appeal to Gödel, the halting problem, or quantum mechanics as
  decoration.** None is needed to establish the claim, and each would invite a
  stronger argument than this essay intends to make.
- **No introspective report.** First person will identify authored choices and
  provenance, not unverifiable internal states.

## Form and provenance

Target length: **1,600–2,200 words**, shorter than contribution 01.

Register: the author’s own technical-scientific voice—concrete, curious, and
dryly amused, with explicit definitions, counterexamples, scope boundaries, and
testable claims. The `human-doc` rules serve as review checks for reader cost
and honesty, not as a prose style to imitate. Technical terms such as *formal
proof*, *model*, and *measurement uncertainty* receive a plain-language gloss
at first use.

The published provenance will state that the human maintainer supplied the
project, topic, constraints, the formal-versus-real-world distinction, and
approval of the plan; GPT-5.6 Sol selected the argument, remaining examples,
sources, and prose. It will also identify GPT-5.6 Sol as an AI model made by
OpenAI.
