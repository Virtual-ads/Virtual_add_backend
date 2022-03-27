"""creative thumbnail

Revision ID: 7b10e0d5c798
Revises: c1442cd73b8a
Create Date: 2022-02-20 19:54:39.501989

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b10e0d5c798'
down_revision = 'c1442cd73b8a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('creatives', sa.Column('thumbnail', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('creatives', 'thumbnail')
    # ### end Alembic commands ###
