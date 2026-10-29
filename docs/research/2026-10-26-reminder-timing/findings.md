# Reminder timing, and how to congratulate: what the evidence supports

Research date: 26 October 2026. Every page cited was read on that date. Figures from a vendor's
own marketing or self-reported platform data are marked **[vendor]**; peer-reviewed work is
marked **[peer-reviewed]**. Anything that could not be confirmed from a page actually read says
so.

The question this answers: is there existing research or a known system for deciding when to
remind a client to train and how to congratulate them, so that RepGarden's reminder engine is
clever without being noisy.

## The short answer

**Spaced repetition does not transfer.** SM-2, FSRS and Duolingo's half-life regression all
solve one problem: predict the moment a memory's recall probability falls to a target, and put a
review there. FSRS states it outright — stability is "the time in days required for
retrievability to decrease from 100% to 90%", and the interval is the inverse of that curve at
the chosen retention. A training reminder has no such quantity to target. There is no
retrievability of a squat session. The two systems also treat a miss in opposite ways: SM-2
resets a lapsed item to a one-day interval, whereas Lally's habit-formation data found that
missing a single opportunity did not materially affect the automaticity curve. No peer-reviewed
work applies SM-2, FSRS or half-life regression to habit or exercise reminders; what exists is a
handful of unevaluated hobby repositories. The nearest honest analogue in the literature is not
a forgetting curve at all but a **dosage variable** — HeartSteps V2 carries a treatment-burden
state that decays exponentially and rises by one each time a message is sent, and uses it to
suppress delivery. That is the idea worth borrowing, and it is a back-off rule, not a scheduler.

**One piece of it does transfer, in an unexpected place.** Duolingo's published notification
bandit penalises a message template by an exponentially decaying function of the days since that
template was last sent to that person — `0.017 x 0.5^(d/15)` — and the paper says it chose
exponential decay because such functions model human memory well, citing the same literature
spaced repetition rests on. The forgetting curve is applied to **the wording you last used**, so
the message stays fresh, and reusing the same template cost them 0.5% of reward. That is worth
copying. The scheduler is not.

**There is no "habit half-life" either.** Habit research measures self-reported automaticity
(the Self-Report Habit Index and its four-item automaticity subscale), which rises towards a
plateau rather than decaying from certainty, and the asymptotic curve fits only about half of
participants. The one serious attempt to model habit decay measured people deliberately
breaking unwanted habits, not wanted habits left to lapse.

**What does transfer, and what to build.** Three findings carry the design:

1. A reminder reliably produces a **short-lived proximal effect** and then habituates. HeartSteps:
   a walking suggestion more than doubled the next thirty minutes' step count at the start of the
   trial (+271 steps) and was undetectable by day 29, decaying about 3% a day. VALENTINE: +17% in
   the next hour for Fitbit users in the first 30 days, nothing after. So a reminder is worth
   sending for the session in front of the client, and is not worth sending as a general drumbeat.
2. The strongest single intervention in the largest gym-attendance experiment ever run was a
   **reward for coming back after a missed workout** (+27% weekly visits, n = 61,293). The
   missed-session nudge is not the weak feature; it is the important one, provided it offers a
   way back rather than a verdict.
3. **Frequency costs users causally.** In a randomised 17,500-user field experiment, each extra
   push per week raised the seven-week uninstall rate by 2.50 percentage points; two pushes a
   week produced 6.46% uninstalls against 1.37% with none. That is the budget the whole engine
   has to live inside.

The engine therefore wants to be a small, fixed rule set on four signals — the scheduled
session, the client's own reminder time, missed-session state, and the trainer's reply — with
hard caps, quiet hours, a back-off, and an explicit allowance of skips. No learning in the first
version. The place for a bandit later is the hour of day, and the way to earn the right to build
one is to randomly withhold a slice of reminders from the start so the data exists.

## The evidence, by theme

### A reminder moves the next hour, then stops working

The framework everyone in this area uses is the **just-in-time adaptive intervention** (JITAI).
Nahum-Shani and colleagues break an intervention into six parts — decision points, intervention
options, tailoring variables, decision rules, proximal outcomes and a distal outcome — and the
paper is blunt about the risk of over-delivery: "Providing support when the person is not
receptive will not be beneficial and may even have negative implications on engagement with the
intervention and intervention fatigue." Receptivity is defined as a transient ability and
willingness to receive support, a function of internal state and context. [peer-reviewed]

**HeartSteps** is the exercise case that put numbers on it. Thirty-seven participants, six
weeks, five decision points a day at times the participants chose themselves, randomised 0.4 no
suggestion / 0.3 walking suggestion / 0.3 anti-sedentary suggestion. A walking suggestion more
than doubled the average 30-minute step count at the start of the study, adding 271 steps
(p < .001); the effect declined about 3% a day and was undetectable by day 29. Averaged over the
whole trial it was a 24% increase (p = .02). The anti-sedentary suggestions had no detectable
effect on step count at all, despite participants saying in exit interviews that they enjoyed
them. [peer-reviewed]

**VALENTINE**, a six-month micro-randomised trial in cardiac rehabilitation (108 participants,
70,552 randomisations, about four decision points a day at a 0.25 send probability so that
roughly one message landed per day), found the same shape and more of it. Fitbit users: +17%
60-minute step count in days 1–30 (95% CI +7% to +28%), 0% in days 31–120, −5% after. Apple
Watch users: +10% early (ns), +6% late. The authors call for adaptive algorithms specifically
"to prevent habituation". [peer-reviewed]

**Bidargaddi's micro-randomised trial** in a mental-health app (1,255 eligible users, six send
slots a day, 89 days) is the only measured time-of-day result I found in a health app: a
tailored message made engagement in the next 24 hours 3.9% more likely overall (RR 1.039), and
the **12:30pm slot was the strongest at +8.8%**, rising to +11.8% at weekends against +7.4% on
weekdays. Note that 61.96% of the app's users had push disabled and were excluded. [peer-reviewed]

Design consequence: a reminder earns its place when it is attached to a specific thing to do
soon. Generic encouragement does not survive contact with a fourth week.

### Reminders do not build the habit, and may not help it at all

This is the finding most likely to be missed, and it changes what the engine is for. A
meta-regression of ten randomised trials of habit-formation interventions for physical activity
(2,349 participants) found an overall effect on automaticity of SMD 0.31 (95% CI 0.14–0.48), but
when the behaviour-change techniques were examined separately, **"prompts and cues" had a
slightly negative, non-significant coefficient** (crude β −0.05, adjusted β −0.16), and
**external or social reward was significantly harmful** (adjusted β −0.40). Problem solving was
the one significantly positive technique. [peer-reviewed]

**HabitWalk**, a micro-randomised trial that independently randomised push reminders and a
morning commitment task each day for 105 days, found **no independent effect of reminders on
habit formation**; only their interaction with the commitment task was positively associated
with habit strength. What predicted habit was cue–behaviour repetition (B = 0.16, 95% CI
0.08–0.23). [peer-reviewed]

The theory agrees. Wood and Neal's account of habit is a direct context-to-response association
learned by repetition in a stable context; once formed, the context triggers the behaviour
without a mediating goal. The implication is uncomfortable for a notifications feature: the
trigger is meant to migrate from the app to the client's own day, and **a reminder that keeps
firing is competing with the mechanism it is supposed to build**. [peer-reviewed]

So the honest framing for RepGarden: reminders get someone to today's session. The habit is
built by the session happening at a consistent time in a stable context, and the engine's job
includes getting out of the way.

### Planning when and where beats being reminded

