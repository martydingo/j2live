from ansible.parsing.dataloader import DataLoader
from ansible.template import Templar, trust_as_template
import yaml


def renderTemplate(yamlVars, jinjaTemplate: str):

    loader = DataLoader()
    variables = yaml.safe_load(yamlVars) or {}

    print(f"yamlVars: {variables}")
    print(f"jinjaTemplate: {jinjaTemplate}")

    templar = Templar(loader=loader, variables=variables)
    trusted_template = trust_as_template(jinjaTemplate)

    try:
        result = templar.template(trusted_template)
        error = False
    except Exception as errMsg:
        result = errMsg
        error = True

    return {"result": result, "error": error}
