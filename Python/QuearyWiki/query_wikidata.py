from qwikidata.sparql import (get_subclasses_of_item,
                              return_sparql_query_results)

sparql_query = [
    # https://www.wikidata.org/wiki/Wikidata:SPARQL_tutorial/ja#SPARQL%E3%81%AE%E5%9F%BA%E6%9C%AC
    """
    SELECT ?child ?childLabel
    WHERE
    {
    # ?child  father   Bach
      ?child wdt:P22 wd:Q1339.
      SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE]". }
    }
    """,

    # Timeline of albums by Manu Chao and Mano Negra
    #defaultView:Timeline
    """
    SELECT ?album ?performerLabel ?albumLabel ?publication_date WHERE {
      VALUES ?performer {
          wd:Q936474
          wd:Q207898
        }
       ?album wdt:P175 ?performer ;
          wdt:P577 ?publication_date .
       SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
    """,

    # list satellites
    """
    SELECT ?satellite  ?satelliteLabel ?satelliteDescription WHERE {
        VALUES ?objclass{
            wd:Q26540
            wd:Q40218
            wd:Q752783
        }
        ?satellite wdt:P31 ?objclass.
        ?satellite wdt:P17 wd:Q30.
        SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
    """,

    # list satellites
    """
    SELECT ?satellite  ?satelliteLabel ?launchdateLabel ?countryLabel ?operator ?operatorLabel ?site ?siteLabel ?satelliteDescription WHERE {
    VALUES ?objclass{
    wd:Q26540
    wd:Q26529
    wd:Q40218
    wd:Q752783
    }
    ?satellite wdt:P31 ?objclass.
    OPTIONAL{ ?satellite wdt:P17 ?country }
    OPTIONAL{ ?satellite wdt:P137 ?operator }
    OPTIONAL{ ?satellite wdt:P1427 ?site }
    ?satellite wdt:P619 ?launchdate.
    SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
    ORDER BY ?launchdate
    """
    ][3]
res = return_sparql_query_results(sparql_query)
print(res)
print(len(res["results"]["bindings"]))

# use convenience function to get subclasses of an item as a list of item ids
#Q_RIVER = "Q4022"
#subclasses_of_river = get_subclasses_of_item(Q_RIVER)
