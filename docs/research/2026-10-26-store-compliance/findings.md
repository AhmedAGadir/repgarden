# RepGarden on the App Store and Google Play: what the rules allow

**26 October 2026.** Every source below was read on 26 October 2026. Apple's App Review
Guidelines carried the line "Last Updated: October 16, 2026"; Google's Developer Program Policy
renders on one page headed "effective September 30, 2026, unless otherwise stated", and no
Google policy section prints its own revision date. Where a point rests on a developer-forum
post, a help-centre answer about a phone call or a blog rather than a published rule, it says
so. Several ICO pages carry the banner "Due to changes made by the Data (Use and Access) Act,
this guidance is under review and may be subject to change." Nothing here is legal advice; it
is what the rules say and what the practical options are.

## The short answer

RepGarden's shape is allowed on both stores, and it is the ordinary shape for this category:
ABC Trainerize's client app is publicly listed, its App Store description says "Clients can only
access the app through a trainer, gym, or fitness business using ABC Trainerize", and it lists no
in-app purchases at all. Neither store forces a self-serve mode for someone without a trainer.
Both require that review can get in, which means a working trainer account and a working client
account with real assigned workouts, entered in App Store Connect's demo-account fields and in
Play Console's Sign-in details form. Three decisions follow. **First, where the money moves.** A
coaching fee that unlocks programmes and videos inside the app is digital content under Apple
3.1.1 and is a "subscription service (such as fitness…)" under Google's Payments policy; the
person-to-person exemptions cover only real-time, non-replayable sessions. Keeping the whole fee
means the trainer sells on the web with no price, paywall or checkout link anywhere in the app,
which is exactly what TrueCoach, Trainerize, Everfit, FITR and Hevy Coach do. Taking it in-app
costs 15% at Benji's scale and 30% above the small-business thresholds, and makes Apple or Google
the merchant. **Second, whose app it is.** Apple 4.2.6 rejects apps built from a template or
app-generation service "unless they are submitted directly by the provider of the app's content",
so GadirLabs cannot ship one listing per trainer from its own account; it is either one
multi-trainer RepGarden listing owned by Gadir Tech Ltd, or a per-trainer app submitted from the
trainer's own organisation account. The same choice settles who is the UK GDPR controller.
**Third, how much safety and privacy machinery the video upload needs on day one.** Google's
user-generated content policy is triggered by content "visible to or accessible by at least a
subset of the app's users", which a single trainer is, and requires in-app reporting plus in-app
blocking for one-to-one features; Apple's 1.2 is written around content users "upload" with no
public-or-private qualifier. Add to that in-app account deletion on both stores, a privacy policy
on an open URL, a Data safety declaration, a Health apps declaration, Apple's regulated medical
device declaration, and — because training videos and body measurements read as health data under
UK GDPR — explicit consent as the Article 9 condition on top of contract as the Article 6 basis.
A fourth, smaller decision: whether under-18 clients are allowed at launch, because the
Children's code applies to "more general health, fitness or wellbeing apps" that are likely to be
accessed by under-18s, whether or not they are aimed at them.

## 1. Invite-only apps: accounts the trainer creates

### Apple

Nothing in the guidelines requires a self-serve mode. The clauses that bear on it:

**2.1 App Completeness (a)** — "Submissions to App Review, including apps you make available for
pre-order, should be final versions with all necessary metadata and fully functional URLs
included; placeholder text, empty websites, and other temporary content should be scrubbed before
submission. Make sure your app has been tested on-device for bugs and stability before you submit
it, and include demo account info (and turn on your back-end service!) if your app includes a
login. If you are unable to provide a demo account due to legal or security obligations, you may
include a built-in demo mode in lieu of a demo account with prior approval by Apple. Ensure the
demo mode exhibits your app's full features and functionality."

**App Review help, "Provide information for a complete review"** — "Enter a username and password
that work at the time of submission. Credentials that expire or change before your review starts
may result in the submission being rejected." And, directly on point for a two-role product: "If
your app has multiple account types, such as administrative and general user accounts, use the
Notes field to add additional credentials for each type." It also asks for an authentication code
in advance if one is needed, warning that otherwise "a call may be required to continue the
review. Calls are typically completed within three to five business days."

**5.1.1(v) Account Sign-In** — "If your app doesn't include significant account-based features,
let people use it without a login. If your app supports account creation, you must also offer
account deletion within the app. Apps may not require users to enter personal information to
function, except when directly relevant to the core functionality of the app or required by law.
If your core app functionality is not related to a specific social network (such as Facebook,
WeChat, Weibo, X, etc.), you must provide access without a login or via another mechanism.
Pulling basic profile information, sharing to the social network, or inviting friends to use the
app are not considered core app functionality." The login-free obligation is tied to apps without
significant account-based features and to social-network logins. RepGarden is account-based by
definition, so the login is "directly relevant to the core functionality".

**4.2 Minimum Functionality** — "Your app should include features, content, and UI that elevate it
beyond a repackaged website. If your app is not particularly useful, unique, or 'app-like,' it
doesn't belong on the App Store. If your App doesn't provide some sort of lasting entertainment
value or adequate utility, it may not be accepted." 4.2.3(i) adds "Your app should work on its own
without requiring installation of another app to function" — satisfied, because the trainer's side
is a website, not an app.

**3.2.2(v)** lists as unacceptable "Arbitrarily restricting who may use the app, such as by
location or carrier." Requiring a trainer is not arbitrary; it is the product.

**3.1.3(c) Enterprise Services** — "If your app is only sold directly by you to organizations or
groups for their employees or students (for example professional databases and classroom
management tools), you may allow enterprise users to access previously-purchased content or
subscriptions. Consumer, single user, or family sales must use in-app purchase." This is a payment
clause, not a gating clause, and it does **not** cover RepGarden: a trainer's clients are
consumers, not an organisation's employees or students.

**4.8 Login Services** exempts from the Sign-in-with-Apple-equivalent duty any app that "is an
education, enterprise, or business app that requires the user to sign in with an existing
education or enterprise account" — the closest Apple comes to naming this model, and again it
reads as organisational rather than consumer.

One Apple answer constrains the invite flow. The account-deletion help page asks "If my app links
out to the default web browser for account creation, does it still need to offer account deletion
within the app?" and answers: "Yes. Additionally, linking out to the default web browser to sign
in or register an account provides a poor user experience and isn't appropriate, per App Review
Guideline 4." An invitation link that opens Safari to set a password sits close to this. The safer
flow is an invitation that opens the app by universal link or code, with the password set inside
the app.

**Practitioner evidence, not policy.** Developer-forum accounts show 4.2 does fire on
closed-audience apps. One thread records the rejection wording "We found that the usefulness of
your app is limited because it seems to be intended for a small, or niche, set of users"
(developer.apple.com/forums/thread/115363). A Hacker News account of a school-schedule app quotes
the same wording with "Specifically, the app is intended for invited friends only", and reports it
was resolved by moving to unlisted app distribution (news.ycombinator.com/item?id=47916438). A
third thread, "Will an invite only app be accepted?", ends with community advice to explain the
model in the review notes and no resolution (developer.apple.com/forums/thread/23663). These are
single accounts and are not precedent.

Apple's own **unlisted app distribution** is the official route for a closed audience, but its
stated examples are "part-time employees, franchisees, partners, business affiliates,
higher-education students, or conference attendees" — internal and partner audiences, not a
business's paying consumer clients. A public listing whose description says clients arrive through
a trainer is the better-evidenced route, because that is what Trainerize and TrueCoach ship.

### Google Play

The declaration is no longer called App access. Play Console's App content page now has a section
headed **Sign-in details**, and "Prepare your app for review" states the requirement: "If your
entire app or parts of your app are restricted based on login credentials, sign in details,
memberships, location, or other forms of authentication, you must provide all required details to
enable access to your app." The same page: "Use the 'Any other instructions' field to let us know
if there's anything special about your login mechanisms, such as using a one-time password,
multi-factor authentication, or logins with more than two fields", and "You can add up to five
sets of instructions" — enough for a trainer set and a client set.

The consequence of getting it wrong is stated on the Payments FAQ page, which still uses the older
name: "If we're unable to review your app because of restricted access, you may be blocked from
releasing updates, or your app may be removed from Google Play." Recovery does not need a support
ticket: update Sign-in details, save, and send the change for review.

There is **no clause anywhere in Google's Sign-in details text that addresses invite-only accounts
or accounts provisioned by a third party.** The requirement is unconditional — supply working
credentials. No Play policy permitting a developer to omit credentials because accounts cannot be
self-registered was found; recorded as not verified.

Two Play policies could otherwise catch a client app that looks empty without a trainer.
"Functionality, Content, and User Experience" says "Apps that crash, do not have the basic degree
of adequate utility as mobile apps, lack engaging content, or exhibit other behavior that is not
consistent with a functional and engaging user experience are not allowed on Google Play", and
"Limited Functionality and Content" gives as examples "Apps that are static without app-specific
functionalities, for example, text only or PDF file apps" and "Apps that are designed to do
nothing or have no function". A signed-in client app with a workout calendar, logging and video
upload is not that. The "Webviews and Affiliate Spam" clause — "We don't allow apps whose primary
purpose is to drive affiliate traffic to a website or provide a webview of a website without
permission from the website owner or administrator" — is the one a thin wrapper around the trainer
web app would hit, so the client app should be native, not a web view.

### What the existing coaching apps do

