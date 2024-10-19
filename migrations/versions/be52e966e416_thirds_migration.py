"""thirds_migration

Revision ID: be52e966e416
Revises: 33c2db44d314
Create Date: 2024-10-18 20:32:22.024669

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'be52e966e416'
down_revision: Union[str, None] = '33c2db44d314'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('orders_idempotency_key_key', 'orders', type_='unique')
    op.drop_column('orders', 'idempotency_key')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('idempotency_key', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.create_unique_constraint('orders_idempotency_key_key', 'orders', ['idempotency_key'])
    # ### end Alembic commands ###
