# Delirium Diagnostic Web App using RDF Ontology (Flask)

from flask import Flask, render_template_string, request
from rdflib import Graph, Namespace, RDF, RDFS
import re

app = Flask(__name__)

# Load Ontology
g = Graph()
g.parse("HughOntology.rdf")

# Define Namespace
DELIR = Namespace("http://www.semanticweb.org/hughm/ontologies/2025/5/Delir#")

# Manual mapping of base symptom types to delirium subtypes
SYMPTOM_SUBTYPES = {
    "Aggression": "Hyperactive",
    "DisorganizedThinking": "Mixed",
    "LossofAppetite": "Hypoactive",
    # Add more mappings here as needed
}

def list_delirium_symptoms():
    symptoms = set()
    for _, _, symptom in g.triples((None, DELIR.hasSymptom, None)):
        label = str(symptom).split('#')[-1]
        clean_label = re.sub(r'\d+$', '', label)
        symptoms.add(clean_label)
    return sorted(symptoms)

def get_symptom_types():
    symptom_types = {}
    for _, _, symptom in g.triples((None, DELIR.hasSymptom, None)):
        symptom_label = str(symptom).split('#')[-1]
        base_symptom = re.sub(r'\d+$', '', symptom_label)

        # Get the rdf:type to extract base class name
        classes = list(g.objects(subject=symptom, predicate=RDF.type))
        for c in classes:
            class_name = str(c).split('#')[-1]
            if class_name in SYMPTOM_SUBTYPES:
                symptom_types[base_symptom] = SYMPTOM_SUBTYPES[class_name]
    return symptom_types

def list_assessment_tools():
    canonical_tools = ["CAM", "CAM-ICU", "4AT", "DOS", "DRSR98", "ICDSC"]
    tools_dict = {}
    for s in g.subjects():
        label = str(s).split('#')[-1]
        base_label = re.sub(r'\d+$', '', label)
        if base_label in canonical_tools:
            comment = None
            for p, o in g.predicate_objects(subject=s):
                if p == RDFS.comment:
                    comment = str(o)
                    break
            # Only record the first non-empty comment for each tool
            if base_label not in tools_dict or (not tools_dict[base_label] and comment):
                tools_dict[base_label] = comment if comment else ""
    return sorted((name, comment) for name, comment in tools_dict.items())

def match_user_symptoms_to_delirium(user_symptoms):
    subtype_counts = {'Hypoactive': 0, 'Hyperactive': 0, 'Mixed': 0}
    matched_symptoms = set()
    symptom_types = get_symptom_types()
    for symptom in user_symptoms:
        clean_symptom = re.sub(r'\d+$', '', symptom)
        if clean_symptom in symptom_types:
            matched_symptoms.add(clean_symptom)
            subtype_counts[symptom_types[clean_symptom]] += 1
    total_matched = len(matched_symptoms)
    if total_matched == 0:
        delirium_type = "None"
    else:
        delirium_type = max(subtype_counts, key=subtype_counts.get)
    return total_matched, len(user_symptoms), delirium_type

@app.route('/', methods=['GET', 'POST'])
def index():
    symptoms = list_delirium_symptoms()
    symptom_types = get_symptom_types()
    tools = list_assessment_tools()
    result = None
    selected_symptoms = []

    if request.method == 'POST':
        selected_symptoms = request.form.getlist('symptoms')
        match_count, total, delirium_type = match_user_symptoms_to_delirium(selected_symptoms)
        if len(symptoms) == 0:
            result = "⚠️ No delirium symptoms are defined in the ontology. Please check your ontology file."
        elif total == 0:
            result = "⚠️ Please select at least one symptom."
        elif match_count / len(symptoms) >= 0.5:
            result = f"⚠️ Based on your input, Delirium may be a possibility ({match_count}/{len(symptoms)} symptoms matched). <b>Type: {delirium_type}</b>"
        else:
            result = f"✅ Your symptoms do not strongly match Delirium ({match_count}/{len(symptoms)} symptoms matched)."

    return render_template_string('''  
    <html>
<head>
    <title>Delirium Symptom Checker</title>
    <style>
        .symptom-label {
            display: inline-block;
            margin: 5px;
            padding: 8px 12px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            border: 2px solid transparent;
            user-select: none;
        }
        .Hyperactive {
            background-color: #ffe5e5;
            border-color: #ff4d4d;
        }
        .Hypoactive {
            background-color: #e5f0ff;
            border-color: #3399ff;
        }
        .Mixed {
            background-color: #fff8e5;
            border-color: #ffcc00;
        }
        input[type=checkbox]:checked + label {
            filter: brightness(1.1);
            font-weight: bold;
            border-width: 3px;
            box-shadow: 0 0 8px 2px rgba(0,0,0,0.25);
        }
    </style>
</head>
<body style="font-family:Arial; margin:2em;">
    <h1>Delirium Symptom Checker</h1>
    <h2>Assessment Tools for Delirium</h2>
    <ul>
      {% for tool in tools %}
        <li>{{ tool[0] }}{% if tool[1] %}: {{ tool[1] }}{% endif %}</li>
      {% endfor %}
    </ul>
    <h3>Symptom Types</h3>
    <ul>
    {% for symptom, s_type in symptom_types.items() %}
        <li>{{ symptom }}: {{ s_type }}</li>
    {% endfor %}
    </ul>
    <form method="POST">
        <p>Select the symptoms you are experiencing:</p>
        {% for symptom in symptoms %}
            <input type="checkbox" name="symptoms" id="{{ symptom }}" value="{{ symptom }}" style="display:none;" {% if symptom in selected_symptoms %}checked{% endif %}>
            <label class="symptom-label {{ symptom_types.get(symptom, '') }}" for="{{ symptom }}">
                {{ symptom }}
            </label>
        {% endfor %}
        <br><br>
        <input type="submit" value="Check">
    </form>
    {% if result %}
        <h2>Result:</h2>
        <p>{{ result|safe }}</p>
    {% endif %}
</body>
</html>
''', symptoms=symptoms, result=result, symptom_types=symptom_types, tools=tools, selected_symptoms=selected_symptoms)

if __name__ == '__main__':
    app.run(debug=True)
