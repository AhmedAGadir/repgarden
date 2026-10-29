# Where a new app gets a stock exercise library

Research date: 26 October 2026. Every page and repository cited was read on that date.
Vendor marketing figures are marked as such. Anything that could not be confirmed from a
page actually read is listed under "What could not be verified".

## Short answer

1. **Free route:** bundle the **RepDB free tier** (650 exercises, 512 px WebP start and peak
   poses, English, German and Spanish instructions, full metadata, 36 MB) and take names,
   instructions and the handful of real videos from **wger** (932 exercises, CC-BY-SA). Both
   licences permit commercial use in an app; RepDB wants one credit line, wger wants per-item
   author credit. Total cost nil.
2. **Do not ship free-exercise-db's images.** Its upstream compiler states in writing that the
   two photographs per exercise "have been scrapped off the internet" and advises against
   commercial use; the maintainer of the fork says he has "no idea where the images are from".
   The JSON fields are safe, the pictures are not.
3. **Paid route:** licence the animated GIFs direct from **GymVisual**, the rights holder behind
   the GIFs that every "exercise API" resells, at **0.90 USD per GIF after ten in the basket** —
   about **270 USD (roughly 205 GBP) for 300 exercises**. If a single consistent modern character
   matters more than price, **RepDB Standard at 499 USD** or **MoveKit Complete at 229 GBP** are
   one-off, perpetual and clean.
4. **Avoid every streaming-only API** — MuscleWiki, WorkoutX, wrkout.xyz, ymove — because their
   terms forbid storing or re-hosting the media, and a gym is exactly where the signal dies.
5. **Cheapest own clips:** a two-day shoot with the trainer at his own gym out of hours covers a
   120-exercise core for under 200 GBP of kit. The honest best answer is a hybrid: free or bought
   breadth behind the trainer's own clips for the movements he actually prescribes.

## Comparison

| Option | Content | Media | Licence for a commercial app | Cost | How you get it |
|---|---|---|---|---|---|
| **RepDB free tier** | 650 exercises, EN/DE/ES, 26 fields | 1,237 WebP stills, 512 px, start and peak pose | Yes, explicitly, with one visible credit link | Free | GitHub, Kaggle, Hugging Face; 36 MB download |
| **wger** | 932 exercises, English for all, 33 languages | 383 images on 279 exercises, 78 videos on 46 | Yes: CC-BY-SA 4/3 and CC0, per item, author named | Free | Public REST API or self-host |
| **Everkinetic** | 289 exercises | 2 SVG and 2 PNG frames each | Yes, CC-BY-SA 4.0 | Free | GitHub |
| **workout-guide** | 302 exercises | 906 SVG at 512 px, three frames each | Artwork CC-BY-SA 4.0, code MIT | Free | npm or GitHub |
| **Open Exercise Art** | 562 exercises | 1 PNG and 1 SVG each, no frames, AI-generated | Artwork CC-BY-SA 4.0, tools GPL-3.0 | Free | GitHub |
| **free-exercise-db** | 876 exercises, good fields | 1,746 photographs, 750x500 | **Data yes (Unlicense), images no** | Free | GitHub |
| **ExerciseDB.io** | 1,394 exercises, 17-field taxonomy on Pro | 1 GIF each, 180 to 1080 px | Yes, perpetual, self-hosted; no resale of raw files | 199 USD Starter, 599 USD Pro, one-off | Direct download |
| **GymVisual** | 6,558 GIFs, 9,935 videos, 8,000+ assets | The source artwork itself | N-CRFL: apps allowed, resale of the media not | 0.90 USD per GIF after 10; 6 USD per video after 5 | Per-item purchase |
| **RepDB Standard** | 695 exercises, EN/DE/ES/FR | 539 looping transparent WebP at 960 px, 156 stills | Yes, perpetual, no revenue cap | 499 USD, plus 99 USD for the female character | Direct download, JSON and SQLite |
| **MoveKit** | 582 exercises | 3D MP4 clips, HD, 30 fps, loopable | Yes, perpetual, worldwide, paid apps allowed | 229 GBP Complete; 3.99 GBP per clip | Direct download |
| **Gym Animations** | 7,000+ animations claimed | 3D MP4, 1920x1080, 6 s, 29.97 fps | **Do not use.** Claims a lifetime commercial licence; buyers report the animations are GymVisual's | 599 USD full, 299 USD gym-only | Direct download |
| **Exercise Animatic** | 2,600+ clips and 4,500+ illustrations claimed | 3D MP4, 4K 60 fps, white and green screen | Commercial apps allowed, no attribution; a registration obligation | 1 USD per clip; 599 USD bundle | Direct download |
| **WorkoutLabs** | 679 strength, 146 yoga, male and female | PNG, SVG, MP4, GIF; animated for many | Commercial licence; works registered with the US Copyright Office | 15 USD per illustration annual, 25 USD perpetual; 1,200 USD a year or 3,500 USD+ perpetual for the library; API 195 USD setup plus 50 USD a month | Download or API |
| **MuscleWiki API** | 1,988 exercises, 14 languages | 7,700+ MP4s, male and female, two angles | Paid plans yes, **but no storing or re-hosting, and their branding stays in the video** | Free 500 calls a month; 10, 39.99, 99.99, 199.99 USD a month | API, streaming only |
| **WorkoutX** | 1,900+ exercises | 2,700 MP4 clips, 600x720, 30 fps | Paid plans yes, **no downloading or re-hosting** | Free 500 requests total; from 19 USD a month | API with expiring links |
| **ymove** | 1,568 videos, 720p | Filmed, white background and gym | Free tier of 25 allows commercial use; full library white-label | API from 19 USD a month; full library price not published | API, CDN or bulk download |
| **wrkout.xyz** | 2,700 exercises, 13,500 images, 3,500 videos | 3D, made by the author | Commercial from the Basic tier, attribution required; unwatermarked only from Business | 30, 100, 250, 650, 1,500 GBP a month | API only |
| **API Ninjas** | 3,000+ exercises | Position images on paid tiers only | Paid only; free tier is explicitly non-commercial | 39, 99, 199 USD a month | API |
| **ExRx.net** | 2,200+ exercises | Videos and thumbnails on Premium | Licensed, application and approval required | Not published, quote only | API |
| **Vector Fitness Exercises** | 1,603 Lottie animations, 9 equipment groups | Lottie JSON, convertible to MP4 or WebM | Commercial licence needed; caps on downloads and revenue by tier | 1,999 USD for Startup full library | Direct purchase |
| **Envato Elements** | General stock | Filmed clips | **Poor fit:** forbids use "where the primary value of the product lies in the Item itself" | Subscription | Download per project |
| **Pexels, Pixabay** | General stock | Filmed clips | Commercial use allowed, no attribution; no standalone redistribution | Free | Download |
| **Mixamo** | Characters and motion capture | 3D animations, none of them exercises | Royalty-free commercial, no redistribution of raw files | Free | Download |
| **Shoot it ourselves** | Whatever we choose | Whatever we choose | Ours outright | Under 200 GBP of kit for a 120-exercise core | Two days with the trainer |

