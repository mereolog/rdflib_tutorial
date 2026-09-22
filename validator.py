from rdflib import Graph, RDF, OWL, RDFS, URIRef


def validate_graph(graph_path: str) -> set:
    validation_issues = set()
    graph = Graph()
    graph.parse(graph_path)
    owl_classes = graph.subjects(predicate=RDF.type, object=OWL.Class)
    for owl_class in owl_classes:
        if isinstance(owl_class, URIRef):
            labels = set(graph.objects(subject=owl_class, predicate=RDFS.label))
            if len(labels) == 0:
                validation_issues.add(owl_class)
    return validation_issues

validation_issues = validate_graph("ontology/ontology.ttl")
for validation_issue in validation_issues:
    print(validation_issue)

raise SystemExit(1 if validation_issues else 0)