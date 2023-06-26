# tink
AWS Lambda, API GateWay and DynomoDB
## TINKOKO MARKET PLACE BACKEND TECHNICAL INTERVIEW TEST

### Using the aws lambda function,dynamodb and api gateway develop the following Rest api endpoints:

#### /create-user (Creating a new user)
#### Request Payload:
```
    {
    "activateUser": false,
    "currency": "NGN",
    "lastName": "Lamidi ",
    "email": "lamiditemitope31@email.com" ,
    "firstName": "Temitope ",
    "phone": "7043330737",
    "role": [buyer / seller],
    "userName": "temi247",
    }
```
#### Response Payload
```
    {
    "id" "h3fons893dfjg944ff" [partion key -pk]
    "activateUser": false,
    "createdAt": "1667213189880",
    "currency": "NGN",
    "lastName": "Lamidi ",
    "email": "lamiditemitope31@email.com" ,
    "firstName": "Temitope ",
    "phone": "7043330737",
    "role": [buyer / seller],
    "userId": "temi247",
    }
```

#### /create-product (Creating a new product)
#### Request Payload:
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
    "sellerId": "634084c8fd2c16ba75c006e8",
    "weight": "500"
    }
```
#### Response Payload:
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
#### /get-user/[:id] (get a user record using the unique id )

#### /get-user/[:user-name] (get a user record using the userName attribute )

#### /update-user/[:id] (update a user record)
#### Request Payload:
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
#### Response Payload:
```
    {
    "id" "h3fons893dfjg944ff" [partion key -pk]
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
#### /list-product (get list of product; Limits=10)
##### Use the sellerId attached to each product to get the seller info (i.e firstName, lastName, userName and profilePic) before returning the list
#### Response Payload:
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
### Programming language: Python (Most preferred) or Node.js

#### SUBMISSION: Create a GitHub repo (and the link is to be forwarded to this email: Tinkokogroup101@gmail.com ) to document all the apis. This doucmentation should contain neccessary info like the logic, api endpoint, payloads and http method for each api. You can reach us for more clarity or explanation at any point. This assessment is to be completed under 48 Hours.

### GOOD LUCK
