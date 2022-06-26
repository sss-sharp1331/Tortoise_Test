# Tortoise_Test
Simple REST API framework for the following Problem Statement.

Problem Statement : 
A detailed breakdown of the workflow

Functionality on the brand partner side
1. Brand partner creates a plan
a. Creates a plan in the database with planID, planName, amountOptions and
tenureOptions, benefitPercentage (for example: 10), benefitType
(cashback/extraVoucher) and any other attributes needed.

2. Brand partner creates promotion for an existing plan
a. Promotion can be limited in two ways
i. By the number of users to get the promotion (for example: 500 users)
ii. By a time period (for example: 22th May 2022 to 24th May 2022)
b. Assume that promotion can only affect benefitPercentage for a given plan

Functionality on the end-user side
1. List the available plans on the platform or the brand
2. Enroll in any of the plans
a. Create an entry in the CustomerGoals table with the planID, userID,
selectedAmount, selectedTenure, startedDate, depositedAmount,
benefitPercentage, benefitType and any other attributes needed.

Design the system to create promotions on plans and show updated information to users based on
the respective promotion type. CustomerGoals table should capture the right information on the
benefitPercentage based on the promotions.

Result : 

API Methods CREATED : 

Promotion APIs for partners : 
GET http://localhost:8000/api/plan/ -> Gets the list of all existing plans 
POST http://localhost:8000/api/plan/ -> Posts the plan in our SQL DB. 
GET http://localhost:8000/api/user/  -> Gets the data of Users and their plans 
POST http://localhost:8000/api/user/ -> Posts the user data in our SQL DB. 

APIs can be accessed by running the server
