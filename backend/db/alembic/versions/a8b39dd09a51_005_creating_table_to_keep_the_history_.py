"""005 - Creating table to keep the history of the FIIś quotations

Revision ID: a8b39dd09a51
Revises: b9b68f7157c2
Create Date: 2022-08-14 11:54:07.113219

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a8b39dd09a51'
down_revision = 'b9b68f7157c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fii_quotation',
    sa.Column('pk', sa.BigInteger(), nullable=False),
    sa.Column('rm_timestamp', sa.BigInteger(), server_default='0', nullable=False),
    sa.Column('fii_pk', sa.BigInteger(), nullable=False),
    sa.Column('quotation_date', sa.DateTime(), nullable=False),
    sa.Column('open_value', sa.Float(), nullable=False),
    sa.Column('high_value', sa.Float(), nullable=False),
    sa.Column('low_value', sa.Float(), nullable=False),
    sa.Column('close_value', sa.Float(), nullable=False),
    sa.Column('volume', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['fii_pk'], ['fii.pk'], name='fii_quotation_fii_pk_fk'),
    sa.PrimaryKeyConstraint('pk'),
    sa.UniqueConstraint('quotation_date', 'fii_pk', 'rm_timestamp', name='fii_quotation_quotation_date_fii_pk_un')
    )
    op.create_index(op.f('ix_fii_quotation_fii_pk'), 'fii_quotation', ['fii_pk'], unique=False)
    op.create_index(op.f('ix_fii_quotation_pk'), 'fii_quotation', ['pk'], unique=False)
    op.create_index(op.f('ix_fii_quotation_quotation_date'), 'fii_quotation', ['quotation_date'], unique=False)
    op.add_column('fii', sa.Column('code_international', sa.Unicode(length=10), nullable=False))
    op.alter_column('fii', 'code',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.Unicode(length=6),
               existing_nullable=False)
    op.create_unique_constraint('fii_code_international_un', 'fii', ['code_international', 'rm_timestamp'])
    op.drop_column('fii', 'value')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('fii', sa.Column('value', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False))
    op.drop_constraint('fii_code_international_un', 'fii', type_='unique')
    op.alter_column('fii', 'code',
               existing_type=sa.Unicode(length=6),
               type_=sa.VARCHAR(length=10),
               existing_nullable=False)
    op.drop_column('fii', 'code_international')
    op.drop_index(op.f('ix_fii_quotation_quotation_date'), table_name='fii_quotation')
    op.drop_index(op.f('ix_fii_quotation_pk'), table_name='fii_quotation')
    op.drop_index(op.f('ix_fii_quotation_fii_pk'), table_name='fii_quotation')
    op.drop_table('fii_quotation')
    # ### end Alembic commands ###
