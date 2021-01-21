
#-#-#-#

#s  1: Relationship basics
#a   : Relationship basics
#s  2: 
#a   : In this section we will have a look at some basics of database relationships.
#s  3: - Advantages of database relationships
#a   : Therefore, first we will have a look at the advantages of database relationships.
#s  4: - Different kinds of relationships
#a   : Then, we will have a look at the different kinds of relationships.

#-#-#-#

#s  1: Advantages of database relationships
#a   : Advantages of database relationships
#s  2:
#a   : We first want to answer the questions, 
#      what are database relationships and why they are used.
#s  3: Mainly two advantages:
#a   : Database relationships have mainly two advantages:
#s  4: <div class="mt-2">- Connection between tables, which are logically related</div>
#a   : First, a database relationship is a connection 
#      between two or more database tables, where the tables
#      are logically related to each other. This gives you the advantage, to structure your data into
#      multiple tables, even when the tables are related to each other and when there is a connection 
#      between the tables. The database relationships are then used, to join the different tables
#      together, to retrieve the information which are required.
#s  5: <div class="ml-4"> - Every user has a address</div>
#a   : Imagine for example, that we store users in our database. Therefore, we will create a users table.
#      We also want to store the addresses of each user, but we want to logically divide this information
#      from the basic user information.
#s  6: <div class="ml-4"> - Table 'users' and table 'addresses' <v-icon>arrow_right_alt</v-icon> every user has one address <v-icon>arrow_right_alt</v-icon>Link user to address with relationship</div>
#a   : To store the basic users information, we will create a table called users.
#      To store the addresses, we create a second seperate table, called addresses. 
#      Now we can use a relationship, to link the two tables together.
#s  6: <div class="ml-4"> - Ed has address 'A' <v-icon>arrow_right_alt</v-icon> 1 relationships from Ed to address 'A'</div>
#a   : For example, imagine we have a user called ed, stored in the users table, and now we also want to store 
#      his address. Then we could store the address 
#      in the table addresses, and we will create a relationship from the users table to this address in 
#      the addresses table. This relationship allows us to know, which address belongs to which user.
#s  7: <div class="mt-2">- Minimizes redundant data</div>
#a   : The second advantage of database relationships is the following. The relationships can also be used to reduce 
#      the redundancy of the data stored in the
#      database. That means, that instead of saving the same information multiple times, it is possible
#      to save it only one time, and then reference to this information multiple times, whenever it is needed.
#s  8: <div class="ml-4"> - table 'users' and table 'products' <v-icon>arrow_right_alt</v-icon> users purcheses a product several times <v-icon>arrow_right_alt</v-icon> link user to product several times</div>
#a   : Imagine for example, we have two tables, one users table, for our users information, 
#      and one products table for the information about the products. 
#      If a user purchases one product serveral times, 
#      then we do not want to save the information
#      about the same product several times, because the information about the product is every time the same, 
#      it is only one product. We therefore can create multiple relationships from the user to the product, so 
#      from the users table to the products table.
#s  9: <div class="ml-4"> - User Ed purchases two times the same pair of shoes <v-icon>arrow_right_alt</v-icon> 2 relationships from Ed to pair of shoes</div>
#a   : For example, the user Ed purchases two times the same pair of shoes. 
#      The information about the user ed are stored
#      in the users table. And the information about the pair of shoe are stored in the products table.
#      We can now create two relationships from the user ed to
#      this pair of shoes in the product table. 
#      With that, we the information about the pair of shoes are only stored one time in our database, but 
#      referenced multiple times.


#-#-#-#
#s  1: Different kinds of relationships
#a   : Different kinds of relationships
#s  2: 
#a   : When dealing with database relationships, 3 different kinds of relationships can be distinguished.
#s  3: <div class="mt-4">- One to one</div>
#a   : First, there is a one to one relationship. This relationship allows only one record in one table to
#      be related to one other record in another table.
#s  4: <div class="ml-4">
#        <div>- One user should only have one address</div>
#        <div><img src="@/assets/images/sql_alchemy_basics_a_07_1.png" height="120px" /></div>
#      </div>
#a   : For example, if we want to specify our database in such a way, that every user can only have one address, 
#      then a one to one relationship between the users table and the addresses table
#      can be used. With such a relationship, every user can only have zero, or one address, but not multiple addresses.
#s  5: <div class="mt-4">- One to many</div>
#a   : Second, there is a one to many relationship. This relationship allows one record in one table to
#      have multiple relationships to other records in another table.
#s  6: <div class="ml-4">
#        <div>- One user can have multiple orders <v-icon>arrow_right_alt</v-icon> every order is only referenced one time</div>
#        <div><img src="@/assets/images/sql_alchemy_basics_a_07_2.png" height="140px" /></div>
#      </div>
#a   : Imagine, that a user can place orders. The users information are stored in the users table, and the information
#      about the orders are stored in the orders table. A user can now place several orders and we will create
#      multiple relationships from the user to each order. So one user will have many orders. This is a one to many
#      relationship from the table users to the table orders. Note, however, that every order is referenced only one time.
#s  7: <div class="mt-4">- Many to many</div>
#a   : Third, there is a many to many relationship. This relationship also allows one record in one table to
#      have multiple records in another table. But, in contrast to the one to many relationship, where the many side of the relationship
#      can only have one reference, in a many to many relationship, both sides can have multiple references.
#s  8: <div class="ml-4">
#        <div> - One order can have multiple products <v-icon>arrow_right_alt</v-icon> one product can be referenced multiple times</div>
#        <div><img src="@/assets/images/sql_alchemy_basics_a_07_3.png" height="140px" /></div>
#      </div>
#a   : Imagine, that a user can place orders and every order can have multiple products. 
#      So we will look at the tables orders and products.
#      An order can have multiple products, but also every product could be part
#      of multiple orders. If you compare this to the one to many relationship with the users and orders table, 
#      then you can see, that every
#      order is referenced only one time. So the user ed has placed 3 orders, order 1, order 2 and order 3. 
#      User fred has placed only
#      one order, the order number 4. Wendy has placed two orders. Every user can place multiple orders, 
#      but every order is referenced only one time. This is in contrast to the many to many relationship. 
#      In the many to many
#      relationship between the orders and the products, the orders and the products can be referenced several times.
#      Looking at the products table, product one
#      is referenced from order 1 and from order 2. And product 4 is also referenced two times, from order 3 and order 4. 
#      Looking at the orders table, order 2 is 
#      referenced to product 1, 2, and 3. And order 4 references product 4 and 5. 
#      So every order can have multiple products, 
#      but every product can also be referenced from multiple orders.


#-#-#-#
# - explain uni- and bidirectionla case
