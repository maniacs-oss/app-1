"""empty message

Revision ID: f939d67374e4
Revises: b4146f7d5277
Create Date: 2020-05-02 18:07:42.275092

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f939d67374e4'
down_revision = 'b4146f7d5277'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('referral', sa.Column('name', sa.String(length=512), nullable=True))
    op.drop_constraint('users_referral_id_fkey', 'users', type_='foreignkey')
    op.create_foreign_key(None, 'users', 'referral', ['referral_id'], ['id'], ondelete='SET NULL')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.create_foreign_key('users_referral_id_fkey', 'users', 'referral', ['referral_id'], ['id'])
    op.drop_column('referral', 'name')
    # ### end Alembic commands ###
