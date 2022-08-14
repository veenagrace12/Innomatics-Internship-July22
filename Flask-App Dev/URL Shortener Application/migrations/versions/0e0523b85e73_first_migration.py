"""First Migration

Revision ID: 0e0523b85e73
Revises: 
Create Date: 2022-08-14 17:38:25.477712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e0523b85e73'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('url_shortener',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('long_url', sa.String(length=100), nullable=True),
    sa.Column('short_url', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('url_shortener')
    # ### end Alembic commands ###