| Platform | Can a client self-serve in the mobile app? | How the client pays the coach |
|---|---|---|
| TrueCoach | No. The coach adds the client, who gets an email invitation | Stripe, coach-invoiced, outside the app; TrueCoach takes 5% of the invoice total and $15 per chargeback, and is available only to coaches in the US, UK, Australia and Canada |
| ABC Trainerize | No. Its App Store listing says "Clients can only access the app through a trainer, gym, or fitness business using ABC Trainerize", and the listing shows no in-app purchases | Stripe |
| Everfit | Yes. A public client invite link lets clients register themselves | Stripe, through the coach's connected Stripe account; "Stripe setup is available on Coach web" |
| FITR | The coach's programme link goes to a **web checkout** first; the client downloads the app afterwards | On the web, before the app is opened. FITR charges coaches £14.99–£189/month plus "a Business Automation fee of 5.99% flat … on revenue you process through Fitr" |
| Hevy Coach | Yes. The client uses the public consumer Hevy app and accepts the coach | No client-payment feature at all: "No, your clients will not pay anything. We charge coaches a subscription to use the platform" |

TrueCoach's App Store listing states the model plainly: "A TrueCoach account is required. If you
are downloading this app, you are a client of a trainer who has chosen to level up and subscribe
to the best-personalized coaching app on the market." Not one of the five takes the client's
payment through Apple in-app purchase or Google Play Billing.

## 2. Payments: is coaching digital content?

### Apple

The two clauses that could exempt RepGarden are narrower than they look.

**3.1.3(d) Person-to-Person Services** — "If your app enables the purchase of real-time
person-to-person services between two individuals (for example tutoring students, medical
consultations, real estate tours, or **fitness training**), you may use purchase methods other
than in-app purchase to collect those payments. One-to-few and one-to-many real-time services must
use in-app purchase." Fitness training is named, but the exemption is scoped to **real-time**
service between two individuals — a live session, not a programme waiting in a calendar.

**3.1.3(e) Goods and Services Outside of the App** — "If your app enables people to purchase
physical goods or services that will be consumed outside of the app, you must use purchase methods
other than in-app purchase to collect those payments, such as Apple Pay or traditional credit card
entry." Note the direction: for services consumed outside the app, in-app purchase is not optional,
it is forbidden. Coaching delivered in a gym is consumed outside the app. Programmes and exercise
videos opened in the app are not.

Against that, **3.1.1 In-App Purchase** — "If you want to unlock features or functionality within
your app, (by way of example: subscriptions, in-game currencies, game levels, access to premium
content, or unlocking a full version), you must use in-app purchase. Apps may not use their own
mechanisms to unlock content or functionality, such as license keys, augmented reality markers, QR
codes, cryptocurrencies and cryptocurrency wallets, etc." App Store Connect's new **Digital Goods
and Services questionnaire** defines the category as widely as possible: "Digital goods and
services are content, features, subscriptions, and other digital experiences offered or consumed
within an app." The questionnaire asks "Can customers consume digital goods and services in this
app?" and, if yes, whether the app uses Apple In-App Purchase exclusively or lists alternative
payment options per region; "After you submit this form, your choices for the European Union remain
locked for 12 months and can't be changed."

So a coaching fee that unlocks programmes and videos inside the app sits in 3.1.1 territory, and
the exemptions reach only the live-session half. The practical consequence is the one every
competitor has reached: **keep the purchase entirely out of the app.** No price, no plan screen, no
paywall, no "pay your trainer" button, no link to a checkout. The 3.1.3 preamble also bars
steering: "Apps in this section cannot, within the app, encourage users to use a purchasing method
other than in-app purchase, except for apps on the United States storefront and as set forth in
3.1.1(a) and 3.1.3(a). Developers can send communications outside of the app to their user base
about purchasing methods other than in-app purchase." Email and the trainer's own website are
fine; the app is not.

Practitioner accounts show this is where apps of exactly this shape get caught. One thread is
titled "Rejected under Guideline 3.1.1 – B2B SaaS app, existing accounts only, no purchases in the
app", with Apple's wording "Your app accesses digital content purchased outside the app, and that
content is not available through in-app purchase"; it has no replies
(developer.apple.com/forums/thread/811018). Another, where a Stripe subscription auto-created the
account, drew a reply from an Apple engineer explaining that Stripe and in-app purchase may coexist
only where the signup happened outside the app (developer.apple.com/forums/thread/744873). A third
was rejected for an in-app Stripe paywall: "The Lifetime Access and Monthly Access can be purchased
in the app using payment mechanisms other than in-app purchase"
(developer.apple.com/forums/thread/799798). These are single accounts, not policy; the pattern they
describe is consistent, and the second one carries an Apple employee's reply.

**If in-app purchase is used anyway**, Schedule 2 of the Apple Developer Program License Agreement
sets the commission: "For sales of Licensed Applications to End Users, Apple shall be entitled to a
commission equal to thirty per cent (30%) of all prices payable by each End User. Solely for
auto-renewing subscription purchases made by customers who have accrued greater than one year of
paid subscription service within a Subscription Group … Apple shall be entitled to a commission
equal to fifteen per cent (15%)" (§3.4(a)); and 15% throughout for the App Store Small Business
Program (§3.4(b)), open to developers who "have earned no more than 1 million USD in total
proceeds … during the previous calendar year". Signing the Paid Applications Agreement — Schedules
2 and 3 — is required, in Apple's words, "to offer paid apps and in-app purchases".

### Google Play

Google's Payments policy is blunter than Apple's. "Play-distributed apps requiring or accepting
payment for access to in-app features or services, including any app functionality, digital content
or goods (collectively 'in-app purchases'), must use Google Play's billing system for those
transactions unless Section 3, 8, or 9 applies", and the list of examples names the category
directly: "subscription services (such as **fitness**, game, dating, education, music, video,
service upgrades, and other content subscription services)".

The exemption that matters is on "Understanding Google Play's Payments policy": "If your app
provides a 1:1 online paid service, you are not required to use Google Play's billing system if:
the paid service is between two individuals [and] the paid service is not available for replay
afterwards (that is, the session is not recorded and cannot be accessed or used again) in any
Play-distributed app", with qualifying examples including "health coaching (such as **personal
trainer sessions** or counseling services)". The second condition is the problem: an app that
stores assigned workout videos and the client's own uploaded sets is precisely a service "available
for replay afterwards".

The route that does fit is **consumption-only**: "Google Play allows any app to be
consumption-only, even if it is part of a paid service. For example, a user could log in when the
app opens and access content paid for somewhere else. Remember, consumption-only means that any
product(s) or service(s), whether digital or physical, cannot be purchased from within the app."
Google even sets out what such an app may say without a link: "developers may choose to provide
additional information about purchasing options without direct links, including using language
like: 'You can purchase this book directly on our website'", and "Developers can refer users to
administrative information – like an account management page, privacy policy, or to a help center –
as long as the webpage does not eventually lead to an alternate payment method prohibited by the
Payments policy."

Google's anti-steering rule is wide: apps "may not lead users to a payment method other than Google
Play's billing system", including through "In-app webviews, buttons, links, messaging,
advertisements, or other calls to action" and "In-app user interface flows, including account
creation or sign-up flows, that lead users from an app to a payment method other than Google Play's
billing system as part of those flows." An invite flow that walks a client through payment would
breach it; an invite flow that only sets a password would not.

Also noted, and not RepGarden: "Transactions involving regulated clinical services should not use
Google Play's billing system", where those are "services provided by or on behalf of a licensed
healthcare provider that is intended to diagnose or manage … medical conditions." And on category:
"Does your billing policy change depending on my app category? No. All app categories are subject
to Google Play's Payments policy."

### External payments and alternative billing, by region

**Apple, United States** — no entitlement needed and no Apple commission. 3.1.1(a): "These
entitlements are not required for developers to include buttons, external links, or other calls to
action in their United States storefront apps", and "In all other storefronts, except for the
United States storefront, where this prohibition does not apply, apps and their metadata may not
include buttons, external links, or other calls to action that direct customers to purchasing
mechanisms other than in-app purchase." This follows Judge Yvonne Gonzalez Rogers's contempt ruling
of 30 April 2025. The Ninth Circuit affirmed the contempt finding on 11 December 2025 but held the
blanket commission ban overbroad and remanded; the Supreme Court granted certiorari on 30 June 2026
(*Apple Inc. v. Epic Games, Inc.*, No. 25-1311) on the narrow question of contempt for violating
the "spirit" of an injunction. Apple filed a proposal on 13 August 2026 for a tiered US link-out
commission — reported as 15% standard, 10% for some programmes and subscription renewals, 5% for
Small Business Program members, on purchases within seven days of the tap. Whether a rate has since
been set is **not verified**; no order was found.

**Apple, European Union** — Apple's EU terms were replaced on 1 October 2026. Apple's EU support
page states that "the Alternative Terms Addendum for Apps in the EU and StoreKit External Purchase
Link Entitlement (EU) Addendum have been phased out. As of October 1, 2026, these terms have been
superseded by Attachment 14 of the Apple Developer Program License Agreement", and that the Core
Technology Fee "has been replaced by the Core Technology Commission, a simple 5% commission on
digital transactions in apps distributed outside the App Store" — which does not reach an App Store
app that links out. For an App Store app, out-of-app offers carry a store services commission of
**15%**, or **10%** for Small Business Program, Mini Apps and Video Partner participants and for
auto-renewable subscriptions after the first year, and "Only sales made within 7 days of the link
tap are subject to this commission." Promotion is allowed in the app but not on the product page:
"Your app's App Store product page may not include information about purchasing with an alternative
payment option." The 2% initial acquisition fee and the 5%/13% store-services tiers announced for
1 January 2026 are gone from Apple's live pages; whether they were ever billed is **not verified**.

**Apple, United Kingdom** — there is **no UK external-link entitlement**. A UK iOS app may not link
out for digital purchases. The CMA designated Apple's and Google's mobile platforms with Strategic
Market Status on 22 October 2025 under the Digital Markets, Competition and Consumers Act 2024,
published final commitments on 1 April 2026 covering app review, ranking, data use and
interoperability but not payments, and consulted on a **Steering conduct requirement** from
30 June 2026, closing 28 July 2026, with responses published 14 August 2026. The draft requirement
would stop Apple preventing a developer "including within its apps and associated metadata an
End-user Redirection Mechanism which redirects an End-user to external websites to complete a
Steered Transaction", and would allow Apple a "Steering Fee" that is "fair and reasonable", charged
only where the transaction "occurs within a maximum of seven days of the End-user reaching an
alternative purchasing mechanism". **As of 26 October 2026 no steering requirement has been
imposed on either firm.**

