# Donor Call proposal

This application serves as a single location for information on donors and other financial contributors. It is intended to help stewards keep track of which donors they've called, when, and various other important data points.

# Models

### - Donor

    - steward (ForeignKey)
    - orgName
    - lastName
    - phone
    - email
    - paymentNum
    - yearTotal
    - lastGift
    - lastGiftDate
    - nextLastGift
    - nextLastGiftDate
    - comments
    - recentCallDate

### - Steward/User

    - donors (ForeignKeys)
    - name
    - pass

# User stories

## All CRUD actions require authorization

- View all stewards and donors
- View an individual steward or donor
- Download a CSV file containing all donor information in the DB
- create, edit, and delete stewards and donors
- add comments to a donor
- see donors associated with currently logged in steward

### post MVP

- see which donors a given steward has called
- Search donors by last name or lastGift size
- click 'called' to update recentCallDate to current time

# Wireframes

- Backend & Endpoints
  https://miro.com/app/board/o9J_kvdwtHQ=/

- Frontend
  https://miro.com/app/board/o9J_kvd_1tM=/

# Technologies

- React.js
- ReactBootstrap
- Django
- Postgresql
- Django Rest Framework
- DRF-Simple JS Web Token
