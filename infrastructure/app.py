from aws_cdk import core
from infra_stack import MediaETLStack

app = core.App()
MediaETLStack(app, "MediaETLStack")
app.synth()