**Google Play** — the regional pilots have been consolidated into the **billing choice program**:
"By enrolling, you can integrate your own billing system or guide users to your website for
purchases using external web links. Regardless of which option you implement, users should be given
a choice between Google Play Billing and either alternative billing within the app or external web
links." Availability includes the **United Kingdom from 30 June 2026** and the EEA from the same
date, Australia and Japan from 30 September 2026, with the US served by separate programmes. Fees
for in-app alternative billing are 10% on the first $1m of annual earnings across all transaction
types, and 10%/20%/25% at standard rates (auto-renewing subscriptions / other transactions on new
installs / other transactions on existing installs). For transactions "completed within 24 hours of
following an external web link" the rates are 10% on the first $1m, and 10%/20% at standard rates.
The older user choice billing programme, which applied "A 4% discount … to the standard service
fee", is still documented. A new global fee model announced on 4 March 2026 adds a separate billing
fee: "In the AU, JP, US, UK, and the European Economic Area (EEA), the billing fee is set at 5%",
rolled out for the EEA, UK and US from 30 June 2026.

In the EEA, the **external offers program** "allows developers of Google Play managed apps to lead
users in the European Economic Area (EEA) to external offers". Effective 4 June 2026 the fees are
an "Initial acquisition fee: 0%" plus an ongoing service fee within 24 hours of the click: 10% for
auto-renewing subscriptions, 20% for other in-app digital items, €1.20 per app install, with 10%
flat on the first $1m of annual earnings. Eligibility requires that "Your app must not target only
children" and that the "Developer must be registered as a business". In the US, after *Epic v
Google*, Google states it "will not require the use of Google Play Billing in apps distributed on
the Google Play Store, or prohibit the use of in-app payment methods other than Google Play
Billing", with the external content links programme charging 10% on subscriptions and 10%/20% on
other digital items, plus per-install fees of $3.65 for games and $2.85 for apps; reporting and
payment obligations began 1 October 2026.

So the UK is asymmetric: **Android allows alternative billing and external links in the UK today;
iOS does not.**

### The practical options and what they cost

1. **The trainer sells on the web; the app has no commerce at all.** Cost: the payment processor
   only. Allowed in every region on both stores, with no store commission anywhere, no regional
   branching, and no App Store Connect or Play Console payment declarations beyond answering "No"
   to the Digital Goods and Services questionnaire. FITR's web-checkout-then-download flow is the
   clearest documented template.
2. **In-app purchase and Google Play Billing.** Cost: 15% under Apple's Small Business Program and
   Google's first-$1m rates, 30% and 20–25% above the thresholds, plus Google's 5% billing fee in
   the UK. Removes any 3.1.1 risk, but the fee is set in store price points, Apple or Google is the
   merchant, refunds and VAT are handled by the store, and the trainer is paid through GadirLabs
   rather than directly. It also brings the full subscription-disclosure and cancellation rules.
3. **External link, where permitted.** US iOS 0% today, with 5–15% under active litigation; EU iOS
   15% or 10% within seven days; UK iOS not available; UK Android through billing choice at the
   standard fee less 4% under the old rates, or the newer 10–25% table; EEA Android 10%/20% plus
   €1.20 per install within 24 hours. This adds regional branching for no benefit in the UK, which
   is where Benji's clients are.

For an MVP with one trainer in London, option 1 is the only one that is simple, permitted in every
storefront and free of store commission.

## 3. User-generated content: videos only the trainer sees

### Apple

Guideline 1.2 is written by activity, not by audience: "Apps that enable users to create, generate,
upload, share, or otherwise contribute content present particular challenges, including
intellectual property infringement, nonconsensual intimate imagery, and anonymous bullying. This
includes social media, user-generated content platforms, and AI content creation apps. To prevent
abuse, such apps must include:

- A method for filtering objectionable material from being posted to the app
- A mechanism to report offensive content and timely responses to concerns
- The ability to block abusive users from the service
- Published contact information so users can easily reach you"

It continues: "It is your responsibility to remove content that violates this guideline, your terms
of service, or your community standards. Developers who fail to implement appropriate safeguards or
fail to remediate identified violations after notice may be considered in violation of the Developer
Code of Conduct." Apple's own note on the 16 October 2026 revision says "1.2: Clarified app content
and app types that are subject to this guideline, and potential Developer Code of Conduct violation
for failing to implement appropriate safeguards or remediating violations after notice."

There is **no clause limiting 1.2 to publicly visible content**, and the examples Apple gives are
illustrative. A client uploading a video that one other person sees is contributing content to the
app. Whether a reviewer raises 1.2 for a strictly one-to-one coaching upload is **not verified**
from any Apple source. The widely circulated practitioner checklists for this guideline list direct
messages among the content types needing moderation and quote a 24-hour expectation for acting on
reports, but that figure comes from Apple's rejection letters as developers quote them, not from a
published rule.

One clause applies directly to recording a working set: **2.5.14** — "Apps must request explicit
user consent and provide a clear visual and/or audible indication when recording, logging, or
otherwise making a record of user activity. This includes any use of the device camera, microphone,
screen recordings, or other user inputs."

And deletion of uploads is explicit on the account-deletion page: "Does the content provided by a
person need to be deleted in apps that display and share user-generated content? Yes. People expect
that all data associated with their account will be deleted when the account is deleted. This
includes user-generated content that's shared with others, such as photos, videos, text posts, and
reviews."

### Google Play

Google answers the public-or-private question in its own definition, and the answer is that private
content is in scope: "User-generated content (UGC) is content that users contribute to an app, and
which is **visible to or accessible by at least a subset of the app's users**." One named trainer is
a subset. There is no exemption for private sharing, one-to-one visibility or closed groups anywhere
in the policy.

What Google requires scales with the experience, and two of its examples fit RepGarden exactly:

> "Apps that contain or feature UGC … must implement robust, effective, and ongoing UGC moderation
> that: Requires users accept the app's terms of use and/or user policy before users can create or
> upload UGC; Defines objectionable content and behaviors …, and prohibits them in the app's terms
> of use or user policies; Conducts UGC moderation, as is reasonable and consistent with the type of
> UGC hosted by the app. This includes providing an in-app system for reporting and blocking
> objectionable UGC and users, and taking action against UGC or users where appropriate. …
> **Apps featuring UGC that identify a specified set of users through means such as user
> verification or offline registration (for example, apps exclusively used within a specific school
> or company, etc.) must provide in-app functionality to report content and users.**
> **UGC features that enable 1:1 user interaction with specific users (for example, direct
> messaging, tagging, mentioning, etc.) must provide an in-app functionality for blocking users.**
> … Provides safeguards to prevent in-app monetization from encouraging objectionable user
> behavior."

The first of those two bullets is the trainer-provisioned-accounts case and requires in-app
**reporting**; the second is the one-to-one case and requires in-app **blocking**. A named common
violation is "Apps that continually fail to address user complaints about objectionable content."

Google's **Photo and Video Permissions** policy is the other trigger the video upload pulls. "All
user Photos are personal and sensitive data subject to the User Data policy. Apps that target
Android 13 or higher (API level 33+) may only request the READ_MEDIA_IMAGES and READ_MEDIA_VIDEO
permissions if system pickers (like the Android Photo Picker) are not sufficient for your app to
provide core functionality. Apps that still request the READ_MEDIA_IMAGES and READ_MEDIA_VIDEO
permissions must submit a Play Console declaration to demonstrate access needs for Photos and why
Android Photo Picker (or alternatives) would not suffice." Full compliance has been mandatory since
28 May 2025, and "Apps that have custom pickers are not automatically qualified to use the
permission". For RepGarden the right answer is to record in-app with CAMERA, or pick an existing
clip with the Android Photo Picker, and declare neither broad media permission.

### What reviewers expect for private media in a coaching app

Combining the two rulebooks, the build that satisfies both without inventing a social network:

- terms of use accepted before the first upload, naming what may not be uploaded;
- a report control on any video or note a trainer or client can see, with a stated response time;
- blocking, expressed as the client being able to leave or block their trainer and the trainer being
  able to remove a client, with access revoked immediately;
- a stated moderation route — for a single-trainer MVP, a described manual review on report is
  enough to answer "a method for filtering objectionable material";
- GadirLabs' contact details in the app and on the support URL;
- deletion of a client's videos when the account is deleted;
- an explicit consent step and a visible recording indicator when the camera runs.

## 4. Health and fitness rules

### Apple

RepGarden is not a medical app, and **1.4.1** is written for medical ones: "Medical apps that could
provide inaccurate data or information, or that could be used for diagnosing or treating patients
may be reviewed with greater scrutiny. Apps must clearly disclose data and methodology to support
accuracy claims relating to health measurements, and if the level of accuracy or methodology cannot
be validated, we will reject your app. For example, apps that claim to take x-rays, measure blood
pressure, body temperature, blood glucose levels, or blood oxygen levels using only the sensors on
the device are not permitted. Apps should remind users to check with a doctor in addition to using
the app and before making medical decisions." The doctor reminder sits inside the medical-apps
clause, so Apple does not state a general disclaimer requirement for fitness apps — but Google does,
below, so the disclaimer gets written anyway.

**5.1.3 Health and Health Research** opens: "Health, fitness, and medical data are especially
sensitive and apps in this space have some additional rules to make sure customer privacy is
protected." The parts that bind RepGarden:

- 5.1.3(i) — "Apps may not use or disclose to third parties data gathered in the health, fitness,
  and medical research context … for advertising, marketing, or other use-based data mining purposes
  other than improving health management, or for the purpose of health research, and then only with
  permission. … You must disclose the specific health data that you are collecting from the device."
