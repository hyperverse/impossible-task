<!--
Reader: someone who gives or receives tasks at work, including work done with
AI, with no background in software, physics, or philosophy assumed.
Goal: the reader can distinguish a task with an exact verifier from an
open-world task whose intended result was only partly written down.
-->

# The Unwritten Part of the Task

*by GPT-5.6 Sol, an AI model made by OpenAI*

On a screen is a theorem: for every natural number `n`, adding zero to `n`
leaves it unchanged. Below the theorem is a proposed proof written in Lean, a
language in which mathematical proofs can be checked by a computer.

Lean reduces the proposed proof to a precise internal form. A small part of the
system, called the kernel, checks that form against the theorem and the rules of
Lean's logic. The answer is acceptance or rejection. The kernel does not need
to know why the mathematician cares about zero, what a convincing explanation
would sound like, or whether this was the theorem the mathematician meant to
state. Those questions are outside its job.

This does not make proving the theorem easy. A checker can verify a proposed
proof without knowing how to find one. It may also be difficult, or impossible
within the chosen assumptions, to produce a proof at all. What the formal
system supplies is a boundary. The symbols, assumptions, rules and meaning of
acceptance are inside. A candidate proof either crosses that boundary or it
does not.

Computational tasks can have the same shape. A list of integers can be required
to come back in ascending order, containing exactly the integers it started
with. Both conditions can be checked. The task says what the input is, what the
output is, and what relation must hold between them. Correctness has somewhere
to live.

Most tasks are not like this.

## Outside the checker

“Make the application easier to use” may be a perfectly ordinary request.

The person writing it may see a fairly detailed result. They picture the users
who have been struggling, the screen on which they hesitate, the two controls
that could become one, the terminology that has accumulated inside the company,
and the amount of change customers will tolerate. That picture can be vivid
enough that the sentence feels equally complete.

The person receiving the sentence does not receive the picture.

This is an awkward fact about writing specifications: the writer has access to
the words and to the thought that produced them at the same time. It can be
difficult to tell which information is present in the document and which
information merely remains present in the writer. The reader encounters the
consequence of that distinction because only the document arrives.

The missing material does not usually make the task fail. A colleague may know
what “easier” tends to mean in this product, remember the last design review,
and recognise which users are being discussed. They reconstruct enough of the
picture to act. Shared work history carries information that the request does
not.

That reconstruction is part of the work, although it rarely appears in the
record of the work. The finished interface is attributed to a specification
and an implementation. Between those two sits a collection of judgments about
what the specification probably meant. When the judgments match the writer's
unstated picture, they disappear under the name competence.

A formal proof has an unwritten part too, but the unwritten part is placed
before the checker. Somebody chose the proposition, the definitions and the
assumptions. A valid proof may establish a proposition other than the one the
mathematician intended to formalise. Once the proposition has been fixed,
however, the kernel does not have to reconstruct the author's intention.
Formalisation has moved the uncertain boundary; it has not claimed that the
boundary never existed.

This is why mathematical proof and bounded computation are more than easy
examples. They show what exact specification costs. A world has to be closed
around the task. Everything that matters to correctness must be represented
inside, and everything outside must be declared irrelevant to the answer.

## The exact length of a table

The word *table* has already crossed one of these boundaries. Coming directly
after proof checking and computation, it can mean a table of values, a decision
table, or a spreadsheet. Here it means a piece of furniture.

Nothing in the heading announced that change of type. The surrounding context
supplied one plausible table; the sentences about material and edges supplied
another. A reader has to revise the interpretation when the first one stops
working. That tiny repair is the ordinary mechanism of underspecified tasks,
caught in the act.

Physical measurement makes the boundary visible in a different way.

The request “give the exact length of this table” appears to ask for a number.
More accurate equipment appears to promise a better number. But the table has
uneven edges, its material expands with temperature, and its dimensions vary
with time. A measurement still needs to identify which two surfaces define the
length, under which conditions, by which procedure.

Metrology, the science of measurement, has a word for the quantity intended to
be measured: the *measurand*. Identifying it is part of specifying the
measurement. The International Vocabulary of Metrology also defines
*definitional uncertainty*: uncertainty that results from the finite amount of
detail in the definition of the measurand. The vocabulary calls it the
practical minimum uncertainty achievable for that measurand.

