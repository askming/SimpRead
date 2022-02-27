> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [copyconstruct.medium.com](https://copyconstruct.medium.com/know-how-your-org-works-or-how-to-become-a-more-effective-engineer-1a3287d1f58d)

> A few months ago, exhausted by a constant stream of people perennially disappointed about reward stru......

A few months ago, exhausted by a constant stream of people perennially disappointed about reward structures at companies, I made what seemed to me a fairly non-controversial statement:

Some of the responses to this were, well, rather pointed. Most people’s dismay seems to have stemmed from the exasperation around “well, shouldn’t I ever try to make anything better, then?”, which is a very reasonable concern.

I’ve been meaning to expand on some of my thoughts on this topic for months, since I felt this warranted a more nuanced and considered discussion than feasible on social media.

This post aims to lay out some of the problems engineers might often encounter and some food for thought on how to be more effective working within the limitations and constraints of organizations.

One caveat I need to mention here is that most of what I describe here is from the perspective of an individual contributor (IC). I’ve never been a manager and have no experience navigating organizational politics as a manager. There are innumerable resources from seasoned managers on how to manoeuvre managerial politics, for those interested.

The Mirage of Aspiration
------------------------

The vast majority of what passes for social media discourse on fairly _any_ topic is fairly aspirational (or cantankerous or plain nasty). Much of such discourse gets amplified to a degree not commensurate with the underlying sagacity. None of this is productive; worse, it gives impressionable people a fairly warped idea of how organizations _must_ function. It’s rather disheartening to see aspirational goals get exalted to such heights that anything that doesn’t scale to their quixotic ideal is often deemed as “toxic” or “dysfunctional” by many.

For a more concrete example, a common talking point is often technical debt. Yes, ideally we should have a culture that prioritizes minimizing technical debt and sustainably building software, not just shipping features. But you’d be very hard-pressed to find a single team or organization that will _ever_ prioritize addressing technical debt _as the primary focus_ for anything beyond maybe a week or two, as opposed to fixing crucial bugs (a _symptom_ of the accumulated technical debt, for sure) or shipping something of value to the company. If your team is hitting all the deliverables on time, then there might be appetite for addressing the issue of technical debt, but in the vast majority of cases, addressing technical debt needs to be undertaken iteratively, aiming for small and easy wins that will inspire confidence and lay the groundwork for you to push for bigger and better improvements without impacting the clip at which your team is shipping.

Social media, blog posts and conferences amplify aspirational ideas. There’s nothing wrong with this in my opinion — it’s important to constantly keep pushing the envelope further, after all.

Your organization, however, rewards _what you actually get done_ that benefits the organization, which might be a very far cry from whatever might be _de rigueur_ on social media.

Know How Your Org Works
-----------------------

One of the _most_ _effective_ things you can do to be successful at your job is to understand how your organization works. This understanding will better inform your outlook on everything from:

*   exactly _what_ technical skill you need to invest effort into getting better at that _will actually be rewarded_
*   how to build lasting relationships with other people on your team or organization that will ultimately dictate the success of a project
*   how to effectively pitch projects or improvements and see these through to completion
*   how to navigate ambiguity
*   how to manage conflicting priorities or expectations
*   how to best deal with setbacks
*   how to weigh the pros and cons of technical choices in the larger context of the organizational realities and needs
*   how to identify and drive quick wins
*   how to discern what’s achievable in precisely what time frame
*   how to use this knowledge to judiciously pick battles
*   and in the worst case, to know when to cut your losses and quit

Managers need to deal with these skills as a part of their job description. So do ICs at the very senior levels, but it’s never too early to start cultivating this knowledge. In fact, a core part of mentoring engineers needs to be schooling them in _how the organization works,_ which will then enable them to build a successful track record of _getting things done._

Shielding non-senior engineers from organizational politics not just stymies their growth but also hinders their visibility into the skills they’d eventually need to learn the hard way, skills for which there exists no easy playbook, even if some managers and senior ICs might take a more short-sighted view and see this as a way to help other engineers “maintain focus”.

Soft Skills Are Hard Skills
---------------------------

This post doesn’t aim to be a comprehensive guide on how to learn such skills, or even a comprehensive list of these skills. What’s worse, there are _no_ fixed set of answers to many of these questions, since there aren’t even a fixed set of _questions_ to begin with. The questions mentioned in this article are simply the ones _I’ve_ encountered. If you were to ask someone else, you might get a very different list. Learning is relatively easy when you know exactly _what_ to learn and _how_ to learn it, and so long as the answer is _unchanging_ (as is the case with many purely technical concepts).

Learning how your organization works is a constant exercise in learning the unknown-unknowns, and in particular, knowing when the answers you’ve arrived at have expired or aren’t fit for purpose anymore. Learning how to make decisions when key pieces of information are missing is also a very important skill, insomuch as it helps you hone another set of valuable skills:

*   how best to gather information you’re missing
*   how and when to get by _without_ doing so

Some of these skills I’m talking about can be learned by talking to people, some needs to be inferred through close observation, and some of this can only be learned the hard way by getting things wrong (or watching other people get things wrong). In organizations that have a culture of constant learning, visibility into failures isn’t something that’s discouraged, though, again, whether _your_ organization is one such which subscribes to this school of thought is something you’d only get to know _if you know how your organization works_. In _particular_, in the remote-first world we’ve all been thrust into.

The most important skill for any engineer to posses is the ability to _learn quickly_. This applies to both technical concepts and sociotechnical concepts. I’m by absolutely no means whatsoever an expert in any of these myself, but over the years, I’d like to think I’ve got a better understanding of _why_ this knowledge is important.

Understand Implicit Hierarchies
-------------------------------

Most organizations have a formal structure. This usually starts with a VP or a director at the top, down to individual teams. If you’re an IC, you’re a leaf node in the org tree.

Most organizations, in my experience, also tend to have something of an _informal_ structure, especially among the ICs. In organizations that make the job titles and levels public, it’s relatively easy to know which engineer might have more clout and influence. In organizations where this is implicit, it’s a lot harder to infer this informal hierarchy, and where exactly you fit in. Sometimes, it’s not so much to do with job titles and levels than with tenure on the team or the organization. And sometimes, it’s some other factor, like subject matter expertise, open source experience, or even something as arbitrary as past employment history.

It’s important to be aware of this informal hierarchy, because as often as not, your work might end up being directly influenced by this hierarchy, irrespective of whatever your personal level and job title might be.

Engineers who wield this influence tend to often to fairly senior, and also tend to be fairly opinionated (and many a time, it isn’t even so much an _opinion_ than _overarching philosophies_ which guide most of their thinking and decision making). These opinions they hold could’ve shaped everything from the way your codebase is structured, to the tooling in use, to the way you test or deploy a system, to the way the system is architected, to the reason why they did or didn’t choose a technology to work with or a team to partner with, to the reason why some things might seem “broken” but never prioritized, and more.

These philosophies (and opinions born and bred thereof) might inevitably end up influencing _your_ efforts to make any change or improvements to the existing system. Unless you understand “why” things are the way they are (and there often is a method to every madness, if you’re patient to dig deep enough), any proposal you might have on “how” to improve the situation might end up very much going against the grain, making it that much more of an uphill task for your proposal to be accepted. Furthermore, it’ll make it seem as though you put in no effort to understand the history of the system, which doesn’t exactly breed a lot of confidence into why you should be entrusted with fixing the system.

Your efforts, as such, need to be multi-pronged:

*   Understand the implicit organizational hierarchy
*   Identify the people who wield undue influence and their way of thinking and general philosophies (by either talking to them, or other people in the organization, or researching their past work, reading any articles or blog posts they might have written, or talks they might have presented, etc.)
*   Identify how the aforementioned philosophies have been previously _successfully_ applied to projects and teams they were on. _Why_ were these efforts considered successful? What were the problems these philosophies solved, and what were the problems they _didn’t_ solve (or exacerbated)?
*   How do you build credibility with them? Can you lean on your past work? Your subject matter expertise? Your previous track record? Is there someone _they_ trust and respect who can vouch for you, for them to take a leap of faith and agree to do things “your” way?

These are all things to consider before making proposals to change a system. Smaller changes might not require this level of circumspection (and might be a good way to net a lot of easy wins), but for anything more involved (and of higher impact), learning _how_ and _why_ your organization makes technical decisions is a non-negotiable requirement.

Cultures: Top-Down, Bottom-Up, and Both
---------------------------------------

Irrespective of titles and hierarchies, most organizations also have a somewhat top-down or bottom-up _culture_ (or a mix of both). I’ve worked in both settings and have seen enough to know that neither one is better than the other. It depends on the kind of engineers you’re working with, their general level of technical skill and experience, their previous experience with various pieces of technology, their background and more.

A top-down culture is one where the most important decisions are made from the top down. The person making the final decision could be either a tech lead, sometimes a manager, or a director level executive. On such teams, a large part of your success boils down to “managing up”. Successfully managing up, in turn, requires grappling with questions with respect to decision maker such as:

*   Are you on the same wavelength as them? Do you both attach the same salience to the problem in question? If not, are you up to the task of impressing upon them the importance and urgency of the problem?
*   Is there some information or knowledge they have (and you don’t) that informs their thinking on the matter? How best can you get this information?
*   Do you both share the same view of the opportunity cost?
*   What are their implicit and explicit biases? What are their blind spots? Can you use some of these to your advantage?
*   What are the things they generally value? What kind of work or behavior impresses them?
*   Is there any specific abstraction or process or methodology they are particularly attached to? Can you lean in on these to more effectively market your opinion to them?
*   What’s the timeline they are comfortable working with to solve the problem? A month? A perf cycle? Many years?
*   What’s your personal level of trust with them? Will they go to bat for you?
*   What does “success” mean to them, and how do they measure it? How have they _typically_ measured it for work that’s in-progress?
*   How do they typically handle setbacks? Have you drawn up contingency plans and discussed it with them?
*   How do they handle failure? Do they assume any responsibility for it, or will you be scapegoated (and possibly fired)?
*   Do they have a culture of blameless postmortems for large-scale team or organizational failures? Are these lessons shared and discussed transparently with everyone on the team and in the organization?
*   What is their previous experience working with partner teams or organizations?
*   Have they been burned badly in the past working with another organization or another team?
*   What’s their organizational reputation? Are they well-liked? Well-respected?
*   How conflict-averse (or not) are they?

Knowing the answer to many of these questions can give you a sense of how best to identify problems, propose solutions, see them through and demonstrate a level of impact that might advance your career meaningfully.

On **bottom-up** teams, the challenge is to manage _laterally (_in _addition_ to managing-up). This includes grappling with conundrums like:

*   How do you build consensus amongst your peers when there’s no top-down decision making authority?
*   How do you break down barriers between different peers?
*   How do conflicts get resolved if there’s no higher authority to mediate? Does it boil down to nitty-gritty quantitative details like metrics, or something more nebulous such as “likeability”?
*   If all key ideas have to originate from the bottom, which ones makes it to the top? How has this worked in the past?
*   Can “code” solve all issues? Can you go prototype an idea you have and then successfully pitch it? Does your team or organization empower you to do this during your business hours, or are you willing to spend your nights and weekends pursuing this goal?
*   Has the problem you’re trying to solve been attempted before? How did that attempt go? What were the failures? Do you understand the proximate cause of these failures? Are you sure you won’t run into the same issues again?
*   What’s the opportunity cost? Can you convince your peers that it’s worth solving right away if it hasn’t been prioritized so far?
*   What’s your scope of influence? Does it extend to just your team, your team and sister teams, or your entire org? Are people outside your team willing to give your solution a whirl?
*   How do you convince different people or teams with different incentives? Is this something you can even do without top-down support?
*   How do you ensure adoption, especially cross-organizational adoption?
*   How do you enlist partners or advocates for your effort? Are there other teams ready to adopt your solution, if you were just to build it, and advocate for it?
*   Do you have key relationships with the stakeholders? Do they trust you? If not, why not? And how would you go about building this trust?
*   How do you convince your peers who’ve had previous bad experiences with your team or project in the past?
*   How do you build credibility?
*   How do you motivate and incentivize your peers in general?
*   What’s the cost of failure? Just one fair to middling perf cycle, or something worse? Who’ll be impacted? Just you? Or your entire team?
*   What are the cultural problems you perceive? In a bottom-up setting where there’s no higher authority that can mandate teams to change how they work, how do culture problems get fixed?

There are many organizations that are top-down in some respects and bottom-up in others. On such teams, you’d need to employ a mix of strategies to successfully thread the needle for many of these issues and chaperone your ideas through to successful execution.

Get comfortable with the “mess”
-------------------------------

Most organizations value and reward people who “get things done”.

You’re _far_ likelier to encounter codebases that have “evolved” over time, with poor documentation, lots of outdated comments and often with little to no tests than you are to encounter ones which are perfectly documented, have well-tested public and internal APIs, and code which is perfectly obvious.

You’re going to _far more productive_ if you learn how to navigate such codebases successfully, which involves learning some of the following:

*   how to gather just the right amount of information to get on with your task
*   how _not_ to get too caught up in the weeds unless required
*   how to read a lot of code at a fast clip and come away with a reasonably good mental model of what it’s trying to do
*   how to come up with hypothesis and use a variety of general purpose techniques and tools to validate the hypothesis
*   how to reproduce bugs quickly without elaborate local configurations and setups
*   and more.

These skills aren’t typically taught in college. They’re seldom talked about on social media or even conferences. It plays to the gallery to harp on about the importance of tests or documentation. I’m not trying to minimize their importance myself. But dealing with mess and ambiguity is a key skill to hone to improve your own productivity when working with code.

The same philosophy applies when working with sociotechnical systems like organizations: _get comfortable with mess_. You’re _far_ likelier to encounter organizations comprising of teams and leaders of:

*   varying levels of skill and ability to deliver on their promises
*   varying (sometimes even opposing) incentives and reward structures
*   varying appetites for risk or change
*   varying philosophical views on software development and systems
*   varying levels of tolerance for failure
*   varying willingness to make investments (in people and projects) with a long-term view in mind

Being successful in such organizations requires quickly learning the topology of the organization and charting pathways to navigate it. Your “personal ideal” might be very much incongruent to the reality on the ground. I’m cynical enough to believe that everyone ultimately is looking out for their own self-interest, and you need to look out for yours.

Get comfortable with mess and seek out ways to untangle it or work around it. Seek alignment when interests align. Be able to identify quickly when such alignment will always prove elusive. Be quick to dissociate amiably when interests are irrevocably in conflict. Know when to batten down the hatches, but more importantly, also know when to cut your losses. Be transparent. Treat people with respect and humility, even when they disagree with you or when you feel they are mistaken (or seemingly acting against the best interests of the team or organization — it could very well be _you_ who fails to appreciate their predicament).

Look For Small (And Any) Wins
-----------------------------

It might take you way longer to truly get the measure of your organization’s sociotechnical politics than to get to speed with a codebase. To build credibility, you need to demonstrate some degree of impact early on, instead of waiting for months to get a lie of the land before you start getting anything done. Chasing small wins and low hanging fruit can be an easy path to productivity. Don’t underestimate the importance of this.

Understand Org Constraints and Manage Your Expectations
-------------------------------------------------------

It’s important to mention that individual managers (much less ICs), can sometimes do only so much when it comes to solving some of the more entrenched organizational problems. DEI is one that comes to mind first. I’ve never seen this problem solved in a bottom-up manner successfully anywhere. Places that have made moderate progress often have enjoyed executive buy-in. Organizations that are serious about DEI have executive compensation tied to the success of DEI efforts.

It’s a folly for ICs or even managers to wade into fixing this issue by their lonesome, without explicit approval from their management chain (ideally with this work recognized in performance reviews). It’s one thing to truly feel passionate about this topic and want to help create change, but please be realistic about expectations and outcomes. Charity Majors wrote a [good post](https://charity.wtf/2021/03/07/know-your-one-job-and-do-it-first/) titled **Know Your “One Job” And Do It First**, and I largely agree with everything she says here.

This is also applicable to a lot of other issues regarding bringing about “wholesale culture change”. Unless you’ve been hired with the explicit mandate to bring about a change in culture (i.e., at the _executive_ level), be wary of embarking on sweeping, ambitious projects or efforts.

That doesn’t mean you don’t have the ability to create any change at all. The most effective instances of culture change I’ve seen have been _incremental_. It’s _far_ easier to identify incremental wins when you’ve already learned the ropes of succeeding within the existing (and flawed) cultural framework than were you to start from the ground up.

Another such example is the promotion process, which is perceived as a biased, opaque and arbitrary process at many companies. While the process might not work for certain ICs on a micro level, the process is the way it is because it clearly _works for the organization_, based on whatever metrics the organization is tracking that you might not be privy to.

Again, you can either learn how the organization’s promotion process works and play your cards right, or if the process seems so arbitrary and unfair you feel you will never have a shot at succeeding, you can try to switch organizations or companies where you feel you might have a fairer crack of the whip. Your manager might able to elaborate on the whys and the wherefores of this process, but managers have competing priorities to juggle and they cannot always guarantee that their primary focus will be the career growth of all of their direct reports at all times. Which, again, is why you need to understand _how your organization truly works_, because you might then be able to seek out people other than your manager who might mentor you into better understanding the organization’s way of doing things.

Conclusion
----------

It’s easy to dismiss much of what’s described in this post as “politics”. The unfortunate reality is that almost everything is political, and beyond a certain level, advancing further requires getting really good at playing this game.

This doesn’t necessarily have to be a negative thing per se, and I suspect the near ubiquitous negative connotations attached to “politics” can be attributed to the fact that a lot of engineers are often clueless when it comes to navigating these nuances, and find it far easier to label things that don’t go their way as “politics”, as opposed to introspecting and learning the hard skills required to make better judgements.

None of this is to suggest that pure technical skills are easy. They are not. As [Matt Klein says](https://twitter.com/mattklein123/status/1130206809308901376?s=20), it’s ALL hard. The reality is that you can have a very gratifying and rewarding career as an engineer if you’re good at the “purely tech” side of things without ever worrying about the kind of problems described here.

But you’re far more likelier to be one of those rare unicorn engineers (and to reiterate, I don’t consider myself to be one, since far be it from me to call myself an expert in the skills described here) who is a real force multiplier if you’re also:

*   good at _solving pressing problems_
*   relentlessly _getting things done_
*   successfully _creating change_ than just endlessly _talking_ about the need to do so

Which, alas, requires understanding how your organization works.