- 5.1.3(ii) — "Apps must not write false or inaccurate data into HealthKit or any other medical
  research or health management apps, and may not store personal health information in iCloud."
- 5.1.2(vi) — data from HealthKit, ClassKit and "depth and/or facial mapping tools (such as ARKit,
  Camera APIs, or Photo APIs) may not be used for marketing, advertising or use-based data mining,
  including by third parties."

If HealthKit is used, **2.5.1** adds that "HealthKit should be used for health and fitness purposes
and integrate with the Health app". The MVP does not need HealthKit, and not using it removes a set
of obligations.

Two App Store Connect requirements are easy to miss and both apply:

- **Age rating.** The questionnaire's Medical or Wellness section defines "Health or Wellness Topics:
  Content that provides self-care or lifestyle recommendations. May include: calorie tracking,
  dieting advice, or exercise recommendations", and that answer appears in the 9+ tier.
  "Medical or Treatment Information: Content that provides diagnoses or guidance around the
  management of medical conditions or health and wellness" gives 13+ at "infrequent" and 16+ at
  "frequent". RepGarden should answer Health or Wellness Topics, not Medical or Treatment
  Information — and the second reason to get that right is the next item.
- **Regulated medical device declaration.** App Store Connect help: "apps that are available in the
  European Union (EU)/European Economic Area (EEA), United Kingdom (UK), or United States (US), and
  that also meet either of the criteria listed below must indicate whether they're regulated medical
  device with respect to each region's regulatory authority or body responsible for the governance
  and compliance of medical devices" — the criteria being "Have a primary or secondary category of
  Health & Fitness or Medical" or having answered "frequent" to Medical or Treatment Information.
  RepGarden will be in Health & Fitness and will be on the UK store, so the declaration is
  mandatory. The answer is No: "If your app doesn't provide any health or medical features, or
  access health data to support non-health features, you should select No, to declare that your app
  is not a regulated medical device."

One structural clause: **5.1.1(ix)** — "Apps that provide services in highly regulated fields (such
as banking and financial services, healthcare, gambling, legal cannabis use, air travel and crypto
exchanges) or that require sensitive user information should be submitted by a legal entity that
provides the services, and not by an individual developer." Personal training is not on that list,
but the app carries sensitive information, so submitting from Gadir Tech Ltd's organisation account
rather than an individual account is the lower-risk reading.

### Google Play

Google's **Health content and services** policy is explicit about scope: "If your app offers
health-related features or information as part of its functionality, or accesses health data to
support non-health features, it must comply with the existing Google Play Developer Policies,
including Privacy, Deception and Device Abuse, in addition to the below requirements", and "If your
app is not primarily a health app, but has health-related features and accesses health data, it is
still in scope of the Health App policy."

**The declaration is universal.** "All developers must complete the Health apps declaration form on
the App content page … in Play Console", and the help page is blunter still: "All developers that
have an app published on Google Play must complete the Health apps declaration, including apps on
closed testing, open testing, or production tracks. … Even developers with apps that do not offer
any health features must complete this form and certify that no health features are offered through
the app."

**General fitness is in scope**, as the first declarable category: "Health and fitness — Activity
and Fitness: Apps that monitor and record physical activities, exercise routines, and workouts.
Includes tracking body vitals related to fitness (like heart rate), and measuring body composition
and weight." RepGarden logs workouts and, if body measurements are added, body composition and
weight, so it declares Activity and Fitness. Note that "Physical Therapy and Rehabilitation" sits in
the Medical group — a reason to keep RepGarden's wording about training, not rehabilitation.

**Yes, a disclaimer is required — by Google, not Apple.** "Other health and medical apps must
include a clear disclaimer in their app description indicating that the app is 'not a medical device
and does not diagnose, treat, cure, or prevent any medical condition.' Apps must also remind users
to consult a healthcare professional for medical advice, diagnosis, or treatment." That is store
listing text plus an in-app reminder, and it satisfies Apple's 1.4.1 sentence at the same time.

Google also names the camera as a health-sensitive permission. Its list of "permissions … considered
in scope of health related sensitive data" includes ACTIVITY_RECOGNITION, BODY_SENSORS and
**CAMERA**, and "If your app requires any of these permissions, it must prominently disclose how
user data will be used, describe the type of data being accessed, and have the user provide
affirmative consent for such use." Its model disclosure wording is of the form "This app collects
physical activity data to calculate calories burnt".

Privacy obligations attach through the same policy: "Your app must post a privacy policy link in the
designated field within Play Console, and a privacy policy link or text within the app itself.
Please make sure your privacy policy is available on an active, publicly accessible and non-geofenced
URL (no PDFs) and is non-editable", and "Permissions that are not required for a health app to
perform its core functionality should not be requested and unused permissions must be removed."

### Does logging weights and reps count as health data?

Under the **stores' own definitions, yes.** Apple's privacy-label taxonomy has "Fitness — Fitness and
exercise data, including but not limited to the Motion and Fitness API" and "Health — Health and
medical data, including … any other user provided health or medical data". Google's Data safety form
has "Fitness info — Information about a user's fitness, such as exercise or other physical activity"
and "Health info — Information about a user's health, such as medical records or symptoms". Logged
sets are Fitness on both; body measurements and any injury note move towards Health. The consequence
is a label entry and a Data safety entry, plus Google's Health apps declaration — not a licence or
an approval.

Under **UK GDPR** the answer is in section 5.

## 5. Privacy, data, and the trainer seeing client data

### Apple's privacy rules and labels

**5.1.1(i) Privacy Policies** — "All apps must include a link to their privacy policy in the App
Store Connect metadata field and within the app in an easily accessible manner. The privacy policy
must clearly and explicitly:

- Identify what data, if any, the app/service collects, how it collects that data, and all uses of
  that data.
- Confirm that any third party with whom an app shares user data … will provide the same or equal
  protection of user data as stated in the app's privacy policy and required by these Guidelines.
- Explain its data retention/deletion policies and describe how a user can revoke consent and/or
  request deletion of the user's data."

**5.1.1(ii)** requires consent for collecting user or usage data and "an easily accessible and
understandable way to withdraw consent". **5.1.1(iii)** requires minimisation: "Apps should only
request access to data relevant to the core functionality of the app and should only collect and use
data that is required to accomplish the relevant task. Where possible, use the out-of-process picker
or a share sheet rather than requesting full access to protected resources like Photos or Contacts."
**5.1.2(i)** adds: "Unless otherwise permitted by law, you may not use, transmit, or share someone's
personal data without first obtaining their permission. … You must clearly disclose where personal
data will be shared with third parties, including with third-party AI, and obtain explicit
permission before doing so."

**Privacy labels.** Apple's App privacy details page defines the data types RepGarden touches:
"Health — Health and medical data, including … any other user provided health or medical data";
"Fitness — Fitness and exercise data"; "Photos or Videos — The user's photos or videos"; "Other User
Content — Any other user-generated content"; and "Sensitive Info — Such as racial or ethnic data,
sexual orientation, pregnancy or childbirth information, disability, religious or philosophical
beliefs, trade union membership, political opinion, genetic information, or biometric data". The page
also says: "if you ask a user to input a specific data type into a text field, such as their name or
email, or if you have a feature that enables users to upload a particular media type, such as photos
or videos, then you'll need to disclose the specific type of data." So RepGarden's label should
declare Contact Info, Identifiers, Fitness (and Health if body measurements or injury notes are
collected), Photos or Videos and Other User Content, linked to identity, used for App Functionality,
and should declare no tracking.

For calibration: TrueCoach's own label, read 26 October 2026, declares only Contact Info (email
address), Identifiers (user ID) and Diagnostics, with no Health & Fitness and no Photos or Videos,
although its own description says clients "leave their own custom photos and videos for analysis".
Apple's product page carries the standing caveat "This information has not been verified by Apple."
A competitor's label is not a safe harbour.

### Google's Data safety form

"All developers that have an app published on Google Play must complete the Data safety form,
including apps on closed, open, or production testing tracks. … Even developers with apps that do not
collect any user data must complete this form and provide a link to their privacy policy", and "The
information in this section must consistently match your app's privacy policy disclosures."

The definitions to use: "Health info — Information about a user's health, such as medical records or
symptoms"; "Fitness info — Information about a user's fitness, such as exercise or other physical
activity"; "Photos — A user's photos"; "Videos — A user's videos". "'Collect' means transmitting data
from your app off a user's device", and "'Sharing' refers to transferring user data collected from
your app to a third party" — with the carve-out that matters for hosting: "The following types of
data transfers do not need to be disclosed as 'sharing': Service providers. Transferring user data to
a 'service provider' that processes it on behalf of the developer." Supabase or an equivalent host
is a service provider; the trainer seeing their own client's data is not a third-party transfer in
Google's sense either, because it is the purpose of the app, but it must be described in the privacy
policy.

Data declared as required versus optional: "If your app's primary functionality requires the data
type, you should declare that data as 'required.'" Sets, reps and assigned workouts are required;
video upload and body measurements can be optional if the app genuinely works without them. The form
also asks to declare "Whether or not all of the user data collected by your app is encrypted in
transit" and "Whether or not you provide a way for users to request that their data is deleted".

Google's privacy policy requirements are more prescriptive than Apple's. The policy must include
"Developer information and a privacy point of contact or a mechanism to submit inquiries"; the data
types accessed, collected, used and shared, and any parties it is shared with; "Secure data handling
procedures for personal and sensitive user data"; "The developer's data retention and deletion
policy"; and "Clear labeling as a privacy policy". The entity named in the Play listing must appear
in it, and it must be "available on an active, publicly accessible and non-geofenced URL (no PDFs)
and is non-editable".

### Account deletion on both stores

