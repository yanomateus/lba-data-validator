"""add column surface_temperature to table biosphere_atmosphere_read

Revision ID: 13b10ef9c088
Revises: 645481c6255a
Create Date: 2019-04-20 16:17:45.928476

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13b10ef9c088'
down_revision = '645481c6255a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('biosphere_atmosphere_read', sa.Column('surface_temperature', sa.Float(), nullable=True))


def downgrade():
    op.drop_column('biosphere_atmosphere_read', 'surface_temperature')
