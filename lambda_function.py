import json
import logging

import boto3

from custom_encoder import CustomEncoder

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamoDBTableName = 'tink'
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(dynamoDBTableName)

getMethod = 'GET'
postMethod = 'POST'
patchMethod = "PATCH"
deleteMethod = "DELETE"
healthPath = '/health'
productsPath = '/products'

def lambda_handler(event, context):
  logger.info(event)
  httpMethod = event['httpMethod']
  path = event["path"]
  if httpMethod == getMethod and path == healthPath:
    response = buildResponse(200)
  elif httpMethod == getMethod and path == productsPath:
    response = getProducts()
  elif httpMethod == getMethod and path.startswith(productsPath):
    response = getProduct(event["queryStringParameters"]["productId"])
  elif httpMethod == postMethod and path == productsPath:
    response = createProduct(json.loads(event["body"]))
  elif httpMethod == patchMethod and path.startswith(productsPath):
    requestBody = json.loads(event["body"])
    response = updateProduct(event["queryStringParameters"]["productId"], requestBody['updateKey'], requestBody['updateValue'])
  elif httpMethod == deleteMethod and path.startswith(productsPath):
    response = deleteProduct(event["queryStringParameters"]["productId"])
  else: 
    response = buildResponse(404, "Not Found")
  return response

def getProduct(productId):
  try:
    response = table.get_item(Key={'productId': productId})
    if 'Item' in response:
      return buildResponse(200, response["Item"])
    else:
      return buildResponse(404, "Product not found")
  except:
    logger.exception("Something went wrong during the getProduct request")
    return buildResponse(500, "Internal Server Error")

def getProducts():
  try:
    response = table.scan()
    return buildResponse(200, response["Items"])
  except:
    logger.exception("Something went wrong during the getProducts request")
    return buildResponse(500, "Internal Server Error")

def createProduct(product):
  try:
    response = table.put_item(Item=product)
    return buildResponse(200, response)
  except:
    logger.exception("Something went wrong during the createProduct request")
    return buildResponse(500, "Internal Server Error")

def updateProduct(productId, updateKey, updateValue):
  try:
    response = table.update_item(Key={'productId': productId}, UpdateExpression=f"set {updateKey}=:v", ExpressionAttributeValues={':v': updateValue}, ReturnValues="UPDATED_NEW")
    return buildResponse(200, response)
  except:
    logger.exception("Something went wrong during the updateProduct request")
    return buildResponse(500, "Internal Server Error")
  
def deleteProduct(productId):
  try:
    response = table.delete_item(Key={'productId': productId}, ReturnValues="ALL_OLD")
    return buildResponse(200, response)
  except:
    logger.exception("Something went wrong during the deleteProduct request")
    return buildResponse(500, "Internal Server Error")

    
def buildResponse(statusCode, body = None):
  response = {
    'statusCode': statusCode,
    'headers': {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*'
    }
  }  
  if body is not None:
    response["body"] = json.dumps(body, cls=CustomEncoder)
  return response