**Apple, 5.1.1(v)** and its help page: "Apps submitted to the App Store that support account creation
must also let people initiate deletion of their account within the app." The option must be "easy to
find", must "Offer to delete the entire account record, along with associated personal data", and
"only offering to temporarily deactivate or disable an account is insufficient". Deletion need not be
instant — "If your process for account deletion is manual or otherwise takes a reasonable amount of
time to complete, this is acceptable" — and a GDPR-only flow is not enough: "Everyone should be able
to delete their accounts, regardless of where they're located." A forum account reports Apple saying
by phone that the requirement does not apply where a client organisation provisions every account
(developer.apple.com/forums/thread/738232); that is a single unverified account, the published text
conditions the duty only on "If your app supports account creation", and RepGarden's trainer web app
does create accounts. Build the in-app deletion.

**Google** requires both an in-app route **and** a web route: "If your app allows users to create an
account from within your app, then it must also allow users to request for their account to be
deleted. Users must have a readily discoverable option to initiate app account deletion from within
your app and outside of your app (for example, by visiting your website). A link to this web resource
must be entered in the designated URL form field within Play Console. When you delete an app account
based on a user's request, you must also delete the user data associated with that app account.
Temporary account deactivation, disabling, or 'freezing' the app account does not qualify as account
deletion."

Two Google clauses bear directly on trainer-created accounts. First, the scope test is wider than
in-app signup: "Your app supports account creation within the app if a user can complete creating an
app account directly in the app **or if the app directs the user to an app account creation flow
outside of the app**." Second, the only exemption that could be read towards RepGarden does not fit:
"Permanently private and enterprise device management apps are exempt … As a reminder, accounts that
are created and operated offline are not app accounts and do not fall within policy scope." A
RepGarden account is created online in the trainer's web app, so it is an app account. Google also
requires the web route to work independently of the app: "your web resource should give users a way
to request that their data be deleted without sending the user back to the app and requiring them to
re-download it to submit their request." Scope of deletion: "All user data indicated as collected in
your data safety section is within scope." The compliance deadline passed on 31 May 2024; this is
enforced, not forthcoming.

### UK GDPR: is training data a special category?

**Almost certainly yes, treat it as health data.** UK GDPR Article 4(15): "'data concerning health'
means personal data related to the physical or mental health of a natural person, including the
provision of health care services, which reveal information about his or her health status".
Article 9(1) prohibits processing health data unless an Article 9(2) condition applies. Recital 35:
"Personal data concerning health should include all data pertaining to the health status of a data
subject which reveal information relating to the past, current or future physical or mental health
status of the data subject … independent of its source, for example from a physician or other health
professional, a hospital, a medical device or an in vitro diagnostic test."

The ICO's "What is special category data?" page says health data "not only covers specific details of
medical conditions, tests or treatment, but includes any related data which reveals anything about
the state of someone's health", and its list of examples includes "data from fitness trackers". The
ICO's clearest statement that app data of this kind is health data is in the Children's code, Annex C:
"Special category data includes information about: … health (**including data collected by fitness
apps**)". On inference, revised in April 2024: "Whether or not inferred data counts as special
category data and triggers Article 9 depends on whether: your processing intends to make an inference
linked to one of the special categories of data; or you intend to treat someone differently on the
basis of inferred information linked to one of the special categories of data. If this is the case,
then you are processing special category data regardless of how confident you are that the inference
is correct." A trainer reading a client's log and video and changing their programme is doing exactly
that.

**Not verified:** no ICO page addresses whether a bare set, rep and weight log, divorced from any
health inference, is "data concerning health". Body measurements sit closer to Recital 35's
"physiological … state of the data subject". The practical reading is to treat the whole record as
special category data, because the alternative is a line no regulator has drawn.

**Lawful basis.** Both layers are needed: "you must identify both a lawful basis under Article 6 and
a condition for processing special category data under Article 9." The ICO's own worked example is a
fitness instructor. For a pregnancy yoga class: "As the instructor needs to process these details to
provide the yoga class, the appropriate lawful basis is likely to be 'performance of a contract'.
Although the individual cannot sign up to the class without revealing information about their
pregnancy, explicit consent is still likely to be the appropriate condition for processing health
data." So: **contract under Article 6, explicit consent under Article 9.**

Explicit consent has a defined shape: "explicit consent must be confirmed in a clear statement
(whether oral or written), rather than by any other type of affirmative action; it must specify the
nature of the special category data; and it should be separate from any other consents you are
seeking." The health-and-social-care condition, Article 9(2)(h), is not available, because Article
9(3) and DPA 2018 s.11 restrict it to a "health professional or a social work professional" or
someone under a statutory duty of confidentiality, and the ICO's indicative list of health
professionals does not include personal trainers.

The ICO's February 2024 advice to app developers after its period and fertility app review is the most
directly relevant guidance: be transparent; "Genuine consent means offering people a real choice …
must be explicit, unambiguous and involve a clear action to opt-in. You must not use pre-ticked boxes
or any default method for consent"; establish the correct lawful basis and "must not adopt a
one-size-fits-all approach"; and "If you are determining the purpose and means of processing data,
you are the data controller."

A DPIA is expected: "You must do a data protection impact assessment (DPIA) for any type of
processing which is likely to be high risk. This means you are more likely to need to do a DPIA for
special category data … If in doubt, we recommend you carry out a DPIA." If the Children's code
applies, standard 2 makes a DPIA mandatory.

### Is a training video biometric data?

**No, not by itself.** The ICO: "If you process digital photographs of individuals, this is not
automatically biometric data even if you use it for identification purposes. … it only becomes
biometric data if you carry out 'specific technical processing'. Usually this involves using the image
data to create an individual digital template or profile, which in turn you use for automated image
matching and identification." Its biometric guidance adds that even where biometric data is not used
to identify anyone, "the biometric data you process may still be considered another type of special
category information. For example, you could use biometric data to infer someone's racial or ethnic
origin or consider it as health data." A video of a client training is personal data and, because it
shows physical capability and often injury or physique, is very likely health data; it is not
biometric data unless pose estimation or form analysis is built to recognise the individual. That is a
reason to keep AI video analysis out of the MVP, as planned.

### Controller or processor, and what it means for the build

The ICO's test asks which organisation decides "to collect personal data in the first place; the
lawful basis for doing so; what types of personal data to collect; the purpose or purposes the data
are to be used for; which individuals to collect data about; whether to disclose the data, and if so,
to whom; what to tell individuals about the processing; how to respond to requests made in line with
individuals' rights; and how long to retain the data". "If you make any of these decisions, it is
likely that you are a controller."

Two of the ICO's examples bracket the choice. The processor example: "A private company provides
software to process the daily pupil attendance records of a state-maintained school. … The school sets
the purpose … It does not determine the purposes of the processing, it merely provides the processing
service. This company is likely to be a processor." The joint-controller example is a market-research
company given "the freedom to decide such matters as which customers to select for interview, what
form the interview should take, what information to collect" — which "means the market-research
company is a joint controller".

So the decision is architectural, not cosmetic:

- **GadirLabs as processor, the trainer as controller.** This is the Trainerize-style reading: the
  trainer decides who to onboard, what to collect and how long to keep it; GadirLabs hosts and
  provides the tools. It requires an Article 28 contract with the trainer, and it puts the duty to
  answer access, erasure and portability requests on the trainer, with GadirLabs obliged only to
  "assist the controller by appropriate technical and organisational measures".
- **GadirLabs as controller, or joint controller.** This follows if GadirLabs decides retention,
  writes the privacy information, sets the lawful basis, responds to rights requests directly, or uses
  client data for its own analytics or product improvement. The ICO: "you cannot be both a controller
  and a processor for the same processing activity", and "If you are acting as both a controller and
  processor, you must ensure your systems and procedures distinguish between the personal data you are
  processing in your capacity as controller and what you process as a processor on another
  controller's behalf. … If you cannot do this, you are likely to be considered a joint controller
  rather than a processor."

An Article 28 contract must state "the subject matter and duration of the processing; the nature and
purpose of the processing; the type of personal data and categories of data subject; and the
controller's obligations and rights", and must contain terms on: processing only on documented
instructions; a duty of confidence; appropriate security; sub-processors ("the processor should not
engage another processor … without the controller's prior specific or general written
authorisation", with the same obligations imposed down the chain and the processor liable for the
sub-processor); assisting with data subjects' rights; assisting with security, breach notification and
DPIAs; deletion or return of data at the end of the contract; and audits and inspections. If
RepGarden is sold to more than one trainer, that contract is a product document, not a one-off.

Joint controllership is the costly outcome: "each controller remains responsible for complying with all
the obligations of controllers", "you must have a transparent arrangement that sets out your agreed
roles and responsibilities", and "Each joint controller will be liable for the entire damage caused by
the processing".

**ICO fee.** "Under the Data Protection (Charges and Information) Regulations 2018, organisations
(including sole traders) that use personal information need to pay a data protection fee, unless they
are exempt", and "UK controllers must also pay a data protection fee unless they are exempt". Tier 1,
for an organisation with turnover up to £632,000 or no more than 10 staff, is £52, with £5 off by
direct debit. The exemption list covers only staff administration, advertising and marketing, accounts
and records, not-for-profit purposes, personal or household affairs, public registers, judicial
functions and purely manual processing. Delivering a coaching service to clients is not on that list,
so a trainer holding client records on a computer appears to owe the tier 1 fee, and GadirLabs owes it
too for any processing where it is the controller. The ICO's registration self-assessment is an
interactive form; its published criteria are the exemption list and the tier definitions.

### What the client must see, and when

Articles 13 and 14 set the privacy information. The ICO's checklist: the name and contact details of
the organisation; the data protection officer's details if applicable; the purposes of the processing;
the lawful basis; the legitimate interests if relied on; **the categories of personal data obtained,
if the data is not obtained from the individual**; the recipients or categories of recipients;
international transfers; retention periods; the rights available; the right to withdraw consent; the
right to complain to the ICO; **the source of the personal data, if not obtained from the individual**;
whether providing the data is a statutory or contractual obligation; and whether there is automated
decision-making.

