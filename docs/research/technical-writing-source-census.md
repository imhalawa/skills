# Technical-writing source census

**Phase:** 1 — candidate gathering and classification only  
**Verified:** 2026-07-31  
**Census size:** 29 candidates  
**Proposed Phase-2 sample:** 18 candidates

## Purpose and boundaries

This census identifies first-party or officially hosted material that could support a later comparative study of excellent technical communication for engineers and computer scientists. It records candidate sources, genres, relevance, and access constraints. It does **not** infer prose patterns, rank writing quality, or synthesize shared techniques.

“First-party” here means the writer, project, publisher, or engineering organization owns or officially hosts the artifact. An organization explaining its own system is first-party even when an individual employee is the named author. Official publisher excerpts and author talks are included for books when the full book is not openly available.

## Strata

1. Practitioner essayists and software-design authors
2. System-design educators and publications
3. Computer-science or algorithm educators using visual explanation
4. Engineering organizations with strong technical blogs or internal guides
5. Documentation, style, and pedagogy systems
6. Book authors with official excerpts, talks, or companion material

The primary stratum below is a sampling label, not a claim that a source fits only one category.

## Candidate census

### 1. Martin Fowler / martinfowler.com

- **Stratum:** 1 — practitioner essayist and software-design author
- **First-party home:** [martinfowler.com](https://martinfowler.com/)
- **Representative artifacts:** [Microservices](https://martinfowler.com/articles/microservices.html); [Strangler Fig](https://martinfowler.com/bliki/StranglerFigApplication.html); [Refactoring: This class is too large](https://martinfowler.com/articles/class-too-large.html)
- **Dominant format:** Long-form essay, short concept note, worked case study
- **Likely relevance:** A large, long-running corpus for explaining architecture vocabulary, software-design choices, and code transformation to working engineers.
- **Accessibility:** Public HTML with diagrams and stable article URLs. Some pages are co-authored or host colleagues' work, so Phase 2 must record the byline rather than treating the whole domain as Fowler-authored.

### 2. Joel Spolsky / Joel on Software

- **Stratum:** 1 — practitioner essayist
- **First-party home:** [Joel on Software](https://www.joelonsoftware.com/)
- **Representative artifacts:** [The Law of Leaky Abstractions](https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/); [Back to Basics](https://www.joelonsoftware.com/2001/12/11/back-to-basics/)
- **Dominant format:** Practitioner essay with code and extended examples
- **Likely relevance:** Explains computer-science and systems ideas to software practitioners while connecting low-level mechanisms to design consequences.
- **Accessibility:** Public HTML. The corpus spans decades; older terminology, external links, and technology claims need historical context.

### 3. Dan Luu

- **Stratum:** 1 — practitioner essayist
- **First-party home:** [danluu.com](https://danluu.com/)
- **Representative artifacts:** [Computer latency: 1977–2017](https://danluu.com/input-lag/); [How web bloat impacts users with slow devices](https://danluu.com/slow-device/)
- **Dominant format:** Evidence-heavy essay and empirical case study
- **Likely relevance:** Long-form explanations that join measurements, systems behavior, user impact, and extensive source trails.
- **Accessibility:** Public, lightweight HTML. Articles can be long and link-dense; some depend on historical measurements or linked datasets that should be checked independently if factual evaluation enters Phase 2.

### 4. Julia Evans / Wizard Zines

- **Stratum:** 1 — practitioner essayist and visual educator
- **First-party home:** [jvns.ca](https://jvns.ca/)
- **Representative artifacts:** [How I got better at debugging](https://jvns.ca/blog/2015/11/22/how-i-got-better-at-debugging/); [Some ways to get better at debugging](https://jvns.ca/blog/2022/08/30/a-way-to-categorize-debugging-skills/); [What’s a network interface?](https://jvns.ca/blog/2017/09/03/network-interfaces/)
- **Dominant format:** Short essay, tutorial, illustrated/zine-derived explainer
- **Likely relevance:** A large body of explanations aimed at programmers learning operating systems, networking, debugging, and tools.
- **Accessibility:** Most blog posts are public HTML; many finished zines are paid products, so the public blog and free samples are the comparable corpus.

### 5. Bret Victor / WorryDream

- **Stratum:** 1 — software-design author and interactive essayist
- **First-party home:** [worrydream.com](https://worrydream.com/)
- **Representative artifacts:** [Learnable Programming](https://worrydream.com/LearnableProgramming/); [Explorable Explanations](https://worrydream.com/ExplorableExplanations/); [Up and Down the Ladder of Abstraction](https://worrydream.com/LadderOfAbstraction/)
- **Dominant format:** Interactive essay, visual demonstration, talk companion
- **Likely relevance:** Makes technical and representational arguments through prose, code, animation, and reader-controlled examples.
- **Accessibility:** Public and mostly self-contained, but interaction requires JavaScript and is not fully preserved by text extraction or print views.

### 6. ByteByteGo

- **Stratum:** 2 — system-design educator/publication
- **First-party home:** [bytebytego.com](https://bytebytego.com/)
- **Representative artifacts:** [Engineering Visual Guides](https://bytebytego.com/guides/); [System Design Blueprint: The Ultimate Guide](https://blog.bytebytego.com/p/ep56-system-design-blueprint-the); [System Design Interview: A Step-By-Step Guide](https://www.youtube.com/watch?v=i7twT3x5yv8)
- **Dominant format:** Visual explainer, newsletter, short video
- **Likely relevance:** A deliberately multi-format corpus for concise explanations of large-scale systems and system-design interviews.
- **Accessibility:** Many visual guides and newsletter posts are public, while courses and portions of the archive are paid. YouTube artifacts often lack an official edited transcript, and some newsletter posts bundle several unrelated mini-topics.

### 7. High Scalability

- **Stratum:** 2 — system-design publication
- **First-party home:** [highscalability.com](https://highscalability.com/)
- **Representative artifacts:** [Amazon Architecture](https://highscalability.com/amazon-architecture/); [Tagged Architecture: Scaling to 100 Million Users](https://highscalability.com/tagged-architecture-scaling-to-100-million-users-1000-server/); [Nifty Architecture Tricks from Wix](https://highscalability.com/nifty-architecture-tricks-from-wix-building-a-publishing-pla/)
- **Dominant format:** Architecture profile, curated case study, guest essay
- **Likely relevance:** A long historical archive of system architecture descriptions, scale numbers, platform inventories, and engineering lessons.
- **Accessibility:** Public HTML, but provenance varies: original editor synthesis, approved reposts, guest posts, and summaries of outside material coexist. Many classic profiles are old and contain dead outbound links or time-bound numbers. Phase 2 must distinguish first-person guest cases from editorial aggregation.

### 8. Hello Interview

- **Stratum:** 2 — system-design and interview educator
- **First-party home:** [Hello Interview Learn](https://www.hellointerview.com/learn)
- **Representative artifacts:** [System Design in a Hurry: Core Concepts](https://www.hellointerview.com/learn/system-design/in-a-hurry/core-concepts); [Scaling Writes](https://www.hellointerview.com/learn/system-design/patterns/scaling-writes); [Core Concepts Quick Reference](https://www.hellointerview.com/learn/system-design/in-a-hurry/core-concepts/quick-reference)
- **Dominant format:** Structured tutorial, visual quick reference, interview-focused deep dive
- **Likely relevance:** Explicitly scopes technical concepts to an identifiable audience and offers overview, deep-dive, pattern, and quick-reference variants.
- **Accessibility:** Substantial public text and diagrams are available, but some videos and advanced content require Premium. Pages are dynamic and may be revised in place, so Phase 2 should record access dates.

### 9. Amazon Builders’ Library

- **Stratum:** 2 — system-design publication backed by an engineering organization
- **First-party home:** [Amazon Builders’ Library](https://aws.amazon.com/builders-library/)
- **Representative artifacts:** [Timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/); [Avoiding insurmountable queue backlogs](https://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs/); [Leader election in distributed systems](https://aws.amazon.com/builders-library/leader-election-in-distributed-systems/)
- **Dominant format:** Practitioner essay and operational design guide
- **Likely relevance:** Senior Amazon engineers explain production-system choices, failure handling, and operational constraints.
- **Accessibility:** Public, but legacy `aws.amazon.com/builders-library/` URLs now redirect to dynamic AWS Builder Center pages. Browser rendering is more dependable than text-only retrieval.

### 10. Google Site Reliability Engineering books

- **Stratum:** 2 — system-design/operations publication
- **First-party home:** [Google SRE](https://sre.google/)
- **Representative artifacts:** [Site Reliability Engineering table of contents](https://sre.google/sre-book/table-of-contents/); [Load Balancing in the Datacenter](https://sre.google/sre-book/load-balancing-datacenter/); [Communication and Collaboration in SRE](https://sre.google/sre-book/communication-and-collaboration/)
- **Dominant format:** Open book chapter, reference, organizational case study
- **Likely relevance:** Combines systems mechanisms, operating practice, and engineering-management material for a professional audience.
- **Accessibility:** Full chapters are public HTML and bylined. The books are multi-author and organization-edited, so author, editor, chapter purpose, and publication date must remain separate variables.

### 11. VisuAlgo / Steven Halim and NUS contributors

- **Stratum:** 3 — visual algorithms educator
- **First-party home:** [VisuAlgo](https://visualgo.net/en)
- **Representative artifacts:** [Linked List, Stack, Queue, and Deque](https://visualgo.net/en/list); [Binary Search Tree and AVL Tree](https://visualgo.net/en/bst); [Recursion Tree/DAG notes](https://visualgo.net/en/recursion/print)
- **Dominant format:** Interactive visualization, e-lecture, printable notes, quiz
- **Likely relevance:** Pairs algorithm animation, pseudocode tracing, explanatory slides, and learner-controlled inputs.
- **Accessibility:** Core visualizations are free, but full interaction is best on a large screen with JavaScript. Some quiz, account, and NUS-class features differ for logged-in users; print views omit animation.

### 12. Red Blob Games / Amit Patel

- **Stratum:** 3 — visual computer-science educator
- **First-party home:** [Red Blob Games](https://www.redblobgames.com/)
- **Representative artifacts:** [Introduction to the A* Algorithm](https://www.redblobgames.com/pathfinding/a-star/introduction.html); [Hexagonal Grids](https://www.redblobgames.com/grids/hexagons/)
- **Dominant format:** Interactive visual tutorial and implementation reference
- **Likely relevance:** Explains graph search, coordinate systems, geometry, and algorithms through prose, pseudocode, diagrams, and manipulable examples.
- **Accessibility:** Public and self-contained. JavaScript/SVG are required for the full explanatory artifact, though the pages retain substantial text and code without interaction.

### 13. Distill

- **Stratum:** 3 — visual computer-science/ML publication
- **First-party home:** [Distill](https://distill.pub/)
- **Representative artifacts:** [Feature Visualization](https://distill.pub/2017/feature-visualization/); [How to Use t-SNE Effectively](https://distill.pub/2016/misread-tsne/)
- **Dominant format:** Peer-reviewed interactive article
- **Likely relevance:** Technical ML exposition integrating mathematical claims, experiments, figures, and live interactive controls.
- **Accessibility:** Public HTML, but Distill is on indefinite hiatus and the corpus is finite. Interactive behavior depends on browser execution; articles often have many contributors with distinct writing, research, and diagram credits.

### 14. Algorithm Visualizer

- **Stratum:** 3 — community visual algorithms educator
- **First-party home:** [Algorithm Visualizer](https://algorithm-visualizer.org/)
- **Representative artifacts:** [Bubble Sort](https://algorithm-visualizer.org/brute-force/bubble-sort); [Binary Search](https://algorithm-visualizer.org/branch-and-bound/binary-search); [Dijkstra’s Shortest Path](https://algorithm-visualizer.org/greedy/dijkstras-shortest-path)
- **Dominant format:** Code-linked interactive visualization
- **Likely relevance:** Makes program execution observable alongside implementation code across multiple languages.
- **Accessibility:** Public, dynamic, and open source. Individual visualizations are community-contributed and uneven in prose depth, categorization, and maintenance; authorship metadata must be retained.

### 15. Cloudflare Blog

- **Stratum:** 4 — engineering organization blog
- **First-party home:** [Cloudflare Blog](https://blog.cloudflare.com/)
- **Representative artifacts:** [Building Cloudflare on Cloudflare](https://blog.cloudflare.com/building-cloudflare-on-cloudflare/); [How Cloudflare’s Architecture Allows Us to Scale to Stop the Largest Attacks](https://blog.cloudflare.com/how-cloudflares-architecture-allows-us-to-scale-to-stop-the-largest-attacks/); [Cloudflare architecture and how BPF eats the world](https://blog.cloudflare.com/cloudflare-architecture-and-how-bpf-eats-the-world/)
- **Dominant format:** Engineering case study, architecture walkthrough, adapted talk transcript
- **Likely relevance:** First-party explanations of deployed network and systems architecture, often with diagrams and concrete operational context.
- **Accessibility:** Public HTML, generally with named authors and reading times. Some posts mix engineering explanation with product positioning, and the platform includes non-engineering categories.

### 16. Netflix Technology Blog

- **Stratum:** 4 — engineering organization blog
- **First-party home:** [Netflix TechBlog](https://netflixtechblog.medium.com/)
- **Representative artifacts:** [Keystone Real-time Stream Processing Platform](https://medium.com/netflix-techblog/keystone-real-time-stream-processing-platform-a3ee651812a); [Engineering Trade-Offs and the Netflix API Re-Architecture](https://medium.com/netflix-techblog/engineering-trade-offs-and-the-netflix-api-re-architecture-64f122b277dd); [How Netflix Scales Its API with GraphQL Federation](https://medium.com/netflix-techblog/how-netflix-scales-its-api-with-graphql-federation-part-1-ae3557c187e2)
- **Dominant format:** Engineering case study and architecture deep dive
- **Likely relevance:** Detailed first-party accounts of evolving distributed platforms, explicit requirements, and system diagrams.
- **Accessibility:** Officially published through Medium. Pages are readable publicly but may trigger sign-in prompts, metering, client-side rendering, or inconsistent extraction. Posts are team-authored and may name many contributors.

### 17. Stripe Engineering

- **Stratum:** 4 — engineering organization blog
- **First-party home:** [Stripe Engineering](https://stripe.com/blog/engineering)
- **Representative artifacts:** [Designing robust and predictable APIs with idempotency](https://stripe.com/blog/idempotency); [Online migrations at scale](https://stripe.com/blog/online-migrations); [Ledger: Stripe’s system for tracking and validating money movement](https://stripe.com/blog/ledger-stripe-system-for-tracking-and-validating-money-movement)
- **Dominant format:** Engineering essay and implementation case study
- **Likely relevance:** Explains APIs, distributed failure, data migrations, and correctness-sensitive financial infrastructure to developers.
- **Accessibility:** Public HTML with named authors. Some older URLs now redirect to `stripe.dev`, and pages carry substantial site chrome; product and recruiting context should not be confused with the explanatory body.

### 18. GitHub Engineering

- **Stratum:** 4 — engineering organization blog
- **First-party home:** [GitHub Engineering](https://github.blog/engineering/)
- **Representative artifacts:** [The technology behind GitHub’s new code search](https://github.blog/engineering/architecture-optimization/the-technology-behind-githubs-new-code-search/); [A brief history of code search at GitHub](https://github.blog/engineering/architecture-optimization/a-brief-history-of-code-search-at-github/); [Introducing DGit](https://github.blog/engineering/architecture-optimization/introducing-dgit/)
- **Dominant format:** Architecture case study and engineering history
- **Likely relevance:** First-party descriptions of search, storage, deployment, and platform evolution, typically tied to a concrete system change.
- **Accessibility:** Public HTML with bylines and diagrams. The engineering taxonomy and URLs have changed over time, and current index pages mix deep dives with shorter product-engineering posts.

### 19. Google developer documentation style guide

- **Stratum:** 5 — documentation/style system
- **First-party home:** [Google developer documentation style guide](https://developers.google.com/style)
- **Representative artifacts:** [Style guide highlights](https://developers.google.com/style/highlights); [Voice and tone](https://developers.google.com/style/tone); [Write for a global audience](https://developers.google.com/style/translation)
- **Dominant format:** Editorial reference
- **Likely relevance:** An explicit, public rule system for software-developer documentation, organization, terminology, accessibility, and global audiences.
- **Accessibility:** Public, searchable HTML and regularly updated. It is normative guidance rather than a naturally occurring explanation, so Phase 2 should not pool it with practitioner essays without genre controls.

### 20. Google Technical Writing Courses

- **Stratum:** 5 — technical-writing pedagogy system
- **First-party home:** [Technical Writing Courses](https://developers.google.com/tech-writing)
- **Representative artifacts:** [Technical Writing One](https://developers.google.com/tech-writing/one); [Audience](https://developers.google.com/tech-writing/one/audience); [Technical Writing Two](https://developers.google.com/tech-writing/two)
- **Dominant format:** Self-study course, pre-class lesson, facilitator-backed curriculum
- **Likely relevance:** Teaches engineers and computer-science students how to plan and author technical documents, with explicit audience and learning objectives.
- **Accessibility:** Public HTML; pre-class material works independently. The full facilitated experience is not observable from the pages alone, the course cannot be downloaded as a unit, and optional videos are not required.

### 21. Diátaxis / Daniele Procida

- **Stratum:** 5 — documentation architecture and pedagogy system
- **First-party home:** [Diátaxis](https://diataxis.fr/)
- **Representative artifacts:** [Diátaxis in five minutes](https://diataxis.fr/start-here/); [Explanation](https://diataxis.fr/explanation/); [Applying Diátaxis](https://diataxis.fr/application/)
- **Dominant format:** Documentation framework, handbook, explanatory essay
- **Likely relevance:** Provides an explicit model relating documentation purpose, user need, content type, and workflow.
- **Accessibility:** Public static HTML and PDF. It is one author’s framework and includes its own conceptual vocabulary; adoption claims should not be treated as independent validation.

### 22. Microsoft Writing Style Guide

- **Stratum:** 5 — documentation/style system
- **First-party home:** [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/)
- **Representative artifacts:** [Microsoft Learn style and voice quick start](https://learn.microsoft.com/en-us/contribute/content/style-quick-start); [Developer content](https://learn.microsoft.com/en-us/style-guide/developer-content/); [Writing style for Windows apps](https://learn.microsoft.com/en-us/windows/apps/design/style/writing-style)
- **Dominant format:** Editorial reference and contributor guide
- **Likely relevance:** Public first-party guidance for technical content, code examples, interface text, voice, and localization-aware writing.
- **Accessibility:** Public HTML. Scope varies between the general guide, Microsoft Learn contributor rules, and product UI guidance; pages include feedback and AI-summary interface elements outside the authored guidance.

### 23. Aditya Bhargava / *Grokking Algorithms*

- **Stratum:** 6 — book author with official publisher material
- **First-party home:** [Manning: Grokking Algorithms, Second Edition](https://www.manning.com/books/grokking-algorithms-second-edition)
- **Representative artifacts:** [Chapter 1: Introduction to algorithms](https://livebook.manning.com/book/grokking-algorithms-second-edition/chapter-1); [Chapter 2: Selection sort](https://livebook.manning.com/book/grokking-algorithms-second-edition/chapter-2/); [About the first edition](https://livebook.manning.com/book/grokking-algorithms/brief-table-of-contents/btoc)
- **Dominant format:** Illustrated book excerpt and tutorial chapter
- **Likely relevance:** An algorithms text explicitly built around illustrations, approachable examples, exercises, code, and a programmer audience.
- **Accessibility:** The publisher page and selected liveBook extracts are official, but access is inconsistent: chapters may be readable to crawlers or signed-in users while returning 403 or a subscription prompt to other sessions. The complete second edition is paid.

### 24. Martin Kleppmann / *Designing Data-Intensive Applications*

- **Stratum:** 6 — book author with companion material and talks
- **First-party home:** [Designing Data-Intensive Applications](https://dataintensive.net/)
- **Representative artifacts:** [Please stop calling databases CP or AP](https://martin.kleppmann.com/2015/05/11/please-stop-calling-databases-cp-or-ap.html); [Turning the database inside-out](https://martin.kleppmann.com/2015/11/05/database-inside-out-at-oredev.html); [Public distributed-systems course announcement and materials](https://martin.kleppmann.com/2020/11/18/distributed-systems-and-elliptic-curves.html)
- **Dominant format:** Book companion, technical essay, talk with transcript/slides, lecture material
- **Likely relevance:** Connects distributed-systems theory, practical system behavior, trade-offs, diagrams, references, and multiple media.
- **Accessibility:** Author essays and several talk transcripts/slides are public; the book itself is paid. Some videos are embedded from third-party hosts, but the author pages provide stable context and often transcripts.

### 25. Robert Nystrom / *Crafting Interpreters*

- **Stratum:** 6 — book author with an open web edition
- **First-party home:** [Crafting Interpreters](https://craftinginterpreters.com/)
- **Representative artifacts:** [A Map of the Territory](https://craftinginterpreters.com/a-map-of-the-territory.html); [Scanning](https://craftinginterpreters.com/scanning.html); [Table of Contents](https://craftinginterpreters.com/contents.html)
- **Dominant format:** Full online book, implementation tutorial, illustrated code walkthrough
- **Likely relevance:** Explains programming-language implementation through a sustained build, diagrams, code, exercises, and narrative asides.
- **Accessibility:** The complete web edition is public and responsive. It is one unusually coherent long-form work, so selecting multiple chapters does not provide independent authors or editorial processes.

### 26. Amy Brown and Greg Wilson, editors / *The Architecture of Open Source Applications*

- **Stratum:** 6 — official open book and first-person architecture anthology
- **First-party home:** [The Architecture of Open Source Applications](https://aosabook.org/en/)
- **Representative artifacts:** [Volume 1 introduction](https://aosabook.org/en/v1/intro1.html); [The Hadoop Distributed File System](https://aosabook.org/en/v1/hdfs.html); [500 Lines or Less introduction](https://aosabook.org/en/500L/introduction.html)
- **Dominant format:** Open book chapter, architecture case study, code-centered tutorial
- **Likely relevance:** Lets system creators describe how substantial software is structured and why, across many applications and author teams.
- **Accessibility:** Full HTML is public under a Creative Commons license. Chapters differ materially in author voice, age, domain, and diagram/code density; the anthology should be sampled by chapter, not treated as one homogeneous writer.

### 27. John Ousterhout / *A Philosophy of Software Design*

- **Stratum:** 6 — book author with official extracts and course material
- **First-party home:** [A Philosophy of Software Design](https://web.stanford.edu/~ouster/cgi-bin/aposd.php)
- **Representative artifacts:** [Managing Complexity lecture notes](https://web.stanford.edu/~ouster/cgi-bin/cs190-spring15/lecture.php?topic=complexity); [Software Design Studio course](https://web.stanford.edu/~ouster/cs190-winter24/); [A Philosophy of Software Design talk](https://www.youtube.com/watch?v=bmSAYlu0NcY)
- **Dominant format:** Official book extract, course notes, lecture/talk
- **Likely relevance:** A linked set of book, course, code-review pedagogy, and public talk material aimed at developing software-design judgment.
- **Accessibility:** The official page provides only selected book extracts; the full book is paid. Stanford course pages vary by year, and the YouTube talk has auto-generated rather than author-edited transcript support.

### 28. Bartosz Ciechanowski

- **Stratum:** 3 — interactive technical educator
- **First-party home:** [ciechanow.ski](https://ciechanow.ski/)
- **Representative artifacts:** [Gears](https://ciechanow.ski/gears/); [Internal Combustion Engine](https://ciechanow.ski/internal-combustion-engine/); [GPS](https://ciechanow.ski/gps/)
- **Dominant format:** Long interactive visual explanation and simulation
- **Likely relevance:** A consistently authored corpus that explains geometry, mechanics, electronics, and computation through prose integrated with manipulable models.
- **Accessibility:** Public, but the full explanatory experience requires JavaScript/WebGL and a capable browser. The subject mix extends beyond software and computer science, which is useful for medium comparison but should be marked in topic controls.

### 29. Seeing Theory / Brown University

- **Stratum:** 3 — visual probability and statistics educator
- **First-party home:** [Seeing Theory](https://seeing-theory.brown.edu/index.html)
- **Representative artifacts:** [Compound Probability](https://seeing-theory.brown.edu/compound-probability/index.html); [Seeing Theory textbook draft](https://seeing-theory.brown.edu/doc/seeing-theory.pdf)
- **Dominant format:** Interactive visual chapter and companion PDF
- **Likely relevance:** Offers the same probability and statistics material through interactive browser chapters and a static textbook-like artifact.
- **Accessibility:** Public, but the site is archived rather than actively developed and interactions require JavaScript. The project has multiple contributors and a bounded topic domain.

## Explicit Phase-2 selection criteria

Phase 2 should select artifacts, not merely domains. Each chosen artifact should be logged with author/byline, title, date, genre, intended audience, access date, and stable URL.

### Artifact-level requirements

1. **First-party ownership:** The artifact is written, published, or officially hosted by the author, project, publisher, or organization whose knowledge it presents. Editorial reposts are eligible only when provenance and permission are explicit.
2. **Technical substance:** It explains a mechanism, algorithm, architecture, design decision, implementation, operational practice, or technical-writing method in enough detail to examine—not merely announce or market it.
3. **Identifiable audience:** The artifact states an audience or makes one reasonably identifiable from prerequisites, framing, task, and publication context.
4. **Observable explanatory choices:** The artifact contains enough authored structure—prose, examples, code, diagrams, sequencing, interaction, or exercises—to support analysis of how an idea is explained.
5. **Accessibility:** The complete artifact needed for analysis is publicly reachable or available through an official excerpt. Phase 2 should exclude artifacts whose essential argument is hidden behind a paywall, login, unavailable video, or missing transcript.
6. **Enough material for comparison:** Prefer at least two substantial artifacts per selected source, or one book-length/interactive artifact with multiple independently analyzable sections. A candidate with only a landing page does not qualify.

### Portfolio-level requirements

7. **Diversity of medium:** The final sample must include conventional essays, visual or interactive explanations, tutorials/course material, engineering case studies, references/style systems, and book excerpts or open chapters. No single dominant format should exceed one third of the sample.
8. **Diversity of topic and setting:** Cover algorithms/CS, software design, distributed systems, production operations, developer tooling, and documentation pedagogy. Include both individual practitioners and organization-edited publications.
9. **Publisher independence:** Do not allow one company, publisher, or platform to supply more than three sample sources. Treat Google SRE, Google style guidance, and Google’s writing course as distinct genres but still count them toward the same company cap.
10. **Comparable units:** Compare like with like before crossing genres—for example, essay with essay, interactive tutorial with interactive tutorial, and normative guide with normative guide. Any cross-genre synthesis must preserve those distinctions.

## Proposed balanced Phase-2 sample

The following 18-source sample assigns three sources to each primary stratum and includes all five required inclusions. This is a proposed corpus, not a quality ranking.

| Stratum | Proposed sources | Principal medium coverage |
|---|---|---|
| 1. Practitioner essayists/design authors | Martin Fowler; Julia Evans; Dan Luu | Design essay, short tutorial/zine-derived post, empirical long-form essay |
| 2. System-design educators/publications | ByteByteGo; High Scalability; Hello Interview | Visual/newsletter/video, architecture profile, structured course/quick reference |
| 3. Visual CS/algorithm educators | VisuAlgo; Red Blob Games; Bartosz Ciechanowski | Animation/e-lecture, interactive algorithm tutorial/reference, long-form simulation |
| 4. Engineering organizations | Cloudflare Blog; Stripe Engineering; GitHub Engineering | Network architecture, correctness-sensitive API/data case, search/storage evolution |
| 5. Documentation/style/pedagogy | Google Technical Writing Courses; Diátaxis; Microsoft Writing Style Guide | Engineer-facing course, documentation framework, normative reference |
| 6. Book authors/official companions | *Grokking Algorithms*; Martin Kleppmann/DDIA; Robert Nystrom/*Crafting Interpreters* | Illustrated excerpt, essay/talk/course companion, full open implementation book |

For manageable comparison, Phase 2 could take two artifacts from each source (36 artifacts), except that long interactive/book works may use two bounded sections from the same work. Candidate substitutions should preserve the same stratum and medium balance. In particular:

- Substitute Amazon Builders’ Library or Google SRE for an organization/system-design source if stable access or historical relevance becomes more important than interview pedagogy.
- Substitute Distill or Seeing Theory when more peer-reviewed ML or probability/statistics exposition is needed; substitute Algorithm Visualizer for VisuAlgo only if community-contributed authorship can be controlled.
- Substitute *The Architecture of Open Source Applications* or John Ousterhout when more book/chapter or software-design coverage is needed.
- Retain High Scalability only with artifacts whose authorship and source trail can be unambiguously classified.

## Sampling limits and concerns

- This is a purposive census of visible candidates, not a systematic or statistically representative survey of technical communication.
- The corpus is English-language and public-web biased. It underrepresents internal design documents, academic textbooks without official excerpts, conference talks without transcripts, paid training, non-English traditions, audio, and print-first explanation.
- Link checks establish that a direct first-party page resolved or was discoverable on 2026-07-31; they do not guarantee permanence. Dynamic sites, redirects, Medium, YouTube, Substack, liveBook, and paid-course surfaces can vary by region, cookies, login state, or later revision.
- Public engineering blogs are self-selected accounts. They may omit proprietary details, failed approaches, or organizational context and sometimes combine technical education with recruiting or product positioning.
- Age is uneven. High Scalability and classic practitioner essays preserve historically influential explanations, while Hello Interview and ByteByteGo are actively revised. Phase 2 must record dates and avoid treating changed terminology or system scale as directly comparable.
- A domain is not a single voice. Fowler’s site, High Scalability, Distill, Google SRE, engineering blogs, Algorithm Visualizer, and AOSA all contain multiple authors or editorial layers.
- Accessibility creates survivorship bias: material with stable public HTML is easier to sample than equally strong books, private memos, or video-first work.
- This phase verified ownership, direct links, format, and likely analytical usefulness. It did not judge factual correctness, measure learning outcomes, or infer common writing patterns.
