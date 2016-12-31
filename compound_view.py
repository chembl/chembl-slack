import time

from compound_template import MESSAGE_TEMPLATE

def render_compound(context):
    msg = MESSAGE_TEMPLATE.copy()
    chembl_id = context["molecule_chembl_id"]
    msg["attachments"][0]["author_name"] = context["pref_name"]
    msg["attachments"][0]["title"] = chembl_id
    msg["attachments"][0]["title_link"] = "https://chembl-glados.herokuapp.com/compound_report_card/{0}/".format(chembl_id)
    msg["attachments"][0]["image_url"] = "https://www.ebi.ac.uk/chembl/api/data/image/{0}.png?engine=indigo&ignoreCoords=1&dimensions=500".format(chembl_id)
    msg["attachments"][0]["thumb_url"] = "https://www.ebi.ac.uk/chembl/api/data/image/{0}.png?engine=indigo&ignoreCoords=1&dimensions=50".format(chembl_id)
    msg["attachments"][0]["text"] = context["molecule_structures"]["standard_inchi_key"]
    msg["attachments"][0]["fields"][0]["value"] = context["max_phase"]
    msg["attachments"][0]["fields"][1]["value"] = context["molecule_properties"]["full_molformula"]
    msg["attachments"][0]["fields"][2]["value"] = context["molecule_structures"]["canonical_smiles"]
    msg["attachments"][0]["fields"][3]["value"] = context["molecule_structures"]["standard_inchi"]
    msg["attachments"][0]["ts"] = int(time.time())
    
    return msg