Implementation intentions are the best-evidenced thing in this whole area, and they are free.
Milne, Orbell and Sheeran randomly allocated 248 UK undergraduates across three conditions for
two weeks: motivational material alone produced 35–38% exercising at least once a week, while
the group that wrote down **when and where** they would exercise reached **91%**. [peer-reviewed]

The gym megastudy built its baseline on the same idea. Milkman and colleagues ran 53
interventions on 61,293 members of 24 Hour Fitness across 46 US states over a four-week
intervention, measured on turnstile check-ins. The baseline arm — "planning, reminders and
microincentives" — asked people to **plan the dates and times they would exercise each week**,
texted them reminders at those scheduled times, and paid 300 points (about US$0.22) per visit.
That produced +0.14 weekly visits, a 9% increase over placebo (p = .006). Every one of the 24
arms that significantly beat placebo contained it. 45% of the 53 arms were significant, in a
range of +9% to +27%, and **no arm significantly reduced gym visits**. [peer-reviewed]

Two things follow. Reminders in the evidence base come bundled with a plan the person made
themselves; the engine should ask the client to confirm their week rather than silently assume
it. And asking is also what the autonomy literature supports: in a 2×2 experiment on 525 Dutch
adults, providing **choice** significantly improved how people rated a digital health
intervention (b = .12, p = .003) while the autonomy-supportive versus controlling **language**
manipulation had no significant effect on any outcome. Choice mattered; tone of voice did not,
at least in that study. [peer-reviewed]

### The hour: consistent, chosen by the client, not computed cleverly

Training at the same time of day is associated with more training and stronger automaticity.
Schumacher and colleagues followed 709 National Weight Control Registry members for a year,
classifying someone as temporally consistent if more than half their weekly sessions fell in one
window. Consistent exercisers reported significantly more MVPA days per week (F = 7.928,
p = .005; about 0.3 days a week more) and higher automaticity (F = 27.593), and baseline
automaticity predicted staying in the same time window a year later (OR 1.511, 95% CI
1.207–1.891). About 62% of early-morning exercisers were still early-morning exercisers a year
on. This is a cohort study, so the direction of causation is not settled. [peer-reviewed]

And the megastudy's randomised test of the same idea came up empty: **"Bonus for consistent
exercise schedule" ranked 27th of the 53 arms** and outperformed none of the others, sitting
alongside the planning-and-reminders baseline at 30th. "Bonus for variable exercise schedule"
ranked 43rd, and rewarding weekday and weekend consistency separately ranked 41st. Paying people
to train at a fixed hour added nothing. [peer-reviewed]

On whether to compute the hour, the clearest evidence says do not over-engineer it. A
three-arm trial of a stress-management app (77 participants, two weeks) compared sensor-timed
"intelligent" notifications (up to three a day, 08:00–22:00), one a day at a random time in a
17:00–20:00 window, and one every 72 hours. Daily beat occasional with a medium effect size, but
**sensor-based intelligent timing gave no advantage over simple daily, and that group had the
highest discontinuation — 60% against 39–42%**. [peer-reviewed]

Design consequence: learn the client's usual hour from their own logged sessions, propose it, and
let them own it. Do not keep moving it.

### A miss is the moment that matters, and a repair is what fixes it

The single best-performing arm in the megastudy was a **bonus of 125 points (US$0.09) for
returning to the gym after a missed workout**: +0.40 weekly visits, a 27% increase over placebo
(p < .001) and 16% over the planning-and-reminders baseline. Larger versions of the same
mechanic also made the top five. Milkman's reading is that it stopped one miss accumulating into
a run of them. Carry-over was real but modest: pooling all 53 arms, every extra visit during the
four weeks produced about 0.28 extra visits over the following ten weeks. [peer-reviewed]

Why a miss is dangerous is well described. Silverman and Barasch, across seven studies, found
that **intact logged streaks increase subsequent engagement relative to broken ones**,
independent of actual past behaviour, because people treat the logged streak as a goal in itself.
Two moderators matter here: the effect is **amplified when people blame themselves** for the
break and **attenuated when the streak can be repaired**. [peer-reviewed] The older construct is
the "what the hell effect" (Cochran and Tesser, 1996) — a small violation licensing a large one —
which is a lab and theoretical account rather than a field-measured effect size.

The best evidence for how to build the repair is Sharif and Shu's **emergency reserves**. In
their field study, 273 participants tracked steps for five weeks; a personal daily step goal was
set at 120% of their own baseline week, and they were assigned to reach it five days a week
(Easy), seven days a week (Hard), or seven days a week with two optional "emergency skips" per
week (Reserve-Weekly) or eight across the month (Reserve-Monthly). Days hitting the goal per
week: **Easy 3.11, Hard 2.83, Reserve-Weekly 4.00**. Probability of hitting the goal the day
after missing it: **Hard 0.37, Easy 0.44, Reserve-Weekly 0.55, Reserve-Monthly 0.48**. Critically,
the benefit appeared **only when the reserve was actually applied** — participants who failed and
did not use a skip persisted no better than the Hard group. A skip the client spends deliberately
is the mechanism; an automatic forgiveness is not. [peer-reviewed]

Timing of the restart has its own evidence. Dai, Milkman and Riis showed that temporal landmarks
open a fresh mental accounting period: gym attendance rose **33% at the start of a new week** and
47% at the start of a new semester. A Monday plan-your-week prompt is the cheapest nudge in this
whole note. [peer-reviewed]

### How much is too much

The causal number comes from a randomised retail field experiment, not a vendor deck. Wohllebe
and colleagues split 17,500 app users into five groups of 3,500 and sent 16 generic pushes over
seven weeks at different frequencies. **Each additional push per week raised the uninstall rate
by 2.50 percentage points** (β = .0250, p = .006). Uninstalls over the period: two a week
**6.46%**; one a week 5.09%; one a fortnight 3.17%; one a month 2.54%; **none 1.37%**. Direct
open rates fell with frequency in every treated group and **rose** in the untreated control
(14.29% → 15.35%); one extra weekly push cut the direct open rate by 12.67% relative to control.
[peer-reviewed]

The consumer-survey evidence agrees in direction. Airship's 2023 survey of 11,000 consumers
across ten countries found **"too many notifications or in-app messages" named by 18% as a
reason they deleted an app**, against 10% for notifications not being relevant — volume beats
irrelevance as the stated trigger. [vendor survey] Localytics' 2017 survey of 1,000 US
smartphone users reported that 10% would disable notifications for an app averaging one a week,
37% at two to five a week and 33% at six to ten, and that 22% would stop using an app sending two
to five a week. [vendor survey, read via contemporaneous reporting because the original post no
longer serves]

How much people already get, and how little they act on: a CHI 2014 analysis of 197.5 million
notifications from 40,191 users put the ten most popular apps at a mean of 44.9 notifications per
user per day, and found users had blacklisted 5.51% of notifying apps. A 2018 study of 794,525
notifications from 278 participants put the median at 56 a day, and measured the conversion to an
app open by type: messaging 63.67%, group messaging 65.81%, social 26.55%, **non-social app
16.19%**, email 15.47%. A fitness app's notification is a non-social app notification. About five
in six of them never lead to the app being opened. [peer-reviewed]

Two further points bound the design. Delivering notifications at detected task breakpoints rather
than at random reduced measured cognitive load by 46% in the lab and 33% in a 16-day field study
(Attelia) — the cost of a badly timed interruption is real and measurable. [peer-reviewed] And
the mechanism to copy from HeartSteps V2 is its explicit burden state: treatment burden evolves
as B(t+1) = λ·B(t) + 1{a message was sent}, a nightly-updated threshold captures the delayed cost
of sending at a given dosage level, and send probabilities are clipped so neither action is ever
certain. Strip the reinforcement learning away and what is left is: count recent sends, decay the
count, and refuse to send when it is high. [peer-reviewed]

