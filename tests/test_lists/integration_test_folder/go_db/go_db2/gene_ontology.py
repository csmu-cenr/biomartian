
from biomartian.non_biomarts.go_db.get_go_data.get_go import get_go_map

def get_ontology():

    return get_go_map("ontology")


def get_term():

    return get_go_map("term")


def get_definition():

    return get_go_map("definition")
