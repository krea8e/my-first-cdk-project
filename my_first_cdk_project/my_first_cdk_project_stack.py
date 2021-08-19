from aws_cdk import (
    aws_s3 as _s3,
    core as cdk
)

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class MyFirstCdkProjectStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        _s3.Bucket(
            self, 
            "myBucketId",
            bucket_name="myfirstcdkproject20210819",
            versioned=False,
            encryption=_s3.BucketEncryption.S3_MANAGED,
            block_public_access=_s3.BlockPublicAccess.BLOCK_ALL
        )

        mybucket = _s3.Bucket(
            self,
            "myBucketId1"
        )

#Create an output and export so that other stacks can use them

        output_1 = cdk.CfnOutput(
            self,
            "myBucketOutput1",                  #Output Key
            value=mybucket.bucket_name,         #Output Value
            description=f"My first CDK Bucket",
            export_name="myBucketOutput1"       #Export name that is available in Export tab in CloudFormation
        )