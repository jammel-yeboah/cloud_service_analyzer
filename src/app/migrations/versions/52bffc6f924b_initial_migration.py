"""Initial Migration

Revision ID: 52bffc6f924b
Revises: 
Create Date: 2022-07-25 01:50:00.114494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52bffc6f924b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reports',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('serviceCategory', sa.String(length=500), nullable=True),
    sa.Column('serviceType', sa.String(length=500), nullable=True),
    sa.Column('serviceRegion', sa.String(length=500), nullable=True),
    sa.Column('instances', sa.String(length=500), nullable=True),
    sa.Column('machineFamily', sa.String(length=500), nullable=True),
    sa.Column('infrastructureType', sa.String(length=500), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reports')
    # ### end Alembic commands ###
