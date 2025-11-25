#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")


        # Sample authors
    abby = Author("Abby")
    moraa = Author("Moraa")

    # Sample magazines
    tech = Magazine("TechWorld", "Technology")
    fashion = Magazine("StyleHub", "Fashion")

    # Sample articles
    a1 = Article(abby, tech, "The Rise of AI")
    a2 = Article(abby, tech, "AI in 2025")
    a3 = Article(moraa, fashion, "Fall Trends 2025")
    a4 = Article(moraa, fashion, "Sustainable Style")
    a5 = Article(moraa, fashion, "Fashion and Climate")


        # Test relationships
    print("Abby's articles:", abby.articles())
    print("Abby's magazines:", abby.magazines())
    print("Abby's topic areas:", abby.topic_areas())

    print("TechWorld articles:", tech.articles())
    print("TechWorld contributors:", tech.contributors())
    print("TechWorld article titles:", tech.article_titles())
    print("TechWorld contributing authors:", tech.contributing_authors())

    print("StyleHub contributors:", fashion.contributors())
    print("StyleHub contributing authors:", fashion.contributing_authors())


    ipdb.set_trace()