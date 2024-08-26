
'''
2. Python Programming Challenges for Customer Service Data Handling

Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

Problem Statement: Develop a program that:

1. Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
2. Implement functions to:
   -Open a new service ticket.
   -Update the status of an existing ticket.
   -Display all tickets or filter by status.
3. With some sample tickets and include functionality for additional ticket entry.

'''

def new_ticket(service, ticket_id, customer_name, issue_description):
    if ticket_id not in service:
        service[ticket_id] = {
            "Customer": customer_name,
            "Issue": issue_description,
            "Status": "open"
        }
        print(f"Ticket {ticket_id} added.")
    else:
        print(f"Ticket {ticket_id} already exist")

def update_status(service, ticket_id, new_status):
    try:
      if ticket_id in service:
          service[ticket_id]["Status"] = new_status
          print(f"Ticket {ticket_id} status updated to {new_status}.")
      else:
          print(f"Ticket {ticket_id} not found.")
                
    except KeyError as e:
        print(f"Error: Key {e} not found in the ticket data.")
    except Exception as e:
         print(f"An unexpected error occurred: {e}")

def display_tickets(service, status_filter):
    for ticket_id in service:
        if service[ticket_id]["Status"] == status_filter:
            print(f"{ticket_id}:")
            print(f"  Customer: {service[ticket_id]['Customer']}")
            print(f"  Issue: {service[ticket_id]['Issue']}")
            print(f"  Status: {service[ticket_id]['Status']}")
            print()  # Add an empty line between tickets for readability
            break



service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}


new_ticket(service_tickets, "Ticket003", "Charlie", "Password reset needed")
update_status(service_tickets, "Ticket001", "closed")
print("Open Tickets:")
display_tickets(service_tickets, status_filter="open")
print("Closed Tickets:")
display_tickets(service_tickets, status_filter="closed")
print(service_tickets)
