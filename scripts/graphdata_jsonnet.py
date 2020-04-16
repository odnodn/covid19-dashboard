import json
import sys
sys.path.append('.')

import insights

templ_vars = {key: func() for (key, func) in insights.insights.items()}
with open("build/graphdata.jsonnet", "w") as file:
    file.write(json.dumps(templ_vars, indent=2))