Vendor benchmarks for health and fitness opt-in and open rates exist but should be treated as
soft. Airship's 2025 report (over 9 billion app users, thousands of apps, 2024 data) is quoted at
a median 54.98% iPhone / 58.48% Android opt-in and 4.25% / 6.6% direct open for Medical, Health
and Fitness, though those per-vertical figures are published as chart images and reached me via an
aggregator. OneSignal's 2024 benchmarks put Health and Fitness opt-in at 43.2% Android / 33.5%
iOS with no stated sample size or period. Braze's send-frequency guidance for the Health vertical
is **one push a month**, two to four total messages a month. Batch's 2025 benchmark (800 billion
messages, 10,000 apps, July 2024 to July 2025) reports overall opt-in of Android 67% (down from
85% after Android 13's runtime permission) and iOS 56%, with contextual triggered campaigns
opening at 14.4% against 4.19% for generic manual sends. All of these are **[vendor]**.

The widely repeated claim that fitness apps should send at 06:00–08:00 and 17:00–19:00 traces
only to vendor blogs with no stated dataset. The only measured health-app result points the other
way, to midday. Say so rather than inheriting the folklore.

### Congratulation: say it about the work, say it at once, and ration it

The most directly usable study here is Motz and colleagues' field experiment on **automated
praise**, n = 1,766 college students. On submitting an assignment, students received either a
push notification praising them for having submitted it, or one highlighting the value of
submitting work for academic success, or nothing. **Only the praise messages improved submission
rates and course performance.** 86.7% of the praise group had a submission rate above the 77%
threshold the authors identified, against 81.6% of controls and 81.4% of the value group
(χ² = 7.2, p = .007); mean submission rates were 1.2% higher. Two details matter more than the
effect size. First, praise was **capped at one per week** on a fixed-interval schedule,
deliberately, "to prevent students from receiving an excess of submission confirmation
notifications" — and it worked at that dose. Second, the paper is explicit that praise directed
at the **task** ("good work") behaves differently from praise directed at the **person** ("good
boy"), the latter risking perceived loss of autonomy. [peer-reviewed]

On whether to attach points or rewards to it, the caution is strong. Deci, Koestner and Ryan's
meta-analysis of 128 experiments found tangible rewards significantly undermined free-choice
intrinsic motivation: engagement-contingent d = −0.40, completion-contingent d = −0.36,
performance-contingent d = −0.28. **Verbal rewards tended to enhance intrinsic motivation.**
[peer-reviewed] The habit meta-regression above found external or social reward significantly
negative for automaticity. Together with the megastudy — where the micro-incentives were
pennies, bundled with planning, and the standout arm used them to buy a *return* rather than a
*streak* — the reading for RepGarden is: congratulate in words, keep the garden as a picture of
the work done, and do not pay per session.

Two supporting strands. Woolley and Fishbach show that **immediate** rewards such as enjoyment
predict persistence at long-term goals where delayed rewards do not — an argument for the
congratulation landing on the completed set, not in a weekly digest. [peer-reviewed] And Michie's
meta-regression of 122 evaluations of healthy-eating and physical-activity interventions
(N = 44,747, pooled d = 0.31) found **self-monitoring explained more heterogeneity than any other
technique (13%)**, and that self-monitoring combined with at least one other control-theory
technique — goal setting, feedback, review of goals — gave d = 0.42 against 0.26 for everything
else. Logging sets and seeing the record back is the active ingredient; the notification is the
wrapper. [peer-reviewed]

Fogg's Behavior Model is the useful vocabulary rather than the evidence: behaviour happens when
motivation, ability and a prompt converge, and when a behaviour does not happen at least one of
the three is missing. Tiny Habits adds the recipe "After I [anchor moment], I will [tiny
behaviour]. Then I celebrate", and Fogg's claim that the immediate positive emotion — he calls it
Shine — is what wires the habit in. That claim is a practitioner model; I found no controlled
trial of the celebration step itself, and the trial evidence for anchoring to an existing routine
is actually a null (see below). Use the anchor-and-celebrate shape, do not cite it as proven.

### The trainer's reply is the strongest thing the app can send

Mohr's **supportive accountability** model is the standard account: adherence to an eHealth
intervention is enhanced by human support, and the mechanism is accountability to a coach the
person sees as trustworthy, benevolent and expert, with process-oriented expectations the person
helped set and visible reciprocity. The effect is moderated by motivation — the more
intrinsically motivated need less. [peer-reviewed]

The quantitative side is mostly from digital mental health rather than training. Renfrew and
colleagues' review found guided interventions outperformed unguided across every outcome they
measured (stress g = 0.76 vs 0.27; depression 0.48 vs 0.23; anxiety 0.48 vs 0.26; burnout 0.69 vs
0.33), and guided formats roughly halve dropout. [peer-reviewed, but mental-health promotion, not
exercise] In exercise specifically, a 12-week randomised trial of 66 care-facility workers found
that **automated daily feedback showing the person their own activity** raised sessions from
2.2 ± 2.0 to 3.2 ± 2.0 a week (total video time 9.3 vs 6.3 hours, p = .044) — roughly 1.5 times
the adherence — with an alert email only after eight consecutive days of non-engagement.
[peer-reviewed] By contrast, a three-arm pilot trial of an automated **virtual coach** found no
difference in adherence against no support at all. [peer-reviewed] And in weight-loss coaching,
participants rated AI-generated messages as more formulaic, less authentic and too data-focused
than human ones. [peer-reviewed]

The reading for RepGarden: the one notification with a human behind it — the trainer's reply
pinned to a moment in the clip — is the one with the strongest claim on the client's attention
and the lowest risk of being experienced as noise. It should not be rationed alongside the
automated messages, and the trainer's reply latency is worth measuring as a product metric.

### What a spaced-repetition system actually optimises, for the record

- **SM-2** (Woźniak's own specification): interval grows multiplicatively by a per-item ease
  factor, `I(n) = I(n−1) × EF`, with EF adjusted by the recall grade and floored at 1.3; any
  failure restarts the item at a one-day interval. No explicit retention target.
- **FSRS**: a difficulty–stability–retrievability model. Stability is defined as the days for
  retrievability to fall from 100% to 90%; the forgetting curve from FSRS-4.5 on is
  `R(t,S) = (1 + (19/81)·t/S)^(−0.5)`; the next interval is `I = S · ln(r)/ln(0.9)` for the user's
  desired retention r, which is simply the curve inverted. Parameters are fitted per user to
  review history by log-loss.
- **Half-life regression** (Settles and Meeder, ACL 2016, Duolingo): predicts a per-item memory
  half-life `h = 2^(Θ·x)` from counts of times seen, correct and incorrect plus lexeme tags,
  fitted on 12.9 million student-word traces, and prioritises practice where predicted recall has
  decayed most. It cut mean absolute error against a Leitner baseline by at least 45% (0.128 vs
  0.235), and in a two-week A/B test on 3.3 million students the variant without lexeme features
  raised daily active use 12.0% (p < .001).

All three predict a probability of **remembering**. None predicts a probability of **turning up**,
and a training session has no analogue of a recall grade to feed back. The modelling idea worth
carrying across is the shape of the state, not the schedule: FSRS keeps a decaying per-item state
and acts on it; HeartSteps V2 keeps a decaying per-person burden state and acts on it. RepGarden
should keep the second.

For completeness on habit timing: the one causal test of whether a time-based cue or a
routine-based cue builds habit faster is a **null**. Keller and colleagues randomised 192 people
to plan a nutrition behaviour against either a clock time or an existing routine, measured daily
automaticity for 84 days, and found no difference between conditions (median 60 days to 95% of
asymptote versus 59). What predicted automaticity was repeated enactment of the plan, at both the
within- and between-person level. Only 27 of 117 protocol-adherent participants met the
definition of successful habit formation. The asymptotic curve was the best fit for just 38% of
participants; a quadratic fitted 56%. [peer-reviewed] The headline numbers people quote come from
Lally and colleagues (96 volunteers, a self-chosen daily behaviour for 12 weeks): median 66 days
to reach 95% of the automaticity asymptote, range 18–254 days. Keller's paper notes that the
asymptotic model fitted poorly for 43 of the 82 participants Lally modelled, so the 66 days is a
median of the well-fitting subset. A 2024 systematic review of 20 studies and 2,601 participants
puts medians at 59–66 days but **means at 106–154 days**, with an individual range of 4–335 days,
and a pooled pre-post habit-score improvement of SMD 0.69 (95% CI 0.49–0.88). [peer-reviewed]
Plan for months, not weeks, and do not promise a client a date.

## How the products do it

Two caveats before the detail. First, almost nothing in this category is documented in an
engineering post; **Duolingo is the exception, and it is the only product here that has published
its algorithm**. Everything else below comes from the company's own support documentation or
help centre, and is marked as such. Second, where I could only reach a third-party write-up I say
so and the claim should be treated as unverified.

### Duolingo — the one published algorithm, and it is not what you would guess

Yancey and Settles, "A Sleeping, Recovering Bandit Algorithm for Optimizing Recurring
Notifications", KDD 2020. This is a real engineering paper with offline and online results, and
three things in it matter for RepGarden.

**The arms are message templates, not send times.** Duolingo sends one daily practice reminder,
whose text is chosen from a pool of hand-written templates, some with eligibility conditions
(a streak template needs a three-day streak; a streak-wager template needs a wager). The bandit
picks the template. Hour of day is not an arm. The paper notes that adding user properties such
as region, device or age "would greatly multiply the number of arms, and thus the amount of data
needed to estimate arm scores", and leaves contextual bandits to future work — at 300 million
users. That is the clearest possible signal about what a one-trainer roster can support.

**The reward is deliberately narrow and short.** Reward is 1 if the user completes a lesson
**within two hours** of the reminder, 0 otherwise, chosen specifically "to minimize the amount of
organic activity counted in our reward function" — a lot of lessons happen whether or not a
notification is sent, and a wide window would drown the signal.

**The recency penalty is the only place a memory model actually appears.** Duolingo found a
novelty effect: fresh templates perform better. So the score of a template is reduced by
`γ · 0.5^(d/h)`, where `d` is the days since that template was last sent **to that user**, with
`γ = 0.017` and a decay **half-life `h` of 15 days**. The paper says plainly that exponential
decay was chosen because such functions "have been shown to model human memory well", citing the
same literature spaced repetition rests on. Reusing the same template, which an unpenalised bandit
would do, cost 0.5% of reward. So the answer to whether anything from spaced repetition transfers
is: **yes, one thing — a forgetting curve over the message you last sent, used to avoid repeating
yourself.** Not a scheduler.

Results: a two-week A/B test against a uniform-random baseline that had itself been tuned over
years gave +0.5% daily active users, +0.4% lessons completed, **+2.2% new-user D1 retention and
+2.0% new-user D7 retention** (all p < 0.05); existing-user D7 was +0.2% and not significant.
Five months after full launch, a permanent **5% uniform-random holdout** showed the bandit's
rounds earning 2.5% more reward. They kept the holdout. So should RepGarden.

On streaks, Duolingo's own help pages were not reachable (the article URLs now redirect to a help
hub). The mechanic as described by third parties: up to two streak freezes can be held, and one is
applied automatically when a day is missed. That is **not** the Sharif and Shu design — automatic
application removes the deliberate act that their data says carries the benefit. Treat the
specifics as unverified and the design point as contested.

### Freeletics — the closest working model for RepGarden

Freeletics' own blog describes Coach Day reminders: notifications sent only on the user's planned
Coach days, timezone-localised. "If you haven't completed your planned Coach training session
before 9 a.m., you'll get a 'morning motivation'", and "Come 6 p.m., and if you haven't had time
to train, you'll also receive an 'afternoon reminder'." Two per planned day at most,
**conditional on the session not being done**, and switchable off per type in the app. [company
blog]

This is the shape to copy: tied to the plan, suppressed by completion, capped at a small number,
and the user can turn it off. RepGarden should use one rather than two, because Freeletics is not
a trainer relationship and has no human reply competing for the same attention.

### Apple, Fitbit and Garmin — fixed thresholds, published, boringly simple

- **Apple Watch Activity** exposes five notification toggles: Stand Reminders, Daily Coaching,
  Goal Completions, Special Challenges and Activity Sharing. Stand reminders fire at **50 minutes
  past the hour** if the stand goal for that hour is not met; Daily Coaching sends encouragement
  when a user is close to a goal and can arrive at any time of day. The "You can still do it"
  evening nudge is the best-known example and has even been written about academically, but
  **I could not confirm Apple's own schedule for it in Apple's documentation** — the toggle names
  and the 50-minute rule come from support-community and third-party guides, not an Apple
  engineering page. [support docs and third-party, partly unverified]
- **Fitbit** reminders to move: the goal is **250 steps per hour**, the reminder appears
  **10 minutes before the hour** if the 250 steps are not done, defaults to **09:00–18:00 seven
  days a week**, and the hours are user-adjustable. [company help centre]
- **Garmin** move alert: "After one hour of inactivity, 'Move!' and the red bar appear. Additional
  segments appear after every 15 minutes of inactivity." It resets with a short walk of a couple
  of minutes. [company manual]

None of these learns anything. All three are a fixed threshold, a fixed offset within the hour, a
user-adjustable active window, and a reset condition. That is roughly the complexity RepGarden
should ship.

### The rest, briefly, from support documentation

- **Headspace**: the user sets meditation reminders themselves — a time and a frequency (daily,
  weekdays or weekends), with an option to block the time on their calendar. Nothing adaptive.
  [company help centre]
- **Noom**: daily lesson reminders whose time the user sets. [third-party reviews; Noom's own
  help pages were not reached]
- **Peloton**: reminders are opt-in per scheduled class — the user schedules a class and taps to
  get a reminder for it. [support pages and third-party guides]
- **WHOOP**: a Daily Outlook each morning and a Day in Review at night, plus Sleep Planner
  notifications recommending a bedtime. Fixed daily rhythm, content personalised from the day's
  data rather than the timing being learned. [company support and blog]
- **Strava**: notifications are social and event-driven — a follower's activity, a comment, a
  mention, a message, shoe mileage — with per-type toggles. I found no published evidence that
  Strava nudges inactive users to train, and no engineering post on notification timing.
  [company help centre]
- **Fitbod**: a weekly workout goal with streaks and previews, and rest-day guidance; the help
  centre documents notification settings but not a reminder schedule. [company help centre]

### The commercial "best time to send" services, and what they need

This is the honest answer to whether a learned send time is realistic in version one. All three
major services need a long history per person:

- **Airship Optimal Send Time**: app opens are localised to the user's time zone and aggregated
  to the hour over **the last 60 days** of activity; the best hour balances the individual's
  pattern against a model of the whole audience, and the model also outputs a **general best hour
  applied to dormant or low-activity users**. Delivery lands within a three-day window around the
  chosen date.
- **Braze Intelligent Timing**: clusters each user's past session times, push direct and
  influenced opens, email opens and clicks, and SMS clicks to find the largest cluster of
  engagement times. Campaigns must be **scheduled 24 hours in advance**.
- **OneSignal Intelligent Delivery**: a **rolling three-month** average of when each user is most
  active, drawn from activity across all apps using OneSignal.

Two takeaways. A new client has no history, so any sensible system needs the audience-level
fallback that Airship builds in — and for RepGarden the better fallback is not an audience average
but **the trainer's own knowledge and the client's own answer**. And Braze's published
recommendation for the Health vertical is one push a month, which is a useful reminder of how
conservative the people selling push software are about health apps.

**Braze's quiet hours** behaviour is worth noting because it is the opposite of what RepGarden
should do: Braze **holds** a message and delivers it when the window ends. For a session reminder
that is wrong — a prompt for a session that has already passed is worse than nothing — so
RepGarden should drop, not queue, with the trainer's reply as the single exception.

## The proposed engine

Designed to be built on what RepGarden already has — a programme assigned to calendar dates,
logged sets, a trainer reply pinned to a clip — with Expo Notifications and a Supabase scheduled
function. Nothing here learns anything in the first version.

### The four signals

| Signal | Where it comes from | Fixed or personalised |
|---|---|---|
| The scheduled session | The programme the trainer assigned to a date | Fixed by the trainer |
| The client's reminder time | One time per weekday, set by the client. Seeded by proposing the median start hour of their last five completed sessions, once five exist | Personalised, owned by the client |
| Missed-session state | Consecutive scheduled sessions with no log, and the skips remaining this month | Computed |
| The trainer's reply | An unread reply or approval on a clip | Event |

Nothing else. No location, no weather, no sensors, no activity recognition. The one trial that
compared sensor-timed notifications against a plain daily send found no advantage and higher
discontinuation (60% against 39–42%).

### The five messages

| # | Message | When | Cap | Evidence it rests on |
|---|---|---|---|---|
| 1 | **Today's session**, naming the work ("Back squats and pulls today") | On a scheduled day, at the client's set time | One per scheduled day | HeartSteps and VALENTINE: the proximal effect is real and attached to a specific session. Megastudy baseline: reminders at times the person planned |
| 2 | **Missed session**, offering the next date and the skip count | The morning after a missed scheduled session, once per missed session | One; never two days running | Megastudy's best arm (+27%) rewarded returning after a miss. Sharif and Shu: a spendable skip restores next-day persistence from 0.37 to 0.55 |
| 3 | **Done**, naming the work, not the person | Immediately on marking a workout complete, in-app always; as a push only if the app is backgrounded | One push per week | Motz: task-directed praise worked, capped at one a week by design; value-framed messages did not work. Woolley and Fishbach: immediate beats delayed |
| 4 | **Your trainer replied** | Immediately, held only for quiet hours | Uncapped | Mohr's supportive accountability; guided beats unguided; automated coaches do not |
| 5 | **Your week** — the sessions scheduled, with the times to confirm or move | Monday morning, once | One per week | Milne, Orbell and Sheeran: writing when and where took exercise from 35–38% to 91%. Dai, Milkman and Riis: gym attendance rises 33% at the start of a week |

### The rules

- **Caps.** At most one automated push a day, at most four a week. Message 4 and anything the
  client triggered do not count. The budget comes from Wohllebe: each extra weekly push cost 2.50
  percentage points of uninstalls over seven weeks, and four a week is already more than Braze
  recommends for the health vertical.
- **Quiet hours.** 21:30 to 07:30 local, client-adjustable. Automated messages due inside the
  window are **dropped, not queued** — a reminder for a session that has passed is worse than
  silence. Message 4 is held until the window opens.
- **Precedence** when two are due at once: 4, then 1, then 2, then 3, then 5. One push wins; the
  rest are dropped for that day, not deferred.
- **Back-off.** If three consecutive sends of one type are neither opened nor followed by a
  logged session, that type drops to once a week for two weeks and the app asks once, in-app,
  whether to move the time or switch it off. This is the HeartSteps V2 burden state made into a
  counter: count recent sends of a type, decay the count, refuse when it is high.
- **Dormancy.** After 14 days with no app open and no logged session, all automated pushes stop.
  The trainer's dashboard shows the client as not being reminded. Nothing resumes on a timer; it
  resumes when the client opens the app or logs a session, or when the trainer sends a reply.
  Precedent: the remote-training trial sent its only alert after eight consecutive days of
  non-engagement.
- **Skips.** Three skips a month, shown as a number. Missing a session spends one, and the client
  taps to spend it. When the skips run out the week simply shows the sessions done out of
  sessions planned. The benefit in Sharif and Shu appeared **only** when the reserve was actually
  applied, so the tap matters and silent forgiveness does not.
- **No consecutive-day streak.** Show sessions completed out of sessions planned this week, which
  resets on Monday. Silverman and Barasch found that a broken logged streak suppresses later
  engagement, amplified when the person blames themselves and attenuated when it can be repaired.
  A weekly ratio with skips is the repairable version.
- **What the client sets.** The reminder time per weekday, quiet hours, each message type on or
  off, and the skip tap. Granular per-type switches rather than one master toggle: PrefMiner found
  people accepted 56.98% of suggested per-app filtering rules, and roughly 70% accepted at least
  half, so the appetite for category-level control is real.
- **Do not repeat yourself.** Each message type draws from a small pool of hand-written
  wordings, and the one used most recently for that client is skipped. This is the single thing
  worth borrowing from the spaced-repetition family: Duolingo penalises a template by
  `0.017 x 0.5^(days since last used / 15)` because fresh wording works better, and found that
  reusing the same template cost 0.5% of reward. Three or four wordings per type and
  "not the last one" is enough; the decay curve is for when there are thousands of users.
- **Wording.** Name the work, not the app. Task-directed, not person-directed. No guilt, no
  all-caps, no emoji. The one trial that manipulated autonomy-supportive versus controlling
  language found no effect on any outcome while **offering a choice did** — so put the effort into
  the choices, and keep the tone plain because there is no reason not to.

### How it is built

One table of planned sends, one row per message with a deduplication key of client, type and
date, so the caps and the back-off are enforced in the database rather than in app code. A
Supabase scheduled function runs every fifteen minutes, picks up the rows now due, checks the
caps and the quiet window, and sends through Expo. **Send from the server, not from the device:**
iOS keeps only 64 pending local notifications per app, so a term's worth of sessions cannot be
pre-scheduled on the phone, and a session the trainer moves would still fire. Expo's push service
allows 600 notifications per second per project and 100 per request, which is far more headroom
than one trainer's roster needs.

### What is personalised and what is fixed

Personalised: the hour, the days, which types are on, quiet hours, the skip balance. All of it
visible and editable by the client.

Fixed for everyone in version one: the caps, the quiet-hour default, the back-off thresholds, the
precedence order, the number of skips, the wording templates. These are the parts a bandit could
eventually learn, and the parts that would be impossible to debug if they varied from day one.

### What to measure

- **Primary.** Proportion of scheduled sessions logged within 24 hours of the scheduled slot, per
  client, per week. This is the distal outcome; everything else is proximal.
- **Per message, proximal.** Session logged **within two hours** of a send — Duolingo chose
  that window deliberately to keep sessions that would have happened anyway out of the measure,
  and the same reasoning applies here. To make it interpretable, **withhold message 1 at random
  for 10–20% of eligible sessions from the first release, and keep the hold-out permanently**.
  That single decision turns the engine into a micro-randomised trial, which is what HeartSteps
  and VALENTINE needed to produce the numbers above, and it is what Duolingo kept running five
  months after launch (a 5% uniform holdout, which showed the bandit still earning 2.5% more
  reward). It is the only way to know whether the reminder is doing anything.
- **Decay.** The same proximal effect split by weeks since the client joined. HeartSteps lost its
  effect by day 29 and VALENTINE by day 30; if RepGarden's does the same, that is the signal to
  reduce the dose rather than rewrite the copy.
- **Harm.** Per-type mute rate, days to first mute, OS-level notification disable rate, push-token
  invalidation as a proxy for deletion. Non-social app notifications convert to an app open only
  16.19% of the time, so a low open rate is not itself a failure; a rising mute rate is.
- **Trainer side.** Median hours from clip upload to trainer reply, and sessions logged in the
  seven days after a reply compared with a week with no reply.
- **Skips.** How many are spent, and the proportion of clients who train the next scheduled day
  after spending one against after a miss with none left.

### Where a bandit or a JITAI could replace a rule later

- **The wording of each message.** This is where Duolingo actually put its bandit: arms are
  message templates, the reward is a session within two hours, and a recency penalty keeps it from
  repeating itself. It is the cheapest arm set to learn because the pool is small and the
  eligibility rules are already there. Start with "not the last one" and replace it with scores
  when there is enough traffic.
- **The hour for message 1.** HeartSteps V2 is the model: a contextual decision with send
  probabilities clipped so no arm is ever certain. The precondition is the random hold-out above
  plus enough clients to pool across. Duolingo, at 300 million users, declined to make user
  attributes into arms because of the data cost; one trainer's roster will not support a learned
  hour, and a learner would overfit one person's holiday. The commercial services need 60 days to
  three months of history per person and still fall back to an audience average.
- **Send or not for message 2.** A contextual bandit with the burden state as a feature, exactly
  as HeartSteps V2 does, replacing the fixed back-off counter.
- **Not the caps and not the quiet hours.** Those are the safety rails that keep the experiment
  from costing users, and the uninstall evidence says the cost is real.

Start with the rules. The hold-out is what buys the option on the rest.

## Sources

All read on 26 October 2026. Where a page would not serve and a figure came through a secondary
report or a search excerpt, that is stated.

### Reminder timing and adaptive intervention

- Nahum-Shani, I., Smith, S. N., Spring, B. J., et al. "Just-in-Time Adaptive Interventions
  (JITAIs) in Mobile Health: Key Components and Design Principles for Ongoing Health Behavior
  Support." *Annals of Behavioral Medicine* 52(6), 2018. https://pmc.ncbi.nlm.nih.gov/articles/PMC5364076/
- Nahum-Shani, I., and Murphy, S. A. "Just-in-Time Adaptive Interventions: Where Are We Now and
  What Is Next?" *Annual Review of Psychology*, 2026.
  https://www.annualreviews.org/content/journals/10.1146/annurev-psych-121024-044244 (abstract and
  search excerpts; full text not retrieved)
