"""initial migration

Revision ID: 6de02d6b2682
Revises: 
Create Date: 2019-08-17 12:11:19.624789

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '6de02d6b2682'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('biosphere_atmosphere_variable',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('minimum_value', sa.Numeric(), nullable=True),
                    sa.Column('maximum_value', sa.Numeric(), nullable=True),
                    sa.PrimaryKeyConstraint('id', name=op.f('pk_biosphere_atmosphere_variable')))
    op.create_table('tower',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id', name=op.f('pk_tower')))
    op.create_table('biosphere_atmosphere_read',
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('variable_id', sa.Integer(), nullable=False),
                    sa.Column('registered_value', sa.Numeric(), nullable=False),
                    sa.Column('registered_at', sa.DateTime(), nullable=False),
                    sa.ForeignKeyConstraint(['variable_id'], ['biosphere_atmosphere_variable.id'],
                                            name=op.f('fk_biosphere_atmosphere_read_variable_id_biosphere_atmosphere_variable')),
                    sa.PrimaryKeyConstraint('id', name=op.f('pk_biosphere_atmosphere_read')))
    op.create_table('instrument',
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('reading_id', sa.Integer(), nullable=True),
                    sa.Column('tower_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['reading_id'], ['biosphere_atmosphere_read.id'],
                                            name=op.f('fk_instrument_reading_id_biosphere_atmosphere_read')),
                    sa.ForeignKeyConstraint(['tower_id'], ['tower.id'], name=op.f('fk_instrument_tower_id_tower')),
                    sa.PrimaryKeyConstraint('id', name=op.f('pk_instrument')))


def downgrade():
    op.drop_table('instrument')
    op.drop_table('biosphere_atmosphere_read')
    op.drop_table('tower')
    op.drop_table('biosphere_atmosphere_variable')
