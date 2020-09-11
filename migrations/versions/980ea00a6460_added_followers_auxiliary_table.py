"""added followers auxiliary table

Revision ID: 980ea00a6460
Revises: b3557ec31f51
Create Date: 2020-09-09 11:19:16.341705

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '980ea00a6460'
down_revision = 'b3557ec31f51'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###