- Klasnja, P., Smith, S., Seewald, N. J., et al. "Efficacy of Contextually Tailored Suggestions for
  Physical Activity: A Micro-randomized Optimization Trial of HeartSteps." *Annals of Behavioral
  Medicine* 53(6), 2019, 573–582. https://academic.oup.com/abm/article/53/6/573/5094421
- Liao, P., Greenewald, K., Klasnja, P., and Murphy, S. "Personalized HeartSteps: A Reinforcement
  Learning Algorithm for Optimizing Physical Activity." *ACM IMWUT*, 2020.
  https://arxiv.org/abs/1909.03539 and https://pmc.ncbi.nlm.nih.gov/articles/PMC8439432/ (the
  burden-state and probability-clipping details came through search excerpts of the full text)
- Golbus, J. R., et al. "Text Messages to Promote Physical Activity in Patients With
  Cardiovascular Disease: A Micro-Randomized Trial of a Just-In-Time Adaptive Intervention"
  (VALENTINE). *Circulation: Cardiovascular Quality and Outcomes*, 2024.
  https://pmc.ncbi.nlm.nih.gov/articles/PMC11251861
- Bidargaddi, N., Almirall, D., Murphy, S., et al. "To Prompt or Not to Prompt? A Microrandomized
  Trial of Time-Varying Push Notifications to Increase Proximal Engagement With a Mobile Health
  App." *JMIR mHealth and uHealth* 6(11):e10123, 2018. https://pmc.ncbi.nlm.nih.gov/articles/PMC6293241/
