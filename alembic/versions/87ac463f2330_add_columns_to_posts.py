"""add columns to posts

Revision ID: 87ac463f2330
Revises: 885fa81710f4
Create Date: 2024-08-06 05:18:35.323243

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '87ac463f2330'
down_revision: Union[str, None] = '885fa81710f4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column("posts",sa.Column(
        "published",sa.Boolean,nullable=False,server_default='True'
    )),
    op.add_column("posts",sa.Column("created_at",sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('NOW()'))            )
    pass



def downgrade():
    op.drop_column("posts","published")
    op.drop_column("posts","created_at")
    pass
