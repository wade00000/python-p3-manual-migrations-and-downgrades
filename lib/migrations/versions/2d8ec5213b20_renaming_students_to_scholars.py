"""Renaming students to scholars

Revision ID: 2d8ec5213b20
Revises: 791279dd0760
Create Date: 2025-05-28 21:33:54.141253

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d8ec5213b20'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None



def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')