- Morrison, L. G., et al. "The Effect of Timing and Frequency of Push Notifications on Usage of a
  Smartphone-Based Stress Management Intervention: An Exploratory Trial." *PLOS ONE*, 3 January
  2017. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0169162

### Planning, rewards and the gym evidence

- Milkman, K. L., Gromet, D., Ho, H., et al. "Megastudies improve the impact of applied
  behavioural science." *Nature* 600, 2021, 478–483.
  https://www.cmu.edu/dietrich/sds/docs/loewenstein/megastudies.pdf (author copy; the Nature page
  requires sign-in)
- Milne, S., Orbell, S., and Sheeran, P. "Combining motivational and volitional interventions to
  promote exercise participation: Protection motivation theory and implementation intentions."
  *British Journal of Health Psychology* 7, 2002, 163–184.
  https://www.semanticscholar.org/paper/e1211ade04288be89211d2c8a60a9494f9a41dcf (the 91% versus
  35–38% figures came through search excerpts; the full paper was not retrieved)
- Gollwitzer, P. M. "Implementation Intentions."
  https://cancercontrol.cancer.gov/sites/default/files/2020-06/goal_intent_attain.pdf
- Dai, H., Milkman, K. L., and Riis, J. "The Fresh Start Effect: Temporal Landmarks Motivate
  Aspirational Behavior." *Management Science* 60(10), 2014.
  https://faculty.wharton.upenn.edu/wp-content/uploads/2014/06/Dai_Fresh_Start_2014_Mgmt_Sci.pdf
