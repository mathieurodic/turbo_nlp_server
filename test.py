from pipeline import *


text = """
    Current therapeutics for schizophrenia, the typical and atypical antipsychotic class of drugs, derive their therapeutic benefit predominantly by antagonism of the dopamine D2 receptor subtype and have robust clinical benefit on positive symptoms of the disease with limited to no impact on negative symptoms and cognitive impairment.
    Driven by these therapeutic limitations of current treatments and the recognition that transmitter systems beyond the dopaminergic system in particular glutamatergic transmission contribute to the etiology of schizophrenia significant recent efforts have focused on the discovery and development of novel treatments for schizophrenia with mechanisms of action that are distinct from current drugs.
    Specifically, compounds selectively targeting the metabotropic glutamate receptor 2/3 subtype, phosphodiesterase subtype 10, glycine transporter subtype 1 and the alpha7 nicotinic acetylcholine receptor have been the subject of intense drug discovery and development efforts.
    Here we review recent clinical experience with the most advanced drug candidates targeting each of these novel mechanisms and discuss whether these new agents are living up to expectations.
"""

for sentence in split_sentences(text):
    print(sentence)
    for t in parse_sentence(sentence):
    # for t in tag_sentence(sentence):
    # for t in tag_lemmatize_sentence(sentence):
        print(t)
    print()
