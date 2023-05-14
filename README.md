# second-deliverable [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7934869.svg)](https://doi.org/10.5281/zenodo.7934869)

Second deliverable of the Artificial Intelligence And Open Science In Research Software Engineering course

Objective: Advanced data analysis on research publications: Given a corpus of 30
papers, group them according common themes, link them in a Research Knowledge
Graph (RKG) together with their metadata and funding information. Use
HuggingFace as an open platform for models.
- Data processing workflow with Spark
- Workflow sketch
- Sample run (PROV)
- Topic modeling on your chosen papers
- Similarity score between papers (based on abstract)
- NER models in the Acknowledgements section
- Experiment as a Research Object
- Follow Best Practices introduced in previous assignment
(containers, registries, releases, documentation, etc.).
Model decisions should be justified

# Requirements : 
- Docker
- Python environment (conda example)
- Google Colab and Drive

# How to run 

1) Open the anaconda3 terminal 

2) Create the conda environment
```bash
conda create --name myenv python=3.10
```

3) Activate the environment 
```bash
conda activate myenv 
```

4) Install all the dependencies located in /docs/requirements.txt using pip
One example:
```bash
pip install example 
```

5) Add in a folder all the downloaded PDFs that you want to have analyzed 

6) Get Grobid Docker image and run it in port 8070 make sure to be on your working directory first
```bash
docker pull lfoppiano/grobid:0.7.2
docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2
```

7) Run the code the input parameter "path" should be the path of the folder where the papers are located
```bash
python IAOSGrupo.py path
```
This will generate the files:
- acknowledges.txt : the acknowledgements of each paper. If there are none present null is placed instead
- order.txt : the list of the titles in order. Is used to mantain the relation between paper and it's elements
- abstract.txt : the abstracts of the papers retrieved from grobid 

8) Input the files into your Google Colab. 

9) Run the Jupyter Notebooks called:
- NER.ipynb : We retrieve the organization associated with the paper
    - Input files: acknowledges.txt and order.txt
    - Output files: title_Ner.txt
- SparkIAOS.ipynb : processes the abstracts removing stop words
    - Input files: abstract.txt and order.txt
    - Output files: cleaned.txt and cleanedTitles.txt
- WikiDataYOpenAlex.ipynb : retrieves extra data though the OpenAlex and WikiData APIs
    - Input files: order.txt
    - Output files: resultadoWikiData.txt and resultadoOpenAlex.txt

10) Run the Jupyter Notebook TopicIAOS.ipynb
    - Input files: cleaned.txt and cleanedTitles.txt.
    - Output files: Topic_words.txt and Title_topic_prop.txt 

11) You will now need to use the docker container. Before creating it download the files from your Google Drive:
  - title_Ner.txt
  - Topic_words.txt
  - Title_topic_prop.txt
  - resultadoWikiData.txt
  - resultadoOpenAlex.txt
 
12) To create the container, use this command in the same directory as the environment:
```bash
docker build -t iaos .
```

13) To run the container:
```bash
docker run -it iaos
```

14) Once the code Grafo.py is running, it will ask for a promt of the intended query. 
The query *must* be written in a single line. 

Some examples are: 
```bash
- PREFIX onto: <http://IAOS.com/def/property#> SELECT ?paper ?doi WHERE { ?paper onto:hasWord ?doi . }
- PREFIX onto: <http://IAOS.com/def/property#> SELECT  ?topic WHERE { <http://IAOS.com/resource/belongs_to/4> onto:belongs_to_topic ?topic . }
- PREFIX onto: <http://IAOS.com/def/property#> SELECT ?cites ?pages WHERE { <http://IAOS.com/resource/paper/Attention_Is_All_You_Need> onto:hasCites ?cites . <http://IAOS.com/resource/paper/Attention_Is_All_You_Need> onto:hasNumPages ?pages . }
- PREFIX onto: <http://IAOS.com/def/property#> SELECT ?paper WHERE { ?paper onto:hasAuthor Sanda-Maria Avram . }
```
You can also run it as a Jupyter Notebook in Google Colab using Grafo.ipynb

