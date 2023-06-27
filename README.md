# TINKOKO MARKET PLACE

### Using the AWS Lambda Function,Dynamodb and API Gateway

<br>

## CREATE USER

#### Endpoint: /create-user

### Logic:

Gets user information from payload, and checks if an existing user with the payload username exists, if user exists, returns a 400 "Bad Request" response else, creates a user and assigns a unique Id.

#### Method: POST

#### Request Body:

```
    {
        "activateUser": false,
        "currency": "NGN",
        "lastName": "Lamidi ",
        "email": "lamiditemitope31@email.com" ,
        "firstName": "Temitope ",
        "phone": "7043330737",
        "role": "seller",
        "userName": "temi247",
    }
```

#### Response Body

```
    {
        "id" "9875ba36-a206-4c5b-a7ce-179fe9f75211",
        "activateUser": false,
        "createdAt": "1667213189880",
        "currency": "NGN",
        "lastName": "Lamidi ",
        "email": "lamiditemitope31@email.com" ,
        "firstName": "Temitope ",
        "phone": "7043330737",
        "role": "seller",
        "userId": "temi247",
    }
```

<br>

## CREATE PRODUCT

#### Endpoint: /create-product

### Logic:

Gets product information from payload, and checks if an creator is a seller, if creator is a not a seller, returns a 400 "Bad Request" response else, creates a product and assigns a unique Id.

#### Method: POST

#### Request Body:

```
    {
        "category": "627cc555046919d2a6f21662",
        "city": "Abuja",
        "count": 10,
        "country": "Nigeria",
        "description": "Banana Flavour Minimum Order Quantity - 10pcs",
        "images": [
        {
        "public_id": "n4t5ccur0shvzrnwlkoy",
        "url": "https://res.cloudinary.com/tinkokooffice/image/upload/v1685421283/n4t5ccur0shvzrnwlkoy.jpg"
        }
        ],
        "price": "1000",
        "productName": "L&Z Yoghurt ",
        "quantity": 100,
        "subCategory": "hLBxpm6XoCWvhQQdsmRjQPZL",
        "sellerId": "875ba36-a206-4c5b-a7ce-179fe9f75211",
        "weight": "500"
    }
```

#### Response Body:

```
    {
        "id": "SaiUFv2oJurhMWq92VAesQKF", [pk],
        "category": "627cc555046919d2a6f21662",
        "city": "Abuja",
        "count": 10,
        "country": "Nigeria",
        "createdAt": "1685421412232",
        "description": "Banana Flavour Minimum Order Quantity - 10pcs",
        "images": [
        {
        "public_id": "n4t5ccur0shvzrnwlkoy",
        "url": "https://res.cloudinary.com/tinkokooffice/image/upload/v1685421283/n4t5ccur0shvzrnwlkoy.jpg"
        }
        ],
        "price": "1000",
        "productName": "L&Z Yoghurt ",
        "quantity": 100,
        "subCategory": "hLBxpm6XoCWvhQQdsmRjQPZL",
        "sellerId": "634084c8fd2c16ba75c006e8",
        "weight": "500"
    }
```

<br>

## GET USER BY ID (get a user record using the unique id )

#### Endpoint: /get-user/[:id]

### Logic:

Gets user by partition key

#### Method: GET

#### Response Body

```
    {
        "id" "9875ba36-a206-4c5b-a7ce-179fe9f75211",
        "activateUser": false,
        "createdAt": "1667213189880",
        "currency": "NGN",
        "lastName": "Lamidi ",
        "email": "lamiditemitope31@email.com" ,
        "firstName": "Temitope ",
        "phone": "7043330737",
        "role": "seller",
        "userId": "temi247",
    }
```

#### /get-user/[:user-name] (get a user record using the userName attribute )

## GET USER BY USERNAME (get a user record using the username )

#### Endpoint: /get-user?username=[:username]

### Logic:

Gets user by index key userId (username)

#### Method: GET

#### Response Body

```
    {
        "id" "9875ba36-a206-4c5b-a7ce-179fe9f75211",
        "activateUser": false,
        "createdAt": "1667213189880",
        "currency": "NGN",
        "lastName": "Lamidi ",
        "email": "lamiditemitope31@email.com" ,
        "firstName": "Temitope ",
        "phone": "7043330737",
        "role": "seller",
        "userId": "temi247",
    }
```

<br>

## UPDATE USER BY ID

#### Endpoint: /update-user/[:id]

### Logic:

Update user with unique Id provided in the path parameters from request body provided.

#### Method: PATCH

#### Request Body:

```
    {
        "photo": [
            {
            "public_id": "n4t5ccur0shvzrnwlkoy",
            "url": "https://res.cloudinary.com/tinkokooffice/image/upload/v1685421283/n4t5ccur0shvzrnwlkoy.jpg"
            }
        ],
        "verificationMeans": "National ID"
        "idNumber": "0257248879HGT"
    }
```

#### Response Body:

```
    {
        "id" "h3fons893dfjg944ff"
        "activateUser": false,
        "createdAt": "1667213189880",
        "currency": "NGN",
        "lastName": "Lamidi ",
        "email": "lamiditemitope31@email.com" ,
        "firstName": "Temitope ",
        "phone": "7043330737",
        "role": [buyer / seller],
        "userId": "temi247",
        "photo": [
            {
            "public_id": "n4t5ccur0shvzrnwlkoy",
            "url": "https://res.cloudinary.com/tinkokooffice/image/upload/v1685421283/n4t5ccur0shvzrnwlkoy.jpg"
            }
        ],
        "verificationMeans": "National ID"
        "idNumber": "0257248879HGT"
    }
```

<br>

## GET PRODUCTS LISTED

#### Endpoint: /list-product?limit=10

### Logic:

Gets products listed and populate the seller information into "posterInfo"

#### Method: GET

#### Response Body:

```
    {
        "LastEvaluatedKey": {
            "id": "633192b485f761e0d94b2bfd"
        },
        "statusCode": 200,
        "length": 10,
        "items": [
            {
                "productName": "Irish Potatoes",

                "category": "627cc5f7046919d2a6f2167d",
                "createdAt": "1663787083980",
                "images": [
                    {
                        "url": "https://res.cloudinary.com/tinkokooffice/image/upload/v1663787065/1663787064948.jpg",
                        "public_id": "1663787064948"
                    }
                ],
                "sellerId": "632ab45bca9584f349e7f0e1",
                "productId": "632b604b0da9bd1d419a07db",
                "posterInfo": {
                    "role": "seller",
                    "firstName": "Yakubu",
                    "lastName": "Rimamnungra",
                    "profilePicUrl": "N/A"
                }
            },
            {
                "productName": "Brown Rabbit",

                "category": "627cc5f7046919d2a6f2167d",
                "createdAt": "1663787083980",
                "images": [
                    {
                        "url": "https://res.cloudinary.com/tinkokooffice/image/upload/v1663787065/1663787064948.jpg",
                        "public_id": "1663787064948"
                    }
                ],
                "sellerId": "632ab45bca9584f349e7f0e1",
                "productId": "632b604b0da9bd1d419a07db",
                "posterInfo": {
                    "role": "seller",
                    "firstName": "Ajayi",
                    "lastName": "Rafel",
                    "profilePicUrl": [
                    {
                        "url": "https://res.cloudinary.com/tinkokooffice/image/upload/v1663787065/1663787064948.jpg",
                        "public_id": "1663787064948"
                    }
                ],
                }
            }

        ]
    }
```
