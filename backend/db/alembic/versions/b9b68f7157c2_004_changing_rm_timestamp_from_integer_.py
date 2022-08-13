"""004 - Changing rm_timestamp from Integer to BigInteger

Revision ID: b9b68f7157c2
Revises: c793a97d4ba5
Create Date: 2022-08-13 15:21:33.623690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9b68f7157c2'
down_revision = 'c793a97d4ba5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('fii', 'rm_timestamp',
               existing_type=sa.INTEGER(),
               type_=sa.BigInteger(),
               existing_nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('fii_dividend', 'rm_timestamp',
               existing_type=sa.INTEGER(),
               type_=sa.BigInteger(),
               existing_nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('fii_type', 'rm_timestamp',
               existing_type=sa.INTEGER(),
               type_=sa.BigInteger(),
               existing_nullable=False,
               existing_server_default=sa.text('0'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('fii_type', 'rm_timestamp',
               existing_type=sa.BigInteger(),
               type_=sa.INTEGER(),
               existing_nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('fii_dividend', 'rm_timestamp',
               existing_type=sa.BigInteger(),
               type_=sa.INTEGER(),
               existing_nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('fii', 'rm_timestamp',
               existing_type=sa.BigInteger(),
               type_=sa.INTEGER(),
               existing_nullable=False,
               existing_server_default=sa.text('0'))
    # ### end Alembic commands ###
