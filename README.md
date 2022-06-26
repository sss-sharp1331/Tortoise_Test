# Tortoise_Test
Simple REST API framework for the following Problem Statement.

Problem Statement :  <br />
A detailed breakdown of the workflow <br />

Functionality on the brand partner side: <br />
1. Brand partner creates a plan <br />
a. Creates a plan in the database with planID, planName, amountOptions and
tenureOptions, benefitPercentage (for example: 10), benefitType
(cashback/extraVoucher) and any other attributes needed. <br />

2. Brand partner creates promotion for an existing plan. <br />
a. Promotion can be limited in two ways <br />
i. By the number of users to get the promotion (for example: 500 users) <br />
ii. By a time period (for example: 22th May 2022 to 24th May 2022) <br />
b. Assume that promotion can only affect benefitPercentage for a given plan. <br />

Functionality on the end-user side: <br />
1. List the available plans on the platform or the brand <br />
2. Enroll in any of the plans <br />
a. Create an entry in the CustomerGoals table with the planID, userID,
selectedAmount, selectedTenure, startedDate, depositedAmount,
benefitPercentage, benefitType and any other attributes needed. <br />

Design the system to create promotions on plans and show updated information to users based on
the respective promotion type. CustomerGoals table should capture the right information on the
benefitPercentage based on the promotions. <br />

Result :  <br />

API Methods CREATED :  <br />

Promotion APIs for partners :  <br />
GET http://localhost:8000/api/plan/ -> Gets the list of all existing plans. <br /> 
POST http://localhost:8000/api/plan/ -> Posts the plan in our SQL DB.  <br />
GET http://localhost:8000/api/user/  -> Gets the data of Users and their plans.  <br />
POST http://localhost:8000/api/user/ -> Posts the user data in our SQL DB.  <br />

APIs can be accessed by running the server <br />
