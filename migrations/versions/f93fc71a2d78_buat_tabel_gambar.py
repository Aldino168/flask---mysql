"""buat tabel gambar

Revision ID: f93fc71a2d78
Revises: b6c6a4235170
Create Date: 2022-05-06 01:38:18.073894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f93fc71a2d78'
down_revision = 'b6c6a4235170'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gambar',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('judul', sa.String(length=80), nullable=False),
    sa.Column('pathname', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('gambar')
    # ### end Alembic commands ###
