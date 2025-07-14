# 🧠 Delirium Diagnostic App (KBS 2025)

A lightweight Flask web application that helps identify potential types of **delirium** (Hyperactive, Hypoactive, or Mixed) based on symptom input. The app uses an **RDF ontology** as its knowledge base to power intelligent inference.

## 🚀 Features

- Select symptoms from a visual interface
- Classifies possible **delirium subtype**
- Lists assessment tools (CAM, 4AT, ICDSC, etc.)
- Uses `rdflib` to parse and reason over an OWL ontology (`HughOntology.rdf`)
- Built with Python and Flask
---

## 🛠️ Requirements

- Python 3.8+
- `rdflib`
- `flask`

Install dependencies:

```bash
pip install flask rdflib
---

##▶️ Running the App

python delirium_web_app.py
Visit http://127.0.0.1:5000/ in your browser.

---
##🧩 About the Ontology
The RDF ontology (HughOntology.rdf) defines:

Classes for symptoms

Delirium types (Hyperactive, Hypoactive, Mixed)

Relationships between symptoms and subtypes

Assessment tools with descriptions

You can edit or expand the ontology to improve diagnostic depth.

---
##📌 Example Use Case
Open the app

Select symptoms (e.g., Aggression, Loss of Appetite)

Submit

The app infers the most likely type of delirium based on symptom types defined in the ontology.

---
##🧠Ontology-Driven Delirium Diagnostic Support Tool
📌 Use Case
Delirium is still a complex and underdiagnosed condition common in hospitalized patients, especially geriatric patients. Accurate diagnosis and classification into subtypes (Hyperactive, Hypoactive, Mixed) is important for timely intervention. The use of an ontology offers a structured way to represent clinical knowledge, symptoms, assessment tools, and their interrelations in a machine-readable format. This web-based tool leverages an RDF/OWL ontology to assist healthcare professionals and researchers in evaluating patient symptoms, determining delirium subtype probability, and referencing standardized assessment tools.

##📍 Situation
Despite existing clinical guidelines, frontline clinicians face difficulty in distinguishing delirium subtypes due to variability in symptom presentation, limited time, and fragmented access to diagnostic tools. Existing digital systems are often not interoperable or are rigidly rule-based.

##⚠️ Complication
Delirium symptoms can overlap with other cognitive conditions, complicating diagnosis.


Knowledge is often distributed across multiple formats (guidelines, papers, EHRs) and lacks semantic interoperability.


Clinical decision support tools are often static and not easily adaptable to evolving medical knowledge, digital technology or new data.



##✅ Solution Implementation
This project introduces a web-based application powered by a custom-built Delirium Ontology (in RDF format). The solution includes:
Ontology Modeling:
 A structured OWL/RDF ontology defines symptom classes (e.g., Aggression, Loss of Appetite), their subtype associations (Hyperactive, Hypoactive, Mixed), and links to assessment tools (e.g., CAM, 4AT).


Interactive Web App:
 Built using Flask and rdflib, users select symptoms via a visual interface. The system matches selected symptoms to ontology-defined subtypes using RDF queries and manual mappings, returning a probable delirium type.


Ontology Graph Visualization:
 A /visualize route dynamically renders an interactive diagram of ontology relationships (e.g., symptoms, subtypes) using networkx and matplotlib.


Extensibility:
 The ontology is modular and can be extended to include severity levels, patient cases, or linked vocabularies like SNOMED CT. The app structure allows future integration with reasoning engines or AI assistants like Claude.



##📊 Impact
Supports accurate delirium recognition and classification


Promotes semantic interoperability in clinical systems


Enhances explainability through graph visualization


Enables iterative knowledge development and feedback loops



🧑‍💻 Author
Hugh McAyaaz
GitHub: @McAyaaz


