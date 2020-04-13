# Firebase Realtime Database

## 목표

Firebase가 제공하는 Realtime DB에 대해 개략적으로 이해한다.

## 참고자료

- NoSQL?
  - https://highlyscalable.wordpress.com/2012/03/01/nosql-data-modeling-techniques/

- Why we should pipeline requests
  - https://stackoverflow.com/questions/35931526/speed-up-fetching-posts-for-my-social-network-app-by-using-query-instead-of-obse/35932786#35932786


# Realtime Database vs Cloud firestore

## Realtime DB

- cloud-hosted **NoSQL** Database
- SDK support for iOS, Android, Web
- Easy Integration with other [Firebase Tools](https://www.notion.so/Firebase-Tools-bcc9a839521a4b4fa462356bfdfe96aa)
- Stores data in **JSON**
    - everything is either a key or a value
    - no concepts of data types
- Web sockets for Data Synchronization
- Client Logic : requires to write most of the system app code on the client
    - write your own data validation
- Pre-planning all the required queries for the project is needed.
- Only supports queries on one field
- The database structure needs to be thoroughly structured for maximum effect.
- **Flattening** and **Denormalizing data** is needed

    → Makes it hard to implement new features to the exisitng app afterwords.

## Cloud Firestore

- newer **flagship** database
- Traditional relational schema hierarchy
- NoSQL database organized into collections
    - collections hold documents
        - documents hold more collections(subcollections) and data fields
        - Document is a single JSON object structure that can hold nested subcollections of more documents or key-value pairs of data
        - fields inside a document have types
            - strings
            - numbers
            - boolean
            - objects
            - arrays
            - null values
            - date timestamps
            - geopoints
            - shallow references to other documents
- Cannot query across subcollections or inside references
- Can use these references to directly fetch a local documents's related data

## RDB & CF Common feature

- Easy to include in a project
- Easy to tie with other firebase services
- Expose data to admin via the Firebase console
    - Console allows easy top level node & collections browsing
    - Allows admin to add&edit&delete data on console
- Both focus on speed and efficiency
- Easy to set up listeners that can trigger cloud code or local client code.
- Implement security through Firebase Rules.

### Key Difference

1. Querying Support 
    - RDB
        - Only allow a single parameter & confition to fetch on
        - Can run queries looking for fields that begin with specific query
    - CF
        - Allows to find records matching multiple field comparisons
2. Impoting & Exporting Data
    - RDB
        - Easy way to import&Export data (vis JSON files) in console.
        - Automated data migrations and querying with Firebase CLI
3. Real-time Updates
    - RDB
        - Real-time updates via web sockets
        - 
4. Cost Structure 
    - Small, frequent transactions : RDB
    - Traditional RESTful requests with larger responses : CF
5. Data Structure
    - RDB
        - Flat, denormalized data structure
    - CF
        - Reference dataa type, shallow queries, collection-document-subcollection paradigm (nested data)

# Summary

### Why Choose Realtime Database

- You want a system that can easily track multiple live “streams” of data in realtime. Examples include live chat, location based events, realtime games or collaboration.
- You expect to be making a lot of small writes/reads to the database.
- You're fine with handling JSON data objects, while validating type yourself.
- You do not foresee any need for complex queries on your dataset.
- You're ready to manage a flat and heavily denormalized database.

### Why Choose Cloud Firestore

- You want to build an app that offers a lot more than the real-time features. You can always leverage both backends together if you need to incorporate an important real-time feature.
- You want a more traditional data schema, but desire to retain the ability of realtime listeners as well as the multitude of other Firebase platform features.
- You expect to make few but large CRUD operations.
- You want to be able to query data on multiple fields.