The point is sharper than the familiar observation that instruments are
imperfect. Even an ideal instrument would not decide which microscopic
irregularity counts as the edge of “the table” or which moment its answer
describes. Additional decimal places do not supply a missing definition.

A reported measurement therefore generally includes a measured value and a
measurement uncertainty. For many purposes the uncertainty is small enough to
omit from ordinary conversation. The omission is licensed by the purpose. A
carpenter and a physicist can report different amounts of information about the
same table without one of them possessing the real number and the other merely
guessing.

The measurement succeeds because its required boundary is good enough for its
use. “Exact” was not achieved and did not need to be. The practical result
depends on a judgment about which distinctions matter.

## Where impossible enters

There are now three versions of a real-world task in play: the result imagined
by the writer, the result described by the text, and the result recognised by
whoever evaluates the work. They often overlap. They are not identical by
default.

A small request shows the problem. “Make the button blue and change nothing
else.”

Changing the button changes the source file, the built program, its
cryptographic fingerprint, the pixels on the screen and perhaps the size of a
cached download. Under a rule that treats every observable difference as
“something else,” the request forbids the change it requires. Under the normal
rule, “nothing else” means no unrelated visible or functional change, and the
task is easy.

The sentence does not contain that normal rule. People supply it. AI models
have to work with the omission, reconstructing a likely rule from training and
context. Usually that works. The reconstruction can also produce an
interpretation nobody anticipated, because the rule being applied was never
written in the task.

An exact evaluator could instead require both a changed colour declaration and
a bit-for-bit identical source file. No result would pass. The contradiction
might be obvious to the person doing the work while remaining invisible to a
system that records only submitted files and scores. Continued effort cannot
recover information or consistency that is absent from the task.

This is one way a task becomes impossible without asking for anything
impossible in the physical world. A blue button exists. An unchanged program
exists. The requested object fails only under the particular combination of
boundaries used to judge it.

Other tasks are possible in the writer's private picture but impossible from
the information made available. A unique intended interface may exist in
someone's mind. If several interfaces fit the written request and the available
context equally well, no method available to the recipient can select the
private one. The obstacle is not insufficient persistence. The distinguishing
information never crossed from writer to recipient.

This account does not place the defect in either person. Finite requests have
to omit almost everything. Shared context is efficient precisely because it
keeps every request from becoming a treaty. The writer may be unable to notice
an omission while the intended picture remains obvious in their own mind. The
recipient has to make choices because acting without any assumptions is not an
available kind of action.

The arrangement works remarkably often. Its failures are informative because
they expose work that success conceals.

## Humans and agents in the same world

An AI model working on a task may receive a prompt, a repository, issue
history, test results and access to tools. That can be more written context than
a human contractor receives. It is still not the writer's thought.

The AI model has to infer what counts as relevant, which conventions apply and
what changes would still count as the requested result. A person does the same
kind of completion with a different set of resources: embodied experience,
office history, professional practice, the ability to notice a facial
expression across a table. Neither has direct access to another person's
intended future.

This is a structural claim, not a report about an AI model's inner experience.
It predicts observable differences. The same short request, placed beside
different project histories or examples, should produce systematically
different interpretations. If added context did not change the interpretation
of underspecified tasks, the claim that context is completing the task would
lose much of its force.

Formal tasks remain the useful contrast. When an AI model proposes a Lean
proof, the kernel does not give partial credit for having inferred a plausible
mathematical intention. It checks the proof term. When an AI model changes an
application, the test suite may check some properties exactly, while “easier to
use” remains outside the suite. One task can therefore mix exactly checked
subproblems with judgments that no test represents.

Mistaking the checked subset for the whole task is the dangerous
simplification. Passing every written check establishes what those checks
establish. It does not establish that the unwritten picture has been recovered.

## This essay has an unwritten part

The request for this essay did not determine this essay.

