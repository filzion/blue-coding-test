Feature: Catalog
"""
The user should be able to use the store catalog.
"""

Background: 
    Given he is logged in
    And he is on the catalog page


Scenario: Validate if the user can add a product from the catalog
    Given there are products on the page
    And The "add to cart" button should appear for the first item 
    # When he adds a product to the cart
    # Then The "remove" button should appear for the first item
    # And the truck icon should display "1"

# Scenario: Validate the truck icon increasing
#     Given there are products on the page
#     When he adds a product to the cart
#     And the truck icon should display "1"

# Scenario Outline: Validate the sort by options
#     Given there are products on the page
#     When he selects the sort by "<sort_option>"
#     Then the first product on the page should be "<first_product>"

# Example:  
#     |sort_option   | first_product                     |
#     | a to z       | Sauce Labs Backpack               |
#     | z to a       | Test.allTheThings() T-Shirt (Red) |
#     | lowest price | Sauce Labs Onesie                 |
#     | highest price| Sauce Labs Fleece Jacket          |
