from diagrams import Diagram, Cluster
from diagrams.aws.compute import Lambda
from diagrams.aws.network import APIGateway
from diagrams.aws.security import Cognito, IAM
from diagrams.aws.storage import S3
from diagrams.aws.general import User
from diagrams.onprem.client import Client

with Diagram("AWS Architecture Diagram", show=False):
    client = User("Mobile Device")
    cognito = Cognito("Amazon Cognito")

    with Cluster(""):
        api_gateway = APIGateway("API Gateway")

        with Cluster("Lambda Functions"):
            lambda_1 = Lambda("ImageUpload")
            lambda_2 = Lambda("ExpenseReport")

        s3 = S3("Amazon S3")
        
        # Adding IAM roles between Lambda functions and S3
        iam_role_1 = IAM("IAM Role")
        iam_role_2 = IAM("IAM Role")

        api_gateway >> lambda_1
        api_gateway >> lambda_2

    client >> cognito >> api_gateway
    lambda_1 >> iam_role_1 >> s3
    lambda_2 >> iam_role_2 >> s3

    # Adding a key/legend in the bottom right corner
    key = Client("Serverless\nRDS free\nArchitecture")







#############################older versions below for reference############################################



# from diagrams import Diagram, Cluster
# from diagrams.aws.compute import Lambda
# from diagrams.aws.network import APIGateway
# from diagrams.aws.security import Cognito
# from diagrams.aws.storage import S3
# from diagrams.onprem.client import Client

# with Diagram("AWS Architecture Diagram", show=False):
#     client = Client("Mobile Device")
#     cognito = Cognito("Amazon Cognito")

#     with Cluster(""):
#         api_gateway = APIGateway("API Gateway")

#         with Cluster("Lambda Functions"):
#             lambda_1 = Lambda("ImageUpload")
#             lambda_2 = Lambda("ExpenseReport")

#         s3 = S3("Amazon S3")

#         api_gateway >> lambda_1
#         api_gateway >> lambda_2

#     client >> cognito >> api_gateway
#     lambda_1 >> s3
#     lambda_2 >> s3





# from diagrams import Diagram, Cluster
# from diagrams.aws.compute import Lambda
# from diagrams.aws.network import APIGateway
# from diagrams.aws.security import Cognito
# from diagrams.aws.storage import S3
# from diagrams.onprem.client import Client

# with Diagram("AWS Architecture Diagram", show=False):
#     client = Client("Mobile Device")
    
#     cognito = Cognito("Amazon Cognito")

#     with Cluster("API Gateway"):
#         api_gateway = APIGateway("API Gateway")

#     with Cluster("Lambda Functions"):
#         lambda_1 = Lambda("Lambda Function 1")
#         lambda_2 = Lambda("Lambda Function 2")

#     s3 = S3("Amazon S3")

#     client >> cognito >> api_gateway >> lambda_1 >> s3
#     api_gateway >> lambda_2 >> s3

# from diagrams import Diagram, Cluster
# from diagrams.aws.compute import Lambda
# from diagrams.aws.network import APIGateway
# from diagrams.aws.security import Cognito
# from diagrams.aws.storage import S3
# from diagrams.onprem.client import Client

# with Diagram("AWS Architecture Diagram", show=False):
#     client = Client("Mobile Device")
    
#     cognito = Cognito("Amazon Cognito")

#     with Cluster("AWS Architecture Diagram"):
#         with Cluster("API Gateway"):
#             api_gateway = APIGateway("API Gateway")

#         with Cluster("Lambda Functions"):
#             lambda_1 = Lambda("Lambda Function 1")
#             lambda_2 = Lambda("Lambda Function 2")

#         s3 = S3("Amazon S3")

#         api_gateway >> lambda_1
#         api_gateway >> lambda_2
    
#     client >> cognito >> api_gateway
#     lambda_1 >> s3
#     lambda_2 >> s3


# from graphviz import Digraph

# # Create a new Digraph
# dot = Digraph(comment='AWS Architecture Diagram')

# # Add the title
# dot.attr(label='AWS Architecture Diagram', labelloc='t', fontsize='20')

# # Define nodes
# dot.node('Mobile Device', 'Mobile Device', shape='box')
# dot.node('Amazon Cognito', 'Amazon Cognito', shape='box', style='filled', fillcolor='red')
# dot.node('API Gateway', 'API Gateway', shape='box', style='filled', fillcolor='purple')
# dot.node('Lambda Function 1', 'Lambda Function 1', shape='box', style='filled', fillcolor='orange')
# dot.node('Lambda Function 2', 'Lambda Function 2', shape='box', style='filled', fillcolor='orange')
# dot.node('Amazon S3', 'Amazon S3', shape='box', style='filled', fillcolor='green')

# # Define edges
# dot.edge('Mobile Device', 'Amazon Cognito')
# dot.edge('Amazon Cognito', 'API Gateway')
# dot.edge('API Gateway', 'Lambda Function 1')
# dot.edge('API Gateway', 'Lambda Function 2')
# dot.edge('Lambda Function 1', 'Amazon S3')
# dot.edge('Lambda Function 2', 'Amazon S3')

# # Create a subgraph to enclose the main content in a box
# with dot.subgraph(name='cluster_0') as c:
#     c.attr(color='lightgrey')
#     c.node('Amazon Cognito')
#     c.node('API Gateway')
#     c.node('Lambda Function 1')
#     c.node('Lambda Function 2')
#     c.node('Amazon S3')
#     c.edge('Amazon Cognito', 'API Gateway')
#     c.edge('API Gateway', 'Lambda Function 1')
#     c.edge('API Gateway', 'Lambda Function 2')
#     c.edge('Lambda Function 1', 'Amazon S3')
#     c.edge('Lambda Function 2', 'Amazon S3')
#     c.attr(label='')

# # Save and render the diagram
# dot.render('aws_architecture_diagram', format='png', view=True)
