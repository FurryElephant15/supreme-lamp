"""first migration Logins

Revision ID: c71c84ebf6bc
Revises: 
Create Date: 2023-08-31 17:24:31.723787

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c71c84ebf6bc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('logins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('OrgName', sa.String(length=120), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('logins', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_logins_OrgName'), ['OrgName'], unique=True)
        batch_op.create_index(batch_op.f('ix_logins_email'), ['email'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('logins', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_logins_email'))
        batch_op.drop_index(batch_op.f('ix_logins_OrgName'))

    op.drop_table('logins')
    # ### end Alembic commands ###