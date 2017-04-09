"""Add comments table

Revision ID: b4e49978febc
Revises: 364e5d80dc7c
Create Date: 2017-04-06 21:59:19.391341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4e49978febc'
down_revision = '364e5d80dc7c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'comments',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('message', sa.Text, nullable=False),
    )
    op.execute('ALTER TABLE comments ADD COLUMN todo_id INTEGER REFERENCES todos(id);')


def downgrade():
    op.drop_table('comments')
