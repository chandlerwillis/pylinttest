#!/usr/bin/env python3

import aws_cdk as cdk

from pythonworkshop.pythonworkshop_stack import PythonworkshopStack

#yes
app = cdk.App()
PythonworkshopStack(app, "pythonworkshop")

app.synth()
