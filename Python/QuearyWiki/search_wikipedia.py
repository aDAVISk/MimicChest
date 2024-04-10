
# Not working appropliately.
import wikipediaapi
# https://pypi.org/project/Wikipedia-API/

wiki_wiki = wikipediaapi.Wikipedia('WikiSearchTest (emailaddress)', 'en')
page_py = wiki_wiki.page('Python_(programming_language)')
print("Page - Title: %s" % page_py.title)
# Page - Title: Python (programming language)

print("Page - Summary: %s" % page_py.summary[0:60])

"""
def print_categorymembers(categorymembers, level=0, max_level=1):
        for c in categorymembers.values():
            print("%s: %s (ns: %d)" % ("*" * (level + 1), c.title, c.ns))
            if c.ns == wikipediaapi.Namespace.CATEGORY and level < max_level:
                print_categorymembers(c.categorymembers, level=level + 1, max_level=max_level)


cat = wiki_wiki.page("Category:Physics")
print("Category members: Category:Physics")
print_categorymembers(cat.categorymembers)
"""
