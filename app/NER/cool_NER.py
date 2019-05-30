from app.preprocessing import cool_preproc
from app import gazetteer
import spacy


def is_gazetteer(cand):
    for name in gazetteer:
        if name == cand.text:
            return True


def spacy_cand(parsed):
    candidates = []
    return candidates


def rules_cand(sent):
    candidates = []
    return candidates


def gazetteer_cand(parsed):
    candidates = []
    return candidates


def chunk_cand(parsed):
    candidates = []
    return candidates


def loc_relation(cand):
    if isinstance(cand, spacy.tokens.span.Span):
        cand = cand.root
    if cand.head.text == 'from':
        return 'from'
    elif cand.head.text == 'to':
        return 'to'
    else:
        return None


def extract(parsed):

    _from = None
    _to = None

    gazetteer_cands = gazetteer_cand(parsed)
    spacy_cands = spacy_cand(parsed)
    rules_cands = rules_cand(parsed)
    chunk_cands = chunk_cand(parsed)

    all_cands = [gazetteer_cands] + [spacy_cands] + [rules_cands] + [chunk_cands]

    for lst in all_cands:
        if lst:
            for cand in lst:
                if loc_relation(cand) == 'from':
                    _from = cand.text
                elif loc_relation(cand) == 'to':
                    _to = cand.text
                else:
                    continue

    return _from, _to


if __name__ == '__main__':
    # Test your stuff.

    s1 = 'from Lviv to New York'
    parsed = cool_preproc(s1)
    print(extract(parsed))
