import json
import logging
import time
import uuid
from boto3.dynamodb.conditions import Key, Attr
import boto3

from custom_encoder import CustomEncoder

logger = logging.getLogger()
logger.setLevel(logging.INFO)

userTableName = 'tink-user'
productTableName = 'tink-product'
dynamodb = boto3.resource('dynamodb', region_name='eu-north-1')

userTable = dynamodb.Table(userTableName)
productTable = dynamodb.Table(productTableName)

getMethod = 'GET'
postMethod = 'POST'
patchMethod = "PATCH"
deleteMethod = "DELETE"
healthPath = '/health'
createUserPath = '/create-user'
getUserPath = '/get-user'
updateUserPath = '/update-user'
createProductPath = '/create-product'
getProductsPath = '/list-product'

def current_millisecond():
    return str(round(time.time() * 1000))

def lambda_handler(event, context):
  logger.info(event)
  logger.info(context)
  print(context)
  print(event)
  httpMethod = event['httpMethod']
  path = event["path"]
  if httpMethod == getMethod and path == healthPath:
    response = buildResponse(200)
  elif httpMethod == postMethod and path == createUserPath:
    response = createUser(json.loads(event["body"]))
  elif httpMethod == postMethod and path == createProductPath:
    response = createProduct(json.loads(event["body"]))
  elif httpMethod == getMethod and path == getUserPath:
    username = event["queryStringParameters"]["username"]
    if username is not None:
      response = getUserByUsername(username)
    else:
      response = buildResponse(400, "Invalid Username Query")
  elif httpMethod == getMethod and path.startswith(getUserPath):
    response = getUser(event["pathParameters"]["id"])
  elif httpMethod == patchMethod and path.startswith(updateUserPath):
    requestBody = json.loads(event["body"])
    productId = event["pathParameters"]["id"]
    response = updateUser(productId, requestBody)
  elif httpMethod == getMethod and path.startswith(getProductsPath):
    response = getProducts(event["queryStringParameters"]["limit"])
  else: 
    response = buildResponse(404, "Not Found")
  return response

# Create user
def createUser(user):
  user["id"] = str(uuid.uuid4())
  user["userId"] = user["userName"]
  del user["userName"]
  try:
    response = userTable.query(IndexName='userId-index', KeyConditionExpression=Key('userId').eq(user['userId']))
    print(response['Items'])
    if 'Items' in response:
      return buildResponse(401, "User with username already exits")
    userTable.put_item(Item=user)
    return buildResponse(200, user)
  except:
    return buildResponse(500, "Internal Server While Creating User")

# Create Product
def createProduct(product):
  product["id"] = str(uuid.uuid4())
  product["createdAt"] = current_millisecond()
  
  try:
    userResponse = userTable.get_item(Key={"id": product['sellerId']})
    print(userResponse)
    if "Item" in userResponse:
      response = productTable.put_item(Item=product)
      return buildResponse(200, product)
    else:
      return buildResponse(401, "Bad Request")
  except:
    logger.exception("Something went wrong during the createProduct request")
    return buildResponse(500, "Internal Server While Creating Product")

# Get User
def getUser(id):
  try:
    response = userTable.get_item(Key={'id': id})
    if 'Item' in response:
      return buildResponse(200, response["Item"])
    else:
      return buildResponse(404, "User not found")
  except:
    return buildResponse(500, "Internal Server while getting user")
  
# Get User By Username
def getUserByUsername(username):
  try:
    response = userTable.query(IndexName='userId-index', KeyConditionExpression=Key('userId').eq(username))
    if 'Items' in response:
      return buildResponse(200, response["Items"][0])
    else:
      return buildResponse(404, "User not found")
  except:
    return buildResponse(500, "Internal Server while getting user by username")

# Update User
def updateUser(id, body):
  try:
    for key in body.keys():
      updateKey = key
      updateValue = body[key]
      response = userTable.update_item(Key={'id': id}, UpdateExpression=f"set {updateKey}=:v", ExpressionAttributeValues={':v': updateValue}, ReturnValues="UPDATED_NEW")
      print(body)
    user = userTable.get_item(Key={'id': id})["Item"]
    return buildResponse(200, user)
  except:
    logger.exception("Something went wrong during the updateProduct request")
    return buildResponse(500, "Internal Server While Updating User")

# Get Products
def getProducts(limit):
  try:
    response = productTable.scan(Limit=int(limit))
    for item in response["Items"]:
      seller = userTable.get_item(Key={'id': item['sellerId']})["Item"]
      item['posterInfo'] = {
        "role": "seller",
        "firstName": seller["firstName"],
        "lastName": seller["lastName"],
        "profilePicUrl": seller["photo"] if "photo" in seller else "N/A",
      }
      
    if "Items" in response:
      body = {
        "statusCode": 200,
        "length": len(response["Items"]),
        "items": response["Items"],
      }
    else:
      body = {
        "statusCode": 404,
      }
    if "LastEvaluatedKey" in response:
      body["LastEvaluatedKey"]= response["LastEvaluatedKey"],
    return buildResponse(200, body)
  except:
    logger.exception("Something went wrong during the getProducts request")
    return buildResponse(500, "Internal Server While Getting Products")
  

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