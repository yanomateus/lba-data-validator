"""create biosphere_atmosphere_read table

Revision ID: 645481c6255a
Revises: 
Create Date: 2019-04-19 15:31:28.314177

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '645481c6255a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'biosphere_atmosphere_read',
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('registered_at', sa.DateTime(), nullable=False),
        sa.Column('atmospheric_pressure', sa.Float(), nullable=True),
        sa.Column('precipitation', sa.Float(), nullable=True),
        sa.Column('air_temperature', sa.Float(), nullable=True),
        sa.Column('soil_temperature_at_2_cm_depth', sa.Float(), nullable=True),
        sa.Column('soil_temperature_at_5_cm_depth', sa.Float(), nullable=True),
        sa.Column('soil_temperature_at_10_cm_depth', sa.Float(), nullable=True),
        sa.Column('soil_temperature_at_20_cm_depth', sa.Float(), nullable=True),
        sa.Column('soil_temperature_at_50_cm_depth', sa.Float(), nullable=True),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_biosphere_atmosphere_read'))
    )


def downgrade():
    op.drop_table('biosphere_atmosphere_read')
