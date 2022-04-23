#!/usr/bin/env python3
"""
This is an example of a LAMBDA that could be issued from a Sumo Logic Webhook
"""
###
### Adapted from:
###
### https://www.ipswitch.com/blog/how-to-create-and-configure-an-aws-vpc-with-python
###
### https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html
###
### Reference:
###
### https://hands-on.cloud/working-with-vpc-in-python-using-boto3/
###
### Disclaimer: Caveat Lector
###
### This is an example only to demonstrate calling a lambda function.
###


### import os
### import sys
### import json
### import datetime

import boto3
import boto3.session

VPCNAME = 'example-lambda-vpc'
VPCADDR = '172.31.0.0/16'
VPCSUBN = '172.31.254.0/24'
AWSTYPE = 'ec2'
ANYADDR = '0.0.0.0/0'
AWSKEYNAME = '<AWSKEYNAME>'
AWSKEYVALUE = '<AWSKEYSECRET>'
AWSREGION = 'us-east-1'

def lambda_handler():
### def lambda_handler(event,context):
    """
    this is a lambda wrapper for the following boto3 logic
    """

    boto3session = boto3.Session(
        aws_access_key_id=AWSKEYNAME,
        aws_secret_access_key=AWSKEYVALUE,
        region_name=AWSREGION
    )

    ec2 = boto3session.resource(AWSTYPE)

    vpc = ec2.create_vpc(CidrBlock=VPCADDR)

    vpc.create_tags(Tags=[{"Key": "Name", "Value": VPCNAME}])
    vpc.wait_until_available()

    ### ec2_client = boto3.client(AWSTYPE)
    ### ec2_client.modify_vpc_attribute( VpcId = vpc.id , EnableDnsSupport = { 'Value': True } )
    ### ec2_client.modify_vpc_attribute( VpcId = vpc.id , EnableDnsHostnames = { 'Value': True } )

    internetgateway = ec2.create_internet_gateway()
    vpc.attach_internet_gateway(InternetGatewayId=internetgateway.id)

    routetable = vpc.create_route_table()
    _route = routetable.create_route(DestinationCidrBlock=ANYADDR, GatewayId=internetgateway.id)

    subnet = ec2.create_subnet(CidrBlock=VPCSUBN, VpcId=vpc.id)
    routetable.associate_with_subnet(SubnetId=subnet.id)

    securitygroup = ec2.create_security_group(GroupName='SSH-ONLY', \
                                              Description='only allow SSH traffic', VpcId=vpc.id)
    securitygroup.authorize_ingress(CidrIp='0.0.0.0/0', IpProtocol='tcp', FromPort=22, ToPort=22)

if __name__ == '__main__':
    lambda_handler()
