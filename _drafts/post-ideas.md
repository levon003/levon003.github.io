this isn't a real draft, it's just a collection of post ideas I want to flesh out:
- my favorite papers from my phd ("10 papers worth reading")
- scoping a data science project (draft already exists for this)
  related: why topic modeling is rarely the right choice
- how I review papers
    Jeff Leek's ["Reviewing academic papers"](https://github.com/jtleek/reviews)
- why not a computer-adaptive test that uses free-response options?
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
- vec2text:
    Identifying text from vectors
    https://github.com/jxmorris12/vec2text/
    Could connect it to the cool "sentence embeddings" blog post from a million years ago
- tips for new Wikipedia editors
    Dos:
    Edit in your interest areas
    Start small
    Read Talk pages if you like drama
    There are lots of cool starter tasks
    Add pages to your Watchlist
    Short descriptions!
    Don'ts:
    Avoid contentious topic areas
        American politics
        Israel/Palestine
        MEDRS: this is a shortcut to a bad time!
        Avoid current events - although articles related to current events are fine/good!
    Avoid stuff related to images
    Avoid categories (edit list articles instead)
 - ANN for vector search
    pgvector's two options
    How much slower the exact approach is than the approximation
    What are the actual costs of the approximation? How much will this hurt retrieval performance, and is this exacerbated at particular values of k (number of highest-similarity entries retrieved)?
