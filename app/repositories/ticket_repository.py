from sqlalchemy import select

from app.models.ticket import Ticket


class TicketRepository:

    def create_ticket(self, db, ticket_data):
        ticket = Ticket(**ticket_data.model_dump())

        db.add(ticket)
        db.flush()

        return ticket

    def get_all_tickets(self, db):
        tickets = db.scalars(select(Ticket)).all()

        return tickets


    def get_ticket_by_id(self, db, ticket_id):
        ticket = db.get(Ticket,ticket_id)

        if ticket is not None:
            print(ticket.subject)

        return ticket

    def update_ticket(self, db, ticket, update_data):

        data = update_data.model_dump(exclude_unset=True)

        for key, value in data.items():
            setattr(ticket, key, value)

        db.flush()

        return ticket

    def delete_ticket(self, db, ticket):
        db.delete(ticket)
        db.flush()