- Milkman, K. L., Minson, J. A., and Volpp, K. G. M. "Holding the Hunger Games Hostage at the Gym:
  An Evaluation of Temptation Bundling." *Management Science* 60(2), 2014.
  https://faculty.wharton.upenn.edu/wp-content/uploads/2013/11/2013_Mgmt_Sci_2.pdf
- Kirgios, E. L., Mandel, G. H., Park, Y., Milkman, K. L., et al. "Teaching temptation bundling to
  boost exercise: A field experiment." *Organizational Behavior and Human Decision Processes*,
  2020. https://www.sciencedirect.com/science/article/pii/S074959782030385X
- Sharif, M. A., and Shu, S. B. "Nudging persistence after failure through emergency reserves."
  *Organizational Behavior and Human Decision Processes* 163, 2021, 17–29.
  https://anderson-review.ucla.edu/wp-content/uploads/2021/03/Sharif-Shu_EmergencyReserveFailure_OBHDP2019.pdf
- Silverman, J., and Barasch, A. "On or Off Track: How (Broken) Streaks Affect Consumer Decisions."
  *Journal of Consumer Research*, 2023.
  https://www.colorado.edu/business/faculty-research/2023/04/19/or-track-how-broken-streaks-affect-consumer-decisions
- Rogers, T., and Milkman, K. L. "Reminders Through Association." *Psychological Science* 27(7),
  2016, 973–986. https://scholar.harvard.edu/files/todd_rogers/files/rogers_milkman_rta.pdf

