"""init

Revision ID: afcb25d4aef4
Revises: 
Create Date: 2022-09-14 00:47:50.929542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'afcb25d4aef4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('eav',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('e_id', sa.Integer(), nullable=False),
    sa.Column('attribute', sa.String(length=256), nullable=False),
    sa.Column('value', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_eav_id'), 'eav', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_eav_id'), table_name='eav')
    op.drop_table('eav')
    # ### end Alembic commands ###
