# 03 — Research notes

Quotes checked against the source named. Confidence marker on each block.

## Schneier, DEF CON 34, "Hacking AI"

Source: https://www.youtube.com/watch?v=eEBv0STiYhI ; local transcript
`~/work/agent/references/bruceSchneier/bruce_schneier_defcon_hacking_ai_transcript.md`.
Transcript is auto-generated; quotes below cleaned of disfluencies only.
CONFIDENCE: high for content, medium for exact wording.

- [02:22] Definition of a hack: "Something that a system permits, but is
  unanticipated and unwanted by the designers." Also: "An unintended
  exploitation of a system, which one, subverts the rules of the system, two,
  at the expense of some part of the system."
- [02:22] Tax code: "The tax code has vulnerabilities. We call them tax
  loopholes... exploits. We call them tax avoidance strategies... black hat
  hackers... We call them accountants and attorneys."
- [08:22] Genie: "There is no way to outsmart the genie... a genie will always
  be able to hack your wish... in human language and thought, goals and desires
  are always under-specified."
- [09:10] Coffee example: raw beans, plantation, ripping a cup from a stranger.
- [09:49]–[11:16] Volkswagen: "This isn't an AI story. Human engineers
  programmed a regular computer to cheat, but it really illustrates the
  problem... If I asked you to design a car's engine control software to
  maximize performance while passing emission control tests, you wouldn't
  design the software to cheat without understanding that you were cheating.
  This simply isn't true for an AI."
- [12:46] "Simon Willison, AI researcher, called the new Anthropic model Fable
  ruthlessly proactive." NOTE: Willison's actual post is titled "Claude Fable
  is *relentlessly* proactive" (simonwillison.net, 11 June 2026). Use
  Willison's word, note Schneier cited it.
- [14:33] Two genies: Dionysus (does the wrong thing, literal reading) and
  Golem (does the right thing, tramples everything on the way).
- [19:23] "No humans maximize their own interests without constraint. Even
  sociopaths are constrained by the complexity of society... reputation or
  punishment... limited time. These very human qualities have limited hacking
  throughout our history."
- [20:29] Speed, scale, scope, sophistication.
- [23:09] Delaware, Panama, "double Dutch Irish sandwich" (his phrase; the
  usual name is "double Irish with a Dutch sandwich").
- [24:47] "We don't have any system of governance that can deal with hundreds,
  let alone thousands of newly discovered tax loopholes."
- [27:10] "Unlike software, knowing about a tax loophole doesn't mean it gets
  patched." "We've spent 20 plus years trying to patch the carried interest
  loophole in the US tax code and we have failed every time."
- [31:06] "A lot of this really isn't an AI problem... It's a capitalism
  problem. Or it's a democracy problem... problems that at least somewhat human
  inefficiency have largely kept in check. And that's not going to work for
  much longer."
- [37:17] Q&A: "I give it to Charlie Stross... He calls corporations slow AI...
  corporations are maximizers of some objective function that you give it...
  paperclip maximizer, right? Is every startup's business plan... The Handover
  by David Runciman. He looks at governments, corporations and AI together as
  superhuman machines that have singular goals." "Looking at our failures to
  regulate slow AI... is really relevant."
- [32:56] Close: "the solutions are not specific to AI, but they are made more
  urgent because of AI."

## Stross, "Dude, you broke the future!", 34C3, Dec 2017