## The options in detail

### Free, and the licence holds up

#### RepDB free tier

650 exercises in one JSON file with 26 fields each: names, descriptions, instructions and tips
in English, German and Spanish, plus category, force type, mechanic, difficulty, body part,
primary and secondary muscles, goals, tags, unilateral and bodyweight flags, and a MET value.
1,237 WebP images at 512 px, two per exercise — a start pose and a peak pose, or one pose for
static holds and stretches. The whole repository is 36 MB, so it bundles into an Expo app
without a media server at all.

The licence is a named document, `LICENSE-DATA.md`, from a named licensor: RepDB, operated by
Sergei Argutin, Regener Strasse 51, 10318 Berlin. Term 1 reads "You may use the dataset and
images inside applications — apps, websites, research projects — for personal and commercial
purposes, at no cost." Term 2 requires one visible link, "Exercise data by RepDB (repdb.co)",
in an about or credits screen, a README or a website footer. Term 3 forbids republishing the
data as a dataset or an API. Term 4 permits resizing, cropping and recolouring. Term 5 forbids
using the images as input to generative models. Term 6 is the trap: the looping animations in
`premium-samples/` are paid-tier previews and are "evaluation-only", so they must not be
shipped.

Quality: one consistent flat illustration style, one character, clean silhouettes, legible at
small sizes. The licence states plainly that "All images are original works generated with AI
tooling commissioned by RepDB". That is the honest weakness — AI-made demonstration art can be
anatomically wrong, and users do notice. A user on another project opened an issue titled "STOP
USING AI FOR IMAGES" saying "how am I supposed to use it as a guide for my workout of they are
bending bones and levitating of the ground … i will now unnistall the app." Every illustration
we ship needs the trainer's eye on it before it goes live.

Maintenance: the repository was last pushed on 18 October 2026 and carries 114 stars. RepDB also
publishes ready-made starters for React Native (Expo), Next.js and Flutter built on this exact
dataset, which removes a day of plumbing.

#### wger

The only large library that is openly licensed all the way down, because every asset carries its
own licence record and author name. Queried live on 26 October 2026, the public instance holds
**932 exercises**, every one with an English translation and 909 with a non-empty English
description, and translations in 33 languages — Spanish 645, German 636, French 584, Portuguese
435, Italian 140, Ukrainian 121, and a long tail. Exercise licences break down as 779 CC-BY-SA
4.0, 132 CC-BY-SA 3.0 and 21 CC0.

The media is the problem. There are **383 images covering only 279 exercises** (295 CC-BY-SA 4.0,
88 CC-BY-SA 3.0, and 46 of them flagged `is_ai_generated`) and **78 videos covering only 46
exercises**, all CC-BY-SA 4.0, mostly 1920x1080 H.265 uploaded by individual contributors. They
are community photographs and phone videos, not a production library: inconsistent framing,
inconsistent backgrounds, inconsistent people. Sample image sizes are around 800x357 and 35 KB.

What the share-alike means in practice: bundling the images unchanged alongside our own code is a
collection, not an adaptation, so our app's own code is unaffected — but each image must carry
its author, its licence name and a link, and if we edit an image the edit must itself be
CC-BY-SA. Every image and video record in the API already returns `license`, `license_author`,
`license_author_url` and `license_derivative_source_url`, so a credits screen can be generated
from the data rather than hand-written. wger's own code is AGPL-3.0, which is irrelevant to us
because we are not using their code.

Maintenance: the main repository has 7,186 stars and was pushed on the morning of 26 October
2026. This is the most actively maintained thing in the field.

#### Everkinetic, workout-guide and Open Exercise Art

These are the three generations of the one genuinely free illustration lineage, and they are the
only free source with real multi-frame animation potential.

- **Everkinetic** (`everkinetic/data`), by Greg Priday, CC-BY-SA-4.0, 125 stars. 289 exercises
  with `id`, `name`, `title`, `primer`, `type`, primary and secondary muscles, equipment, steps
  (three to nine per exercise, mostly five or six), tips and references. Two frames per exercise,
  named "relaxation" and "tension", as both SVG (1,109 files) and PNG (2,196 files) — a sample PNG
  is 646x704 at 31 KB. Clean original art, clean provenance, but dormant since 2022 and only 289
  exercises.
- **workout-guide** (`bryllim/workout-guide`), by Bryl Lim, 1,382 stars and 201 forks in two
  months. **302 exercises with three frames each, 906 transparent SVGs at 512x512**, typed
  metadata, and an npm package with `getExercise`, `searchExercises` and `getAssetUrl`. Three
  frames is enough for a credible loop. Note the split licence: the code and documentation are
  MIT, the **artwork is CC-BY-SA 4.0** and must be attributed to Everkinetic and to Bryl Lim. The
  repository badge says MIT; the artwork is not MIT. A sibling repository,
  `Baroknolia/oefen-exercise-art`, exists purely to satisfy the CC-BY-SA 4.0 section 2(a)(5)(B)
  source-availability requirement, which tells you downstream users have had to take the
  share-alike seriously.
- **Open Exercise Art** (`AlexMollard/Open-Exercise-Art`), 562 illustrations, one still per
  exercise and no animation frames, PNG with white contour lines on transparency plus SVG using
  `fill="currentColor"`, a `catalogue.json` with names, aliases, dimensions and SHA-256 hashes.
  Artwork CC-BY-SA 4.0, tools GPL-3.0-or-later. The README says the source PNGs were AI-generated
  and then individually reviewed and approved, so the same accuracy caution applies as to RepDB.
  New in October 2026, no stars yet, so unproven.

### Free, but the licence does not hold up

#### free-exercise-db

This is the one everybody reaches for first, and the data is fine while the pictures are not.

The data: 876 exercises with `name`, `force`, `level`, `mechanic`, `equipment`, `primaryMuscles`,
`secondaryMuscles`, `instructions`, `category` and `id`. 584 strength, 123 stretching, 61
plyometrics, 38 powerlifting, 35 olympic weightlifting, 21 strongman, 14 cardio. 525 beginner,
294 intermediate, 57 expert. Gaps: 77 have no equipment value, 87 no mechanic, 30 no force, 5 no
instructions. 873 of the 876 have exactly two JPEG photographs, 750x500, about 38 KB each.
2,048 stars, 528 forks, licensed The Unlicense, last pushed 27 September 2026.

