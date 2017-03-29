"""Add todo table

Revision ID: 364e5d80dc7c
Revises: 
Create Date: 2017-03-28 21:40:36.676737

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '364e5d80dc7c'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'todos',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
    )

def downgrade():
    op.drop_table('todos')