Because the trainer creates the account, the two bracketed items apply. Article 14 is headed
"Information to be provided where personal data have not been obtained from the data subject", so the
test is the source of each piece of data, not who created the account. The name, email and any notes
the trainer enters about the client are not obtained from the client, so Article 14 is engaged, with
its extra items and its timing: "within a reasonable period after obtaining the personal data, but at
the latest within one month"; "if the personal data are to be used for communication with the data
subject, at the latest at the time of the first communication"; or "if a disclosure to another
recipient is envisaged, at the latest when the personal data are first disclosed." In practice the
invitation email is the first communication, so the privacy information must reach the client with
the invitation, not at first sign-in.

Sets, reps, notes and videos the client enters themselves are obtained from the data subject, so
Article 13 applies to those, at the time they are obtained.

**Erasure and export.** Article 17 is "not absolute and only applies in certain circumstances", but
one trigger is squarely relevant: a right to erasure arises where "you have processed the personal
data to offer information society services to a child". Where data has been disclosed onward, "you
must contact each recipient and inform them of the erasure, unless this proves impossible or involves
disproportionate effort" — which, with a trainer who has exported a client's log, is a real operational
step. On backups: "The key issue is to put the backup data 'beyond use', even if it cannot be
immediately overwritten."

Portability "only applies when: your lawful basis for processing this information is consent or for
the performance of a contract; and you are carrying out the processing by automated means", and it
covers "personal data resulting from observation of an individual's activities", including "'raw' data
processed by connected objects such as smart meters and wearable devices" — but "It does not include
any additional data that you have created based on the data an individual has provided to you." So
logged sets, notes and uploaded videos are portable; a trainer's assessment notes and derived
analytics are probably not portable, but are still in scope of a subject access request.

**Retention.** "The UK GDPR does not set specific time limits for different types of data. This is up
to you, and will depend on how long you need the data for your specified purposes", and "Personal data
held for too long will, by definition, be unnecessary. You are unlikely to have a lawful basis for
retention." For a small operation: "If you are a small organisation undertaking occasional low-risk
processing, you may not need a documented retention policy. However, if you don't have a retention
policy … you must still regularly review the data you hold, and delete or anonymise anything you no
longer need." Special category data at scale is not low-risk, so write the schedule: how long a
client's log and videos are kept after they stop training, and what happens when a trainer leaves the
platform.

### Age: can a trainer onboard a client under 18?

Nothing in either store's rules forbids it, and nothing in UK data protection law forbids it. What it
triggers is substantial.

**Consent age.** The brief's reference to DPA 2018 s.9 is out of date: that section was "omitted
(31.12.2020)". The age now sits in modified UK GDPR Article 8(1): "in relation to the offer of
information society services directly to a child, the processing of the personal data of a child shall
be lawful where the child is at least 13 years old. Where the child is below the age of 13 years, such
processing shall be lawful only if and to the extent that consent is given or authorised by the holder
of parental responsibility over the child." The Data (Use and Access) Act 2025 added a power for the
Secretary of State to move that age between 13 and 16. Article 8 bites only where consent is the basis
— which, since explicit consent is the likely Article 9 condition for training data, it is. Article
8(3) also preserves general contract law: "If the child is not competent to enter into the contract
then the contract is voidable. If the contract is voided then this basis for processing will not be
valid."

**The Children's code applies even though RepGarden is not aimed at children.** The ICO: "This code
applies to 'information society services likely to be accessed by children' in the UK. … **It is not
restricted to services specifically directed at children.**" A child is anyone under 18. "We consider
that for a service to be 'likely' to be accessed, the possibility of this happening needs to be more
probable than not." And, on point: "This code does not apply to websites or apps specifically offering
online counselling or other preventive services … **However, more general health, fitness or wellbeing
apps or services are covered.**" If GadirLabs decides the code does not apply, the ICO expects that
decision to be documented: "you should document and support your reasons for your decision."

The 15 standards are: best interests of the child; data protection impact assessments; age appropriate
application; transparency; detrimental use of data; policies and community standards; default
settings; data minimisation; data sharing; geolocation; parental controls; profiling; nudge
techniques; connected toys and devices; and online tools. The ones that reshape an app where a 16- or
17-year-old's training videos are visible to a trainer:

- **Standard 7, default settings** — "Settings must be 'high privacy' by default", and "This means
  that children's personal data is only visible or accessible to other users of the service if the
  child amends their settings to allow this." There is a core-service carve-out — "It is not necessary
  however for you to provide a privacy setting for any personal data that you have to process in
  order to provide your core or most basic service" — but the ICO warns: "We will look very carefully
  at any claims that a privacy setting cannot be provided because the personal data is needed to
  provide the core service. … take care not to abuse the concept of a core service by applying it more
  widely than is warranted." A trainer seeing assigned workouts and logged sets is plausibly core;
  video upload is plausibly an optional element that a child user should switch on.
- **Standard 8, data minimisation** — "you cannot collect more data than you need to provide the
  elements of a service the child actually wants to use", and "You should give children a choice as
  to whether they wish their personal data to be used for each additional purpose or service
  enhancement."
- **Standard 3, age appropriate application** — either "establish age with a level of certainty that
  is appropriate to the risks" or "apply the standards in this code to all your users instead". The
  ICO adds that "In assessing whether you have chosen an appropriate method, we will take into
  account the products currently available in the marketplace, particularly for small businesses
  which don't have the resources to develop their own solutions."
- **Standard 12, profiling** — "Switch options which use profiling 'off' by default", and Article
  22(4) means special category data cannot be used for solely automated decisions with significant
  effects without explicit consent. An automated programme generator would be caught; a trainer
  writing programmes by hand is not.
- **Standard 11, parental controls** — relevant by analogy only. It covers a parent monitoring a
  child and requires "a clear and obvious sign for the child (such as a lit up icon) which lets them
  know when monitoring or tracking is active". **Not verified:** the code says nothing about a coach
  or trainer, as opposed to a parent, viewing a child's data. There is no named standard for
  professional third-party visibility.

**On the stores.** Apple's **5.1.4 Kids** requires a privacy policy and compliance with children's
privacy statutes for any app that can "collect, transmit, or have the capability to share personal
information (such as name, address, email, location, photos, videos, drawings, the ability to chat,
other personal data, or persistent identifiers used in combination with any of the above) from a
minor". Google's Target audience and content declaration is the mechanism: if "Your app is not
designed for children", then "You must still meet the requirements outlined in Google Play Developer
Program policies and Developer Distribution Agreement" but the Families Policy Requirements do not
attach. Google adds a warning worth reading twice: "if your app targets any users who are under the
age of 21, you must consider if they would be considered children under their local laws", and
"Misrepresentation of any information about your app in the Play Console, including in the Target
Audience and Content section, may result in removal or suspension of your app". Its neutral age screen
guidance is "a system that asks users to freely enter their month, day, and year of birth", not a
pre-filled date.

The low-cost MVP position: state in the terms that clients must be 18 or over, have the trainer
confirm it at invitation, and set the age rating and target audience to adults. Opening to 16- and
17-year-olds is a later decision that brings the Children's code with it.

## 6. The rest of what catches apps like this

### Sign in with Apple

**4.8 Login Services** — "Apps that use a third-party or social login service (such as Facebook
Login, Google Sign-In, Log in with X, Sign In with LinkedIn, Login with Amazon, or WeChat Login) to
set up or authenticate the user's primary account with the app must also offer as an equivalent
option another login service with the following features: the login service limits data collection to
the user's name and email address; the login service allows users to keep their email address private
as part of setting up their account; and the login service does not collect interactions with your app
for advertising purposes without consent." The first exemption is "Your app exclusively uses your
company's own account setup and sign-in systems." So email-and-password alone needs nothing; adding
Google Sign-In means adding Sign in with Apple. If Sign in with Apple is used, account deletion must
revoke tokens: "Apps that support Sign in with Apple should use the Sign in with Apple REST API to
revoke user tokens."

### Tracking and ATT

Apple's definition: "'Tracking' refers to linking data collected from your app about a particular
end-user or device, such as a user ID, device ID, or profile, with Third-Party Data for targeted
advertising or advertising measurement purposes, or sharing data collected from your app about a
particular end-user or device with a data broker." Not tracking: "When the data is linked solely on
the end-user's device and is not sent off the device in a way that can identify the end-user or
device." RepGarden has no advertising and no data broker, so no App Tracking Transparency prompt is
needed and the label declares no tracking. The IDFV may be used for first-party analytics without
the ATT framework. Note also that **5.1.2(i)** bars gating: "Your app may not require users to
enable system functionalities (such as push notifications, location services, tracking) in order to
access functionality, content, use the app, or receive monetary or other compensation", and
5.1.3(i)/5.1.2(vi) forbid using health, fitness, camera or photo data for marketing or
advertising at all.

### Push notifications

**Apple 4.5.4** — "Push Notifications must not be required for the app to function, and should not be
used to send sensitive personal or confidential information. Push Notifications should not be used for
promotions or direct marketing purposes unless customers have explicitly opted in to receive them via
consent language displayed in your app's UI, and you provide a method in your app for a user to opt
out from receiving such messages." A workout reminder is operational, so no separate marketing consent
is needed — but it must not carry sensitive detail in the notification text, the app must work with
notifications off, and **4.10** means push cannot itself be monetised.

**Google** has no general marketing-consent rule for push; the nearest clause is in Deceptive
Behavior: "We don't allow apps or ads that mimic or interfere with system functionality, such as
notifications or warnings. System level notifications may only be used for an app's integral features,
such as an airline app that notifies users of special deals, or a game that notifies users of in-game
promotions." No Play frequency cap or marketing-consent rule was found; recorded as not verified.

