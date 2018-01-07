---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* B.S. in Computer Science, Henan University, 2011
* M.S. in Computer Science, Jilin University, 2014
* M.S. in Data Science, WPI, 2016 

Work experience
======
* Data Analyst Intern, CloudParticle 
  * Participated in a wide range of data analysis projects, including vehicle rental reservation, credit card authorization recycling prediction, Google Adwords campaign automatic monitor
  * Responsible for build pipeline to do data preprocess, feature engineering, model selection and evaluation

* Data Engineer Intern, Pfizer
  * Enabled automatic process for Hadoop ingestion of data from multiple sources, created scripts to parse multi-formats data into json and parquet format
  * Connected MapR with Spotfire/ Tableau, used Apache Drill to create both json and parquet view to generate overlay visualizations  


* Data Analyst Intern, Zakipoint Health Inc.
  * Developed a web-based simulation and analysis tool with Django framework to preprocess raw Pharmacy claim data, find potential cost driver under various scenarios, and display results by D3.js
  * Designed the data model, manipulated data storing and querying in mongoDB integrated with PyMongo 

  
Skills
======
* Skill 1
* Skill 2
  * Sub-skill 2.1
  * Sub-skill 2.2
  * Sub-skill 2.3
* Skill 3

Publications
======
  <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Service and leadership
======
* Currently signed in to 43 different slack teams
