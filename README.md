OSP
Online Sales Portal , Software Engineering Lab Spring 2023

• Developed an online sales portal,where people can buy and sell their products on the same platform.

• Designed portal such that there is a scope for Manager,who can control the processes in the system.

• Developed the frontend part using HTML,CSS and Bootsrap and backend using Django.

Problem Statement:

A business group wants to set up an on-line portal where people can buy and sell on the same platform – one-stop store for both the buyer and the seller.

The on-line portal should have the following features:

      A. Categorization of items:
      
      a. Electronics & Technology,
      
      b. Books,
      
      c. Real Estate,
      
      d. Cars & Bikes,
      
      e. Education & Learning,
      
      f. Home & Lifestyle,
      
      g. Cellphone,
      
      h. …
Manager can add / remove categories of items in the portal.

B. There are two types of users of the system:

a. Managers: They manage the portal. Every manager has to create an account with the following information:

    i.Name
    
    ii.Gender
    
    iii.Date-of-Birth
    
    iv.Address including house no, street, locality and city
    
    v.Telephone number
    
    vi.Email
    
    vii.IM ID
    
    viii.Biometric ID
    
b. Customers: They use the portal to buy and sell products. Every customer has to create an account with the following information:

    i.Name
    
    ii.City
    
    iii.Telephone number
    
    iv.Email
    
    v.IM ID (optional)
    
    vi.On creation of an account, the system generates an ID and a password for the user and communicates through the email.
       The ID is unique and cannot be changed. The password can be changed by the user.
       
C. For Seller: To sell, the users can upload various items by specifying the following information:

    a. Category of the item
    
    b. Photo of the item
    
    c. Price
    
    d. The age of the item (if not new)
    
    e. Name of the manufacturing company
    
    f. City
    
    g. Some specific information about that particular product.
    
D. For Buyer: The buyer can do the following:

    a. Search for item and find the list of the sellers who have uploaded that particular item for sale.
    
    b. Raise a request to buy an item. Offers a price.
    
    c. Negotiate on the selling price. It the seller agrees with a certain price then only buyer can buy it.
    
    d. Pay the money on-line.
    
    e. A buyer cannot buy a heavy item like refrigerator if its seller location (city) is not the same.
    
E. For Manager: The manager can do the following:

    a. Manage buyers / sellers
    
    b. Manage categories; change categories of items if needed
    
    c. Review items and rejects items of poor quality
    
    d. Help negotiations - talk to (over email or chat) buyer and seller both to help bridge small gaps or to assist with delivery logistics
    
    e. Perform audit of matched buy-sell of items