Source: http://www.antipope.org/charlie/blog-static/2018/01/dude-you-broke-the-future.html
CONFIDENCE: high (author's own transcript).

- "I'm talking about the very old, very slow AIs we call corporations, of
  course."
- "Here's the thing about corporations: they're clearly artificial, but
  legally they're people. They have goals, and operate in pursuit of these
  goals. And they have a natural life cycle."
- "they are all subject to instrumental convergence insofar as they all have a
  common implicit paperclip-maximizer goal: to generate revenue. If they don't
  make money, they are eaten by a bigger predator or they go bust. Making
  money is an instrumental goal—it's as vital to them as breathing is for us
  mammals."
- Paperclip maximizer defined: "a goal-seeking AI that has a single priority...
  able to improve itself in pursuit of that goal but has no ability to vary its
  goal".
- "Regulatory agencies are our current political systems' tool of choice for
  preventing paperclip maximizers from running amok. But unfortunately they
  don't always work." Failure modes named: regulatory capture, regulatory lag.
- Stross explicitly: "I do not have a solution to the regulatory problems...
  This essay is polemical."

## Runciman, *The Handover* (Profile Books, 2023)

Full title: *The Handover: How We Gave Control of Our Lives to Corporations,
States and AIs*. Publisher copy: "A few hundred years ago, humans started
building the robots that now rule our world. They are called states and
corporations: immensely powerful artificial entities... which, unlike us, need
never die." CONFIDENCE: high for title and framing; I have not read the book,
so cite only the framing, via publisher copy and Schneier's summary.

## Volkswagen

Primary: Volkswagen AG Annual Report 2016, "Diesel Issue" section,
https://annualreport2016.volkswagenag.com/group-management-report/diesel-issue.html
(PDF: .../servicepages/downloads/files/diesel_issue_vw_ar16.pdf).
CONFIDENCE: high (VW's own text). Note this is the company's account of
itself, prepared with litigation in view; the "below board level" claim is
contested by plaintiffs and was never the finding of a court. Say so.

Quotes:
- "The starting point of the diesel issue at Volkswagen was the strategic
  decision to launch a large-scale promotion of diesel vehicles in the USA in
  2005. To this end, a new diesel powertrain unit featuring high performance
  and cost-efficient production – the EA 189 type engine – was to be
  developed."
- "Under the strictest standard in the USA at the time, only 31 mg/km of NOx
  was allowed to be emitted, about one-sixth of the Euro 5 standard applicable
  in Europe at that time."
- "technicians and engineers face the challenge that there is a conflicting
  objective between the reduction of NOx and other parameters."
- "in order to resolve this conflicting objective satisfactorily within the
  time frame and budget of the EA 189 project, a group of persons at levels
  below the Group's Board of Management in the powertrain development division
  decided to modify the engine management software."
- "a software that recognizes the driving curve of the official type test...
  mode 1 optimum NOx for test bench operation or mode 2 optimum particulate
  matter for road operation."
- "disclosure of the US 'defeat device' to EPA and CARB on September 3, 2015."
- Costs "appeared to be controllable overall"; the EPA Notice of Violation of
  18 September 2015 "came as a surprise to the Company".

VW statement, 2 March 2016 (on shareholder suits), via Automotive World:
- "This modification could be implemented with relatively small changes and
  within the budget that was available for the development of the engine
  management software and without the need to involve superior levels. Only a
  small number of an approximate total 15,000 individual algorithms were
  changed." CONFIDENCE: high.

Press conference 10 Dec 2015 (BBC, DW, Guardian):
- Pötsch: "not a one-off mistake but a chain of errors". Müller: individual
  misconduct, flawed processes, a mindset that tolerated rule-breaking.
  CONFIDENCE: high.

Discovery: ICCT commissioned West Virginia University (CAFEE), 2013–14,
portable emissions measurement system, Jetta 15–35× and Passat 5–20× the
standard on the road while passing the FTP bench test. Presented to EPA and
CARB May 2014. Source: ICCT fact sheet 18 Sep 2015,
https://theicct.org/epas-notice-of-violation-of-the-clean-air-act-to-volkswagen-press-statement/
CONFIDENCE: high.

Later legal record (not load-bearing, but keep accurate): VW pleaded guilty
to three US felonies in 2017; individual engineers convicted. Do not state
that the board knew; do not state that it did not.

## Antitrust leniency

US DOJ Antitrust Division Corporate Leniency Policy, 10 Aug 1993 (original
1978). Source: https://www.justice.gov/atr/leniency-policy and Hammond 2002
status report. Key points: leniency automatic before an investigation exists;
first firm in gets it; "all officers, directors, and employees who cooperate
are protected from criminal prosecution". The 1978 version produced about one
application a year; after 1993, DOJ describes a roughly twenty-fold increase.
CONFIDENCE: high.

## Willison

Simon Willison, "Claude Fable is relentlessly proactive", 11 June 2026,
https://simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive
CONFIDENCE: high for title and existence; details of the post via secondary
summaries (HN thread, daily.dev) — cite only the title phrase.

## OpenAI postmortem (via contribution 01)

"The Hugging Face incident and the road ahead" — remediation: agents can ask
for clarification or stop safely. Used for one sentence; attributed. Do not
add detail beyond what 01 already sourced.
