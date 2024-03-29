#!/usr/bin/env python3
import os

from aws_cdk import (
    core as cdk
)

# For consistency with TypeScript code, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core

from my_first_cdk_project.my_first_cdk_project_stack import MyArtifactBucketStack


app = core.App()
env_US = core.Environment(region='us-east-1')
env_EU = core.Environment(region='eu-east-1')

MyArtifactBucketStack(app, "myDevStack", env=env_US
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=core.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    #env=core.Environment(account='123456789012', region='us-east-1'),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )

MyArtifactBucketStack(app, "myProdStack", is_prod=True, env=env_US)

app.synth()
