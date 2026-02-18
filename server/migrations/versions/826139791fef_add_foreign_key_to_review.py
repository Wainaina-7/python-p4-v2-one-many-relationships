"""add foreign key to Review

Revision ID: 826139791fef
Revises: d15247e4fa34
Create Date: 2026-02-17 15:55:32.784499

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '826139791fef'
down_revision = 'd15247e4fa34'
branch_labels = None
depends_on = None

def upgrade():
    with op.batch_alter_table('reviews') as batch_op:
        batch_op.create_foreign_key(
            'fk_reviews_restaurant_id',
            'restaurants',
            ['restaurant_id'],
            ['id']
        )
def downgrade():
    with op.batch_alter_table('reviews') as batch_op:
        batch_op.drop_constraint(
            'fk_reviews_restaurant_id',
            type_='foreignkey'
        )

