"""Renaming grade to scores

Revision ID: e0d0ad9a21f2
Revises: 2d8ec5213b20
Create Date: 2025-05-28 21:51:55.943094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0d0ad9a21f2'
down_revision = '2d8ec5213b20'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # 1. Create the new table with only the columns you care about
    op.create_table(
        'scholars_tmp',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('scores', sa.String)
    )

    # 2. Copy data from the old table into the new one (grade → scores)
    op.execute("""
        INSERT INTO scholars_tmp (id, scores)
        SELECT id, grade FROM scholars
    """)

    # 3. Drop the old table
    op.drop_table('scholars')

    # 4. Rename new table to the original name
    op.rename_table('scholars_tmp', 'scholars')

def downgrade() -> None:
    # 1. Create the new table with only the columns you care about
    op.create_table(
        'scholars_tmp',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('grade', sa.String)
    )

    # 2. Copy data from the old table into the new one (grade → scores)
    op.execute("""
        INSERT INTO scholars_tmp (id, grade)
        SELECT id, scores FROM scholars
    """)

    # 3. Drop the old table
    op.drop_table('scholars')

    # 4. Rename new table to the original name
    op.rename_table('scholars_tmp', 'scholars')
