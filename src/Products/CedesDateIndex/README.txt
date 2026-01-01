# Copyright (c) 2007 Webin Concept (Brussels, BELGIUM).
# http://www.webinconcept.be -- webinconcept@gmail.com

DateIndex README

  
CedesDateIndex is a pluggable index which :

    o It normalizes the indexed value to an integer representation
      with a granularity of one *DAY*. 

    o It normalizes the 'query' value into the same form.
    
    o It saves a default value for Objects which don't have the indexed attributes

    
Used to index Cedes Resources in a smart way:
   
    - articles are indexed according to their publication date (day granularity)
    - other resource are date 'agnostic' which means that the search catalog will always return them