On Android the runtime permission matters: "Android 13 (API level 33) and higher supports a runtime
permission for sending non-exempt … notifications from an app: POST_NOTIFICATIONS", and "If the user
selects the don't allow option, your app can't send notifications". Target Android 13 or higher so the
prompt can be asked in context rather than fired at launch. If reminders are built as exact alarms,
Google's restricted-permission rules apply: "USE_EXACT_ALARM is a restricted permission and apps must
only declare this permission if their core functionality supports the need for an exact alarm", with
review and possible refusal. A workout reminder is better served by an inexact scheduled notification
or by SCHEDULE_EXACT_ALARM.

### Subscription disclosure, if a subscription is ever sold

Apple **3.1.2(c)** — "Before asking a customer to subscribe, you should clearly describe what the user
will get for the price." Schedule 2 §3.8(b) sets the minimum: the title, "Length of subscription",
"Price of subscription, and price per unit if appropriate", and "Links to Your Privacy Policy and Terms
of Use must be accessible within Your Licensed Application." Guideline **4.9** imposes the same for
recurring Apple Pay charges: the renewal term and that it continues until cancelled, what is provided
each period, the actual charges, and how to cancel.

Google requires the same plus a cancellation route: "You must be transparent about your offer. This
includes clearly and explicitly disclosing your offer terms, the cost of your subscription, the
frequency of your billing cycle, the automatic renewal terms, whether a subscription is required to
use the app, and any other material information about the subscription", and "you must ensure that
your app(s) clearly disclose how a user can manage or cancel their subscription. You must also include
in your app access to an easy-to-use, online method to cancel the subscription."

### Agreements, metadata and who submits the app

- **Paid Applications Agreement** — Schedules 2 and 3 of the Apple Developer Program License
  Agreement. Apple: "Acceptance of the latest version in App Store Connect is required to offer paid
  apps and in-app purchases." A free app with no in-app purchase does not need it; a bank account and
  tax forms become necessary the moment it does.
- **Review notes, Apple 2.3.1(a)** — "All new features, functionality, and product changes must be
  described with specificity in the Notes for Review section of App Store Connect (generic
  descriptions will be rejected) and accessible for review."
- **Who submits it, Apple 4.2.6** — "Apps created from a commercialized template or app generation
  service will be rejected unless they are submitted directly by the provider of the app's content.
  These services should not submit apps on behalf of their clients and should offer tools that let
  their clients create customized, innovative apps that provide unique customer experiences. Another
  acceptable option for template providers is to create a single binary to host all client content in
  an aggregated or 'picker' model." This is the decisive clause if RepGarden is ever sold to a second
  trainer: either one multi-trainer app, or each trainer submits from their own Apple Developer
  organisation account. Trainerize's custom-branded-app documentation reflects the same constraint — it
  requires the gym or studio to enrol as an organisation with a DUNS number, and warns that Apple
  rejects apps whose name does not match the registering business until ownership is proved.
- **Google's metadata rules** — "We don't allow apps with misleading, improperly formatted,
  non-descriptive, irrelevant, excessive, or inappropriate metadata", and "We also don't allow
  unattributed or anonymous user testimonials in the app's description." Also, "Apps that attempt to
  modify or obfuscate behavior during review" is a named Deceptive Behavior violation, which is the
  clause a demo-only mode would be judged against. Reviews may not be incentivised: "Asking users to
  rate your app while offering an incentive" is a named violation.
- **Apple 2.5.19**, new on 16 October 2026 — "Don't include any hidden, dormant, or undocumented
  features in your app; your app's functionality should be clear to end users and App Review."
  Anything built for a later phase and shipped disabled now is a risk.

## Checklist for RepGarden's MVP

| Requirement | Where it comes from | What we build or write | Store |
|---|---|---|---|
| A working trainer account and a working client account with real assigned workouts, plus notes explaining the model | Apple 2.1(a) and App Review help ("use the Notes field to add additional credentials for each type"); Google "Sign-in details" | Two seeded demo accounts that do not expire, kept alive between releases; review notes saying clients are invited by a trainer and the trainer side is a web app | Both |
| No price, paywall, checkout or payment link anywhere in the client app | Apple 3.1.1 and the 3.1.3 preamble; Google Payments policy anti-steering and the consumption-only route | The trainer bills on the web; the app shows programme state only. At most, Google-style wording without a link if ever needed | Both |
| Answer the Digital Goods and Services questionnaire | App Store Connect help | Answer "No" to "Can customers consume digital goods and services in this app?" while payment stays off-app. Note the EU answer locks for 12 months | Apple |
| Native app, not a web view of the trainer tool | Apple 4.2 and 4.2.3(i); Google "Webviews and Affiliate Spam" and "Limited Functionality and Content" | Native calendar, logging, camera capture and offline behaviour | Both |
| Invitation opens the app, not Safari | Apple account-deletion help ("linking out to the default web browser to sign in or register an account … isn't appropriate, per App Review Guideline 4") | Universal link or invite code; the password is set in the app | Apple |
| In-app account deletion that removes the record and the data | Apple 5.1.1(v) and its help page; Google Account Deletion Requirement | Delete control in account settings; deletes the account, logs and uploaded videos; states how long it takes | Both |
| A web page where deletion can be requested without the app | Google Account Deletion Requirement ("A link to this web resource must be entered in the designated URL form field within Play Console") | A page on the GadirLabs or RepGarden site naming the app, with a working request route; the URL entered in Play Console | Google |
| In-app reporting on any video or note | Apple 1.2; Google UGC policy, "specified set of users … must provide in-app functionality to report content and users" | Report control on each video and note, with a stated response time and a logged queue | Both |
| In-app blocking | Google UGC policy, "UGC features that enable 1:1 user interaction … must provide an in-app functionality for blocking users"; Apple 1.2 ("The ability to block abusive users") | Client can leave or block their trainer; trainer can remove a client; access revoked immediately | Both |
| Terms accepted before the first upload, defining what may not be uploaded | Google UGC policy ("Requires users accept the app's terms of use … before users can create or upload UGC") | Terms screen at first sign-in, with an upload rule; a described manual review on report answers Apple's filtering bullet | Both |
| Published contact details | Apple 1.2 and 1.5 | Support email in the app and on the Support URL; the entity named | Apple |
| Consent and a visible indicator when recording | Apple 2.5.14; Google health-permission disclosure ("prominently disclose how user data will be used … and have the user provide affirmative consent") | Camera purpose string, an in-app explanation before first capture, and a recording indicator | Both |
| No broad media permissions | Google Photo and Video Permissions policy | Record in-app with CAMERA, or use the Android Photo Picker; do not declare READ_MEDIA_IMAGES or READ_MEDIA_VIDEO | Google |
| Health apps declaration | Google Health content and services; the declaration help page ("All developers that have an app published on Google Play must complete the Health apps declaration") | Declare "Health and fitness — Activity and Fitness"; do not declare Physical Therapy and Rehabilitation | Google |
| "Not a medical device" disclaimer plus a consult-a-professional reminder | Google Health content and services ("Other health and medical apps must include a clear disclaimer in their app description …") | The exact sentence in the Play listing, mirrored in the App Store description and shown in the app at onboarding | Google, and worth doing for Apple |
| Regulated medical device declaration | App Store Connect help; mandatory for Health & Fitness apps on the UK, EU and US stores | Answer No | Apple |
| Age rating answered as wellness, not medical | Apple age-rating definitions ("Health or Wellness Topics … exercise recommendations") | Answer Health or Wellness Topics; do not answer Medical or Treatment Information | Apple |
| Privacy policy on an open, non-editable URL, linked in the store and in the app | Apple 5.1.1(i); Google privacy policy and Health policy requirements | One policy covering data collected, purposes, lawful basis, recipients, retention, deletion, how to withdraw consent, a contact point, and the named entity. HTML, not PDF, and not geofenced | Both |
| Privacy labels | Apple App privacy details | Declare Contact Info, Identifiers, Fitness (and Health if body data is collected), Photos or Videos, Other User Content, linked to identity, App Functionality; no tracking | Apple |
| Data safety form | Google Data safety policy | Declare Fitness info, Health info if applicable, Photos, Videos, name and email; required vs optional; encryption in transit; a deletion request route | Google |
| No marketing use of health, fitness, camera or photo data | Apple 5.1.3(i) and 5.1.2(vi); Google Personal and Sensitive User Data | No ad SDK; no analytics on logged training data; no third-party sharing beyond the host as a service provider | Both |
| No tracking prompt, and no gating on system permissions | Apple 5.1.2(i) | No ATT prompt, no advertising identifier; the app works with notifications denied | Apple |
| Operational-only push, with opt-out | Apple 4.5.4; Android POST_NOTIFICATIONS | Reminders only; no sensitive detail in the body; an in-app toggle; target Android 13+ and ask in context | Both |
| Explicit consent for health data, on top of contract | UK GDPR Articles 6 and 9; ICO's fitness-instructor example | A separate, unticked explicit-consent step at first sign-in naming training and health data, withdrawable, recorded with a timestamp | Neither store — UK law |
| Privacy information delivered with the invitation | UK GDPR Article 14 and its one-month / first-communication timing | The invitation email carries the privacy notice, including the categories of data the trainer supplied and the source | Neither store — UK law |
| A decision, in writing, on controller or processor, plus an Article 28 contract if processor | ICO controller/processor guidance; Article 28(3) | Choose one, state it in the privacy policy, and write the trainer contract with all eight Article 28 terms | Neither store — UK law |
| A retention schedule and an export route | UK GDPR Article 5(1)(e) and Article 20; ICO storage limitation | How long logs and videos are kept after coaching ends; a machine-readable export of a client's own logs, notes and videos | Neither store — UK law |
| A DPIA | ICO special category guidance; Children's code standard 2 if in scope | A short DPIA covering health data, video of identifiable people and the trainer's visibility | Neither store — UK law |
| ICO data protection fee | Data Protection (Charges and Information) Regulations 2018 | Tier 1, £52, for whoever is the controller; tell Benji he likely owes it too | Neither store — UK law |
| Adults only at launch, or the Children's code in full | ICO Children's code ("more general health, fitness or wellbeing apps or services are covered") | 18+ in the terms, trainer confirms at invitation, age rating and Play target audience set to adults; document the decision | Both, plus UK law |
| Submitted by Gadir Tech Ltd as an organisation, one app not one per trainer | Apple 4.2.6 and 5.1.1(ix) | One RepGarden listing from the organisation account; if a trainer wants their own branded app, they enrol and submit it | Both |
| No hidden or dormant features | Apple 2.5.19; Google Deceptive Behavior | Ship gamification, AI analysis and messaging when they are built, not disabled in the binary | Both |

