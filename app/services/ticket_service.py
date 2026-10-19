from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.ticket import Ticket
from app.repositories.ticket_repository import TicketRepository
from app.schemas.ticket import TicketCreate

class TicketService:

    def __init__(self):
        self.repository = TicketRepository()

    def create_ticket(self, db, ticket_data):
        try:
            ticket = self.repository.create_ticket(db, ticket_data)

            db.commit()
            db.refresh(ticket)

            return ticket

        except Exception:
            db.rollback()
            raise

    def get_all_tickets(self, db):
        return self.repository.get_all_tickets(db)

    def get_ticket_by_id(self, db, ticket_id):
        ticket =  self.repository.get_ticket_by_id(db,ticket_id)
        if ticket is None:
            raise HTTPException(
                status_code=404,
                detail="Ticket not found"
            )

        return ticket

    from fastapi import HTTPException

    def update_ticket(self, db, ticket_id, update_data):

        ticket = self.repository.get_ticket_by_id(db, ticket_id)

        if ticket is None:
            raise HTTPException(
                status_code=404,
                detail="Ticket not found"
            )

        try:
            updated_ticket = self.repository.update_ticket(
                db, ticket, update_data
            )

            db.commit()
            db.refresh(updated_ticket)

            return updated_ticket

        except Exception:
            db.rollback()
            raise

    def delete_ticket(self, db, ticket_id):
        ticket = self.repository.get_ticket_by_id(db, ticket_id)

        if ticket is None:
            raise HTTPException(
                status_code=404,
                detail="Ticket not found"
            )

        try:
            self.repository.delete_ticket(db, ticket)

            db.commit()

        except Exception:
            db.rollback()
            raise