### Habit formation, cues and the consistent hour

- Lally, P., van Jaarsveld, C. H. M., Potts, H. W. W., and Wardle, J. "How are habits formed:
  Modelling habit formation in the real world." *European Journal of Social Psychology* 40(6),
  2010, 998–1009. https://onlinelibrary.wiley.com/doi/10.1002/ejsp.674 (paywalled; the figures
  here are as restated in Lally and Gardner 2013 and Keller et al. 2021)
- Lally, P., and Gardner, B. "Promoting habit formation." *Health Psychology Review* 7(sup1), 2013.
  https://www.cykelvaeksthuset.dk/media/az3linp0/promoting-habit-formation.pdf
- Keller, J., Kwasnicka, D., Klaiber, P., Sichert, L., Lally, P., and Fleig, L. "Habit formation
  following routine-based versus time-based cue planning: A randomized controlled trial."
  *British Journal of Health Psychology* 26(3), 2021, 807–824.
  https://bpspsychub.onlinelibrary.wiley.com/doi/10.1111/bjhp.12504
- Singh, B., Murphy, A., Maher, C., and Smith, A. E. "Time to Form a Habit: A Systematic Review and
  Meta-Analysis of Health Behaviour Habit Formation and Its Determinants." *Healthcare* 12(23),
  2024, 2488. https://www.mdpi.com/2227-9032/12/23/2488
- Ma, H., Wang, A., Pei, R., and Piao, M. "Effects of habit formation interventions on physical
  activity habit strength: meta-analysis and meta-regression." *International Journal of
  Behavioral Nutrition and Physical Activity* 20:109, 2023.
  https://pmc.ncbi.nlm.nih.gov/articles/PMC10498635/
- Baretta, D., Gillmann, L., Edgren, R., and Inauen, J. "HabitWalk: A micro-randomized trial to
  understand and promote habit formation in physical activity." *Applied Psychology: Health and
  Well-Being* 17(1), 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC11635918/
- Edgren, R., Baretta, D., and Inauen, J. "The temporal trajectories of habit decay in daily life."
  *Applied Psychology: Health and Well-Being* 17(1), 2025.
  https://pmc.ncbi.nlm.nih.gov/articles/PMC11635905/
- Schumacher, L. M., Thomas, J. G., Wing, R. R., Raynor, H. A., Rhodes, R. E., and Bond, D. S.
  "Sustaining regular exercise during weight loss maintenance: The role of consistent exercise
  timing." *Journal of Physical Activity and Health* 18(10), 2021, 1253–1260.
  https://pmc.ncbi.nlm.nih.gov/articles/PMC8764567/
- Wood, W., and Neal, D. T. "A new look at habits and the habit–goal interface." *Psychological
  Review* 114(4), 2007. https://dornsife.usc.edu/wendy-wood/wp-content/uploads/sites/183/2023/10/wood.neal_.2007psychrev_a_new_look_at_habits_and_the_interface_between_habits_and_goals.pdf
- Verplanken, B., and Orbell, S. "Reflections on past behavior: A self-report index of habit
  strength." *Journal of Applied Social Psychology* 33(6), 2003.
  https://repository.essex.ac.uk/12688/

### Spaced repetition

- Woźniak, P. "Application of a computer to improve the results obtained in working with the
  SuperMemo method" (the SM-2 specification). https://super-memory.com/english/ol/sm2.htm
- Open Spaced Repetition. "The Algorithm" (FSRS).
  https://github.com/open-spaced-repetition/awesome-fsrs/wiki/The-Algorithm and
  https://github.com/open-spaced-repetition/free-spaced-repetition-scheduler
- Settles, B., and Meeder, B. "A Trainable Spaced Repetition Model for Language Learning."
  *Proceedings of ACL 2016*, 1848–1858. https://research.duolingo.com/papers/settles.acl16.pdf
- Tabibian, B., et al. "Unbounded Human Learning: Optimal Scheduling for Spaced Repetition."
  https://arxiv.org/abs/1602.07032
- Zhang, C., et al. "Theory-based Habit Modeling for Enhancing Behavior Prediction."
  https://arxiv.org/abs/2101.01637 (preprint; the nearest thing to a habit-state estimator, and it
  schedules nothing)
- Tarantino, V., Ntoumanis, N., Neville, R., et al. "Effectiveness of booster strategies to promote
  physical activity maintenance: a systematic review and meta-analysis." *IJBNPA* 22:138, 2025.
  https://pmc.ncbi.nlm.nih.gov/articles/PMC12587685/ (the closest behaviour-change analogue to
  spacing: more boosters helped, the schedule was inconclusive)

### Notification volume, fatigue and benchmarks

- Wohllebe, A., Hübner, D.-S., Radtke, U., and Podruzsik, S. "Mobile apps in retail: Effect of push
  notification frequency on app user behavior." *Innovative Marketing* 17(2), 2021, 102–111.
  https://businessperspectives.org/images/pdf/applications/publishing/templates/article/assets/15070/IM_2021_02_Wohllebe.pdf
- Sahami Shirazi, A., Henze, N., Dingler, T., Pielot, M., Weber, D., and Schmidt, A. "Large-Scale
  Assessment of Mobile Notifications." *CHI 2014*.
  https://pielot.org/pubs/Sahami2014-CHI-NotificationsLarge.pdf
- Pielot, M., Church, K., and de Oliveira, R. "An In-Situ Study of Mobile Phone Notifications."
  *MobileHCI 2014*. https://pielot.org/pubs/Pielot2014-MobileHCI-Notifications.pdf
- Pielot, M., Vradi, A., and Park, S. "Dismissed! A Detailed Exploration of How Mobile Phone Users
  Handle Precipitous Notifications." *MobileHCI 2018*.
  https://www.interruptions.net/literature/Pielot-MobileHCI18.pdf
- Mehrotra, A., Hendley, R., and Musolesi, M. "PrefMiner: Mining User's Preferences for Intelligent
  Mobile Notification Management." *UbiComp 2016*.
  https://www.mircomusolesi.org/papers/ubicomp16.pdf
- Okoshi, T., et al. "Attelia" / "Reducing users' perceived mental effort due to interruptive
  notifications in multi-device mobile environments." *UbiComp 2015*.
  https://www.ht.sfc.keio.ac.jp/~slash/research/attelia/
- Freyne, J., et al. "Push Notifications in Diet Apps: Influencing Engagement Times and Tasks."
  *International Journal of Human–Computer Interaction* 33(10), 2017.
  https://www.tandfonline.com/doi/abs/10.1080/10447318.2017.1289725
- Airship. *2025 Mobile App Push Notification Benchmarks*. **[vendor]**
  https://growth.airship.com/rs/313-QPJ-195/images/Airship-2025-Push-Notification-Benchmarks-EN.pdf
- Airship. *2023 Mobile Consumer Survey* (11,000 consumers, ten countries, with Sapio Research).
  **[vendor survey]**
  https://growth.airship.com/rs/313-QPJ-195/images/Airship-2023-Mobile-Consumer-Survey-EN.pdf
- Airship. "How many push notifications should you send per month?" 2026 benchmarks. **[vendor]**
  https://www.airship.com/blog/how-many-push-notifications-should-you-send-per-month/
- Braze. "Send Frequency: What 'Just Right' Looks Like, Vertical by Vertical." 2020. **[vendor]**
  https://www.braze.com/resources/articles/send-frequency-what-just-right-looks-like-vertical-by-vertical