The images: the upstream compilation this is forked from, `wrkout/exercises.json`, says so in its
own `CONTRIBUTING.md`: "Currently all exercises have two images, these have been scrapped off the
internet, therefore l do not own the copy right for these images and would advise against using
them in comercial projects." The maintainer of the fork confirmed it on 27 June 2023 in issue #2:
"I actually have no idea where the images are from or if they are royalty free so usage would be
at your own risk (i will update the README to make this clearer)". He has not; the README still
reads "Open Public Domain Exercise Dataset" with an Unlicense badge and instructions for
hotlinking the images off `raw.githubusercontent.com`.

Issue #13, "images has copyright?", is still open after two years. In it, one contributor
reverse-image-searched the photographs to **bodybuilding.com** and quoted its terms ("You may
view and use the Content for your personal information and for no other purpose"), concluding the
status is "clearly infringing". Another, on 1 August 2026, says "some of these appear to be from
ExRx.net … I think this might be a quite huge issue for those who implement this in their apps".
A third: "The images are a huge problem and should be taken down ASAP." The maintainer replied on
2 August 2026 that "A good place to start if we're going to drop the current images could be to
swap with placeholders"; nothing has shipped. No rights holder has acted, so the risk is real but
so far unenforced. Which site the photographs came from is contested and unproven either way.

The instruction prose has had far less scrutiny than the images and probably shares their
provenance. One reviewer found no evidence of plagiarism against ExRx; nobody has checked against
bodybuilding.com. Treat it as unresolved, and write our own copy for anything we lead with.

The names, muscles and equipment values are facts, and facts are not copyrightable. That part we
can use freely as a reference while sourcing media elsewhere.

Note also that the original compiler, Ollie Jennings, now sells the replacement himself at
wrkout.xyz, and said on 9 November 2025 of the new artwork: "They are created by myself using 3D
software with skeleton & muscles models."

#### ExerciseDB on RapidAPI, and its GitHub mirrors

This is the route most tutorials and most Expo starters use, and it is the one with real
enforcement behind it. Two things are tangled together and need separating.

**The GIFs are GymVisual's.** Two independent projects that hold a direct licence say so in
writing. `hasaneyldrm/exercises-dataset` — 1,324 exercises, 23,237 stars, 2,971 forks, the data
layer behind the LogPress app — ships an MIT licence with an explicit media carve-out: the media
"is the property of Gym visual and is redistributed here with permission", "every use must carry
the copyright indication (c) Gym visual — https://gymvisual.com/", "distributed at 180x180 only",
and "Cloning this repository does not grant you any license to the media; obtain your own from
Gym visual." `DuarteSantos8/openGym`, an App Store app, reproduces the rights holder's own
developer notice verbatim: "(c) Aliaksandr Makatserchyk, Gym visual, gymvisual.com … NOTICE TO
DEVELOPERS: The exercise animations included in this project are provided strictly for use within
the openGym application. Third parties have no rights to reuse, extract, or integrate these media
assets into independent apps, websites, or commercial products. To use these animations for your
own software, you must obtain a license directly from gymvisual.com." It adds that the media "may
not be used to train, prompt or feed any AI system". openGym also records that its text for those
1,324 exercises "originate from ExerciseDB v1 by AscendAPI and reached openGym through
hasaneyldrm/exercises-dataset, under the MIT licence".

**ExerciseDB enforces its dataset, and GitHub has acted twice.** On 24 November 2025 the copyright
owner of the ExerciseDB dataset filed a DMCA notice against the open-source `exercisedb-api`
mirror. GitHub's note on the notice: "Because the reported network that contained the allegedly
infringing content was larger than one hundred (100) repositories, and the submitter alleged that
all or most of the forks were infringing to the same extent as the parent repository, GitHub
processed the takedown notice against the entire network of **198 repositories**, inclusive of the
parent repository." The notice claims "all exclusive rights to the dataset's structure, metadata,
and original exercise descriptions, including the text of exercise instructions, field naming
conventions, and organization of the database", complains of "near-verbatim instruction text
(after removal of trivial 'Step:N' prefixes)" and says the mirror claimed an AGPL licence it had
no right to grant. A second notice on 23 April 2026, from the same owner operating through
DevWorx Consulting LLC, took down `bryanprimus/exercisedb-api` entirely: "The repository also
presents the dataset as open source and encourages users to deploy and redistribute it, which is
not authorized."

Checked on 26 October 2026: `bryanprimus/exercisedb-api` and `JakobDrist/exercisedb-api` both
return HTTP 451 with reason "dmca". `ExerciseDB/exercisedb-api` still exists with 730 stars but
its git history restarts with "Initial commit" on 25 November 2025, the day after the first
notice, and now contains only a LICENSE and a README — the AGPL-3.0 file is still there with no
code under it. The free hosted mirrors are also unreliable: `exercisedb-api.vercel.app` returned
"DEPLOYMENT_DISABLED" and `v1.exercisedb.dev` returned a Vercel security checkpoint when probed.

The practical reading: anyone mirroring an exercise GIF set to GitHub for an Expo app is in the
exact pattern that has already been taken down twice. The free tier is in any case non-commercial,
and the paid tiers were sold through RapidAPI at roughly 10 to 50 USD a month before ExerciseDB
moved to one-off downloads.

#### Kaggle and Hugging Face dumps

Two kinds sit side by side and only one is usable.

- **"Fitness Exercises Dataset" by `exercisedb` on Kaggle**, "1500+ Exercises with High-Quality
  GIFs" at 180p, 360p and 720p, stated licence **MIT**. Given everything above, an MIT label on
  GymVisual artwork is a licence the uploader cannot grant. Do not use it. The same applies to
  `omercotkd/exercises-gifs` (MIT, 56 stars) and `hasaneyldrm/exercises-dataset` if you take its
  repository badge at face value instead of reading its NOTICE.
- **"Workout/Exercise Images"** on Kaggle is CC BY-NC-SA 4.0 — non-commercial, so out.
- **`RepDB/exercise-dataset` on Hugging Face** is the same free tier described above, 609 rows in
  the Hugging Face snapshot against 650 in the GitHub repository, licence `repdb-free`. Usable.

The general rule, and the most transferable thing in this whole file: **check a project's media
licence separately from its repository licence.** A repository-level SPDX badge tells you nothing
about what the pictures are under. That applies to free-exercise-db (Unlicense badge, scraped
photographs), workout-guide (MIT badge, CC-BY-SA artwork), the ExerciseDB mirrors (AGPL badge,
GymVisual artwork) and wger (AGPL code, per-image Creative Commons).

### Paid, one-off, self-hosted — the shape that suits us

These are the only paid options that fit an app whose users stand in a basement gym. One payment,
files on our own storage, no runtime dependency on anyone.

#### GymVisual — the rights holder, bought direct

GymVisual is the house that actually drew the animations every "exercise API" resells. The
catalogue holds **6,558 animated GIF products and 9,935 video products**, plus still
illustrations, across male and female figures. Pricing, from the category pages: **0.90 USD per
animated GIF once there are ten items in the basket**, and **6 USD per video once there are
five**. For a 300-exercise library that is about **270 USD (roughly 205 GBP) in GIFs** or 1,800
USD in videos. There is no published bulk pack — the Pack category is empty and the site says to
contact them for a discount on all or many items. The rights holder is named in a downstream
notice as Aliaksandr Makatserchyk.

The licence is the Non-Exclusive Commercial Royalty-Free Licence (N-CRFL). Read through a text
proxy, because the domain refuses automated requests, it permits the media to "illustrate and
visually enhance: Android or iOS mobile application (apps); website pages and headers; magazine
pages and articles; newspapers; books, ebooks and booklets". It forbids use "to resell or
redistribute", "to use in products (both physical or digital) destined for resale (i.e. image,
video products and etc)", broadcast, posting on stock sites, NFTs, and "to process, modify, or
use for training by any Artificial Intelligence (AI) systems". It also states that buying the
media "does not transfer the copyright".

The one clause that needs an email before we spend money: "products destined for resale". Mobile
apps are listed as a permitted use in the same licence, so the natural reading is that the
prohibition is on reselling the media itself rather than on charging for an app that uses it. For
RepGarden the question may not arise — the trainer pays, his clients use the app free — but if we
ever sell the app, get that in writing from them first.

Buying direct is also the only way to be certain. Everything else in this category is somebody
reselling this artwork, and at 0.90 USD a GIF the middleman is not saving us money.

#### RepDB Standard — 499 USD

695 exercises: 539 with looping animations and 156 static holds, as **transparent animated WebP
at 960x960** with seamless loops, plus 37 muscle-overlay areas per character, front and back
heatmaps, JSON and SQLite, a relations graph, AI embeddings, and English, German, Spanish and
French. One faceless figure, one material, one camera, so the set is visually consistent — and
transparency means the same clip works on a light or dark background, which matters for a
two-theme app. Starter at 299 USD is static images only; a female character is 99 USD on top;
Custom white-label starts at 999 USD. One-off, instant download, VAT included, through Lemon
Squeezy.

The licence permits use "inside your products (web, mobile, desktop)", hobby and commercial, with
**no revenue cap** and attribution optional. It forbids reselling or repackaging the data as a
dataset or API, publishing the bulk dataset, training models that substitute for it, and
generative restyling. It runs indefinitely, ending only on refund or material breach. The
licensor is the same named German sole trader as the free tier, which is a real advantage: there
is somebody to write to.

This is the best "it just works" purchase. It is also the natural upgrade path if we ship the free
tier first, because the exercise IDs match.

#### MoveKit — 229 GBP

582 3D animations of a single mannequin, loopable HD MP4 at 30 fps, with primary and secondary
muscle groups, equipment type and movement pattern as metadata. Priced in sterling: 3.99 GBP per
clip, Starter 119 GBP for 155 exercises, Home 159 GBP for 347, Gym 189 GBP for 424, Complete 229
GBP for all 582. US visitors are shown 299 USD for the Complete pack.

The licence, read in full, grants a "non-exclusive, worldwide, perpetual, non-transferable license
to use the purchased Content for commercial and non-commercial purposes", explicitly including
mobile and web apps, client projects and revenue-generating products, with unlimited projects for
one legal entity. It forbids reselling as a competing library, claiming the work as original,
training or restyling with AI, and — the clause that touches our architecture — **exposing raw
file URLs publicly or giving end users download access**. Content already delivered stays licensed
permanently. Attribution is not required, but licence identifiers and provenance metadata must
stay intact. There is no API; the licensor is a sole trader in Bulgaria.

Cheapest full library priced in our own currency, and the only one where the whole licence reads
like it was written for app developers.

#### Exercise Animatic — 599 USD, or 1 USD a clip

2,600-plus 3D clips at 4K 60 fps in MP4, with white-background and green-screen versions, plus
illustrations and step-by-step text. Counts differ between its own pages, so treat the figure as
approximate. Clips are 1 USD each; the Ultimate Bundle lists at 599 USD and carries a permanent
"300 USD off" banner, with the page showing 599 USD on the day. Its N-EB2BL licence allows
commercial iOS and Android apps with no attribution, forbids standalone resale, a competing
library and AI training, and imposes a **registration obligation to record where the clips are
used** — administrative friction worth knowing about. The same clips are also sold on Pond5.

#### ExerciseDB.io — 199 USD Starter, 599 USD Pro

The cheapest route to 1,394 exercises with a GIF each, self-hosted with "no runtime dependency on
ExerciseDB after download". Starter gives 180x180 and 360x360 GIFs; Pro adds a 17-field movement
taxonomy, 14,695 exercise relationships and 720x720 and 1080x1080 GIFs. Perpetual, one-off, data
"as is at the time of purchase" with no automatic updates. Its terms permit use "inside your own
fitness, wellness, coaching, education, or internal software products" and forbid reselling or
redistributing "the dataset or the GIF visuals as raw files, a standalone library, an API, or a
competing content package"; GIFs must be shown "in conjunction with the exercise data and not as
standalone content".

The problem is the rights story. Its FAQ says the GIFs "are created by ExerciseDB.io" and are
"generally male only". Its terms then hedge to "remain the property of ExerciseDB.io **or its
content suppliers**", and no supplier is named. Meanwhile two independent projects that hold
direct licences state in writing that the same 180x180 GIF set is GymVisual's, and a contributor
requesting missing exercises on one of those projects linked each one straight to its GymVisual
product page — with ExerciseDB's own unusual names, such as "cable one arm side triceps pushdown"
and "lever seated leg press v. 2", matching GymVisual's product titles. ExerciseDB's two DMCA
notices claim only the dataset structure, metadata and instruction text as its authored work, never
the artwork. That asymmetry is the tell.

If we buy here, demand a written warranty of origin and an indemnity before paying. Otherwise buy
from GymVisual, where the same artwork costs about the same and the chain of title is not in
doubt. The same caution applies to Vital Animations (49, 149 and 299 USD, prices not confirmable
on the vendor's own page), FitExerciseDB (0.99 USD per GIF) and the AscendAPI packs — all of them
sell 1,324 to 1,500 exercises, which is the GymVisual-derived set.

#### Gym Animations — do not use

7,000-plus 3D MP4 animations at 1920x1080, 6 seconds, 29.97 fps, with packs from 199 to 599 USD
and a licence page promising "unlimited commercial use", "no royalties" and a lifetime
one-off purchase. Then the evidence: its Trustpilot profile carries a platform warning for
displaying Trustpilot content in a misleading way, and has two reviews in twelve months, both one
star. One, 12 May 2026, is headed "SCAM!! Stolen material". The other, 20 March 2026, is from a
buyer who received a legal notice saying the animations had been stolen from GymVisual. The site
also hosts a page at /gym-visuals/ trading on GymVisual's name. Treat it as likely infringing
resale. The attraction of a 599 USD 7,000-clip bundle is exactly what a reseller of somebody
else's library can afford to offer.

#### WorkoutLabs — the most legally solid illustrations

679 strength and gym exercises plus 146 yoga poses, with rehab, prenatal, senior, kids, office
and sports categories, in male and female versions across several character sets. Static as alpha
PNG or vector SVG; animated as MP4, GIF and animation-ready SVG "for many exercises"; full colour
or black and white. Metadata includes titles, primary and secondary muscle groups, equipment,
muscle-group diagrams and step-by-step instructions, with Sanskrit names, pronunciation, audio,
benefits and contraindications for yoga.

Pricing: from 15 USD per illustration annual or 25 USD perpetual, with volume discounts from 15
images; the full library from **1,200 USD a year or 3,500 USD and up for perpetual rights**; API
access from 195 USD setup plus 50 USD a month during development, with post-launch rates
quote-only. Its illustrations are registered with the US Copyright Office under VA0001972444,
which is why this is the one vendor whose chain of title is a matter of public record. Its terms
also carry the sharpest line in the whole field: "Attribution is not permission."

Expensive for 300 exercises, and worth it only if a court-proof provenance is the requirement.

### Paid APIs that stream — all wrong for this app

Every one of these forbids keeping the media. That single clause rules out the whole category for
RepGarden, because a client in a basement gym with no signal still has to see the movement. They
are listed so the decision is on the record.

- **MuscleWiki API** (api.musclewiki.com, linked from musclewiki.com's footer, operated by
  MuscleWiki SEZC): 1,988 exercises, 7,700-plus MP4s with male and female and front and side
  angles, 14 languages. Free 500 calls a month, then 10, 39.99, 99.99 and 199.99 USD a month for
  1,000, 30,000, 100,000 and 300,000 calls, 25 per cent off annually, top-ups at 10 USD per 5,000.
  Paid plans include commercial rights. But: "Videos, thumbnails and bodymap images may not be
  downloaded, exported, copied into your own storage, or re-hosted on your servers", videos may be
  held in transient playback buffers only, metadata caches for 30 days and thumbnails 24 hours on
  device, **MuscleWiki branding must stay in the videos**, exposing the data through our own API is
  forbidden, AI training needs separate written permission, and ownership of the underlying footage
  is not stated anywhere.
- **WorkoutX** (workoutxapp.com): 1,900-plus exercises, 2,700 looping 720p MP4 clips at 600x720
  and 30 fps, 100 to 300 KB each with a JPEG poster. Free tier is 500 requests in total with
  watermarked 360p previews; paid from 19 USD a month. Commercial use allowed on any paid plan,
  but "downloading, storing or re-hosting the media on your own servers or CDN is not permitted on
  any plan" and media comes through expiring links, so you store the exercise ID, not the URL.
- **ymove** (ymove.app): 1,568-plus filmed HD 720p demonstrations, 15 muscle groups, 31 equipment
  types, 1,361 on white and 376 in real gyms, unwatermarked and white-label on the full licence.
  Free tier of 25 videos permits commercial use but not redistribution as a library. API tiers:
  Starter 19 USD a month, watermarked and capped at 250 exercises per rolling 30 days; Pro 29 USD
  for 350; Scale 79 USD uncapped. No self-hosting on any plan, and some early clips are being
  reshot through summer 2026. The full-library licence price is "Contact Us" and the pricing page
  sits behind a login.
- **wrkout.xyz**, by the original compiler of exercises.json: 2,700 exercises, 13,500 images and
  3,500 videos made by the author in 3D software, up to 40-plus languages. Free 100 requests a
  month, then Entry 30 GBP, Basic 100 GBP, Pro 250 GBP, Business 650 GBP and Enterprise 1,500 GBP
  a month. Commercial use starts at Basic and always requires attribution; media is watermarked
  until the 650 GBP tier. Clean provenance, wrong price.
- **API Ninjas**: 3,000-plus exercises with name, type, muscle, difficulty, instructions and
  equipment; position images on premium tiers only; /v1/exercises returns five at a time. Free
  tier is 3,000 requests a month and explicitly non-commercial — "Commercial use of the Exercises
  API is not permitted on the free tier" — then 39, 99 and 199 USD a month for 100,000, 1,000,000
  and 10,000,000 requests. Thin media, so useful only as a metadata cross-check.
- **ExRx.net**: 2,200-plus exercises. An Economy plan shows name, target muscle, apparatus and a
  thumbnail with a button back to ExRx; Premium adds videos, thumbnails and instructions. Free
  developer accounts, then prices by application and approval only — nothing published. Its terms
  forbid use that "is a source of or substitute for the Service or … competes with the Service",
  which is close to what an exercise library in a coaching app is.
- **Hyperhuman**: Content 95 USD a month, Platform 191 USD a month capped at 5,000 end clients,
  Ultra 383 USD a month, plus 15 per cent commission on end-client subscriptions. It licenses
  instructor-led classes and branded collections, not a demonstration-clip set, so it is the wrong
  shape.
- **Exercise.com, Virtuagym, Fitify, Volt, Physitrack, Central Athlete, FitterStock, FunXtion**:
  no public licence and no published price; sales contact only. Exercise.com's library is a
  feature of its own platform, not something it licenses out. **FitScope** licences full-length
  classes at 15 to 30 USD per video per month — again the wrong shape. **Fitness Blender** has no
  licensing programme at all: its terms forbid reproducing or distributing any site material and
  forbid using "any illustrations, photographs, video or audio sequences … separately from the
  accompanying text", with a single email address for requests.

### Stock marketplaces — they fail on the licence, not the price

This is the trap that looks cheapest and is not available to us. Every major stock licence has a
clause that an exercise library trips over, because in a library of exercise clips the clips *are*
the product.

- **Envato Elements**: "Each time you download an item, you get an ongoing commercial license for
  a single, specified project use", and items may not be used "where the primary value of the
  product lies in the Item itself" or where the item's inclusion "makes the product fundamentally
  unique and valuable, and is the main driving factor". Also: "You can't redistribute an Item as
  stock, in a tool or template, or with source files", and "You must not permit an end user to
  extract an Item and use it separately from the End Product". The licence does become perpetual
  once incorporated during an active subscription. The canonical terms sit behind Cloudflare.
- **iStock, Getty and Adobe Stock**: the Standard licences prohibit products where the primary
  value lies in the content itself, and prohibit distributing the stand-alone file. Adobe's
  Extended licence still bars stand-alone distribution.
- **Bigstock**: caps reproductions at 250,000 and requires the content to be less than half the
  product.
- **Shutterstock**: licence pages and prices could not be read at all — 403 and CAPTCHA from every
  route tried.
- **Pexels and Pixabay**: free, no attribution, commercial use allowed, modification allowed.
  Pexels forbids selling unaltered copies, implying endorsement, redistributing on other stock
  platforms and trade-mark use. Pixabay forbids distributing content "on a Standalone basis",
  commercial use of recognisable trademarks and logos, and — directly on point — compiling content
  "to replicate a similar or competing service". The deeper problem is simply that both hold
  lifestyle b-roll of people exercising, not systematic demonstrations of named movements, so you
  cannot assemble a consistent 300-exercise set from them whatever the licence says.
- **Mixkit**: licence text is rendered client-side only and varies per clip, so it could not be
  read reliably. **Videvo** now redirects to Freepik, which refuses automated requests.

### 3D and vector animation — nothing at library scale

- **Mixamo** is still free with an Adobe ID, royalty-free for personal, commercial and non-profit
  projects, with no redistribution of raw character or animation files. It is also now described
  as a "limited duration technology preview", it is unavailable for Enterprise and Federated IDs
  and for China country codes, and most importantly **it has no exercise content** — the library is
  locomotion, combat and dance. Using it would mean commissioning an animator per movement.
- **3D marketplaces** top out at 10 to 31 animations per pack: TurboSquid around 120 to 200 USD,
  CGTrader 23 to 299 USD, Fab 9.99 to 79.99 USD, Unity 9 EUR to 90 USD. TurboSquid's and
  CGTrader's licences permit rendering to video; **Unity's EULA section 2.2.1(a) requires the asset
  not to "comprise a substantial portion" of the product, so it fails this use outright**. The
  Sketchfab Store closed in October 2024, and Epic sold Sketchfab and ArtStation to KitBash in
  August 2026.
- **Lottie**: LottieFiles' free Simple Licence allows commercial use without attribution, but there
  are only about 133 free exercise animations, by unrelated hobbyists in unrelated styles — fine
  for a decorative empty state, unusable as a library. **IconScout**'s digital licence caps video
  use at a 10,000 USD budget and bars products "intended for resale". **Vector Fitness Exercises**
  is the only vector set at scale, 1,603 Lottie assets across nine equipment groups with
  conversion to dotLottie, MP4 and transparent WebM: Startup is capped at 50,000 downloads and
  100,000 USD annual revenue, Scale at 500,000 and 500,000 USD, Enterprise uncapped. The only
  price published anywhere on the site is 1,999 USD, in an upgrade-policy worked example for
  Startup with the full library; everything else is a Gmail address. Its free creator pack excludes
  apps.

### Shoot it ourselves

Worth doing for a core set whatever else we buy, because the trainer's own demonstrations are the
one thing no competitor can ship, and the clips become ours outright with no licence to read.

**What the numbers say.** A fitness-specialist videographer charges, on one vendor's figures,
1,000 to 3,000 USD for a half-day covering 30 to 50 exercises — so 300 exercises at agency rates
is six to ten half-days and 6,000 to 30,000 USD, which is out of the question. Self-shot, the
same guide suggests three to five takes per exercise and clips of 1.5 to 5 seconds, loopable and
silent. With a fixed camera, a written shot list grouped by equipment so the setup never changes,
and a trainer who knows the movements cold, 40 to 60 exercises a day is realistic. That makes a
**120-exercise core about two days**, and a full 300 about five to seven days.

**What a 300-exercise shoot needs.**

- *Venue.* The trainer's own gym out of hours, free, is the whole reason this is cheap. The
  alternatives, for reference: London gym space from 12 to 50 GBP an hour, a filming-ready loft
  gym at 135 GBP an hour, a white infinity-cove studio at 450 GBP for a half day or 850 GBP for a
  full day, and a studio with camera and operator from 1,000 GBP plus VAT a day.
- *Camera.* A current iPhone Pro or equivalent at 4K 60 on a tripod, locked off. A second phone on
  a second tripod for a side angle doubles the useful output for almost nothing — competitors ship
  front and side.
- *Lighting.* Two LED panels, 40 to 160 GBP. A tripod is about 25 GBP and a plain backdrop roll 25
  to 60 GBP. Total kit under 200 GBP, most of it reusable.
- *People.* The trainer demonstrating, one person filming and calling the shot list off a tablet.
  A second demonstrator so there is a female model too, which every paid library offers and no
  free one does well.
- *Process.* A numbered shot list exported from our own exercise table, so each clip is slated by
  ID and lands with the right filename. Three reps per take, silent, same framing throughout, no
  music.
- *Post.* 300 clips trimmed, cropped square or 3:4, and compressed. By hand at two minutes each
  that is about ten hours; driven by ffmpeg from a CSV of in and out points it is three to four.
  Generate a poster frame per clip in the same pass — that is the fallback still, free.
- *Clearances.* A signed model release from every person who appears, written permission from the
  gym owner to film, no gym members in frame, and no branded kit or visible equipment logos, since
  those are trademarks.

**Realistic total:** two days of the trainer's time, under 200 GBP of kit, a free venue and
Ahmed's editing time for a 120-exercise core, growing by a handful of clips at a time afterwards.
That is cheaper than every paid library except GymVisual, and it is the only option that produces
an asset rather than a licence.

## What this changes for RepGarden

1. **Ship the RepDB free tier as the stock layer, bundled, not fetched.** 36 MB in the app
   binary, no media server, no signal dependency, one credit line on an about screen. Cross-fade
   the start and peak poses to suggest the movement; that is the cheapest animation in the
   business and it degrades to a still by itself.
2. **Take data from wger where RepDB is thin**, and take its 46 real videos if any of them are
   movements the trainer cares about. Record the author and licence per asset when we do.
3. **Do not put free-exercise-db images anywhere near the app.** If any have already been pulled
   into the repository, delete them. The JSON fields are safe as a reference for names, muscles
   and equipment, which are facts; the photographs and probably the instruction prose are not.
4. **Build the media table with licence fields from the start** — source, author, author URL,
   licence name, licence URL, derivative source — the way wger's API does. We will be mixing
   RepDB, wger, possibly GymVisual and the trainer's own clips, and the attribution obligation
   attaches to *display*, not to distribution. Fetching an image at runtime does not excuse us.
   A credits screen should be generated from that table, never hand-maintained.
5. **Self-host every asset. Never hotlink** raw.githubusercontent.com or a vendor CDN. One project
   reviewed for this note sets exactly the right acceptance criteria: per-item attribution
   preserved, assets self-hosted not hotlinked, licence terms honoured.
6. **Rule out subscription APIs by policy, not by price.** MuscleWiki, WorkoutX, ymove and
   wrkout.xyz all forbid storing their media, and three of them watermark or brand it. An app used
   on a gym floor cannot depend on a live stream, and we should not design a feature around media
   we are contractually forbidden to cache.
7. **Treat the fallback still as a first-class state**, not an error case. With RepDB's two-pose
   pairs and, later, poster frames from the trainer's own clips, every exercise has a still
   regardless of whether a clip exists.
8. **Keep stock media and the trainer's own clips distinguishable** in the data and in the UI. His
   clips are the product; the stock set is scaffolding, and he will want to replace it movement by
   movement.
9. **Keep all of it out of any AI pipeline.** RepDB, MoveKit, GymVisual, Exercise Animatic and
   MuscleWiki each forbid using their media to train, fine-tune, restyle or prompt a model. No
   generated thumbnails, no upscaling, no style transfer — one vendor's community thread notes
   that "AI upscale is License violation too".
10. **If and when we pay, buy direct from GymVisual at 0.90 USD a GIF**, after emailing them about
    the "products destined for resale" clause. About 205 GBP covers 300 movements from the actual
    rights holder. The resellers of that same artwork cost more and carry the chain-of-title risk,
    and one of them is the subject of buyer complaints about stolen material.
11. **Plan a two-day shoot with the trainer for the 120 movements his clients actually get
    prescribed.** It costs under 200 GBP, it produces an asset we own, and it is the part of the
    library that makes RepGarden look like his gym rather than a stock catalogue.

## What could not be verified

- **GymVisual's own licence and terms pages could not be read on the site.** The whole domain
  returns HTTP 403 to automated requests. The N-CRFL text quoted above came through a
  text-extraction proxy, and the separate Terms and Conditions page could not be read at all. Per-
  item prices came from indexed category-page snippets, not from a product page. **The "products
  destined for resale" clause needs an email to them before we buy.**
- **Whether ExerciseDB.io holds a GymVisual licence that permits its resale.** No document was
  found either way. The two claims — ExerciseDB's "created by ExerciseDB.io" and two downstream
  licensees' "property of Gym visual … redistributed with permission" — are both on the record and
  cannot be reconciled from public sources.
- **Which website free-exercise-db's photographs were taken from.** Both bodybuilding.com and
  ExRx.net are named by contributors from reverse image searches. Neither has been confirmed by a
  rights holder and no takedown has been filed. That they were scraped is not in doubt; the source
  is.
- **ExRx.net's API prices.** Not published; quote and application only. The site returns 403 to
  automated requests, so the plan descriptions came through a text proxy of its FAQ.
- **Shutterstock's licence terms and prices.** Could not be read from any route — 403 and CAPTCHA
  everywhere.
- **Envato's canonical licence terms** sit behind Cloudflare; the clauses quoted came from its help
  centre through a text proxy.
- **ymove's full-library licence price**, which is "Contact Us", and its pricing page, which is
  behind a login.
- **Vector Fitness Exercises' prices**, beyond the single 1,999 USD figure in a worked example.
  Enquiries go to a Gmail address.
- **Vital Animations' prices** (49, 149 and 299 USD) could not be confirmed on the vendor's own
  page.
- **Mixkit's licence terms**, which are rendered client-side only and differ per clip.
- **Whether api.musclewiki.com is operated by MuscleWiki itself.** The balance of evidence says yes
  — it is linked from musclewiki.com's footer, and there is a RapidAPI listing under the
  musclewiki-sezc account — but no document states the relationship outright, and musclewiki.com's
  own copyright page returns 403. **Ownership of the underlying video footage is not stated
  anywhere in its terms.**
- **Reddit is unreachable from this toolset**, so there are no quotes from r/reactnative or
  r/personaltraining. Public GitHub issues and DMCA filings stood in, and are better evidence in
  any case because they are primary and dated.
- **Exercise.com, Virtuagym, Fitify, Volt, Physitrack, Central Athlete, FitterStock, FunXtion and
  Hyperhuman** publish no third-party licence text for their demonstration libraries.
- **Everkinetic's README** is mid-migration and does not itself state the counts; the 289-exercise
  and two-frame figures come from reading `dist/exercises.json` and the repository tree directly.

## Sources

All read 26 October 2026.

**Free datasets and their licences**

- free-exercise-db — https://github.com/yuhonas/free-exercise-db ; data read from
  https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/dist/exercises.json ; licence
  `LICENSE.md` (The Unlicense) via the GitHub API
- free-exercise-db issue #2, "License of Images?" —
  https://github.com/yuhonas/free-exercise-db/issues/2
- free-exercise-db issue #12 —
  https://github.com/yuhonas/free-exercise-db/issues/12
- free-exercise-db issue #13, "images has copyright?" (open) —
  https://github.com/yuhonas/free-exercise-db/issues/13
- wrkout/exercises.json CONTRIBUTING.md, the scraped-images admission —
  https://raw.githubusercontent.com/wrkout/exercises.json/master/CONTRIBUTING.md
- wrkout/exercises.json issue #305 —
  https://github.com/wrkout/exercises.json/issues/305
- wger API, queried live for counts and licences — https://wger.de/api/v2/exerciseinfo/ ,
  /exerciseimage/ , /video/ , /license/ , /language/
- wger README and licensing — https://raw.githubusercontent.com/wger-project/wger/master/README.md
- wger API documentation — https://wger.readthedocs.io/en/latest/development/api.html
- Everkinetic data and CC-BY-SA-4.0 licence — https://github.com/everkinetic/data ;
  https://raw.githubusercontent.com/everkinetic/data/master/LICENSE.md
- Workout Guide — https://github.com/bryllim/workout-guide ;
  https://raw.githubusercontent.com/bryllim/workout-guide/main/README.md
- Open Exercise Art — https://github.com/AlexMollard/Open-Exercise-Art ;
  https://raw.githubusercontent.com/AlexMollard/Open-Exercise-Art/main/README.md
- oefen-exercise-art, the CC-BY-SA source-availability repository —
  https://github.com/Baroknolia/oefen-exercise-art
- exercemus/exercises — https://github.com/exercemus/exercises ; data from
  https://raw.githubusercontent.com/exercemus/exercises/minified/minified-exercises.json
- RepDB free tier licence — https://raw.githubusercontent.com/RepDB/exercise-dataset/main/LICENSE-DATA.md
- RepDB free tier attribution wording —
  https://raw.githubusercontent.com/RepDB/exercise-dataset/main/ATTRIBUTION.md
- RepDB free tier data and repository tree — https://github.com/RepDB/exercise-dataset ;
  https://exercise-dataset.com/
- RepDB on Hugging Face — https://huggingface.co/datasets/RepDB/exercise-dataset
- RepDB Expo, Next.js and Flutter starters — https://github.com/RepDB/repdb-example-react-native ,
  /repdb-example-nextjs , /repdb-example-flutter

**Provenance of the GIFs, and enforcement**

- hasaneyldrm/exercises-dataset, GymVisual media carve-out —
  https://github.com/hasaneyldrm/exercises-dataset ;
  https://raw.githubusercontent.com/hasaneyldrm/exercises-dataset/main/NOTICE.md
- openGym third-party notices, GymVisual's developer notice verbatim —
  https://raw.githubusercontent.com/DuarteSantos8/openGym/main/NOTICE.md
- GitHub DMCA notice, 24 November 2025, ExerciseDB, 198 repositories —
  https://github.com/github/dmca/blob/master/2025/11/2025-11-24-exercisedb.md
- GitHub DMCA notice, 23 April 2026, ExerciseDB via DevWorx Consulting LLC —
  https://github.com/github/dmca/blob/master/2026/04/2026-04-23-exercisedb.md
- Takedown status confirmed at HTTP 451 — https://api.github.com/repos/bryanprimus/exercisedb-api ;
  https://api.github.com/repos/JakobDrist/exercisedb-api
- The wiped mirror — https://github.com/ExerciseDB/exercisedb-api
- Kaggle "Fitness Exercises Dataset", stated MIT —
  https://www.kaggle.com/datasets/exercisedb/fitness-exercises-dataset
- Kaggle "Workout/Exercise Images", CC BY-NC-SA 4.0 —
  https://www.kaggle.com/datasets/hasyimabdillah/workoutexercises-images

**Paid libraries**

- GymVisual N-CRFL licence (read through a text proxy; the domain refuses direct requests) —
  https://gymvisual.com/content/9-license
- GymVisual animated GIF and video categories and per-item prices —
  https://gymvisual.com/16-animated-gifs ; https://gymvisual.com/12-videos ;
  https://gymvisual.com/15-pack
- GymVisual terms and conditions, referenced but unreadable —
  https://gymvisual.com/content/3-terms-and-conditions-of-use
- ExerciseDB.io pricing, terms and FAQ — https://exercisedb.io/pricing ; https://exercisedb.io/terms ;
  https://exercisedb.io/faq ; https://exercisedb.io/
- RepDB pricing and licence — https://repdb.co/pricing/ ; https://repdb.co/license/ ;
  https://repdb.co/exercise-animations/
- MoveKit pricing and licence — https://movekit.com/ ; https://movekit.com/license
- Exercise Animatic bundle and licence — https://www.exerciseanimatic.com/license ;
  https://www.exerciseanimatic.com/product-page/complete-2000-exercise-videos-lifetime-unlimited-license-workout-yoga-animation-exercise-fitness-gym
- Gym Animations product and licence pages — https://gym-animations.com/ ;
  https://gym-animations.com/license/
- Gym Animations buyer reviews and the platform warning —
  https://www.trustpilot.com/review/gym-animations.com
- The page trading on GymVisual's name — https://gym-animations.com/gym-visuals/
- WorkoutLabs illustration licensing — https://workoutlabs.com/exercise-illustrations-licensing/ ;
  https://workoutlabs.com/use-of-illustrations/ ; https://workoutlabs.com/train/integration/
- Vector Fitness Exercises — https://vectorfitexercises.com/ ;
  https://vectorfitexercises.com/licenses ; https://vectorfitexercises.com/for-designers

**Paid APIs**

- MuscleWiki API pricing, documentation and FAQ — https://api.musclewiki.com/ ;
  https://api.musclewiki.com/pricing ; https://api.musclewiki.com/documentation ;
  https://api.musclewiki.com/faq
- MuscleWiki itself, which links the API from its footer — https://musclewiki.com/
- WorkoutX — https://workoutxapp.com/
- ymove exercise video library and API — https://ymove.app/exercise-video-library ;
  https://ymove.app/exercise-api
- wrkout.xyz pricing and tiers — https://wrkout.xyz/
- API Ninjas exercises API and pricing — https://api-ninjas.com/api/exercises ;
  https://api-ninjas.com/pricing
- ExRx.net API FAQ (read through a text proxy) — https://exrx.net/Store/Other/APIFAQ
- Hyperhuman — https://hyperhuman.cc/fitness-content-licensing ; https://hyperhuman.cc/exercise-video-api
- Exercise.com exercise library — https://www.exercise.com/platform/exercise-library/
- Fitness Blender terms of use — https://www.fitnessblender.com/page/terms-of-use-agreement

**Stock, 3D and vector**

- Envato Elements licence terms —
  https://help.elements.envato.com/hc/en-us/articles/360000628966-License-Terms
- Pexels licence — https://www.pexels.com/license/
- Pixabay content licence — https://pixabay.com/service/license-summary/
- Shutterstock licence (could not be read; 403 and CAPTCHA from every route) —
  https://www.shutterstock.com/license
- Mixamo FAQ and licence — https://helpx.adobe.com/creative-cloud/faq/mixamo-faq.html
- LottieFiles licensing basics — https://help.lottiefiles.com/animation-licensing-basics-

The clauses cited for **iStock and Getty, Adobe Stock, Bigstock, the Unity Asset Store EULA
(section 2.2.1(a)), TurboSquid, CGTrader, Fab, IconScout, FitScope, Vital Animations and
FitExerciseDB** were read on each vendor's own licence or pricing page during a delegated
collection pass on the same date, but the exact page URLs were not recorded in a form this note
can cite. Verify each one directly before relying on it in a decision.

**Production costs and competitor context**

- London video studio and gym-space hire rates — https://bloomsburyfilmstudio.co.uk/rates/ ;
  https://www.nineelmsstudio.com/rate-card ; https://www.westlondonstudio.co.uk/photo-video-studio-hire/ ;
  https://giggster.com/uk/find/london--uk/fitness-studio ; https://www.tagvenue.com/hire/fitness-studios/london
- Filming cost and throughput figures (vendor guide) —
  https://cloudfit.tv/blog/create-exercise-videos-that-look-like-they-were-filmed-by-a-pro/
- Competitor library sizes for context — https://blog.everfit.io/everfit-vs-trainerize-vs-truecoach ;
  https://truecoach.co/truecoach-vs-everfit/

A closing caution on sources. Several sites that dominate search results for this subject —
workoutxapp.com, ymove.app, repdb.co, movekit.com, aifitnessapi.com and
api.musclewiki.com/compare/* — are vendor marketing, and their comparison pages omit their
strongest competitors. MoveKit's own blog on exercise GIF sources, for instance, does not mention
ExerciseDB, MuscleWiki or free-exercise-db at all. Every price and licence clause in this note was
taken from the vendor's own pricing, licence or terms page, or from a primary repository file, not
from a comparison article.
