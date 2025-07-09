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

▶️ Running the App

python delirium_web_app.py
Visit http://127.0.0.1:5000/ in your browser.

---
🧩 About the Ontology
The RDF ontology (HughOntology.rdf) defines:

Classes for symptoms

Delirium types (Hyperactive, Hypoactive, Mixed)

Relationships between symptoms and subtypes

Assessment tools with descriptions

You can edit or expand the ontology to improve diagnostic depth.

---
📌 Example Use Case
Open the app

Select symptoms (e.g., Aggression, Loss of Appetite)

Submit

The app infers the most likely type of delirium based on symptom types defined in the ontology.

---

🧑‍💻 Author
Hugh McAyaaz
GitHub: @McAyaaz