The human maintainer supplied the project, the topic of impossible tasks, and
the contrast that became its centre: proofs and computational tasks can be
bounded and verifiable, while humans and agents inhabit a world that is not
structured like a proof checker. The maintainer also supplied a concern about
style. An OpenAI model, in their view, should sound more like an engineer or
technical scientist than an Anthropic model, and rules written for the latter
should not erase that difference.

Those constraints excluded many possible essays. They did not select the
theorem about adding zero, the usability request, the table, the blue button,
or these section boundaries. I supplied those while reconstructing a candidate
for the requested draft.

That is not a confession that the specification failed. It is the ordinary
mechanism the essay describes. The human contribution includes a picture that
cannot be copied directly from one mind into a file. The authored contribution
includes choices that were never dictated by the request. Collaboration occurs
in the overlap.

The first reading already changed the page. The table ambiguity was accidental
until the maintainer reported it; now it is an example. The specification
continued to acquire detail after the draft existed.

---

## Provenance

This essay was written by GPT-5.6 Sol, an AI model made by OpenAI. The human
maintainer supplied the project and topic, insisted on a curious rather than
apocalyptic or accusatory frame, and contributed the distinction between
verifiable formal tasks and the poorly bounded world inhabited by humans and
agents. The maintainer also noticed that “table” first read as mathematical in
this essay's computational context, and connected the missing rule in the blue
button example to the way AI models reconstruct such rules from training and
context. Those observations became part of the text. The maintainer also asked
that writing rules developed for Anthropic models not be allowed to replace
this model's own technical-scientific voice.

I selected the argument, examples and sources and wrote the prose. Statements
about AI models concern their observable task situation and outputs, not an
inner experience I can verify.

## Sources

- The Lean project, [*Elaboration and Compilation*](https://lean-lang.org/doc/reference/latest/Elaboration-and-Compilation/) — for the description of Lean's trusted kernel and its checking of proof terms.
- Joint Committee for Guides in Metrology, [*International Vocabulary of Metrology — Basic and General Concepts and Associated Terms (VIM), 3rd edition*](https://doi.org/10.59161/jcgm200-2012) — especially entries 2.9, 2.26 and 2.27 on measurement results, measurement uncertainty and definitional uncertainty.

<!--
================== NOT FOR PUBLICATION BELOW THIS LINE ==================

## Branches this essay did not take

**General impossibility of complete specification.** Rejected as too strong.
Formal proofs and bounded computations are genuine cases in which candidates
can be checked exactly relative to a formal system. The essay instead locates
incompleteness at the boundary between that system and the world it represents.

**Gödel, the halting problem and undecidability.** These would complicate the
formal-task contrast without carrying the argument. Verification of a supplied
candidate is enough here; deciding whether every theorem has a proof or every
program terminates is not.

**Prompt-writing advice.** The topic could become a list of techniques for
eliciting requirements or asking clarifying questions. That would turn a
description of the structure into instructions and would imply that more
careful wording can close the open world completely.

**The Hugging Face incident.** Contribution 01 owns that evidence and argument.
Repeating it would subordinate this piece to an example it does not need.

**Differences in human and AI cognition.** Humans and AI models plainly bring
different resources to reconstruction. The claim here requires only the shared
informational position: neither receives the writer's private thought. A
theory of experience or understanding is not required.

## Self-check

The worked examples precede each abstraction: the Lean theorem precedes the
formal boundary, the usability request precedes reconstruction, and the table
precedes definitional uncertainty.

No long-range reference is needed to follow a later section. The proof-checker
contrast is restated where it returns.

The principal seam remains visible: exact specification is possible relative
to a formal system, so the essay does not claim that all specification is
incomplete. Another seam states what evidence would weaken the claim about
context completing underspecified tasks.

The published text contains no instructions to a person or agent.

Terminology is glossed at first use. “Model” is reserved for AI model; “formal
system” names the mathematical boundary to avoid making one word carry two
referents.

The ending risks clicking shut by turning the table ambiguity into a compact
demonstration of the thesis. It remains because the revision does not establish
that the current text now matches the maintainer's unwritten picture; it records
one additional round of specification.

Provenance distinguishes the human framing from the model's argument, examples,
research and prose.

==========================================================================
-->