- OneSignal. *Mobile App Benchmarks of 2024*. **[vendor]**
  https://onesignal.com/mobile-app-benchmarks-2024
- Batch. *Benchmark notifications push & CRM mobile 2025*. **[vendor]**
  https://batch.com/ressources/etudes/benchmark-notifications-push-crm-mobile
- CleverTap. *300 Billion Push Notifications* report, 2019. **[vendor]**
  https://clevertap.com/blog/push-notification-report/
- Localytics push notification survey, 2018 (1,000 US smartphone users, fielded November 2017).
  **[vendor survey]** Original post no longer serves; figures read via
  https://www.emarketer.com/content/app-users-are-more-open-to-push-notifications-than-they-were-two-years-ago

### Congratulation, feedback and coach contact

- Motz, B. A., Canning, E. A., Green, D. J., Mallon, M. G., and Quick, J. D. "The Influence of
  Automated Praise on Behavior and Performance." *Technology, Mind, and Behavior*, 2021.
  https://doi.org/10.1037/tmb0000042 ; PDF read at
  https://s3.wp.wsu.edu/uploads/sites/2445/2021/08/Motz-et-al.-2021-TMB.pdf
- Deci, E. L., Koestner, R., and Ryan, R. M. "A Meta-Analytic Review of Experiments Examining the
  Effects of Extrinsic Rewards on Intrinsic Motivation." *Psychological Bulletin* 125(6), 1999,
  627–668. https://home.ubalt.edu/tmitch/642/articles%20syllabus/Deci%20Koestner%20Ryan%20meta%20IM%20psy%20bull%2099.pdf
- Woolley, K., and Fishbach, A. "Immediate Rewards Predict Adherence to Long-Term Goals."
  *Personality and Social Psychology Bulletin* 43(2), 2017, 151–162.
  https://kaitlinwoolley.com/wp-content/uploads/2017/08/woolleyfishbachpspb.pdf
- Michie, S., Abraham, C., Whittington, C., McAteer, J., and Gupta, S. "Effective techniques in
  healthy eating and physical activity interventions: A meta-regression." *Health Psychology*
  28(6), 2009. https://core.ac.uk/download/pdf/17050054.pdf
- Mohr, D. C., Cuijpers, P., and Lehman, K. "Supportive Accountability: A Model for Providing Human
  Support to Enhance Adherence to eHealth Interventions." *Journal of Medical Internet Research*
  13(1):e30, 2011. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3221353/
- Renfrew, M. E., Morton, D. P., Morton, J. K., and Przybylko, G. "The Influence of Human Support
  on the Effectiveness of Digital Mental Health Promotion Interventions for the General
  Population." *Frontiers in Psychology*, 2021.
  https://www.theliftproject.global/wp-content/uploads/The-Influence-of-Human-Support-on-the-Effectiveness-of-Digital-Me.pdf
  (effect sizes read via search excerpts of this paper; the PDF text layer would not extract)
- Suzuki, Y., Kawamoto, H., Matsuda, T., et al. "Evaluation of the Effectiveness of Feedback in a
  Remote Monitoring Home-Based Training System for Workers: A Medium-Scale Randomized
  Parallel-Group Controlled Trial." *Healthcare* 13(16), 2025, 2069.
  https://pmc.ncbi.nlm.nih.gov/articles/PMC12385635/
- Fogg, B. J. The Fogg Behavior Model. https://behaviormodel.org/ and *Tiny Habits*, 2019
  (anchor moment and celebration; a practitioner model, not a trial)
- Vandenbosch, J., et al. "Identifying the Most Autonomy-Supportive Message Frame in Digital Health
  Communication: A 2×2 Between-Subjects Experiment." *Journal of Medical Internet Research*, 2019.
  https://pmc.ncbi.nlm.nih.gov/articles/PMC6914245/

### Products, from their own documentation where possible

- Yancey, K. P., and Settles, B. "A Sleeping, Recovering Bandit Algorithm for Optimizing Recurring
  Notifications." *KDD '20*. https://research.duolingo.com/papers/yancey.kdd20.pdf ;
  replication data (200 million practice reminders over 35 days)
  https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/23ZWVI
- Freeletics. "Coach Day reminders to keep you on track." **[company blog]**
  https://www.freeletics.com/en/blog/posts/freeletics-coach-day-reminders/
- Fitbit. "What are the reminders on my Fitbit device?" **[company help centre]**
  https://help.fitbit.com/articles/en_US/Help_article/1878.htm
- Garmin. "Using the Move Alert", Venu 2 Series owner's manual. **[company manual]**
  https://www8.garmin.com/manuals/webhelp/GUID-D93137A9-B374-4A24-8A4D-A66C9AC91265/EN-US/GUID-55E4ED28-E438-4F65-A526-690F8FD5FF31.html
- Apple Watch Activity notification toggles and the 50-minutes-past-the-hour stand reminder.
  **[support community and third-party guides; not confirmed in Apple's own documentation]**
  https://www.imore.com/how-customize-notifications-activity-app-apple-watch and
  https://macreports.com/how-to-change-stand-goal-and-disable-time-to-stand-notifications/
- Headspace. "How can I set up Reminders?" **[company help centre]**
  https://help.headspace.com/hc/en-us/articles/115008276788-How-can-I-set-up-Reminders
- Strava. "Strava Notifications." **[company help centre]**
  https://support.strava.com/hc/en-us/articles/216918367-Strava-Notifications
- Fitbod. "Weekly Workout Goal, Previews & Streaks." **[company help centre]**
  https://fitbod.zendesk.com/hc/en-us/articles/360013245993-Weekly-Workout-Schedule-Previews
- WHOOP. Daily Outlook, Day in Review and Sleep Planner. **[company support and blog]**
  https://www.whoop.com/us/en/thelocker/new-ai-guidance-from-whoop/ and
  https://support.whoop.com/s/article/The-Haptic-Alarm-Dashboard
- Duolingo streak freeze mechanics. **[third-party only; Duolingo's own help article now redirects
  to its help hub, so the two-freeze limit and automatic application are unverified]**
  https://duolingo.deconstructoroffun.com/mechanics/streaks

### Learned send time, and quiet hours, as the platforms implement them

- Airship. "Optimal Send Time" (60 days of hourly app opens, audience fallback for low-activity
  users). **[vendor docs]**
  https://www.airship.com/docs/guides/features/intelligence-ai/predictive/optimal-send-time/ and
  https://www.airship.com/blog/our-machine-learning-model-for-predictive-send-time-optimization/
- Braze. "Intelligent Timing" (clusters past engagement; 24 hours' scheduling lead). **[vendor
  docs]** https://www.braze.com/docs/user_guide/brazeai/intelligence_suite/intelligent_timing
- Braze. "Quiet hours" (messages are held and delivered after the window, not dropped). **[vendor
  docs]** https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/quiet_hours
- OneSignal. "Intelligent Delivery" (rolling three-month activity average). **[vendor]**
  https://onesignal.com/blog/increase-open-rates-by-up-to-23-percent-with-intelligent-delivery/

### Platform constraints for the build

- Expo. "Sending notifications" (600 notifications per second per project, 100 per request).
  https://docs.expo.dev/push-notifications/sending-notifications/
- Expo. `expo-notifications` reference (daily, weekly, calendar and date triggers for locally
  scheduled notifications). https://docs.expo.dev/versions/latest/sdk/notifications/
- Apple Developer Forums on the 64-pending-local-notification limit per app, which rules out
  pre-scheduling a whole programme on the device. https://developer.apple.com/forums/thread/811171
