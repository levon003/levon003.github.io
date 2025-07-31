this isn't a real draft, it's just a collection of post ideas I want to flesh out:
- my favorite papers from my phd ("10 papers worth reading", draft already exists in my email for this)
- scoping a data science project (draft already exists in my email for this)
  related: why topic modeling is rarely the right choice
- why not a computer-adaptive test that uses free-response options?
    ["Computer-Adaptive Testing: A Methodology Whose Time Has Come"] by Mike Linacre
    (And textbook [Invariant Measurement Using Rasch Models in the Social, Behavioral, and Health Sciences ](https://www.routledge.com/Invariant-Measurement-Using-Rasch-Models-in-the-Social-Behavioral-and-Health-Sciences/EngelhardJr-Wang/p/book/9781032603391))
    LLM for generating questions on the fly
    Claim: 5-minute conversation with a tutor beats a 30-minute CAT
    Proxy task: e.g. binary
    In language learning, they use Yes/No "is this a real word" as a validated CAT.
    [LexTALE](https://www.lextale.com/validity.html) I scored 100% lol
    https://www.lextale.com/pdf/Lemhofer_Broersma_2012.pdf
    https://www.nature.com/articles/s41598-021-85907-x#Bib1
    Overview: https://www-cambridge-org.wikipedialibrary.idm.oclc.org/core/journals/annual-review-of-applied-linguistics/article/computer-adaptive-testing-in-second-language-contexts/928BA5479DAEF6146251EDA1AAD03FF9
- open-source contributions
    https://github.com/burnash/gspread/pull/1529
    https://github.com/iterative/dvc.org/pull/5312
    https://github.com/mediawiki-utilities/python-oresapi/pull/1
    https://github.com/prosegrinder/python-cmudict/pull/121
    https://github.com/jupyter/jupyter-sphinx/pull/286
- vec2text:
    Identifying text from vectors
    https://github.com/jxmorris12/vec2text/
    Could connect it to the cool "sentence embeddings" blog post from a million years ago: https://www.robinsloan.com/notes/voyages-in-sentence-space/
- tips for new Wikipedia editors
    Dos:
    Edit in your interest areas
    Start small
    Read Talk pages if you like drama
    There are lots of cool starter tasks
        Citation Hunt: https://citationhunt.toolforge.org
        Pages with no sources:
        Can even search by category, e.g. [computing-related pages with no sources](https://en.wikipedia.org/w/index.php?sort=random&search=articletopic%3Acomputing+incategory%3A%22All+articles+lacking+sources%E2%80%8E%22&title=Special%3ASearch&profile=advanced&fulltext=1&ns0=1)
    Add pages to your Watchlist
    Short descriptions!
    Don'ts:
    Avoid contentious topic areas
        American politics
        Israel/Palestine
        MEDRS: this is a shortcut to a bad time!
        Avoid current events - although articles _related_ to current events are fine/good!
    Avoid stuff related to images
    Avoid categories (edit list articles instead)
         but do play Catfishing
 - ANN for vector search
    pgvector's two options
    How much slower the exact approach is than the approximation
    What are the actual costs of the approximation? How much will this hurt retrieval performance, and is this exacerbated at particular values of k (number of highest-similarity entries retrieved)?
 - Interesting question:
https://x.com/its_vayishu/status/1915389208790712466
>You're working with high-dimensional data (e.g., neural net embeddings). How do you test for multivariate normality? Why do tests like Shapiro-Wilk or KS break in high dims? And how do these assumptions affect models like PCA or GMMs?
 - number of individual Pokemon articles on Wikipedia over time
    Would need to figure out how to run a script on Toolforge/Cloud VPS these days
    See: https://wikitech.wikimedia.org/wiki/Help:Shared_storage
 - No import side-effects in Python!!! Just stop it!!!!
 - Draw rate at various Chess ELOs and time controls