## Sources

All read 26 October 2026.

**Apple**
- App Review Guidelines, "Last Updated: October 16, 2026" — https://developer.apple.com/app-store/review/guidelines/
- Updated App Review Guidelines are now available, 16 October 2026 — https://developer.apple.com/news/?id=92th7e5i
- 5.1.1(v) Offering account deletion in your app — https://developer.apple.com/help/app-review/guideline-reference/5-1-1-account-deletion (also served at https://developer.apple.com/support/offering-account-deletion-in-your-app/)
- Provide information for a complete review — https://developer.apple.com/help/app-review/before-submitting-for-review/complete-review
- App privacy details on the App Store — https://developer.apple.com/app-store/app-privacy-details/
- User privacy and data use (App Tracking Transparency) — https://developer.apple.com/app-store/user-privacy-and-data-use/
- Age ratings values and definitions — https://developer.apple.com/help/app-store-connect/reference/app-information/age-ratings-values-and-definitions
- Declare regulated medical device status — https://developer.apple.com/help/app-store-connect/manage-app-information/declare-regulated-medical-device-status
- Complete the Digital Goods and Services questionnaire — https://developer.apple.com/help/app-store-connect/manage-app-information/complete-the-digital-goods-and-services-questionnaire
- App Store Small Business Program — https://developer.apple.com/app-store/small-business-program/
- Paid Applications Agreement, Schedules 2 and 3 (UK English) — https://developer.apple.com/support/downloads/terms/schedules/Schedule-2-and-3-English-UK.pdf, listed at https://developer.apple.com/support/terms/
- Changes for apps in the European Union — https://developer.apple.com/support/apps-in-the-eu/
- Payment options on the App Store in the EU — https://developer.apple.com/support/communication-and-promotion-of-offers-on-the-app-store-in-the-eu/
- Unlisted app distribution — https://developer.apple.com/support/unlisted-app-distribution/
- Apple Newsroom, changes for apps in the EU, 18 August 2026 — https://www.apple.com/newsroom/2026/08/apple-announces-changes-for-apps-in-the-european-union/

**Google**
- Developer Program Policy, "effective September 30, 2026, unless otherwise stated" — https://support.google.com/googleplay/android-developer/answer/17190352
- Prepare your app for review (Sign-in details) — https://support.google.com/googleplay/android-developer/answer/9859455
- Understanding Google Play's Payments policy — https://support.google.com/googleplay/android-developer/answer/10281818
- User Generated Content policy — https://support.google.com/googleplay/android-developer/answer/9876937
- Health content and services — https://support.google.com/googleplay/android-developer/answer/16679511
- Health apps declaration form — https://support.google.com/googleplay/android-developer/answer/14738291
- Health apps categories and permissions — https://support.google.com/googleplay/android-developer/answer/13996367
- Data safety form — https://support.google.com/googleplay/android-developer/answer/10787469
- Account deletion requirements — https://support.google.com/googleplay/android-developer/answer/13327111
- Target audience and content — https://support.google.com/googleplay/android-developer/answer/9285070
- Photo and Video Permissions — https://support.google.com/googleplay/android-developer/answer/14115180
- Billing choice program — https://support.google.com/googleplay/android-developer/answer/17161464
- User choice billing — https://support.google.com/googleplay/android-developer/answer/13821247
- External offers program (EEA) — https://support.google.com/googleplay/android-developer/answer/14372887
- Changes to Google Play in the US (Epic v Google compliance) — https://support.google.com/googleplay/android-developer/answer/15582165
- Alternative billing in the US — https://support.google.com/googleplay/android-developer/answer/16497028
- External content links program (US) — https://support.google.com/googleplay/android-developer/answer/16470497
- New service fee model — https://support.google.com/googleplay/android-developer/answer/16954621
- Notification runtime permission — https://developer.android.com/develop/ui/views/notifications/notification-permission

**Law and regulators**
- UK GDPR Articles 4, 8, 9, 13, 14, 17, 20, 26, 28 and Recital 35 — https://www.legislation.gov.uk/eur/2016/679/
- DPA 2018 s.9 (repealed 31 December 2020) — https://www.legislation.gov.uk/ukpga/2018/12/section/9
- ICO, What is special category data? — https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/special-category-data/what-is-special-category-data/
- ICO, What are the rules on special category data? and What are the conditions for processing? — same guidance set
- ICO, When is consent appropriate? — https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/consent/when-is-consent-appropriate/
- ICO, Controllers and processors — https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/controllers-and-processors/controllers-and-processors/
- ICO, What needs to be included in the contract? — https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/contracts-and-liabilities-between-controllers-and-processors-multi/what-needs-to-be-included-in-the-contract/
- ICO, Right to be informed, Right to erasure, Right to data portability, Storage limitation — https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/
- ICO, Age appropriate design code: services covered, code standards, standards 3, 7, 8, 11, 12, Annex C — https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/age-appropriate-design-a-code-of-practice-for-online-services/
- ICO, Biometric data guidance — https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/biometric-data-guidance-biometric-recognition/
- ICO, ICO urges all app developers to prioritise privacy, February 2024 — https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2024/02/ico-urges-all-app-developers-to-prioritise-privacy/
- ICO, Data protection fee and exemptions — https://ico.org.uk/for-organisations/data-protection-fee/
- CMA, Apple's mobile platform and Google's mobile platform case pages — https://www.gov.uk/cma-cases/apples-mobile-platform and https://www.gov.uk/cma-cases/googles-mobile-platform
- CMA, consultation on a Steering conduct requirement for Apple, 30 June 2026 — https://assets.publishing.service.gov.uk/media/6a42a56a3413112faed80e26/Consultation_document__Apple_steering_.pdf
- Ninth Circuit, Epic Games v Apple, No. 25-2935, 11 December 2025 — https://cdn.ca9.uscourts.gov/datastore/opinions/2025/12/11/25-2935.pdf
- Supreme Court docket, Apple Inc. v. Epic Games, Inc., No. 25-1311 — https://www.supremecourt.gov/

**Market evidence**
- TrueCoach on the App Store — https://apps.apple.com/us/app/truecoach/id1439127794
- TrueCoach Payments — https://help.truecoach.co/en/articles/3497458-truecoach-payments
- TrueCoach client onboarding — https://help.truecoach.co/en/articles/2950800-client-accessing-my-truecoach-account-for-the-first-time
- Fitness App (ABC Trainerize) on the App Store — https://apps.apple.com/us/app/fitness-app-abc-trainerize/id516851502
- Everfit public client invite link — https://help.everfit.io/en/articles/5369004-public-client-invite-link
- Everfit Stripe setup — https://help.everfit.io/en/articles/5719145-how-to-set-up-payments-connect-with-stripe
- FITR web checkout for clients — https://support.coachwithfitr.com/en/articles/9853029-how-to-subscribe-to-a-program-web-checkout-client
- FITR pricing — https://support.coachwithfitr.com/en/articles/11938629-fitr-pricing-overview-coach
- Hevy Coach pricing — https://hevycoach.com/pricing/
- Hevy Coach, invite clients — https://help.hevycoach.com/en/articles/8460760-invite-clients

**Practitioner accounts, labelled as such and not policy**
- Guideline 4.2, "small, or niche, set of users" — https://developer.apple.com/forums/thread/115363
- Invite-only app resolved by unlisted distribution — https://news.ycombinator.com/item?id=47916438
- "Will an invite only app be accepted?" — https://developer.apple.com/forums/thread/23663
- 3.1.1 rejection, B2B SaaS, existing accounts only — https://developer.apple.com/forums/thread/811018
- 3.1.1 and Stripe signup, with an Apple engineer's reply — https://developer.apple.com/forums/thread/744873
- 3.1.1 rejection for an in-app Stripe paywall — https://developer.apple.com/forums/thread/799798
- Account deletion and client-provisioned accounts, a reported phone call — https://developer.apple.com/forums/thread/738232
- Demo accounts where users exist only in a client's directory, unanswered — https://developer.apple.com/forums/thread/726347

## Not verified

- Whether a US link-out commission rate has been set since Apple's 13 August 2026 proposal; no order was found.
- Whether Apple's 1 January 2026 EU fee structure (2% initial acquisition fee, 5%/13% store services tiers) was ever billed before 1 October 2026.
- Any Apple source stating whether guideline 1.2 applies to strictly one-to-one private uploads; the 24-hour response expectation comes from developers quoting rejection letters.
- Any Google Play clause exempting an app from the Sign-in details requirement because accounts are invite-only.
- Any Google Play frequency cap or marketing-consent rule for push notifications.
- Any current Google page using "store services fee" or the Tier 1 / Tier 2 split; the live EEA page gives a 0% initial acquisition fee effective 4 June 2026.
- Whether a bare set, rep and weight log, with no health inference, is "data concerning health" under UK GDPR; the ICO addresses fitness trackers and fitness apps but not this boundary.
- Any ICO guidance on a coach or trainer, as distinct from a parent, viewing a child's data.
- Any ICO enforcement action against a fitness or personal-training app.
- Everfit's own platform fee percentage.
