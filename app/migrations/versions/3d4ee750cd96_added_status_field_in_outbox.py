"""Added status field in outbox

Revision ID: 3d4ee750cd96
Revises: 0cc21e3e21e2
Create Date: 2024-11-16 13:49:31.337408

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3d4ee750cd96'
down_revision: Union[str, None] = '0cc21e3e21e2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
