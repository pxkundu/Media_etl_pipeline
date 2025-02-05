from aws_cdk import core
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_glue as glue
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_redshift as redshift

class MediaETLStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # S3 Bucket
        data_bucket = s3.Bucket(self, "MediaDataBucket",
                                 bucket_name="media-etl-data-bucket",
                                 versioned=True,
                                 removal_policy=core.RemovalPolicy.DESTROY)

        # Glue Database
        glue_database = glue.Database(self, "MediaGlueDB", database_name="media_analytics")

        # Lambda Function
        lambda_function = _lambda.Function(
            self, "ETLLambda",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="lambda_handler.lambda_handler",
            code=_lambda.Code.from_asset("src/automation"),
            timeout=core.Duration.minutes(5)
        )

        # Redshift Cluster
        redshift_cluster = redshift.Cluster(
            self, "RedshiftCluster",
            cluster_name="media-redshift-cluster",
            master_user=redshift.Login(username="admin"),
            vpc=None  # Add proper VPC configuration
        )

        core.CfnOutput(self, "S3BucketName", value=data_bucket.bucket_name)
        core.CfnOutput(self, "GlueDatabaseName", value=glue_database.database_name)

app = core.App()
MediaETLStack(app, "MediaETLStack")
app.synth()
